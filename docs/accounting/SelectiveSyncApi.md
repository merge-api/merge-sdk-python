# MergePythonSDK.accounting.SelectiveSyncApi

All URIs are relative to *https://api.merge.dev/api/accounting/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**selective_sync_configurations_list**](SelectiveSyncApi.md#selective_sync_configurations_list) | **GET** /selective-sync/configurations | 
[**selective_sync_configurations_update**](SelectiveSyncApi.md#selective_sync_configurations_update) | **PUT** /selective-sync/configurations | 
[**selective_sync_meta_list**](SelectiveSyncApi.md#selective_sync_meta_list) | **GET** /selective-sync/meta | 


# **selective_sync_configurations_list**
> [LinkedAccountSelectiveSyncConfiguration] selective_sync_configurations_list()



Get a linked account's selective syncs.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.accounting
from MergePythonSDK.accounting.api import selective_sync_api
from MergePythonSDK.accounting.model.linked_account_selective_sync_configuration import LinkedAccountSelectiveSyncConfiguration
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
    api_instance = selective_sync_api.SelectiveSyncApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.selective_sync_configurations_list()
        pprint(api_response)
    except MergePythonSDK.accounting.ApiException as e:
        print("Exception when calling SelectiveSyncApi->selective_sync_configurations_list: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[LinkedAccountSelectiveSyncConfiguration]**](LinkedAccountSelectiveSyncConfiguration.md)

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

# **selective_sync_configurations_update**
> [LinkedAccountSelectiveSyncConfiguration] selective_sync_configurations_update(linked_account_selective_sync_configuration_list_request)



Replace a linked account's selective syncs.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.accounting
from MergePythonSDK.accounting.api import selective_sync_api
from MergePythonSDK.accounting.model.linked_account_selective_sync_configuration_list_request import LinkedAccountSelectiveSyncConfigurationListRequest
from MergePythonSDK.accounting.model.linked_account_selective_sync_configuration import LinkedAccountSelectiveSyncConfiguration
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
    api_instance = selective_sync_api.SelectiveSyncApi(api_client)
    linked_account_selective_sync_configuration_list_request = LinkedAccountSelectiveSyncConfigurationListRequest(
        sync_configurations=[
            LinkedAccountSelectiveSyncConfigurationRequest(
                linked_account_conditions=[
                    LinkedAccountConditionRequest(
                        condition_schema_id="condition_schema_id_example",
                        operator="operator_example",
                        value=None,
                    ),
                ],
            ),
        ],
    ) # LinkedAccountSelectiveSyncConfigurationListRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.selective_sync_configurations_update(linked_account_selective_sync_configuration_list_request)
        pprint(api_response)
    except MergePythonSDK.accounting.ApiException as e:
        print("Exception when calling SelectiveSyncApi->selective_sync_configurations_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linked_account_selective_sync_configuration_list_request** | [**LinkedAccountSelectiveSyncConfigurationListRequest**](LinkedAccountSelectiveSyncConfigurationListRequest.md)|  |

### Return type

[**[LinkedAccountSelectiveSyncConfiguration]**](LinkedAccountSelectiveSyncConfiguration.md)

### Authorization

[accountTokenAuth](../README.md#accountTokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **selective_sync_meta_list**
> PaginatedConditionSchemaList selective_sync_meta_list()



Get metadata for the conditions available to a linked account.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.accounting
from MergePythonSDK.accounting.api import selective_sync_api
from MergePythonSDK.accounting.model.paginated_condition_schema_list import PaginatedConditionSchemaList
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
    api_instance = selective_sync_api.SelectiveSyncApi(api_client)
    common_model = "common_model_example" # str |  (optional)
    cursor = "cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw" # str | The pagination cursor value. (optional)
    page_size = 1 # int | Number of results to return per page. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.selective_sync_meta_list(common_model=common_model, cursor=cursor, page_size=page_size)
        pprint(api_response)
    except MergePythonSDK.accounting.ApiException as e:
        print("Exception when calling SelectiveSyncApi->selective_sync_meta_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **common_model** | **str**|  | [optional]
 **cursor** | **str**| The pagination cursor value. | [optional]
 **page_size** | **int**| Number of results to return per page. | [optional]

### Return type

[**PaginatedConditionSchemaList**](PaginatedConditionSchemaList.md)

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

