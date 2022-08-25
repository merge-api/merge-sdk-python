# MergePythonSDK.crm.ForceResyncApi

All URIs are relative to *https://api.merge.dev/api/crm/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sync_status_resync_create**](ForceResyncApi.md#sync_status_resync_create) | **POST** /sync-status/resync | 


# **sync_status_resync_create**
> [SyncStatus] sync_status_resync_create()



Force re-sync of all models. This is only available for organizations on Merge's Grow and Expand plans.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.crm
from MergePythonSDK.crm.api import force_resync_api
from MergePythonSDK.crm.model.sync_status import SyncStatus
from pprint import pprint
# Defining the host is optional and defaults to https://api.merge.dev/api/crm/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = MergePythonSDK.crm.Configuration(
    host = "https://api.merge.dev/api/crm/v1"
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
configuration = MergePythonSDK.crm.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with MergePythonSDK.crm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = force_resync_api.ForceResyncApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.sync_status_resync_create()
        pprint(api_response)
    except MergePythonSDK.crm.ApiException as e:
        print("Exception when calling ForceResyncApi->sync_status_resync_create: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[SyncStatus]**](SyncStatus.md)

### Authorization

[accountTokenAuth](../README.md#accountTokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

