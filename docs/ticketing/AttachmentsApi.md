# MergePythonSDK.ticketing.AttachmentsApi

All URIs are relative to *https://api.merge.dev/api/ticketing/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attachments_create**](AttachmentsApi.md#attachments_create) | **POST** /attachments | 
[**attachments_download_retrieve**](AttachmentsApi.md#attachments_download_retrieve) | **GET** /attachments/{id}/download | 
[**attachments_list**](AttachmentsApi.md#attachments_list) | **GET** /attachments | 
[**attachments_meta_post_retrieve**](AttachmentsApi.md#attachments_meta_post_retrieve) | **GET** /attachments/meta/post | 
[**attachments_retrieve**](AttachmentsApi.md#attachments_retrieve) | **GET** /attachments/{id} | 


# **attachments_create**
> TicketingAttachmentResponse attachments_create(ticketing_attachment_endpoint_request)



Creates an `Attachment` object with the given values.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.ticketing
from MergePythonSDK.ticketing.api import attachments_api
from MergePythonSDK.ticketing.model.ticketing_attachment_response import TicketingAttachmentResponse
from MergePythonSDK.ticketing.model.ticketing_attachment_endpoint_request import TicketingAttachmentEndpointRequest
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
    api_instance = attachments_api.AttachmentsApi(api_client)
    ticketing_attachment_endpoint_request = TicketingAttachmentEndpointRequest(
        model=AttachmentRequest(
            file_name="Screenshot.png",
            ticket="0958cbc6-6040-430a-848e-aafacbadf4ae",
            file_url="http://alturl.com/p749b",
            content_type="jpeg",
            uploaded_by="28b54125-287f-494d-965e-3c5b330c9a68",
            integration_params={
                "key": None,
            },
            linked_account_params={
                "key": None,
            },
        ),
    ) # TicketingAttachmentEndpointRequest | 
    is_debug_mode = True # bool | Whether to include debug fields (such as log file links) in the response. (optional)
    run_async = True # bool | Whether or not third-party updates should be run asynchronously. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.attachments_create(ticketing_attachment_endpoint_request)
        pprint(api_response)
    except MergePythonSDK.ticketing.ApiException as e:
        print("Exception when calling AttachmentsApi->attachments_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.attachments_create(ticketing_attachment_endpoint_request, is_debug_mode=is_debug_mode, run_async=run_async)
        pprint(api_response)
    except MergePythonSDK.ticketing.ApiException as e:
        print("Exception when calling AttachmentsApi->attachments_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticketing_attachment_endpoint_request** | [**TicketingAttachmentEndpointRequest**](TicketingAttachmentEndpointRequest.md)|  |
 **is_debug_mode** | **bool**| Whether to include debug fields (such as log file links) in the response. | [optional]
 **run_async** | **bool**| Whether or not third-party updates should be run asynchronously. | [optional]

### Return type

[**TicketingAttachmentResponse**](TicketingAttachmentResponse.md)

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

# **attachments_download_retrieve**
> file_type attachments_download_retrieve(id)



Returns an `Attachment` object with the given `id`.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.ticketing
from MergePythonSDK.ticketing.api import attachments_api
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
    api_instance = attachments_api.AttachmentsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.attachments_download_retrieve(id)
        pprint(api_response)
    except MergePythonSDK.ticketing.ApiException as e:
        print("Exception when calling AttachmentsApi->attachments_download_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**file_type**

### Authorization

[accountTokenAuth](../README.md#accountTokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attachments_list**
> PaginatedAttachmentList attachments_list()



Returns a list of `Attachment` objects.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.ticketing
from MergePythonSDK.ticketing.api import attachments_api
from MergePythonSDK.ticketing.model.paginated_attachment_list import PaginatedAttachmentList
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
    api_instance = attachments_api.AttachmentsApi(api_client)
    created_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created after this datetime. (optional)
    created_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created before this datetime. (optional)
    cursor = "cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw" # str | The pagination cursor value. (optional)
    expand = "ticket" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional) if omitted the server will use the default value of "ticket"
    include_deleted_data = True # bool | Whether to include data that was marked as deleted by third party webhooks. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)
    modified_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, only objects synced by Merge after this date time will be returned. (optional)
    modified_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, only objects synced by Merge before this date time will be returned. (optional)
    page_size = 1 # int | Number of results to return per page. (optional)
    remote_id = "remote_id_example" # str, none_type | The API provider's ID for the given object. (optional)
    ticket_id = "ticket_id_example" # str | If provided, will only return comments for this ticket. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.attachments_list(created_after=created_after, created_before=created_before, cursor=cursor, expand=expand, include_deleted_data=include_deleted_data, include_remote_data=include_remote_data, modified_after=modified_after, modified_before=modified_before, page_size=page_size, remote_id=remote_id, ticket_id=ticket_id)
        pprint(api_response)
    except MergePythonSDK.ticketing.ApiException as e:
        print("Exception when calling AttachmentsApi->attachments_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **created_after** | **datetime**| If provided, will only return objects created after this datetime. | [optional]
 **created_before** | **datetime**| If provided, will only return objects created before this datetime. | [optional]
 **cursor** | **str**| The pagination cursor value. | [optional]
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional] if omitted the server will use the default value of "ticket"
 **include_deleted_data** | **bool**| Whether to include data that was marked as deleted by third party webhooks. | [optional]
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]
 **modified_after** | **datetime**| If provided, only objects synced by Merge after this date time will be returned. | [optional]
 **modified_before** | **datetime**| If provided, only objects synced by Merge before this date time will be returned. | [optional]
 **page_size** | **int**| Number of results to return per page. | [optional]
 **remote_id** | **str, none_type**| The API provider&#39;s ID for the given object. | [optional]
 **ticket_id** | **str**| If provided, will only return comments for this ticket. | [optional]

### Return type

[**PaginatedAttachmentList**](PaginatedAttachmentList.md)

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

# **attachments_meta_post_retrieve**
> MetaResponse attachments_meta_post_retrieve()



Returns metadata for `TicketingAttachment` POSTs.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.ticketing
from MergePythonSDK.ticketing.api import attachments_api
from MergePythonSDK.ticketing.model.meta_response import MetaResponse
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
    api_instance = attachments_api.AttachmentsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.attachments_meta_post_retrieve()
        pprint(api_response)
    except MergePythonSDK.ticketing.ApiException as e:
        print("Exception when calling AttachmentsApi->attachments_meta_post_retrieve: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **attachments_retrieve**
> Attachment attachments_retrieve(id)



Returns an `Attachment` object with the given `id`.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.ticketing
from MergePythonSDK.ticketing.api import attachments_api
from MergePythonSDK.ticketing.model.attachment import Attachment
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
    api_instance = attachments_api.AttachmentsApi(api_client)
    id = "id_example" # str | 
    expand = "ticket" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional) if omitted the server will use the default value of "ticket"
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.attachments_retrieve(id)
        pprint(api_response)
    except MergePythonSDK.ticketing.ApiException as e:
        print("Exception when calling AttachmentsApi->attachments_retrieve: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.attachments_retrieve(id, expand=expand, include_remote_data=include_remote_data)
        pprint(api_response)
    except MergePythonSDK.ticketing.ApiException as e:
        print("Exception when calling AttachmentsApi->attachments_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional] if omitted the server will use the default value of "ticket"
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]

### Return type

[**Attachment**](Attachment.md)

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

