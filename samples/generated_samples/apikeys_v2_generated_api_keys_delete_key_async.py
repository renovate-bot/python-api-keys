# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated code. DO NOT EDIT!
#
# Snippet for DeleteKey
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-api-keys


# [START apikeys_v2_generated_ApiKeys_DeleteKey_async]
from google.cloud import api_keys_v2


async def sample_delete_key():
    # Create a client
    client = api_keys_v2.ApiKeysAsyncClient()

    # Initialize request argument(s)
    request = api_keys_v2.DeleteKeyRequest(
        name="name_value",
    )

    # Make the request
    operation = client.delete_key(request=request)

    print("Waiting for operation to complete...")

    response = await operation.result()

    # Handle the response
    print(response)

# [END apikeys_v2_generated_ApiKeys_DeleteKey_async]
