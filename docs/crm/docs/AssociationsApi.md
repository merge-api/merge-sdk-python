# MergePythonSDK.crm.AssociationsApi

All URIs are relative to *https://api.merge.dev/api/crm/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_object_classes_custom_objects_associations_list**](AssociationsApi.md#custom_object_classes_custom_objects_associations_list) | **GET** /custom-object-classes/{custom_object_class_id}/custom-objects/{object_id}/associations | 
[**custom_object_classes_custom_objects_associations_update**](AssociationsApi.md#custom_object_classes_custom_objects_associations_update) | **PUT** /custom-object-classes/{source_class_id}/custom-objects/{source_object_id}/associations/{target_class_id}/{target_object_id}/{association_type_id} | 


# **custom_object_classes_custom_objects_associations_list**
> PaginatedAssociationList custom_object_classes_custom_objects_associations_list(custom_object_class_id, object_id)



Returns a list of `Association` objects.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.crm
from MergePythonSDK.crm.api import associations_api

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
    api_instance = associations_api.AssociationsApi(api_client)
    custom_object_class_id = "custom_object_class_id_example" # str | 
    object_id = "object_id_example" # str | 
    association_type_id = "association_type_id_example" # str | If provided, will only return opportunities with this association_type. (optional)
    created_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created after this datetime. (optional)
    created_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created before this datetime. (optional)
    cursor = "cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw" # str | The pagination cursor value. (optional)
    expand = "association_type" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional) if omitted the server will use the default value of "association_type"
    include_deleted_data = True # bool | Whether to include data that was marked as deleted by third party webhooks. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)
    modified_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, only objects synced by Merge after this date time will be returned. (optional)
    modified_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, only objects synced by Merge before this date time will be returned. (optional)
    page_size = 1 # int | Number of results to return per page. (optional)
    remote_id = "remote_id_example" # str, none_type | The API provider's ID for the given object. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.custom_object_classes_custom_objects_associations_list(custom_object_class_id, object_id)
        pprint(api_response)
    except MergePythonSDK.crm.ApiException as e:
        print("Exception when calling AssociationsApi->custom_object_classes_custom_objects_associations_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.custom_object_classes_custom_objects_associations_list(custom_object_class_id, object_id, association_type_id=association_type_id, created_after=created_after, created_before=created_before, cursor=cursor, expand=expand, include_deleted_data=include_deleted_data, include_remote_data=include_remote_data, modified_after=modified_after, modified_before=modified_before, page_size=page_size, remote_id=remote_id)
        pprint(api_response)
    except MergePythonSDK.crm.ApiException as e:
        print("Exception when calling AssociationsApi->custom_object_classes_custom_objects_associations_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_object_class_id** | **str**|  |
 **object_id** | **str**|  |
 **association_type_id** | **str**| If provided, will only return opportunities with this association_type. | [optional]
 **created_after** | **datetime**| If provided, will only return objects created after this datetime. | [optional]
 **created_before** | **datetime**| If provided, will only return objects created before this datetime. | [optional]
 **cursor** | **str**| The pagination cursor value. | [optional]
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional] if omitted the server will use the default value of "association_type"
 **include_deleted_data** | **bool**| Whether to include data that was marked as deleted by third party webhooks. | [optional]
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]
 **modified_after** | **datetime**| If provided, only objects synced by Merge after this date time will be returned. | [optional]
 **modified_before** | **datetime**| If provided, only objects synced by Merge before this date time will be returned. | [optional]
 **page_size** | **int**| Number of results to return per page. | [optional]
 **remote_id** | **str, none_type**| The API provider&#39;s ID for the given object. | [optional]

### Return type

[**PaginatedAssociationList**](PaginatedAssociationList.md)

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

# **custom_object_classes_custom_objects_associations_update**
> Association custom_object_classes_custom_objects_associations_update(association_type_id, source_class_id, source_object_id, target_class_id, target_object_id)



Creates an Association between `source_object_id` and `target_object_id` of type `association_type_id`.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.crm
from MergePythonSDK.crm.api import associations_api
from MergePythonSDK.crm.model.association import Association
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
    api_instance = associations_api.AssociationsApi(api_client)
    association_type_id = "association_type_id_example" # str | 
    source_class_id = "source_class_id_example" # str | 
    source_object_id = "source_object_id_example" # str | 
    target_class_id = "target_class_id_example" # str | 
    target_object_id = "target_object_id_example" # str | 
    is_debug_mode = True # bool | Whether to include debug fields (such as log file links) in the response. (optional)
    run_async = True # bool | Whether or not third-party updates should be run asynchronously. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.custom_object_classes_custom_objects_associations_update(association_type_id, source_class_id, source_object_id, target_class_id, target_object_id)
        pprint(api_response)
    except MergePythonSDK.crm.ApiException as e:
        print("Exception when calling AssociationsApi->custom_object_classes_custom_objects_associations_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.custom_object_classes_custom_objects_associations_update(association_type_id, source_class_id, source_object_id, target_class_id, target_object_id, is_debug_mode=is_debug_mode, run_async=run_async)
        pprint(api_response)
    except MergePythonSDK.crm.ApiException as e:
        print("Exception when calling AssociationsApi->custom_object_classes_custom_objects_associations_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **association_type_id** | **str**|  |
 **source_class_id** | **str**|  |
 **source_object_id** | **str**|  |
 **target_class_id** | **str**|  |
 **target_object_id** | **str**|  |
 **is_debug_mode** | **bool**| Whether to include debug fields (such as log file links) in the response. | [optional]
 **run_async** | **bool**| Whether or not third-party updates should be run asynchronously. | [optional]

### Return type

[**Association**](Association.md)

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

