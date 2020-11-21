// Copyright 2018 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

'use strict';

let launchTerminal = document.getElementById('launchTerminal');

chrome.storage.sync.get('color', function(data) {
  //launchTerminal.style.backgroundColor = data.color;
 // launchTerminal.setAttribute('value', data.color);
 // launchTerminal.setContent = 'Launch Terminal'
  
});

launchTerminal.onclick = function(element) {
  let color = element.target.value;
  chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    chrome.tabs.executeScript(
        tabs[0].id,
        {code: 'document.body.style.backgroundColor = "' + color + '";'});
        chrome.tabs.executeScript(null, {
          file: 'content_script.js'
        });
  });
};
