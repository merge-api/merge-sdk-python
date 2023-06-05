# MergePythonSDK.crm.AssociationTypesApi

All URIs are relative to *https://api.merge.dev/api/crm/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_object_classes_association_types_create**](AssociationTypesApi.md#custom_object_classes_association_types_create) | **POST** /custom-object-classes/{custom_object_class_id}/association-types | 
[**custom_object_classes_association_types_list**](AssociationTypesApi.md#custom_object_classes_association_types_list) | **GET** /custom-object-classes/{custom_object_class_id}/association-types | 
[**custom_object_classes_association_types_meta_post_retrieve**](AssociationTypesApi.md#custom_object_classes_association_types_meta_post_retrieve) | **GET** /custom-object-classes/{custom_object_class_id}/association-types/meta/post | 
[**custom_object_classes_association_types_retrieve**](AssociationTypesApi.md#custom_object_classes_association_types_retrieve) | **GET** /custom-object-classes/{custom_object_class_id}/association-types/{id} | 


# **custom_object_classes_association_types_create**
> CRMAssociationTypeResponse custom_object_classes_association_types_create(x_account_token, custom_object_class_id, crm_association_type_endpoint_request)



Creates an `AssociationType` object with the given values.

### Example

* Api Key Authentication (tokenAuth):

```python
import time
import MergePythonSDK.crm
from MergePythonSDK.crm.api import association_types_api
from MergePythonSDK.crm.model.crm_association_type_response import CRMAssociationTypeResponse
from MergePythonSDK.crm.model.crm_association_type_endpoint_request import CRMAssociationTypeEndpointRequest
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

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with MergePythonSDK.crm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = association_types_api.AssociationTypesApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    custom_object_class_id = "custom_object_class_id_example" # str | 
    crm_association_type_endpoint_request = CRMAssociationTypeEndpointRequest(
        model=AssociationTypeRequestRequest(
            source_object_class=ObjectClassDescriptionRequest(
                id="id_example",
                origin_type=OriginTypeEnum("CUSTOM_OBJECT"),
            ),
            target_object_classes=[
                ObjectClassDescriptionRequest(
                    id="id_example",
                    origin_type=OriginTypeEnum("CUSTOM_OBJECT"),
                ),
            ],
            remote_key_name="remote_key_name_example",
            display_name="display_name_example",
            cardinality=CardinalityEnum("ONE_TO_ONE"),
            is_required=False,
        ),
    ) # CRMAssociationTypeEndpointRequest | 
    is_debug_mode = True # bool | Whether to include debug fields (such as log file links) in the response. (optional)
    run_async = True # bool | Whether or not third-party updates should be run asynchronously. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.custom_object_classes_association_types_create(x_account_token, custom_object_class_id, crm_association_type_endpoint_request)
        pprint(api_response)
    except MergePythonSDK.crm.ApiException as e:
        print("Exception when calling AssociationTypesApi->custom_object_classes_association_types_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.custom_object_classes_association_types_create(x_account_token, custom_object_class_id, crm_association_type_endpoint_request, is_debug_mode=is_debug_mode, run_async=run_async)
        pprint(api_response)
    except MergePythonSDK.crm.ApiException as e:
        print("Exception when calling AssociationTypesApi->custom_object_classes_association_types_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **custom_object_class_id** | **str**|  |
 **crm_association_type_endpoint_request** | [**CRMAssociationTypeEndpointRequest**](CRMAssociationTypeEndpointRequest.md)|  |
 **is_debug_mode** | **bool**| Whether to include debug fields (such as log file links) in the response. | [optional]
 **run_async** | **bool**| Whether or not third-party updates should be run asynchronously. | [optional]

### Return type

[**CRMAssociationTypeResponse**](CRMAssociationTypeResponse.md)

### Authorization

[tokenAuth](../README.md#tokenAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **custom_object_classes_association_types_list**
> PaginatedAssociationTypeList custom_object_classes_association_types_list(x_account_token, custom_object_class_id)



Returns a list of `AssociationType` objects.

### Example

* Api Key Authentication (tokenAuth):

```python
import time
import MergePythonSDK.crm
from MergePythonSDK.crm.api import association_types_api

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

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with MergePythonSDK.crm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = association_types_api.AssociationTypesApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    custom_object_class_id = "custom_object_class_id_example" # str | 
    created_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created after this datetime. (optional)
    created_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created before this datetime. (optional)
    cursor = "cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw" # str | The pagination cursor value. (optional)
    expand = "target_object_classes" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional) if omitted the server will use the default value of "target_object_classes"
    include_deleted_data = True # bool | Whether to include data that was marked as deleted by third party webhooks. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)
    modified_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, only objects synced by Merge after this date time will be returned. (optional)
    modified_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, only objects synced by Merge before this date time will be returned. (optional)
    page_size = 1 # int | Number of results to return per page. (optional)
    remote_id = "remote_id_example" # str, none_type | The API provider's ID for the given object. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.custom_object_classes_association_types_list(x_account_token, custom_object_class_id)
        pprint(api_response)
    except MergePythonSDK.crm.ApiException as e:
        print("Exception when calling AssociationTypesApi->custom_object_classes_association_types_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.custom_object_classes_association_types_list(x_account_token, custom_object_class_id, created_after=created_after, created_before=created_before, cursor=cursor, expand=expand, include_deleted_data=include_deleted_data, include_remote_data=include_remote_data, modified_after=modified_after, modified_before=modified_before, page_size=page_size, remote_id=remote_id)
        pprint(api_response)
    except MergePythonSDK.crm.ApiException as e:
        print("Exception when calling AssociationTypesApi->custom_object_classes_association_types_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **custom_object_class_id** | **str**|  |
 **created_after** | **datetime**| If provided, will only return objects created after this datetime. | [optional]
 **created_before** | **datetime**| If provided, will only return objects created before this datetime. | [optional]
 **cursor** | **str**| The pagination cursor value. | [optional]
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional] if omitted the server will use the default value of "target_object_classes"
 **include_deleted_data** | **bool**| Whether to include data that was marked as deleted by third party webhooks. | [optional]
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]
 **modified_after** | **datetime**| If provided, only objects synced by Merge after this date time will be returned. | [optional]
 **modified_before** | **datetime**| If provided, only objects synced by Merge before this date time will be returned. | [optional]
 **page_size** | **int**| Number of results to return per page. | [optional]
 **remote_id** | **str, none_type**| The API provider&#39;s ID for the given object. | [optional]

### Return type

[**PaginatedAssociationTypeList**](PaginatedAssociationTypeList.md)

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

# **custom_object_classes_association_types_meta_post_retrieve**
> MetaResponse custom_object_classes_association_types_meta_post_retrieve(x_account_token, custom_object_class_id)



Returns metadata for `CRMAssociationType` POSTs.

### Example

* Api Key Authentication (tokenAuth):

```python
import time
import MergePythonSDK.crm
from MergePythonSDK.crm.api import association_types_api
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

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with MergePythonSDK.crm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = association_types_api.AssociationTypesApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    custom_object_class_id = "custom_object_class_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.custom_object_classes_association_types_meta_post_retrieve(x_account_token, custom_object_class_id)
        pprint(api_response)
    except MergePythonSDK.crm.ApiException as e:
        print("Exception when calling AssociationTypesApi->custom_object_classes_association_types_meta_post_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **custom_object_class_id** | **str**|  |

### Return type

[**MetaResponse**](MetaResponse.md)

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

# **custom_object_classes_association_types_retrieve**
> AssociationType custom_object_classes_association_types_retrieve(x_account_token, custom_object_class_id, id)



Returns an `AssociationType` object with the given `id`.

### Example

* Api Key Authentication (tokenAuth):

```python
import time
import MergePythonSDK.crm
from MergePythonSDK.crm.api import association_types_api
from MergePythonSDK.crm.model.association_type import AssociationType
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

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with MergePythonSDK.crm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = association_types_api.AssociationTypesApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    custom_object_class_id = "custom_object_class_id_example" # str | 
    id = "id_example" # str | 
    expand = "target_object_classes" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional) if omitted the server will use the default value of "target_object_classes"
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.custom_object_classes_association_types_retrieve(x_account_token, custom_object_class_id, id)
        pprint(api_response)
    except MergePythonSDK.crm.ApiException as e:
        print("Exception when calling AssociationTypesApi->custom_object_classes_association_types_retrieve: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.custom_object_classes_association_types_retrieve(x_account_token, custom_object_class_id, id, expand=expand, include_remote_data=include_remote_data)
        pprint(api_response)
    except MergePythonSDK.crm.ApiException as e:
        print("Exception when calling AssociationTypesApi->custom_object_classes_association_types_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **custom_object_class_id** | **str**|  |
 **id** | **str**|  |
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional] if omitted the server will use the default value of "target_object_classes"
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]

### Return type

[**AssociationType**](AssociationType.md)

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

