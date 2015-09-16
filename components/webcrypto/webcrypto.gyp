# Copyright 2015 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'targets': [
    {
      'target_name': 'webcrypto',
      'type': 'static_library',
      'dependencies': [
        '../../base/base.gyp:base',
        '../../crypto/crypto.gyp:crypto',
        '../../third_party/boringssl/boringssl.gyp:boringssl',
        '../../third_party/WebKit/public/blink.gyp:blink',
      ],
      'include_dirs': [
        '..',
      ],
      'sources': [
        'algorithm_dispatch.cc',
        'algorithm_dispatch.h',
        'algorithm_implementation.cc',
        'algorithm_implementation.h',
        'algorithm_registry.cc',
        'algorithm_registry.h',
        'algorithms/aes.cc',
        'algorithms/aes.h',
        'algorithms/aes_cbc.cc',
        'algorithms/aes_ctr.cc',
        'algorithms/aes_gcm.cc',
        'algorithms/aes_kw.cc',
        'algorithms/ec.cc',
        'algorithms/ec.h',
        'algorithms/ecdh.cc',
        'algorithms/ecdsa.cc',
        'algorithms/hkdf.cc',
        'algorithms/hmac.cc',
        'algorithms/key.cc',
        'algorithms/key.h',
        'algorithms/pbkdf2.cc',
        'algorithms/rsa.cc',
        'algorithms/rsa.h',
        'algorithms/rsa_oaep.cc',
        'algorithms/rsa_pss.cc',
        'algorithms/rsa_sign.cc',
        'algorithms/rsa_sign.h',
        'algorithms/rsa_ssa.cc',
        'algorithms/sha.cc',
        'algorithms/util_openssl.cc',
        'algorithms/util_openssl.h',
        'crypto_data.cc',
        'crypto_data.h',
        'generate_key_result.cc',
        'generate_key_result.h',
        'jwk.cc',
        'jwk.h',
        'platform_crypto.h',
        'status.cc',
        'status.h',
        'webcrypto_impl.cc',
        'webcrypto_impl.h',
        'webcrypto_util.cc',
        'webcrypto_util.h',
      ],
    },
  ],
}
