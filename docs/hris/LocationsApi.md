# MergePythonSDK.hris.LocationsApi

All URIs are relative to *https://api.merge.dev/api/hris/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**locations_list**](LocationsApi.md#locations_list) | **GET** /locations | 
[**locations_retrieve**](LocationsApi.md#locations_retrieve) | **GET** /locations/{id} | 


# **locations_list**
> PaginatedLocationList locations_list()



Returns a list of `Location` objects.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.hris
from MergePythonSDK.hris.api import locations_api
from MergePythonSDK.hris.model.paginated_location_list import PaginatedLocationList
from pprint import pprint
# Defining the host is optional and defaults to https://api.merge.dev/api/hris/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = MergePythonSDK.hris.Configuration(
    host = "https://api.merge.dev/api/hris/v1"
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
configuration = MergePythonSDK.hris.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with MergePythonSDK.hris.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = locations_api.LocationsApi(api_client)
    created_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created after this datetime. (optional)
    created_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created before this datetime. (optional)
    cursor = "cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw" # str | The pagination cursor value. (optional)
    include_deleted_data = True # bool | Whether to include data that was marked as deleted by third party webhooks. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)
    modified_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, only objects synced by Merge after this date time will be returned. (optional)
    modified_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, only objects synced by Merge before this date time will be returned. (optional)
    page_size = 1 # int | Number of results to return per page. (optional)
    remote_fields = "location_type" # str | Deprecated. Use show_enum_origins. (optional) if omitted the server will use the default value of "location_type"
    remote_id = "remote_id_example" # str, none_type | The API provider's ID for the given object. (optional)
    show_enum_origins = "location_type" # str | Which fields should be returned in non-normalized form. (optional) if omitted the server will use the default value of "location_type"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.locations_list(created_after=created_after, created_before=created_before, cursor=cursor, include_deleted_data=include_deleted_data, include_remote_data=include_remote_data, modified_after=modified_after, modified_before=modified_before, page_size=page_size, remote_fields=remote_fields, remote_id=remote_id, show_enum_origins=show_enum_origins)
        pprint(api_response)
    except MergePythonSDK.hris.ApiException as e:
        print("Exception when calling LocationsApi->locations_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **created_after** | **datetime**| If provided, will only return objects created after this datetime. | [optional]
 **created_before** | **datetime**| If provided, will only return objects created before this datetime. | [optional]
 **cursor** | **str**| The pagination cursor value. | [optional]
 **include_deleted_data** | **bool**| Whether to include data that was marked as deleted by third party webhooks. | [optional]
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]
 **modified_after** | **datetime**| If provided, only objects synced by Merge after this date time will be returned. | [optional]
 **modified_before** | **datetime**| If provided, only objects synced by Merge before this date time will be returned. | [optional]
 **page_size** | **int**| Number of results to return per page. | [optional]
 **remote_fields** | **str**| Deprecated. Use show_enum_origins. | [optional] if omitted the server will use the default value of "location_type"
 **remote_id** | **str, none_type**| The API provider&#39;s ID for the given object. | [optional]
 **show_enum_origins** | **str**| Which fields should be returned in non-normalized form. | [optional] if omitted the server will use the default value of "location_type"

### Return type

[**PaginatedLocationList**](PaginatedLocationList.md)

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

# **locations_retrieve**
> Location locations_retrieve(id)



Returns a `Location` object with the given `id`.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.hris
from MergePythonSDK.hris.api import locations_api
from MergePythonSDK.hris.model.location import Location
from pprint import pprint
# Defining the host is optional and defaults to https://api.merge.dev/api/hris/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = MergePythonSDK.hris.Configuration(
    host = "https://api.merge.dev/api/hris/v1"
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
configuration = MergePythonSDK.hris.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with MergePythonSDK.hris.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = locations_api.LocationsApi(api_client)
    id = "id_example" # str | 
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)
    remote_fields = "location_type" # str | Deprecated. Use show_enum_origins. (optional) if omitted the server will use the default value of "location_type"
    show_enum_origins = "location_type" # str | Which fields should be returned in non-normalized form. (optional) if omitted the server will use the default value of "location_type"

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.locations_retrieve(id)
        pprint(api_response)
    except MergePythonSDK.hris.ApiException as e:
        print("Exception when calling LocationsApi->locations_retrieve: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.locations_retrieve(id, include_remote_data=include_remote_data, remote_fields=remote_fields, show_enum_origins=show_enum_origins)
        pprint(api_response)
    except MergePythonSDK.hris.ApiException as e:
        print("Exception when calling LocationsApi->locations_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]
 **remote_fields** | **str**| Deprecated. Use show_enum_origins. | [optional] if omitted the server will use the default value of "location_type"
 **show_enum_origins** | **str**| Which fields should be returned in non-normalized form. | [optional] if omitted the server will use the default value of "location_type"

### Return type

[**Location**](Location.md)

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

