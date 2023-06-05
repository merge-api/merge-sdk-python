# MergePythonSDK.accounting.JournalEntriesApi

All URIs are relative to *https://api.merge.dev/api/accounting/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**journal_entries_create**](JournalEntriesApi.md#journal_entries_create) | **POST** /journal-entries | 
[**journal_entries_list**](JournalEntriesApi.md#journal_entries_list) | **GET** /journal-entries | 
[**journal_entries_meta_post_retrieve**](JournalEntriesApi.md#journal_entries_meta_post_retrieve) | **GET** /journal-entries/meta/post | 
[**journal_entries_retrieve**](JournalEntriesApi.md#journal_entries_retrieve) | **GET** /journal-entries/{id} | 


# **journal_entries_create**
> JournalEntryResponse journal_entries_create(x_account_token, journal_entry_endpoint_request)



Creates a `JournalEntry` object with the given values.

### Example

* Api Key Authentication (tokenAuth):

```python
import time
import MergePythonSDK.accounting
from MergePythonSDK.accounting.api import journal_entries_api
from MergePythonSDK.accounting.model.journal_entry_response import JournalEntryResponse
from MergePythonSDK.accounting.model.journal_entry_endpoint_request import JournalEntryEndpointRequest
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

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with MergePythonSDK.accounting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = journal_entries_api.JournalEntriesApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    journal_entry_endpoint_request = JournalEntryEndpointRequest(
        model=JournalEntryRequest(
            transaction_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
            payments=[
                "payments_example",
            ],
            memo="memo_example",
            currency=None,
            exchange_rate="-80",
            company="company_example",
            lines=[
                JournalLineRequest(
                    remote_id="121222",
                    account="9d892439-5fab-4dbb-8bd8-34f7f96c7912",
                    net_amount=25.54,
                    tracking_category="d25d609b-945f-4762-b55a-1c8fb220c43c",
                    tracking_categories=["d25d609b-945f-4762-b55a-1c8fb220c43c","9b840d2-686a-465a-8a8e-7b028498f8e4","a47e11b6-c73b-4a0c-be31-130fc48177fa"],
                    contact="d2d5ea3c-b032-11ec-b909-0242ac120002",
                    description="Cash payment for lunch",
                    exchange_rate="2.9",
                    integration_params={
                        "key": None,
                    },
                    linked_account_params={
                        "key": None,
                    },
                ),
            ],
            posting_status=None,
            integration_params={
                "key": None,
            },
            linked_account_params={
                "key": None,
            },
        ),
    ) # JournalEntryEndpointRequest | 
    is_debug_mode = True # bool | Whether to include debug fields (such as log file links) in the response. (optional)
    run_async = True # bool | Whether or not third-party updates should be run asynchronously. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.journal_entries_create(x_account_token, journal_entry_endpoint_request)
        pprint(api_response)
    except MergePythonSDK.accounting.ApiException as e:
        print("Exception when calling JournalEntriesApi->journal_entries_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.journal_entries_create(x_account_token, journal_entry_endpoint_request, is_debug_mode=is_debug_mode, run_async=run_async)
        pprint(api_response)
    except MergePythonSDK.accounting.ApiException as e:
        print("Exception when calling JournalEntriesApi->journal_entries_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **journal_entry_endpoint_request** | [**JournalEntryEndpointRequest**](JournalEntryEndpointRequest.md)|  |
 **is_debug_mode** | **bool**| Whether to include debug fields (such as log file links) in the response. | [optional]
 **run_async** | **bool**| Whether or not third-party updates should be run asynchronously. | [optional]

### Return type

[**JournalEntryResponse**](JournalEntryResponse.md)

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

# **journal_entries_list**
> PaginatedJournalEntryList journal_entries_list(x_account_token)



Returns a list of `JournalEntry` objects.

### Example

* Api Key Authentication (tokenAuth):

```python
import time
import MergePythonSDK.accounting
from MergePythonSDK.accounting.api import journal_entries_api

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

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with MergePythonSDK.accounting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = journal_entries_api.JournalEntriesApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    company_id = "company_id_example" # str | If provided, will only return journal entries for this company. (optional)
    created_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created after this datetime. (optional)
    created_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created before this datetime. (optional)
    cursor = "cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw" # str | The pagination cursor value. (optional)
    expand = "lines,payments,tracking_categories,company" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)
    include_deleted_data = True # bool | Whether to include data that was marked as deleted by third party webhooks. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)
    modified_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, only objects synced by Merge after this date time will be returned. (optional)
    modified_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, only objects synced by Merge before this date time will be returned. (optional)
    page_size = 1 # int | Number of results to return per page. (optional)
    remote_id = "remote_id_example" # str, none_type | The API provider's ID for the given object. (optional)
    transaction_date_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type | If provided, will only return objects created after this datetime. (optional)
    transaction_date_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type | If provided, will only return objects created before this datetime. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.journal_entries_list(x_account_token)
        pprint(api_response)
    except MergePythonSDK.accounting.ApiException as e:
        print("Exception when calling JournalEntriesApi->journal_entries_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.journal_entries_list(x_account_token, company_id=company_id, created_after=created_after, created_before=created_before, cursor=cursor, expand=expand, include_deleted_data=include_deleted_data, include_remote_data=include_remote_data, modified_after=modified_after, modified_before=modified_before, page_size=page_size, remote_id=remote_id, transaction_date_after=transaction_date_after, transaction_date_before=transaction_date_before)
        pprint(api_response)
    except MergePythonSDK.accounting.ApiException as e:
        print("Exception when calling JournalEntriesApi->journal_entries_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **company_id** | **str**| If provided, will only return journal entries for this company. | [optional]
 **created_after** | **datetime**| If provided, will only return objects created after this datetime. | [optional]
 **created_before** | **datetime**| If provided, will only return objects created before this datetime. | [optional]
 **cursor** | **str**| The pagination cursor value. | [optional]
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional]
 **include_deleted_data** | **bool**| Whether to include data that was marked as deleted by third party webhooks. | [optional]
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]
 **modified_after** | **datetime**| If provided, only objects synced by Merge after this date time will be returned. | [optional]
 **modified_before** | **datetime**| If provided, only objects synced by Merge before this date time will be returned. | [optional]
 **page_size** | **int**| Number of results to return per page. | [optional]
 **remote_id** | **str, none_type**| The API provider&#39;s ID for the given object. | [optional]
 **transaction_date_after** | **datetime, none_type**| If provided, will only return objects created after this datetime. | [optional]
 **transaction_date_before** | **datetime, none_type**| If provided, will only return objects created before this datetime. | [optional]

### Return type

[**PaginatedJournalEntryList**](PaginatedJournalEntryList.md)

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

# **journal_entries_meta_post_retrieve**
> MetaResponse journal_entries_meta_post_retrieve(x_account_token)



Returns metadata for `JournalEntry` POSTs.

### Example

* Api Key Authentication (tokenAuth):

```python
import time
import MergePythonSDK.accounting
from MergePythonSDK.accounting.api import journal_entries_api
from MergePythonSDK.accounting.model.meta_response import MetaResponse
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

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with MergePythonSDK.accounting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = journal_entries_api.JournalEntriesApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.journal_entries_meta_post_retrieve(x_account_token)
        pprint(api_response)
    except MergePythonSDK.accounting.ApiException as e:
        print("Exception when calling JournalEntriesApi->journal_entries_meta_post_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |

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

# **journal_entries_retrieve**
> JournalEntry journal_entries_retrieve(x_account_token, id)



Returns a `JournalEntry` object with the given `id`.

### Example

* Api Key Authentication (tokenAuth):

```python
import time
import MergePythonSDK.accounting
from MergePythonSDK.accounting.api import journal_entries_api
from MergePythonSDK.accounting.model.journal_entry import JournalEntry
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

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with MergePythonSDK.accounting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = journal_entries_api.JournalEntriesApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    id = "id_example" # str | 
    expand = "lines,payments,tracking_categories,company" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.journal_entries_retrieve(x_account_token, id)
        pprint(api_response)
    except MergePythonSDK.accounting.ApiException as e:
        print("Exception when calling JournalEntriesApi->journal_entries_retrieve: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.journal_entries_retrieve(x_account_token, id, expand=expand, include_remote_data=include_remote_data)
        pprint(api_response)
    except MergePythonSDK.accounting.ApiException as e:
        print("Exception when calling JournalEntriesApi->journal_entries_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **id** | **str**|  |
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional]
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]

### Return type

[**JournalEntry**](JournalEntry.md)

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

