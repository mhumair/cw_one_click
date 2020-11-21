// Copyright 2018 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

'use strict';

var port = chrome.runtime.connectNative("one_click");

/*
Listen for messages from the app.
*/
port.onMessage.addListener((response) => {
  console.log("Received: " + response);
});


chrome.runtime.onInstalled.addListener(function() {
  //console.log('The color is green.');
  chrome.storage.sync.set({color: '#3aa757'}, function() {
    console.log('The color is green.');
  });
  chrome.declarativeContent.onPageChanged.removeRules(undefined, function() {
    chrome.declarativeContent.onPageChanged.addRules([{
      conditions: [new chrome.declarativeContent.PageStateMatcher({
        pageUrl: {hostEquals: 'platform.cloudways.com'},
      })],
      actions: [new chrome.declarativeContent.ShowPageAction()]
    }]);
  });
});
chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
    //console.log(request);
    if("action" in request && request.action == 'openBrowser'){
       console.log(request.ip)
       console.log("Sending:  ping");
      // chrome.extension.getBackgroundPage().console.log('hello');
       port.postMessage(request);
    }
  }
);
