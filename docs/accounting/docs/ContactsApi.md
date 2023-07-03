# MergePythonSDK.accounting.ContactsApi

All URIs are relative to *https://api.merge.dev/api/accounting/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**contacts_create**](ContactsApi.md#contacts_create) | **POST** /contacts | 
[**contacts_list**](ContactsApi.md#contacts_list) | **GET** /contacts | 
[**contacts_meta_post_retrieve**](ContactsApi.md#contacts_meta_post_retrieve) | **GET** /contacts/meta/post | 
[**contacts_retrieve**](ContactsApi.md#contacts_retrieve) | **GET** /contacts/{id} | 


# **contacts_create**
> ContactResponse contacts_create(contact_endpoint_request)



Creates a `Contact` object with the given values.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.accounting
from MergePythonSDK.accounting.api import contacts_api
from MergePythonSDK.accounting.model.contact_response import ContactResponse
from MergePythonSDK.accounting.model.contact_endpoint_request import ContactEndpointRequest
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
    api_instance = contacts_api.ContactsApi(api_client)
    contact_endpoint_request = ContactEndpointRequest(
        model=ContactRequest(
            name="Gil Feig's Pickleball Team",
            is_supplier=True,
            is_customer=True,
            email_address="pickleball@merge.dev",
            tax_number="12-3456789",
            status=None,
            currency="USD",
            company="595c8f97-2ac4-45b7-b000-41bdf43240b5",
            addresses=["2f2702aa-8948-492b-a412-2acdf6d2c499","d98c7428-8dda-48a8-a1da-c570f65e2375"],
            phone_numbers=[
                AccountingPhoneNumberRequest(
                    number="+3198675309",
                    type="Mobile",
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
    ) # ContactEndpointRequest | 
    is_debug_mode = True # bool | Whether to include debug fields (such as log file links) in the response. (optional)
    run_async = True # bool | Whether or not third-party updates should be run asynchronously. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.contacts_create(contact_endpoint_request)
        pprint(api_response)
    except MergePythonSDK.accounting.ApiException as e:
        print("Exception when calling ContactsApi->contacts_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.contacts_create(contact_endpoint_request, is_debug_mode=is_debug_mode, run_async=run_async)
        pprint(api_response)
    except MergePythonSDK.accounting.ApiException as e:
        print("Exception when calling ContactsApi->contacts_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_endpoint_request** | [**ContactEndpointRequest**](ContactEndpointRequest.md)|  |
 **is_debug_mode** | **bool**| Whether to include debug fields (such as log file links) in the response. | [optional]
 **run_async** | **bool**| Whether or not third-party updates should be run asynchronously. | [optional]

### Return type

[**ContactResponse**](ContactResponse.md)

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

# **contacts_list**
> PaginatedContactList contacts_list()



Returns a list of `Contact` objects.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.accounting
from MergePythonSDK.accounting.api import contacts_api

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
    api_instance = contacts_api.ContactsApi(api_client)
    company_id = "company_id_example" # str | If provided, will only return contacts for this company. (optional)
    created_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created after this datetime. (optional)
    created_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created before this datetime. (optional)
    cursor = "cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw" # str | The pagination cursor value. (optional)
    expand = "addresses,phone_numbers,company" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)
    include_deleted_data = True # bool | Whether to include data that was marked as deleted by third party webhooks. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)
    modified_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, only objects synced by Merge after this date time will be returned. (optional)
    modified_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, only objects synced by Merge before this date time will be returned. (optional)
    page_size = 1 # int | Number of results to return per page. (optional)
    remote_fields = "status" # str | Deprecated. Use show_enum_origins. (optional) if omitted the server will use the default value of "status"
    remote_id = "remote_id_example" # str, none_type | The API provider's ID for the given object. (optional)
    show_enum_origins = "status" # str | Which fields should be returned in non-normalized form. (optional) if omitted the server will use the default value of "status"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.contacts_list(company_id=company_id, created_after=created_after, created_before=created_before, cursor=cursor, expand=expand, include_deleted_data=include_deleted_data, include_remote_data=include_remote_data, modified_after=modified_after, modified_before=modified_before, page_size=page_size, remote_fields=remote_fields, remote_id=remote_id, show_enum_origins=show_enum_origins)
        pprint(api_response)
    except MergePythonSDK.accounting.ApiException as e:
        print("Exception when calling ContactsApi->contacts_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| If provided, will only return contacts for this company. | [optional]
 **created_after** | **datetime**| If provided, will only return objects created after this datetime. | [optional]
 **created_before** | **datetime**| If provided, will only return objects created before this datetime. | [optional]
 **cursor** | **str**| The pagination cursor value. | [optional]
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional]
 **include_deleted_data** | **bool**| Whether to include data that was marked as deleted by third party webhooks. | [optional]
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]
 **modified_after** | **datetime**| If provided, only objects synced by Merge after this date time will be returned. | [optional]
 **modified_before** | **datetime**| If provided, only objects synced by Merge before this date time will be returned. | [optional]
 **page_size** | **int**| Number of results to return per page. | [optional]
 **remote_fields** | **str**| Deprecated. Use show_enum_origins. | [optional] if omitted the server will use the default value of "status"
 **remote_id** | **str, none_type**| The API provider&#39;s ID for the given object. | [optional]
 **show_enum_origins** | **str**| Which fields should be returned in non-normalized form. | [optional] if omitted the server will use the default value of "status"

### Return type

[**PaginatedContactList**](PaginatedContactList.md)

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

# **contacts_meta_post_retrieve**
> MetaResponse contacts_meta_post_retrieve()



Returns metadata for `Contact` POSTs.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.accounting
from MergePythonSDK.accounting.api import contacts_api
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
    api_instance = contacts_api.ContactsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.contacts_meta_post_retrieve()
        pprint(api_response)
    except MergePythonSDK.accounting.ApiException as e:
        print("Exception when calling ContactsApi->contacts_meta_post_retrieve: %s\n" % e)
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

# **contacts_retrieve**
> Contact contacts_retrieve(id)



Returns a `Contact` object with the given `id`.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.accounting
from MergePythonSDK.accounting.api import contacts_api
from MergePythonSDK.accounting.model.contact import Contact
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
    api_instance = contacts_api.ContactsApi(api_client)
    id = "id_example" # str | 
    expand = "addresses,phone_numbers,company" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)
    remote_fields = "status" # str | Deprecated. Use show_enum_origins. (optional) if omitted the server will use the default value of "status"
    show_enum_origins = "status" # str | Which fields should be returned in non-normalized form. (optional) if omitted the server will use the default value of "status"

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.contacts_retrieve(id)
        pprint(api_response)
    except MergePythonSDK.accounting.ApiException as e:
        print("Exception when calling ContactsApi->contacts_retrieve: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.contacts_retrieve(id, expand=expand, include_remote_data=include_remote_data, remote_fields=remote_fields, show_enum_origins=show_enum_origins)
        pprint(api_response)
    except MergePythonSDK.accounting.ApiException as e:
        print("Exception when calling ContactsApi->contacts_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional]
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]
 **remote_fields** | **str**| Deprecated. Use show_enum_origins. | [optional] if omitted the server will use the default value of "status"
 **show_enum_origins** | **str**| Which fields should be returned in non-normalized form. | [optional] if omitted the server will use the default value of "status"

### Return type

[**Contact**](Contact.md)

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

