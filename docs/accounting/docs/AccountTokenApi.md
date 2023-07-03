# MergePythonSDK.accounting.AccountTokenApi

All URIs are relative to *https://api.merge.dev/api/accounting/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_token_retrieve**](AccountTokenApi.md#account_token_retrieve) | **GET** /account-token/{public_token} | 


# **account_token_retrieve**
> AccountToken account_token_retrieve(public_token)



Returns the account token for the end user with the provided public token.

### Example

* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.accounting
from MergePythonSDK.accounting.api import account_token_api
from MergePythonSDK.accounting.model.account_token import AccountToken
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

# Configure Bearer authorization: bearerAuth
configuration = MergePythonSDK.accounting.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with MergePythonSDK.accounting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = account_token_api.AccountTokenApi(api_client)
    public_token = "public_token_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.account_token_retrieve(public_token)
        pprint(api_response)
    except MergePythonSDK.accounting.ApiException as e:
        print("Exception when calling AccountTokenApi->account_token_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_token** | **str**|  |

### Return type

[**AccountToken**](AccountToken.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
