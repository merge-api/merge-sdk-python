# MergePythonSDK.accounting.PassthroughApi

All URIs are relative to *https://api.merge.dev/api/accounting/v1*

| Method                                                         | HTTP request          | Description |
| -------------------------------------------------------------- | --------------------- | ----------- |
| [**passthrough_create**](PassthroughApi.md#passthrough_create) | **POST** /passthrough |

# **passthrough_create**

> RemoteResponse passthrough_create(data_passthrough_request)

Pull data from an endpoint not currently supported by Merge.

### Example

- Api Key Authentication (accountTokenAuth):
- Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.accounting
from MergePythonSDK.accounting.api import passthrough_api
from MergePythonSDK.shared.model.remote_response import RemoteResponse
from MergePythonSDK.accounting.model.data_passthrough_request import DataPassthroughRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.merge.dev/api/accounting/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = MergePythonSDK.accounting.Configuration(
    host = "https://api.merge.dev/api/accounting/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: accountTokenAuth
configuration.api_key['accountTokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accountTokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = MergePythonSDK.accounting.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with MergePythonSDK.accounting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = passthrough_api.PassthroughApi(api_client)
    data_passthrough_request = DataPassthroughRequest(
        method=None,
        path="/scooters",
        base_url_override="base_url_override_example",
        data="{"company": "Lime", "model": "Gen 2.5"}",
        multipart_form_data=[
            MultipartFormFieldRequest(
                name="resume",
                data="SW50ZWdyYXRlIGZhc3QKSW50ZWdyYXRlIG9uY2U=",
                encoding=None,
                file_name="resume.pdf",
                content_type="application/pdf",
            ),
        ],
        headers={
            "key": None,
        },
        request_format=None,
        normalize_response=True,
    ) # DataPassthroughRequest |

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.passthrough_create(data_passthrough_request)
        pprint(api_response)
    except MergePythonSDK.accounting.ApiException as e:
        print("Exception when calling PassthroughApi->passthrough_create: %s\n" % e)
```

### Parameters

| Name                         | Type                                                    | Description | Notes |
| ---------------------------- | ------------------------------------------------------- | ----------- | ----- |
| **data_passthrough_request** | [**DataPassthroughRequest**](DataPassthroughRequest.md) |             |

### Return type

[**RemoteResponse**](RemoteResponse.md)

### Authorization

[accountTokenAuth](../README.md#accountTokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
| ----------- | ----------- | ---------------- |
| **200**     |             | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
