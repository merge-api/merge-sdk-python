# MergePythonSDK.ticketing.CollectionsApi

All URIs are relative to *https://api.merge.dev/api/ticketing/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**collections_list**](CollectionsApi.md#collections_list) | **GET** /collections | 
[**collections_retrieve**](CollectionsApi.md#collections_retrieve) | **GET** /collections/{id} | 
[**collections_users_list**](CollectionsApi.md#collections_users_list) | **GET** /collections/{parent_id}/users | 


# **collections_list**
> PaginatedCollectionList collections_list()



Returns a list of `Collection` objects.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.ticketing
from MergePythonSDK.ticketing.api import collections_api

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

# Configure API key authorization: accountTokenAuth
configuration.api_key['accountTokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accountTokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = MergePythonSDK.ticketing.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with MergePythonSDK.ticketing.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = collections_api.CollectionsApi(api_client)
    collection_type = "LIST" # str, none_type | If provided, will only return collections of the given type.  * `LIST` - LIST * `PROJECT` - PROJECT (optional)
    created_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created after this datetime. (optional)
    created_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created before this datetime. (optional)
    cursor = "cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw" # str | The pagination cursor value. (optional)
    expand = "parent_collection" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional) if omitted the server will use the default value of "parent_collection"
    include_deleted_data = True # bool | Whether to include data that was marked as deleted by third party webhooks. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)
    modified_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, only objects synced by Merge after this date time will be returned. (optional)
    modified_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, only objects synced by Merge before this date time will be returned. (optional)
    page_size = 1 # int | Number of results to return per page. (optional)
    parent_collection_id = "parent_collection_id_example" # str | If provided, will only return collections whose parent collection matches the given id. (optional)
    remote_fields = "collection_type" # str | Deprecated. Use show_enum_origins. (optional) if omitted the server will use the default value of "collection_type"
    remote_id = "remote_id_example" # str, none_type | The API provider's ID for the given object. (optional)
    show_enum_origins = "collection_type" # str | Which fields should be returned in non-normalized form. (optional) if omitted the server will use the default value of "collection_type"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.collections_list(collection_type=collection_type, created_after=created_after, created_before=created_before, cursor=cursor, expand=expand, include_deleted_data=include_deleted_data, include_remote_data=include_remote_data, modified_after=modified_after, modified_before=modified_before, page_size=page_size, parent_collection_id=parent_collection_id, remote_fields=remote_fields, remote_id=remote_id, show_enum_origins=show_enum_origins)
        pprint(api_response)
    except MergePythonSDK.ticketing.ApiException as e:
        print("Exception when calling CollectionsApi->collections_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_type** | **str, none_type**| If provided, will only return collections of the given type.  * &#x60;LIST&#x60; - LIST * &#x60;PROJECT&#x60; - PROJECT | [optional]
 **created_after** | **datetime**| If provided, will only return objects created after this datetime. | [optional]
 **created_before** | **datetime**| If provided, will only return objects created before this datetime. | [optional]
 **cursor** | **str**| The pagination cursor value. | [optional]
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional] if omitted the server will use the default value of "parent_collection"
 **include_deleted_data** | **bool**| Whether to include data that was marked as deleted by third party webhooks. | [optional]
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]
 **modified_after** | **datetime**| If provided, only objects synced by Merge after this date time will be returned. | [optional]
 **modified_before** | **datetime**| If provided, only objects synced by Merge before this date time will be returned. | [optional]
 **page_size** | **int**| Number of results to return per page. | [optional]
 **parent_collection_id** | **str**| If provided, will only return collections whose parent collection matches the given id. | [optional]
 **remote_fields** | **str**| Deprecated. Use show_enum_origins. | [optional] if omitted the server will use the default value of "collection_type"
 **remote_id** | **str, none_type**| The API provider&#39;s ID for the given object. | [optional]
 **show_enum_origins** | **str**| Which fields should be returned in non-normalized form. | [optional] if omitted the server will use the default value of "collection_type"

### Return type

[**PaginatedCollectionList**](PaginatedCollectionList.md)

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

# **collections_retrieve**
> Collection collections_retrieve(id)



Returns a `Collection` object with the given `id`.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.ticketing
from MergePythonSDK.ticketing.api import collections_api
from MergePythonSDK.ticketing.model.collection import Collection
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

# Configure API key authorization: accountTokenAuth
configuration.api_key['accountTokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accountTokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = MergePythonSDK.ticketing.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with MergePythonSDK.ticketing.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = collections_api.CollectionsApi(api_client)
    id = "id_example" # str | 
    expand = "parent_collection" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional) if omitted the server will use the default value of "parent_collection"
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)
    remote_fields = "collection_type" # str | Deprecated. Use show_enum_origins. (optional) if omitted the server will use the default value of "collection_type"
    show_enum_origins = "collection_type" # str | Which fields should be returned in non-normalized form. (optional) if omitted the server will use the default value of "collection_type"

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.collections_retrieve(id)
        pprint(api_response)
    except MergePythonSDK.ticketing.ApiException as e:
        print("Exception when calling CollectionsApi->collections_retrieve: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.collections_retrieve(id, expand=expand, include_remote_data=include_remote_data, remote_fields=remote_fields, show_enum_origins=show_enum_origins)
        pprint(api_response)
    except MergePythonSDK.ticketing.ApiException as e:
        print("Exception when calling CollectionsApi->collections_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional] if omitted the server will use the default value of "parent_collection"
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]
 **remote_fields** | **str**| Deprecated. Use show_enum_origins. | [optional] if omitted the server will use the default value of "collection_type"
 **show_enum_origins** | **str**| Which fields should be returned in non-normalized form. | [optional] if omitted the server will use the default value of "collection_type"

### Return type

[**Collection**](Collection.md)

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

# **collections_users_list**
> PaginatedUserList collections_users_list(parent_id)



Returns a list of `User` objects.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.ticketing
from MergePythonSDK.ticketing.api import collections_api

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

# Configure API key authorization: accountTokenAuth
configuration.api_key['accountTokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accountTokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = MergePythonSDK.ticketing.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with MergePythonSDK.ticketing.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = collections_api.CollectionsApi(api_client)
    parent_id = "parent_id_example" # str | 
    cursor = "cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw" # str | The pagination cursor value. (optional)
    expand = "teams" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional) if omitted the server will use the default value of "teams"
    include_deleted_data = True # bool | Whether to include data that was marked as deleted by third party webhooks. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)
    page_size = 1 # int | Number of results to return per page. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.collections_users_list(parent_id)
        pprint(api_response)
    except MergePythonSDK.ticketing.ApiException as e:
        print("Exception when calling CollectionsApi->collections_users_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.collections_users_list(parent_id, cursor=cursor, expand=expand, include_deleted_data=include_deleted_data, include_remote_data=include_remote_data, page_size=page_size)
        pprint(api_response)
    except MergePythonSDK.ticketing.ApiException as e:
        print("Exception when calling CollectionsApi->collections_users_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **str**|  |
 **cursor** | **str**| The pagination cursor value. | [optional]
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional] if omitted the server will use the default value of "teams"
 **include_deleted_data** | **bool**| Whether to include data that was marked as deleted by third party webhooks. | [optional]
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]
 **page_size** | **int**| Number of results to return per page. | [optional]

### Return type

[**PaginatedUserList**](PaginatedUserList.md)

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

