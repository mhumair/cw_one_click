var ip = document.getElementsByClassName("srv-crid-sec1-row  srv-crid-sec1-row1 layout-wrap layout-align-start-center layout-row")[0].getElementsByClassName("clipboard ng-binding")[0].innerText;
var username = document.getElementsByClassName("srv-crid-sec1-row  srv-crid-sec1-row2 layout-wrap layout-align-start-start layout-row")[0].getElementsByClassName("clipboard ng-binding")[0].innerText;
var password = document.getElementsByClassName("srv-crid-sec1-row srv-crid-sec1-row3 layout-wrap layout-align-start-start layout-row")[0].getElementsByClassName("clipboard ng-binding")[0].innerText;
alert("IP : "+ip+" Username : "+username+" Pass :"+password);

chrome.runtime.sendMessage({"action":"openBrowser","ip":ip,"username":username,"password":password,login:"login"},function(r){
    // process response from background script if you need, hide button, for example
});