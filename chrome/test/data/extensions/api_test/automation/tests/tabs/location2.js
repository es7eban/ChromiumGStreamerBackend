// Copyright 2016 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

var allTests = [
  // This is a regression test for a particular layout where the
  // automation API was returning the wrong location for an element.
  // See ../../sites/location2.html for the layout.
  function testLocation2() {
    var textbox = rootNode.find({ role: RoleType.textField });
    assertEq(0, textbox.location.left - rootNode.location.left);
    assertEq(100, textbox.location.top - rootNode.location.top);
    chrome.test.succeed();
  }
];

setUpAndRunTests(allTests, 'location2.html');
