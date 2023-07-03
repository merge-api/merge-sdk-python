# MergePythonSDK.crm.CustomObjectsApi

All URIs are relative to *https://api.merge.dev/api/crm/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_object_classes_custom_objects_create**](CustomObjectsApi.md#custom_object_classes_custom_objects_create) | **POST** /custom-object-classes/{custom_object_class_id}/custom-objects | 
[**custom_object_classes_custom_objects_list**](CustomObjectsApi.md#custom_object_classes_custom_objects_list) | **GET** /custom-object-classes/{custom_object_class_id}/custom-objects | 
[**custom_object_classes_custom_objects_meta_patch_retrieve**](CustomObjectsApi.md#custom_object_classes_custom_objects_meta_patch_retrieve) | **GET** /custom-object-classes/{custom_object_class_id}/custom-objects/meta/patch/{id} | 
[**custom_object_classes_custom_objects_meta_post_retrieve**](CustomObjectsApi.md#custom_object_classes_custom_objects_meta_post_retrieve) | **GET** /custom-object-classes/{custom_object_class_id}/custom-objects/meta/post | 
[**custom_object_classes_custom_objects_partial_update**](CustomObjectsApi.md#custom_object_classes_custom_objects_partial_update) | **PATCH** /custom-object-classes/{custom_object_class_id}/custom-objects/{id} | 
[**custom_object_classes_custom_objects_retrieve**](CustomObjectsApi.md#custom_object_classes_custom_objects_retrieve) | **GET** /custom-object-classes/{custom_object_class_id}/custom-objects/{id} | 


# **custom_object_classes_custom_objects_create**
> CRMCustomObjectResponse custom_object_classes_custom_objects_create(custom_object_class_id, crm_custom_object_endpoint_request)



Creates a `CustomObject` object with the given values.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.crm
from MergePythonSDK.crm.api import custom_objects_api
from MergePythonSDK.crm.model.crm_custom_object_endpoint_request import CRMCustomObjectEndpointRequest
from MergePythonSDK.crm.model.crm_custom_object_response import CRMCustomObjectResponse
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
    api_instance = custom_objects_api.CustomObjectsApi(api_client)
    custom_object_class_id = "custom_object_class_id_example" # str | 
    crm_custom_object_endpoint_request = CRMCustomObjectEndpointRequest(
        model=CustomObjectRequest(
            fields={
                "key": None,
            },
        ),
    ) # CRMCustomObjectEndpointRequest | 
    is_debug_mode = True # bool | Whether to include debug fields (such as log file links) in the response. (optional)
    run_async = True # bool | Whether or not third-party updates should be run asynchronously. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.custom_object_classes_custom_objects_create(custom_object_class_id, crm_custom_object_endpoint_request)
        pprint(api_response)
    except MergePythonSDK.crm.ApiException as e:
        print("Exception when calling CustomObjectsApi->custom_object_classes_custom_objects_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.custom_object_classes_custom_objects_create(custom_object_class_id, crm_custom_object_endpoint_request, is_debug_mode=is_debug_mode, run_async=run_async)
        pprint(api_response)
    except MergePythonSDK.crm.ApiException as e:
        print("Exception when calling CustomObjectsApi->custom_object_classes_custom_objects_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_object_class_id** | **str**|  |
 **crm_custom_object_endpoint_request** | [**CRMCustomObjectEndpointRequest**](CRMCustomObjectEndpointRequest.md)|  |
 **is_debug_mode** | **bool**| Whether to include debug fields (such as log file links) in the response. | [optional]
 **run_async** | **bool**| Whether or not third-party updates should be run asynchronously. | [optional]

### Return type

[**CRMCustomObjectResponse**](CRMCustomObjectResponse.md)

### Authorization

[accountTokenAuth](../README.md#accountTokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_object_classes_custom_objects_list**
> PaginatedCustomObjectList custom_object_classes_custom_objects_list(custom_object_class_id)



Returns a list of `CustomObject` objects.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.crm
from MergePythonSDK.crm.api import custom_objects_api

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
    api_instance = custom_objects_api.CustomObjectsApi(api_client)
    custom_object_class_id = "custom_object_class_id_example" # str | 
    created_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created after this datetime. (optional)
    created_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created before this datetime. (optional)
    cursor = "cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw" # str | The pagination cursor value. (optional)
    include_deleted_data = True # bool | Whether to include data that was marked as deleted by third party webhooks. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)
    include_remote_fields = True # bool | Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format. (optional)
    modified_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, only objects synced by Merge after this date time will be returned. (optional)
    modified_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, only objects synced by Merge before this date time will be returned. (optional)
    page_size = 1 # int | Number of results to return per page. (optional)
    remote_id = "remote_id_example" # str, none_type | The API provider's ID for the given object. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.custom_object_classes_custom_objects_list(custom_object_class_id)
        pprint(api_response)
    except MergePythonSDK.crm.ApiException as e:
        print("Exception when calling CustomObjectsApi->custom_object_classes_custom_objects_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.custom_object_classes_custom_objects_list(custom_object_class_id, created_after=created_after, created_before=created_before, cursor=cursor, include_deleted_data=include_deleted_data, include_remote_data=include_remote_data, include_remote_fields=include_remote_fields, modified_after=modified_after, modified_before=modified_before, page_size=page_size, remote_id=remote_id)
        pprint(api_response)
    except MergePythonSDK.crm.ApiException as e:
        print("Exception when calling CustomObjectsApi->custom_object_classes_custom_objects_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_object_class_id** | **str**|  |
 **created_after** | **datetime**| If provided, will only return objects created after this datetime. | [optional]
 **created_before** | **datetime**| If provided, will only return objects created before this datetime. | [optional]
 **cursor** | **str**| The pagination cursor value. | [optional]
 **include_deleted_data** | **bool**| Whether to include data that was marked as deleted by third party webhooks. | [optional]
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]
 **include_remote_fields** | **bool**| Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format. | [optional]
 **modified_after** | **datetime**| If provided, only objects synced by Merge after this date time will be returned. | [optional]
 **modified_before** | **datetime**| If provided, only objects synced by Merge before this date time will be returned. | [optional]
 **page_size** | **int**| Number of results to return per page. | [optional]
 **remote_id** | **str, none_type**| The API provider&#39;s ID for the given object. | [optional]

### Return type

[**PaginatedCustomObjectList**](PaginatedCustomObjectList.md)

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

# **custom_object_classes_custom_objects_meta_patch_retrieve**
> MetaResponse custom_object_classes_custom_objects_meta_patch_retrieve(custom_object_class_id, id)



Returns metadata for `CRMCustomObject` PATCHs.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.crm
from MergePythonSDK.crm.api import custom_objects_api
from MergePythonSDK.crm.model.meta_response import MetaResponse
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
    api_instance = custom_objects_api.CustomObjectsApi(api_client)
    custom_object_class_id = "custom_object_class_id_example" # str | 
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.custom_object_classes_custom_objects_meta_patch_retrieve(custom_object_class_id, id)
        pprint(api_response)
    except MergePythonSDK.crm.ApiException as e:
        print("Exception when calling CustomObjectsApi->custom_object_classes_custom_objects_meta_patch_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_object_class_id** | **str**|  |
 **id** | **str**|  |

### Return type

[**MetaResponse**](MetaResponse.md)

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

# **custom_object_classes_custom_objects_meta_post_retrieve**
> MetaResponse custom_object_classes_custom_objects_meta_post_retrieve(custom_object_class_id)



Returns metadata for `CRMCustomObject` POSTs.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.crm
from MergePythonSDK.crm.api import custom_objects_api
from MergePythonSDK.crm.model.meta_response import MetaResponse
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
    api_instance = custom_objects_api.CustomObjectsApi(api_client)
    custom_object_class_id = "custom_object_class_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.custom_object_classes_custom_objects_meta_post_retrieve(custom_object_class_id)
        pprint(api_response)
    except MergePythonSDK.crm.ApiException as e:
        print("Exception when calling CustomObjectsApi->custom_object_classes_custom_objects_meta_post_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_object_class_id** | **str**|  |

### Return type

[**MetaResponse**](MetaResponse.md)

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

# **custom_object_classes_custom_objects_partial_update**
> CRMCustomObjectResponse custom_object_classes_custom_objects_partial_update(custom_object_class_id, id, patched_crm_custom_object_endpoint_request)



Updates a `CustomObject` object with the given `id`.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.crm
from MergePythonSDK.crm.api import custom_objects_api
from MergePythonSDK.crm.model.patched_crm_custom_object_endpoint_request import PatchedCRMCustomObjectEndpointRequest
from MergePythonSDK.crm.model.crm_custom_object_response import CRMCustomObjectResponse
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
    api_instance = custom_objects_api.CustomObjectsApi(api_client)
    custom_object_class_id = "custom_object_class_id_example" # str | 
    id = "id_example" # str | 
    patched_crm_custom_object_endpoint_request = PatchedCRMCustomObjectEndpointRequest(
        model=CustomObjectRequest(
            fields={
                "key": None,
            },
        ),
    ) # PatchedCRMCustomObjectEndpointRequest | 
    is_debug_mode = True # bool | Whether to include debug fields (such as log file links) in the response. (optional)
    run_async = True # bool | Whether or not third-party updates should be run asynchronously. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.custom_object_classes_custom_objects_partial_update(custom_object_class_id, id, patched_crm_custom_object_endpoint_request)
        pprint(api_response)
    except MergePythonSDK.crm.ApiException as e:
        print("Exception when calling CustomObjectsApi->custom_object_classes_custom_objects_partial_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.custom_object_classes_custom_objects_partial_update(custom_object_class_id, id, patched_crm_custom_object_endpoint_request, is_debug_mode=is_debug_mode, run_async=run_async)
        pprint(api_response)
    except MergePythonSDK.crm.ApiException as e:
        print("Exception when calling CustomObjectsApi->custom_object_classes_custom_objects_partial_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_object_class_id** | **str**|  |
 **id** | **str**|  |
 **patched_crm_custom_object_endpoint_request** | [**PatchedCRMCustomObjectEndpointRequest**](PatchedCRMCustomObjectEndpointRequest.md)|  |
 **is_debug_mode** | **bool**| Whether to include debug fields (such as log file links) in the response. | [optional]
 **run_async** | **bool**| Whether or not third-party updates should be run asynchronously. | [optional]

### Return type

[**CRMCustomObjectResponse**](CRMCustomObjectResponse.md)

### Authorization

[accountTokenAuth](../README.md#accountTokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_object_classes_custom_objects_retrieve**
> CustomObject custom_object_classes_custom_objects_retrieve(custom_object_class_id, id)



Returns a `CustomObject` object with the given `id`.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.crm
from MergePythonSDK.crm.api import custom_objects_api
from MergePythonSDK.crm.model.custom_object import CustomObject
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
    api_instance = custom_objects_api.CustomObjectsApi(api_client)
    custom_object_class_id = "custom_object_class_id_example" # str | 
    id = "id_example" # str | 
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)
    include_remote_fields = True # bool | Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.custom_object_classes_custom_objects_retrieve(custom_object_class_id, id)
        pprint(api_response)
    except MergePythonSDK.crm.ApiException as e:
        print("Exception when calling CustomObjectsApi->custom_object_classes_custom_objects_retrieve: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.custom_object_classes_custom_objects_retrieve(custom_object_class_id, id, include_remote_data=include_remote_data, include_remote_fields=include_remote_fields)
        pprint(api_response)
    except MergePythonSDK.crm.ApiException as e:
        print("Exception when calling CustomObjectsApi->custom_object_classes_custom_objects_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_object_class_id** | **str**|  |
 **id** | **str**|  |
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]
 **include_remote_fields** | **bool**| Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format. | [optional]

### Return type

[**CustomObject**](CustomObject.md)

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

