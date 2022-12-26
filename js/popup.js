
    document.getElementById("Hint").addEventListener("click",revealHint);

    chrome.tabs.query({active: true, currentWindow: true},askForHint);
    function askForHint(tabs){
        let msg = "getHint";
        chrome.tabs.sendMessage(tabs[0].id,msg,showHint);
       }

    function showHint(response){
        if (response == "Wrong URL"){
            console.log(response);
        }
        else  {
            for (let i=0;i<5;i++){
            document.getElementById("letter"+i.toString()).textContent = response[i];
        }
    }
        // document.getElementById("Hint").style.filter = "blur: '0.25rem'"
    }
    function revealHint(){
        document.querySelector("#Hint").className = "hintAnimation";
    }
