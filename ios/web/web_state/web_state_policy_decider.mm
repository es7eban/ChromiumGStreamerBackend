// Copyright 2015 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

#include "ios/web/public/web_state/web_state_policy_decider.h"

#import "ios/web/public/web_state/web_state.h"
#import "ios/web/web_state/web_state_impl.h"

namespace web {

WebStatePolicyDecider::WebStatePolicyDecider(WebState* web_state)
    : web_state_(web_state) {
  DCHECK(web_state_);
  web_state_->AddPolicyDecider(this);
}

WebStatePolicyDecider::~WebStatePolicyDecider() {
  if (web_state_) {
    web_state_->RemovePolicyDecider(this);
  }
}

bool WebStatePolicyDecider::ShouldAllowRequest(NSURLRequest* request) {
  return true;
}

bool WebStatePolicyDecider::ShouldAllowResponse(NSURLResponse* response) {
  return true;
}

void WebStatePolicyDecider::ResetWebState() {
  web_state_->RemovePolicyDecider(this);
  web_state_ = nullptr;
}

}  // namespace web
