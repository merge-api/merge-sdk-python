# MergePythonSDK.ticketing.ForceResyncApi

All URIs are relative to *https://api.merge.dev/api/ticketing/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sync_status_resync_create**](ForceResyncApi.md#sync_status_resync_create) | **POST** /sync-status/resync | 


# **sync_status_resync_create**
> [SyncStatus] sync_status_resync_create(x_account_token)



Force re-sync of all models. This is available for all organizations via the dashboard. Force re-sync is also available programmatically via API for monthly, quarterly, and highest sync frequency customers on the Core, Professional, or Enterprise plans. Doing so will consume a sync credit for the relevant linked account.

### Example

* Api Key Authentication (tokenAuth):

```python
import time
import MergePythonSDK.ticketing
from MergePythonSDK.ticketing.api import force_resync_api
from MergePythonSDK.ticketing.model.sync_status import SyncStatus
from pprint import pprint
# Defining the host is optional and defaults to https://api.merge.dev/api/ticketing/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = MergePythonSDK.ticketing.Configuration(
    host = "https://api.merge.dev/api/ticketing/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with MergePythonSDK.ticketing.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = force_resync_api.ForceResyncApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.sync_status_resync_create(x_account_token)
        pprint(api_response)
    except MergePythonSDK.ticketing.ApiException as e:
        print("Exception when calling ForceResyncApi->sync_status_resync_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |

### Return type

[**[SyncStatus]**](SyncStatus.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

