# MergePythonSDK.accounting.ExpensesApi

All URIs are relative to *https://api.merge.dev/api/accounting/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**expenses_create**](ExpensesApi.md#expenses_create) | **POST** /expenses | 
[**expenses_list**](ExpensesApi.md#expenses_list) | **GET** /expenses | 
[**expenses_meta_post_retrieve**](ExpensesApi.md#expenses_meta_post_retrieve) | **GET** /expenses/meta/post | 
[**expenses_retrieve**](ExpensesApi.md#expenses_retrieve) | **GET** /expenses/{id} | 


# **expenses_create**
> ExpenseResponse expenses_create(x_account_token, expense_endpoint_request)



Creates an `Expense` object with the given values.

### Example

* Api Key Authentication (tokenAuth):

```python
import time
import MergePythonSDK.accounting
from MergePythonSDK.accounting.api import expenses_api
from MergePythonSDK.accounting.model.expense_endpoint_request import ExpenseEndpointRequest
from MergePythonSDK.accounting.model.expense_response import ExpenseResponse
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
    api_instance = expenses_api.ExpensesApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    expense_endpoint_request = ExpenseEndpointRequest(
        model=ExpenseRequest(
            transaction_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
            account="9d892439-5fab-4dbb-8bd8-34f7f96c7912",
            contact="3d263469-51a1-4766-9205-f6c997826be1",
            total_amount=10000.0,
            currency=None,
            exchange_rate="2.9",
            company="595c8f97-2ac4-45b7-b000-41bdf43240b5",
            memo="New employee supplies",
            lines=[
                ExpenseLineRequest(
                    remote_id="121222",
                    item="b38c59b0-a9d7-4740-b1ee-5436c6751e3d",
                    net_amount=25.54,
                    tracking_category="b38c59b0-a9d7-4740-b1ee-5436c6751e3d",
                    tracking_categories=["b38c59b0-a9d7-4740-b1ee-5436c6751e3d","9b840d2-686a-465a-8a8e-7b028498f8e4","a47e11b6-c73b-4a0c-be31-130fc48177fa"],
                    company="595c8f97-2ac4-45b7-b000-41bdf43240b5",
                    account="2a56344a-a491-11ec-b909-0242ac120002",
                    contact="c640b80b-fac9-409f-aa19-1f9221aec445",
                    description="MacBook Pro",
                    exchange_rate="2.9",
                    integration_params={
                        "key": None,
                    },
                    linked_account_params={
                        "key": None,
                    },
                ),
            ],
            tracking_categories=["b38c59b0-a9d7-4740-b1ee-5436c6751e3d","9b840d2-686a-465a-8a8e-7b028498f8e4","a47e11b6-c73b-4a0c-be31-130fc48177fa"],
            integration_params={
                "key": None,
            },
            linked_account_params={
                "key": None,
            },
        ),
    ) # ExpenseEndpointRequest | 
    is_debug_mode = True # bool | Whether to include debug fields (such as log file links) in the response. (optional)
    run_async = True # bool | Whether or not third-party updates should be run asynchronously. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.expenses_create(x_account_token, expense_endpoint_request)
        pprint(api_response)
    except MergePythonSDK.accounting.ApiException as e:
        print("Exception when calling ExpensesApi->expenses_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.expenses_create(x_account_token, expense_endpoint_request, is_debug_mode=is_debug_mode, run_async=run_async)
        pprint(api_response)
    except MergePythonSDK.accounting.ApiException as e:
        print("Exception when calling ExpensesApi->expenses_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **expense_endpoint_request** | [**ExpenseEndpointRequest**](ExpenseEndpointRequest.md)|  |
 **is_debug_mode** | **bool**| Whether to include debug fields (such as log file links) in the response. | [optional]
 **run_async** | **bool**| Whether or not third-party updates should be run asynchronously. | [optional]

### Return type

[**ExpenseResponse**](ExpenseResponse.md)

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

# **expenses_list**
> PaginatedExpenseList expenses_list(x_account_token)



Returns a list of `Expense` objects.

### Example

* Api Key Authentication (tokenAuth):

```python
import time
import MergePythonSDK.accounting
from MergePythonSDK.accounting.api import expenses_api

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
    api_instance = expenses_api.ExpensesApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    company_id = "company_id_example" # str | If provided, will only return expenses for this company. (optional)
    created_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created after this datetime. (optional)
    created_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created before this datetime. (optional)
    cursor = "cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw" # str | The pagination cursor value. (optional)
    expand = "tracking_categories,account,contact,company" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)
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
        api_response = api_instance.expenses_list(x_account_token)
        pprint(api_response)
    except MergePythonSDK.accounting.ApiException as e:
        print("Exception when calling ExpensesApi->expenses_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.expenses_list(x_account_token, company_id=company_id, created_after=created_after, created_before=created_before, cursor=cursor, expand=expand, include_deleted_data=include_deleted_data, include_remote_data=include_remote_data, modified_after=modified_after, modified_before=modified_before, page_size=page_size, remote_id=remote_id, transaction_date_after=transaction_date_after, transaction_date_before=transaction_date_before)
        pprint(api_response)
    except MergePythonSDK.accounting.ApiException as e:
        print("Exception when calling ExpensesApi->expenses_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **company_id** | **str**| If provided, will only return expenses for this company. | [optional]
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

[**PaginatedExpenseList**](PaginatedExpenseList.md)

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

# **expenses_meta_post_retrieve**
> MetaResponse expenses_meta_post_retrieve(x_account_token)



Returns metadata for `Expense` POSTs.

### Example

* Api Key Authentication (tokenAuth):

```python
import time
import MergePythonSDK.accounting
from MergePythonSDK.accounting.api import expenses_api
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
    api_instance = expenses_api.ExpensesApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.expenses_meta_post_retrieve(x_account_token)
        pprint(api_response)
    except MergePythonSDK.accounting.ApiException as e:
        print("Exception when calling ExpensesApi->expenses_meta_post_retrieve: %s\n" % e)
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

# **expenses_retrieve**
> Expense expenses_retrieve(x_account_token, id)



Returns an `Expense` object with the given `id`.

### Example

* Api Key Authentication (tokenAuth):

```python
import time
import MergePythonSDK.accounting
from MergePythonSDK.accounting.api import expenses_api
from MergePythonSDK.accounting.model.expense import Expense
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
    api_instance = expenses_api.ExpensesApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    id = "id_example" # str | 
    expand = "tracking_categories,account,contact,company" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.expenses_retrieve(x_account_token, id)
        pprint(api_response)
    except MergePythonSDK.accounting.ApiException as e:
        print("Exception when calling ExpensesApi->expenses_retrieve: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.expenses_retrieve(x_account_token, id, expand=expand, include_remote_data=include_remote_data)
        pprint(api_response)
    except MergePythonSDK.accounting.ApiException as e:
        print("Exception when calling ExpensesApi->expenses_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **id** | **str**|  |
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional]
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]

### Return type

[**Expense**](Expense.md)

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

