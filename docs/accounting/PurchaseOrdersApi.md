# MergePythonSDK.accounting.PurchaseOrdersApi

All URIs are relative to *https://api.merge.dev/api/accounting/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**purchase_orders_create**](PurchaseOrdersApi.md#purchase_orders_create) | **POST** /purchase-orders | 
[**purchase_orders_list**](PurchaseOrdersApi.md#purchase_orders_list) | **GET** /purchase-orders | 
[**purchase_orders_meta_post_retrieve**](PurchaseOrdersApi.md#purchase_orders_meta_post_retrieve) | **GET** /purchase-orders/meta/post | 
[**purchase_orders_retrieve**](PurchaseOrdersApi.md#purchase_orders_retrieve) | **GET** /purchase-orders/{id} | 


# **purchase_orders_create**
> PurchaseOrderResponse purchase_orders_create(x_account_token, purchase_order_endpoint_request)



Creates a `PurchaseOrder` object with the given values.

### Example

* Api Key Authentication (tokenAuth):

```python
import time
import MergePythonSDK.accounting
from MergePythonSDK.accounting.api import purchase_orders_api
from MergePythonSDK.accounting.model.purchase_order_endpoint_request import PurchaseOrderEndpointRequest
from MergePythonSDK.accounting.model.purchase_order_response import PurchaseOrderResponse
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
    api_instance = purchase_orders_api.PurchaseOrdersApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    purchase_order_endpoint_request = PurchaseOrderEndpointRequest(
        model=PurchaseOrderRequest(
            status=None,
            issue_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
            delivery_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
            delivery_address="delivery_address_example",
            customer="customer_example",
            vendor="vendor_example",
            memo="memo_example",
            company="company_example",
            total_amount=3.14,
            currency=None,
            exchange_rate="-80",
            line_items=[
                PurchaseOrderLineItemRequest(
                    remote_id="121222",
                    description="Pickleball paddles",
                    unit_price=25.0,
                    quantity=10.0,
                    item="0958cbc6-6040-430a-848e-aafacbadf4ae",
                    account="account_example",
                    tracking_category="f1214c24-2702-4617-b74b-3ddecfc0d384",
                    tracking_categories=["f1214c24-2702-4617-b74b-3ddecfc0d384","9b840d2-686a-465a-8a8e-7b028498f8e4","a47e11b6-c73b-4a0c-be31-130fc48177fa"],
                    tax_amount="10.0",
                    total_line_amount="260.0",
                    currency=None,
                    exchange_rate="2.9",
                    company="595c8f97-2ac4-45b7-b000-41bdf43240b5",
                    integration_params={
                        "key": None,
                    },
                    linked_account_params={
                        "key": None,
                    },
                ),
            ],
            integration_params={
                "key": None,
            },
            linked_account_params={
                "key": None,
            },
        ),
    ) # PurchaseOrderEndpointRequest | 
    is_debug_mode = True # bool | Whether to include debug fields (such as log file links) in the response. (optional)
    run_async = True # bool | Whether or not third-party updates should be run asynchronously. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.purchase_orders_create(x_account_token, purchase_order_endpoint_request)
        pprint(api_response)
    except MergePythonSDK.accounting.ApiException as e:
        print("Exception when calling PurchaseOrdersApi->purchase_orders_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.purchase_orders_create(x_account_token, purchase_order_endpoint_request, is_debug_mode=is_debug_mode, run_async=run_async)
        pprint(api_response)
    except MergePythonSDK.accounting.ApiException as e:
        print("Exception when calling PurchaseOrdersApi->purchase_orders_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **purchase_order_endpoint_request** | [**PurchaseOrderEndpointRequest**](PurchaseOrderEndpointRequest.md)|  |
 **is_debug_mode** | **bool**| Whether to include debug fields (such as log file links) in the response. | [optional]
 **run_async** | **bool**| Whether or not third-party updates should be run asynchronously. | [optional]

### Return type

[**PurchaseOrderResponse**](PurchaseOrderResponse.md)

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

# **purchase_orders_list**
> PaginatedPurchaseOrderList purchase_orders_list(x_account_token)



Returns a list of `PurchaseOrder` objects.

### Example

* Api Key Authentication (tokenAuth):

```python
import time
import MergePythonSDK.accounting
from MergePythonSDK.accounting.api import purchase_orders_api

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
    api_instance = purchase_orders_api.PurchaseOrdersApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    company_id = "company_id_example" # str | If provided, will only return purchase orders for this company. (optional)
    created_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created after this datetime. (optional)
    created_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created before this datetime. (optional)
    cursor = "cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw" # str | The pagination cursor value. (optional)
    expand = "line_items,tracking_categories,delivery_address,vendor,company" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)
    include_deleted_data = True # bool | Whether to include data that was marked as deleted by third party webhooks. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)
    issue_date_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type | If provided, will only return objects created after this datetime. (optional)
    issue_date_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type | If provided, will only return objects created before this datetime. (optional)
    modified_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, only objects synced by Merge after this date time will be returned. (optional)
    modified_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, only objects synced by Merge before this date time will be returned. (optional)
    page_size = 1 # int | Number of results to return per page. (optional)
    remote_fields = "status" # str | Deprecated. Use show_enum_origins. (optional) if omitted the server will use the default value of "status"
    remote_id = "remote_id_example" # str, none_type | The API provider's ID for the given object. (optional)
    show_enum_origins = "status" # str | Which fields should be returned in non-normalized form. (optional) if omitted the server will use the default value of "status"

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.purchase_orders_list(x_account_token)
        pprint(api_response)
    except MergePythonSDK.accounting.ApiException as e:
        print("Exception when calling PurchaseOrdersApi->purchase_orders_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.purchase_orders_list(x_account_token, company_id=company_id, created_after=created_after, created_before=created_before, cursor=cursor, expand=expand, include_deleted_data=include_deleted_data, include_remote_data=include_remote_data, issue_date_after=issue_date_after, issue_date_before=issue_date_before, modified_after=modified_after, modified_before=modified_before, page_size=page_size, remote_fields=remote_fields, remote_id=remote_id, show_enum_origins=show_enum_origins)
        pprint(api_response)
    except MergePythonSDK.accounting.ApiException as e:
        print("Exception when calling PurchaseOrdersApi->purchase_orders_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **company_id** | **str**| If provided, will only return purchase orders for this company. | [optional]
 **created_after** | **datetime**| If provided, will only return objects created after this datetime. | [optional]
 **created_before** | **datetime**| If provided, will only return objects created before this datetime. | [optional]
 **cursor** | **str**| The pagination cursor value. | [optional]
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional]
 **include_deleted_data** | **bool**| Whether to include data that was marked as deleted by third party webhooks. | [optional]
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]
 **issue_date_after** | **datetime, none_type**| If provided, will only return objects created after this datetime. | [optional]
 **issue_date_before** | **datetime, none_type**| If provided, will only return objects created before this datetime. | [optional]
 **modified_after** | **datetime**| If provided, only objects synced by Merge after this date time will be returned. | [optional]
 **modified_before** | **datetime**| If provided, only objects synced by Merge before this date time will be returned. | [optional]
 **page_size** | **int**| Number of results to return per page. | [optional]
 **remote_fields** | **str**| Deprecated. Use show_enum_origins. | [optional] if omitted the server will use the default value of "status"
 **remote_id** | **str, none_type**| The API provider&#39;s ID for the given object. | [optional]
 **show_enum_origins** | **str**| Which fields should be returned in non-normalized form. | [optional] if omitted the server will use the default value of "status"

### Return type

[**PaginatedPurchaseOrderList**](PaginatedPurchaseOrderList.md)

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

# **purchase_orders_meta_post_retrieve**
> MetaResponse purchase_orders_meta_post_retrieve(x_account_token)



Returns metadata for `PurchaseOrder` POSTs.

### Example

* Api Key Authentication (tokenAuth):

```python
import time
import MergePythonSDK.accounting
from MergePythonSDK.accounting.api import purchase_orders_api
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
    api_instance = purchase_orders_api.PurchaseOrdersApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.purchase_orders_meta_post_retrieve(x_account_token)
        pprint(api_response)
    except MergePythonSDK.accounting.ApiException as e:
        print("Exception when calling PurchaseOrdersApi->purchase_orders_meta_post_retrieve: %s\n" % e)
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

# **purchase_orders_retrieve**
> PurchaseOrder purchase_orders_retrieve(x_account_token, id)



Returns a `PurchaseOrder` object with the given `id`.

### Example

* Api Key Authentication (tokenAuth):

```python
import time
import MergePythonSDK.accounting
from MergePythonSDK.accounting.api import purchase_orders_api
from MergePythonSDK.accounting.model.purchase_order import PurchaseOrder
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
    api_instance = purchase_orders_api.PurchaseOrdersApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    id = "id_example" # str | 
    expand = "line_items,tracking_categories,delivery_address,vendor,company" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)
    remote_fields = "status" # str | Deprecated. Use show_enum_origins. (optional) if omitted the server will use the default value of "status"
    show_enum_origins = "status" # str | Which fields should be returned in non-normalized form. (optional) if omitted the server will use the default value of "status"

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.purchase_orders_retrieve(x_account_token, id)
        pprint(api_response)
    except MergePythonSDK.accounting.ApiException as e:
        print("Exception when calling PurchaseOrdersApi->purchase_orders_retrieve: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.purchase_orders_retrieve(x_account_token, id, expand=expand, include_remote_data=include_remote_data, remote_fields=remote_fields, show_enum_origins=show_enum_origins)
        pprint(api_response)
    except MergePythonSDK.accounting.ApiException as e:
        print("Exception when calling PurchaseOrdersApi->purchase_orders_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **id** | **str**|  |
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional]
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]
 **remote_fields** | **str**| Deprecated. Use show_enum_origins. | [optional] if omitted the server will use the default value of "status"
 **show_enum_origins** | **str**| Which fields should be returned in non-normalized form. | [optional] if omitted the server will use the default value of "status"

### Return type

[**PurchaseOrder**](PurchaseOrder.md)

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

