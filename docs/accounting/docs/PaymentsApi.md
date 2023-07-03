# MergePythonSDK.accounting.PaymentsApi

All URIs are relative to *https://api.merge.dev/api/accounting/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payments_create**](PaymentsApi.md#payments_create) | **POST** /payments | 
[**payments_list**](PaymentsApi.md#payments_list) | **GET** /payments | 
[**payments_meta_post_retrieve**](PaymentsApi.md#payments_meta_post_retrieve) | **GET** /payments/meta/post | 
[**payments_retrieve**](PaymentsApi.md#payments_retrieve) | **GET** /payments/{id} | 


# **payments_create**
> PaymentResponse payments_create(payment_endpoint_request)



Creates a `Payment` object with the given values.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.accounting
from MergePythonSDK.accounting.api import payments_api
from MergePythonSDK.accounting.model.payment_endpoint_request import PaymentEndpointRequest
from MergePythonSDK.accounting.model.payment_response import PaymentResponse
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

# Configure API key authorization: accountTokenAuth
configuration.api_key['accountTokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accountTokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = MergePythonSDK.accounting.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with MergePythonSDK.accounting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = payments_api.PaymentsApi(api_client)
    payment_endpoint_request = PaymentEndpointRequest(
        model=PaymentRequest(
            transaction_date=dateutil_parser('2020-03-31T00:00:00Z'),
            contact="5b3c1341-a20f-4e51-b72c-f3830a16c97b",
            account="d6e687d6-0c36-48a1-8114-35324b5cb38f",
            currency=None,
            exchange_rate="2.9",
            company="595c8f97-2ac4-45b7-b000-41bdf43240b5",
            total_amount=50.0,
            tracking_categories=["b38c59b0-a9d7-4740-b1ee-5436c6751e3d","9b840d2-686a-465a-8a8e-7b028498f8e4","a47e11b6-c73b-4a0c-be31-130fc48177fa"],
            integration_params={
                "key": None,
            },
            linked_account_params={
                "key": None,
            },
        ),
    ) # PaymentEndpointRequest | 
    is_debug_mode = True # bool | Whether to include debug fields (such as log file links) in the response. (optional)
    run_async = True # bool | Whether or not third-party updates should be run asynchronously. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.payments_create(payment_endpoint_request)
        pprint(api_response)
    except MergePythonSDK.accounting.ApiException as e:
        print("Exception when calling PaymentsApi->payments_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.payments_create(payment_endpoint_request, is_debug_mode=is_debug_mode, run_async=run_async)
        pprint(api_response)
    except MergePythonSDK.accounting.ApiException as e:
        print("Exception when calling PaymentsApi->payments_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_endpoint_request** | [**PaymentEndpointRequest**](PaymentEndpointRequest.md)|  |
 **is_debug_mode** | **bool**| Whether to include debug fields (such as log file links) in the response. | [optional]
 **run_async** | **bool**| Whether or not third-party updates should be run asynchronously. | [optional]

### Return type

[**PaymentResponse**](PaymentResponse.md)

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

# **payments_list**
> PaginatedPaymentList payments_list()



Returns a list of `Payment` objects.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.accounting
from MergePythonSDK.accounting.api import payments_api

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

# Configure API key authorization: accountTokenAuth
configuration.api_key['accountTokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accountTokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = MergePythonSDK.accounting.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with MergePythonSDK.accounting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = payments_api.PaymentsApi(api_client)
    account_id = "account_id_example" # str | If provided, will only return payments for this account. (optional)
    company_id = "company_id_example" # str | If provided, will only return payments for this company. (optional)
    contact_id = "contact_id_example" # str | If provided, will only return payments for this contact. (optional)
    created_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created after this datetime. (optional)
    created_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created before this datetime. (optional)
    cursor = "cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw" # str | The pagination cursor value. (optional)
    expand = "tracking_categories,contact,account,company" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)
    include_deleted_data = True # bool | Whether to include data that was marked as deleted by third party webhooks. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)
    modified_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, only objects synced by Merge after this date time will be returned. (optional)
    modified_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, only objects synced by Merge before this date time will be returned. (optional)
    page_size = 1 # int | Number of results to return per page. (optional)
    remote_id = "remote_id_example" # str, none_type | The API provider's ID for the given object. (optional)
    transaction_date_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type | If provided, will only return objects created after this datetime. (optional)
    transaction_date_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type | If provided, will only return objects created before this datetime. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.payments_list(account_id=account_id, company_id=company_id, contact_id=contact_id, created_after=created_after, created_before=created_before, cursor=cursor, expand=expand, include_deleted_data=include_deleted_data, include_remote_data=include_remote_data, modified_after=modified_after, modified_before=modified_before, page_size=page_size, remote_id=remote_id, transaction_date_after=transaction_date_after, transaction_date_before=transaction_date_before)
        pprint(api_response)
    except MergePythonSDK.accounting.ApiException as e:
        print("Exception when calling PaymentsApi->payments_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| If provided, will only return payments for this account. | [optional]
 **company_id** | **str**| If provided, will only return payments for this company. | [optional]
 **contact_id** | **str**| If provided, will only return payments for this contact. | [optional]
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

[**PaginatedPaymentList**](PaginatedPaymentList.md)

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

# **payments_meta_post_retrieve**
> MetaResponse payments_meta_post_retrieve()



Returns metadata for `Payment` POSTs.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.accounting
from MergePythonSDK.accounting.api import payments_api
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

# Configure API key authorization: accountTokenAuth
configuration.api_key['accountTokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accountTokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = MergePythonSDK.accounting.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with MergePythonSDK.accounting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = payments_api.PaymentsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.payments_meta_post_retrieve()
        pprint(api_response)
    except MergePythonSDK.accounting.ApiException as e:
        print("Exception when calling PaymentsApi->payments_meta_post_retrieve: %s\n" % e)
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

# **payments_retrieve**
> Payment payments_retrieve(id)



Returns a `Payment` object with the given `id`.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.accounting
from MergePythonSDK.accounting.api import payments_api
from MergePythonSDK.accounting.model.payment import Payment
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

# Configure API key authorization: accountTokenAuth
configuration.api_key['accountTokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['accountTokenAuth'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = MergePythonSDK.accounting.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with MergePythonSDK.accounting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = payments_api.PaymentsApi(api_client)
    id = "id_example" # str | 
    expand = "tracking_categories,contact,account,company" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.payments_retrieve(id)
        pprint(api_response)
    except MergePythonSDK.accounting.ApiException as e:
        print("Exception when calling PaymentsApi->payments_retrieve: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.payments_retrieve(id, expand=expand, include_remote_data=include_remote_data)
        pprint(api_response)
    except MergePythonSDK.accounting.ApiException as e:
        print("Exception when calling PaymentsApi->payments_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional]
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]

### Return type

[**Payment**](Payment.md)

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

