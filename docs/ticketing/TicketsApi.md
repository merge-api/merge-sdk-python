# MergePythonSDK.ticketing.TicketsApi

All URIs are relative to *https://api.merge.dev/api/ticketing/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tickets_collaborators_list**](TicketsApi.md#tickets_collaborators_list) | **GET** /tickets/{id}/collaborators | 
[**tickets_create**](TicketsApi.md#tickets_create) | **POST** /tickets | 
[**tickets_list**](TicketsApi.md#tickets_list) | **GET** /tickets | 
[**tickets_meta_patch_retrieve**](TicketsApi.md#tickets_meta_patch_retrieve) | **GET** /tickets/meta/patch/{id} | 
[**tickets_meta_post_retrieve**](TicketsApi.md#tickets_meta_post_retrieve) | **GET** /tickets/meta/post | 
[**tickets_partial_update**](TicketsApi.md#tickets_partial_update) | **PATCH** /tickets/{id} | 
[**tickets_retrieve**](TicketsApi.md#tickets_retrieve) | **GET** /tickets/{id} | 


# **tickets_collaborators_list**
> PaginatedUserList tickets_collaborators_list(id)



Returns a `User` object with the given `id`.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.ticketing
from MergePythonSDK.ticketing.api import tickets_api
from MergePythonSDK.ticketing.model.paginated_user_list import PaginatedUserList
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
    api_instance = tickets_api.TicketsApi(api_client)
    id = "id_example" # str | 
    cursor = "cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw" # str | The pagination cursor value. (optional)
    expand = "teams" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional) if omitted the server will use the default value of "teams"
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)
    page_size = 1 # int | Number of results to return per page. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.tickets_collaborators_list(id)
        pprint(api_response)
    except MergePythonSDK.ticketing.ApiException as e:
        print("Exception when calling TicketsApi->tickets_collaborators_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.tickets_collaborators_list(id, cursor=cursor, expand=expand, include_remote_data=include_remote_data, page_size=page_size)
        pprint(api_response)
    except MergePythonSDK.ticketing.ApiException as e:
        print("Exception when calling TicketsApi->tickets_collaborators_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **cursor** | **str**| The pagination cursor value. | [optional]
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional] if omitted the server will use the default value of "teams"
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

# **tickets_create**
> TicketResponse tickets_create(ticket_endpoint_request)



Creates a `Ticket` object with the given values.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.ticketing
from MergePythonSDK.ticketing.api import tickets_api
from MergePythonSDK.ticketing.model.ticket_response import TicketResponse
from MergePythonSDK.ticketing.model.ticket_endpoint_request import TicketEndpointRequest
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
    api_instance = tickets_api.TicketsApi(api_client)
    ticket_endpoint_request = TicketEndpointRequest(
        model=TicketRequest(
            remote_id="19202938",
            name="Please add more integrations",
            assignees=["17a54124-287f-494d-965e-3c5b330c9a68"],
            creator="creator_example",
            due_date=dateutil_parser('2022-10-11T00:00:00Z'),
            status=None,
            description="Can you please add more integrations? It'll make syncing data much easier!",
            project="fb8c55b6-1cb8-4b4c-9fb6-17924231619d",
            ticket_type="incident",
            account="0958cbc6-6040-430a-848e-aafacbadf4ae",
            contact="65c345ba-6870-4974-87ba-dd31509c367a",
            parent_ticket="75b33d04-30d2-4f3e-be45-27838bc94342",
            attachments=["42747df1-95e7-46e2-93cc-66f1191edca5","92f972d0-2526-434b-9409-4c3b468e08f0"],
            tags=["enterprise","other-tag"],
            remote_created_at=dateutil_parser('2021-11-10T00:00:00Z'),
            remote_updated_at=dateutil_parser('2021-12-09T00:00:00Z'),
            completed_at=dateutil_parser('2021-12-09T00:00:00Z'),
            ticket_url="https://thirdpartysoftware.com/project/3/issue/1",
            priority=None,
            integration_params={
                "key": None,
            },
            linked_account_params={
                "key": None,
            },
        ),
    ) # TicketEndpointRequest | 
    is_debug_mode = True # bool | Whether to include debug fields (such as log file links) in the response. (optional)
    run_async = True # bool | Whether or not third-party updates should be run asynchronously. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.tickets_create(ticket_endpoint_request)
        pprint(api_response)
    except MergePythonSDK.ticketing.ApiException as e:
        print("Exception when calling TicketsApi->tickets_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.tickets_create(ticket_endpoint_request, is_debug_mode=is_debug_mode, run_async=run_async)
        pprint(api_response)
    except MergePythonSDK.ticketing.ApiException as e:
        print("Exception when calling TicketsApi->tickets_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticket_endpoint_request** | [**TicketEndpointRequest**](TicketEndpointRequest.md)|  |
 **is_debug_mode** | **bool**| Whether to include debug fields (such as log file links) in the response. | [optional]
 **run_async** | **bool**| Whether or not third-party updates should be run asynchronously. | [optional]

### Return type

[**TicketResponse**](TicketResponse.md)

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

# **tickets_list**
> PaginatedTicketList tickets_list()



Returns a list of `Ticket` objects.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.ticketing
from MergePythonSDK.ticketing.api import tickets_api
from MergePythonSDK.ticketing.model.paginated_ticket_list import PaginatedTicketList
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
    api_instance = tickets_api.TicketsApi(api_client)
    account_id = "account_id_example" # str | If provided, will only return tickets for this account. (optional)
    assignee_ids = "assignee_ids_example" # str | If provided, will only return tickets assigned to the assignee_ids; multiple assignee_ids can be separated by commas. (optional)
    completed_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type | If provided, will only return tickets completed after this datetime. (optional)
    completed_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type | If provided, will only return tickets completed before this datetime. (optional)
    contact_id = "contact_id_example" # str | If provided, will only return tickets for this contact. (optional)
    created_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created after this datetime. (optional)
    created_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created before this datetime. (optional)
    cursor = "cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw" # str | The pagination cursor value. (optional)
    due_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type | If provided, will only return tickets due after this datetime. (optional)
    due_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type | If provided, will only return tickets due before this datetime. (optional)
    expand = "attachments,assignees,project,account,contact,creator,parent_ticket" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)
    include_deleted_data = True # bool | Whether to include data that was marked as deleted by third party webhooks. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)
    modified_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects modified after this datetime. (optional)
    modified_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects modified before this datetime. (optional)
    page_size = 1 # int | Number of results to return per page. (optional)
    parent_ticket_id = "parent_ticket_id_example" # str | If provided, will only return sub tickets of the parent_ticket_id. (optional)
    priority = "HIGH" # str, none_type | If provided, will only return tickets of this priority. (optional)
    project_id = "project_id_example" # str | If provided, will only return tickets for this project. (optional)
    remote_fields = "status" # str | Which fields should be returned in non-normalized form. (optional) if omitted the server will use the default value of "status"
    remote_id = "remote_id_example" # str, none_type | The API provider's ID for the given object. (optional)
    status = "CLOSED" # str, none_type | If provided, will only return tickets of this status. (optional)
    tags = "tags_example" # str | If provided, will only return tickets matching the tags; multiple tags can be separated by commas. (optional)
    ticket_type = "ticket_type_example" # str, none_type | If provided, will only return tickets of this type. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.tickets_list(account_id=account_id, assignee_ids=assignee_ids, completed_after=completed_after, completed_before=completed_before, contact_id=contact_id, created_after=created_after, created_before=created_before, cursor=cursor, due_after=due_after, due_before=due_before, expand=expand, include_deleted_data=include_deleted_data, include_remote_data=include_remote_data, modified_after=modified_after, modified_before=modified_before, page_size=page_size, parent_ticket_id=parent_ticket_id, priority=priority, project_id=project_id, remote_fields=remote_fields, remote_id=remote_id, status=status, tags=tags, ticket_type=ticket_type)
        pprint(api_response)
    except MergePythonSDK.ticketing.ApiException as e:
        print("Exception when calling TicketsApi->tickets_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| If provided, will only return tickets for this account. | [optional]
 **assignee_ids** | **str**| If provided, will only return tickets assigned to the assignee_ids; multiple assignee_ids can be separated by commas. | [optional]
 **completed_after** | **datetime, none_type**| If provided, will only return tickets completed after this datetime. | [optional]
 **completed_before** | **datetime, none_type**| If provided, will only return tickets completed before this datetime. | [optional]
 **contact_id** | **str**| If provided, will only return tickets for this contact. | [optional]
 **created_after** | **datetime**| If provided, will only return objects created after this datetime. | [optional]
 **created_before** | **datetime**| If provided, will only return objects created before this datetime. | [optional]
 **cursor** | **str**| The pagination cursor value. | [optional]
 **due_after** | **datetime, none_type**| If provided, will only return tickets due after this datetime. | [optional]
 **due_before** | **datetime, none_type**| If provided, will only return tickets due before this datetime. | [optional]
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional]
 **include_deleted_data** | **bool**| Whether to include data that was marked as deleted by third party webhooks. | [optional]
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]
 **modified_after** | **datetime**| If provided, will only return objects modified after this datetime. | [optional]
 **modified_before** | **datetime**| If provided, will only return objects modified before this datetime. | [optional]
 **page_size** | **int**| Number of results to return per page. | [optional]
 **parent_ticket_id** | **str**| If provided, will only return sub tickets of the parent_ticket_id. | [optional]
 **priority** | **str, none_type**| If provided, will only return tickets of this priority. | [optional]
 **project_id** | **str**| If provided, will only return tickets for this project. | [optional]
 **remote_fields** | **str**| Which fields should be returned in non-normalized form. | [optional] if omitted the server will use the default value of "status"
 **remote_id** | **str, none_type**| The API provider&#39;s ID for the given object. | [optional]
 **status** | **str, none_type**| If provided, will only return tickets of this status. | [optional]
 **tags** | **str**| If provided, will only return tickets matching the tags; multiple tags can be separated by commas. | [optional]
 **ticket_type** | **str, none_type**| If provided, will only return tickets of this type. | [optional]

### Return type

[**PaginatedTicketList**](PaginatedTicketList.md)

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

# **tickets_meta_patch_retrieve**
> MetaResponse tickets_meta_patch_retrieve(id)



Returns metadata for `Ticket` PATCHs.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.ticketing
from MergePythonSDK.ticketing.api import tickets_api
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
    api_instance = tickets_api.TicketsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.tickets_meta_patch_retrieve(id)
        pprint(api_response)
    except MergePythonSDK.ticketing.ApiException as e:
        print("Exception when calling TicketsApi->tickets_meta_patch_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **tickets_meta_post_retrieve**
> MetaResponse tickets_meta_post_retrieve()



Returns metadata for `Ticket` POSTs.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.ticketing
from MergePythonSDK.ticketing.api import tickets_api
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
    api_instance = tickets_api.TicketsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.tickets_meta_post_retrieve()
        pprint(api_response)
    except MergePythonSDK.ticketing.ApiException as e:
        print("Exception when calling TicketsApi->tickets_meta_post_retrieve: %s\n" % e)
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

# **tickets_partial_update**
> TicketResponse tickets_partial_update(id, patched_ticket_endpoint_request)



Updates a `Ticket` object with the given `id`.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.ticketing
from MergePythonSDK.ticketing.api import tickets_api
from MergePythonSDK.ticketing.model.patched_ticket_endpoint_request import PatchedTicketEndpointRequest
from MergePythonSDK.ticketing.model.ticket_response import TicketResponse
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
    api_instance = tickets_api.TicketsApi(api_client)
    id = "id_example" # str | 
    patched_ticket_endpoint_request = PatchedTicketEndpointRequest(
        model=PatchedTicketRequest(
            name="Please add more integrations",
            assignees=["17a54124-287f-494d-965e-3c5b330c9a68"],
            creator="creator_example",
            due_date=dateutil_parser('2022-10-11T00:00:00Z'),
            status=None,
            description="Can you please add more integrations? It'll make syncing data much easier!",
            project="fb8c55b6-1cb8-4b4c-9fb6-17924231619d",
            ticket_type="incident",
            account="0958cbc6-6040-430a-848e-aafacbadf4ae",
            contact="65c345ba-6870-4974-87ba-dd31509c367a",
            parent_ticket="75b33d04-30d2-4f3e-be45-27838bc94342",
            tags=["enterprise","other-tag"],
            remote_created_at=dateutil_parser('2021-11-10T00:00:00Z'),
            remote_updated_at=dateutil_parser('2021-12-09T00:00:00Z'),
            completed_at=dateutil_parser('2021-12-09T00:00:00Z'),
            ticket_url="https://thirdpartysoftware.com/project/3/issue/1",
            priority=None,
            integration_params={
                "key": None,
            },
            linked_account_params={
                "key": None,
            },
        ),
    ) # PatchedTicketEndpointRequest | 
    is_debug_mode = True # bool | Whether to include debug fields (such as log file links) in the response. (optional)
    run_async = True # bool | Whether or not third-party updates should be run asynchronously. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.tickets_partial_update(id, patched_ticket_endpoint_request)
        pprint(api_response)
    except MergePythonSDK.ticketing.ApiException as e:
        print("Exception when calling TicketsApi->tickets_partial_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.tickets_partial_update(id, patched_ticket_endpoint_request, is_debug_mode=is_debug_mode, run_async=run_async)
        pprint(api_response)
    except MergePythonSDK.ticketing.ApiException as e:
        print("Exception when calling TicketsApi->tickets_partial_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **patched_ticket_endpoint_request** | [**PatchedTicketEndpointRequest**](PatchedTicketEndpointRequest.md)|  |
 **is_debug_mode** | **bool**| Whether to include debug fields (such as log file links) in the response. | [optional]
 **run_async** | **bool**| Whether or not third-party updates should be run asynchronously. | [optional]

### Return type

[**TicketResponse**](TicketResponse.md)

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

# **tickets_retrieve**
> Ticket tickets_retrieve(id)



Returns a `Ticket` object with the given `id`.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.ticketing
from MergePythonSDK.ticketing.api import tickets_api
from MergePythonSDK.ticketing.model.ticket import Ticket
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
    api_instance = tickets_api.TicketsApi(api_client)
    id = "id_example" # str | 
    expand = "attachments,assignees,project,account,contact,creator,parent_ticket" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)
    remote_fields = "status" # str | Which fields should be returned in non-normalized form. (optional) if omitted the server will use the default value of "status"

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.tickets_retrieve(id)
        pprint(api_response)
    except MergePythonSDK.ticketing.ApiException as e:
        print("Exception when calling TicketsApi->tickets_retrieve: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.tickets_retrieve(id, expand=expand, include_remote_data=include_remote_data, remote_fields=remote_fields)
        pprint(api_response)
    except MergePythonSDK.ticketing.ApiException as e:
        print("Exception when calling TicketsApi->tickets_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional]
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]
 **remote_fields** | **str**| Which fields should be returned in non-normalized form. | [optional] if omitted the server will use the default value of "status"

### Return type

[**Ticket**](Ticket.md)

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

