let rowNumber = 0;
let hint;
chrome.tabs.query({active: true, currentWindow: true},askForHint);

document.getElementById("Hint").addEventListener("click",revealHint);

function askForHint(tabs){
    let msg = {msg:"getHint"};
    chrome.tabs.sendMessage(tabs[0].id,msg,showHint);
   }

function showHint(response){
    if (response == "Wrong URL"){
        console.log(response);
    }
    else  {
        hint = response.Hint;
        console.log(response);
        rowNumber = response.rowNumber;

        for (let i=0;i<5;i++){
        document.getElementById("letter"+i.toString()).textContent = response.Hint[i];
        }
    }
}
function revealHint(){
    console.log("clck");
    document.querySelector("#Hint").className = "hintAnimation";
    document.getElementById("Hint").removeEventListener("click",revealHint);
    document.getElementsByClassName("hintAnimation")[0].addEventListener("click",fillHint);
}
function fillHint(){
    chrome.tabs.query({active: true, currentWindow: true},function(tabs){
        let msg = {msg:"fillHint",row: rowNumber, hint: hint };
        chrome.tabs.sendMessage(tabs[0].id,msg);
    });

    document.getElementsByClassName("hintAnimation")[0].removeEventListener("click",fillHint);
    document.getElementsByClassName("hintAnimation")[0].addEventListener("click",function(){chrome.tabs.query({active: true, currentWindow: true},askForHint)});
    document.querySelector("#Hint").className = "";
    document.getElementById("Hint").addEventListener("click",revealHint);
}


