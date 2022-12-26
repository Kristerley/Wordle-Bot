chrome.browserAction.onClicked.addListener(buttonClicked)

function buttonClicked(tab){
    let msg = "getHint";
    chrome.tabs.sendMessage(tab.id,msg);

}
