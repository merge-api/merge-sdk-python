# MergePythonSDK.crm.LeadsApi

All URIs are relative to *https://api.merge.dev/api/crm/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**leads_create**](LeadsApi.md#leads_create) | **POST** /leads | 
[**leads_list**](LeadsApi.md#leads_list) | **GET** /leads | 
[**leads_meta_post_retrieve**](LeadsApi.md#leads_meta_post_retrieve) | **GET** /leads/meta/post | 
[**leads_remote_field_classes_list**](LeadsApi.md#leads_remote_field_classes_list) | **GET** /leads/remote-field-classes | 
[**leads_retrieve**](LeadsApi.md#leads_retrieve) | **GET** /leads/{id} | 


# **leads_create**
> LeadResponse leads_create(lead_endpoint_request)



Creates a `Lead` object with the given values.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.crm
from MergePythonSDK.crm.api import leads_api
from MergePythonSDK.crm.model.lead_endpoint_request import LeadEndpointRequest
from MergePythonSDK.crm.model.lead_response import LeadResponse
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
    api_instance = leads_api.LeadsApi(api_client)
    lead_endpoint_request = LeadEndpointRequest(
        model=LeadRequest(
            owner="0358cbc6-2040-430a-848e-aafacbadf3aa",
            lead_source="API Blogger",
            title="Co-Founder",
            company="Merge API",
            first_name="Gil",
            last_name="Feig",
            addresses=[
                AddressRequest(
                    street_1="50 Bowling Green Dr",
                    street_2="Golden Gate Park",
                    city="San Francisco",
                    state="CA",
                    postal_code="94122",
                    country=None,
                    address_type=None,
                    integration_params={
                        "key": None,
                    },
                    linked_account_params={
                        "key": None,
                    },
                ),
            ],
            email_addresses=[
                EmailAddressRequest(
                    email_address="merge_is_hiring@merge.dev",
                    email_address_type="Work",
                    integration_params={
                        "key": None,
                    },
                    linked_account_params={
                        "key": None,
                    },
                ),
            ],
            phone_numbers=[
                PhoneNumberRequest(
                    phone_number="+3198675309",
                    phone_number_type="Mobile",
                    integration_params={
                        "key": None,
                    },
                    linked_account_params={
                        "key": None,
                    },
                ),
            ],
            converted_date=dateutil_parser('2022-03-10T00:00:00Z'),
            converted_contact="converted_contact_example",
            converted_account="9c9de072-29cf-48e3-9578-1ca5b145b40e",
            integration_params={
                "key": None,
            },
            linked_account_params={
                "key": None,
            },
            remote_fields=[
                RemoteFieldRequest(
                    remote_field_class="b057d1d2-c204-4da8-a74c-c91d1a260614",
                    value={
                        "key": None,
                    },
                ),
            ],
        ),
    ) # LeadEndpointRequest | 
    is_debug_mode = True # bool | Whether to include debug fields (such as log file links) in the response. (optional)
    run_async = True # bool | Whether or not third-party updates should be run asynchronously. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.leads_create(lead_endpoint_request)
        pprint(api_response)
    except MergePythonSDK.crm.ApiException as e:
        print("Exception when calling LeadsApi->leads_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.leads_create(lead_endpoint_request, is_debug_mode=is_debug_mode, run_async=run_async)
        pprint(api_response)
    except MergePythonSDK.crm.ApiException as e:
        print("Exception when calling LeadsApi->leads_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lead_endpoint_request** | [**LeadEndpointRequest**](LeadEndpointRequest.md)|  |
 **is_debug_mode** | **bool**| Whether to include debug fields (such as log file links) in the response. | [optional]
 **run_async** | **bool**| Whether or not third-party updates should be run asynchronously. | [optional]

### Return type

[**LeadResponse**](LeadResponse.md)

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

# **leads_list**
> PaginatedLeadList leads_list()



Returns a list of `Lead` objects.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.crm
from MergePythonSDK.crm.api import leads_api

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
    api_instance = leads_api.LeadsApi(api_client)
    converted_account_id = "converted_account_id_example" # str | If provided, will only return leads with this account. (optional)
    converted_contact_id = "converted_contact_id_example" # str | If provided, will only return leads with this contact. (optional)
    created_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created after this datetime. (optional)
    created_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created before this datetime. (optional)
    cursor = "cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw" # str | The pagination cursor value. (optional)
    expand = "owner,converted_contact,converted_account" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)
    include_deleted_data = True # bool | Whether to include data that was marked as deleted by third party webhooks. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)
    include_remote_fields = True # bool | Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format. (optional)
    modified_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, only objects synced by Merge after this date time will be returned. (optional)
    modified_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, only objects synced by Merge before this date time will be returned. (optional)
    owner_id = "owner_id_example" # str | If provided, will only return leads with this owner. (optional)
    page_size = 1 # int | Number of results to return per page. (optional)
    remote_id = "remote_id_example" # str, none_type | The API provider's ID for the given object. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.leads_list(converted_account_id=converted_account_id, converted_contact_id=converted_contact_id, created_after=created_after, created_before=created_before, cursor=cursor, expand=expand, include_deleted_data=include_deleted_data, include_remote_data=include_remote_data, include_remote_fields=include_remote_fields, modified_after=modified_after, modified_before=modified_before, owner_id=owner_id, page_size=page_size, remote_id=remote_id)
        pprint(api_response)
    except MergePythonSDK.crm.ApiException as e:
        print("Exception when calling LeadsApi->leads_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **converted_account_id** | **str**| If provided, will only return leads with this account. | [optional]
 **converted_contact_id** | **str**| If provided, will only return leads with this contact. | [optional]
 **created_after** | **datetime**| If provided, will only return objects created after this datetime. | [optional]
 **created_before** | **datetime**| If provided, will only return objects created before this datetime. | [optional]
 **cursor** | **str**| The pagination cursor value. | [optional]
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional]
 **include_deleted_data** | **bool**| Whether to include data that was marked as deleted by third party webhooks. | [optional]
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]
 **include_remote_fields** | **bool**| Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format. | [optional]
 **modified_after** | **datetime**| If provided, only objects synced by Merge after this date time will be returned. | [optional]
 **modified_before** | **datetime**| If provided, only objects synced by Merge before this date time will be returned. | [optional]
 **owner_id** | **str**| If provided, will only return leads with this owner. | [optional]
 **page_size** | **int**| Number of results to return per page. | [optional]
 **remote_id** | **str, none_type**| The API provider&#39;s ID for the given object. | [optional]

### Return type

[**PaginatedLeadList**](PaginatedLeadList.md)

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

# **leads_meta_post_retrieve**
> MetaResponse leads_meta_post_retrieve()



Returns metadata for `Lead` POSTs.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.crm
from MergePythonSDK.crm.api import leads_api
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
    api_instance = leads_api.LeadsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.leads_meta_post_retrieve()
        pprint(api_response)
    except MergePythonSDK.crm.ApiException as e:
        print("Exception when calling LeadsApi->leads_meta_post_retrieve: %s\n" % e)
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

# **leads_remote_field_classes_list**
> PaginatedRemoteFieldClassList leads_remote_field_classes_list()



Returns a list of `RemoteFieldClass` objects.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.crm
from MergePythonSDK.crm.api import leads_api

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
    api_instance = leads_api.LeadsApi(api_client)
    cursor = "cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw" # str | The pagination cursor value. (optional)
    include_deleted_data = True # bool | Whether to include data that was marked as deleted by third party webhooks. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)
    include_remote_fields = True # bool | Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format. (optional)
    page_size = 1 # int | Number of results to return per page. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.leads_remote_field_classes_list(cursor=cursor, include_deleted_data=include_deleted_data, include_remote_data=include_remote_data, include_remote_fields=include_remote_fields, page_size=page_size)
        pprint(api_response)
    except MergePythonSDK.crm.ApiException as e:
        print("Exception when calling LeadsApi->leads_remote_field_classes_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| The pagination cursor value. | [optional]
 **include_deleted_data** | **bool**| Whether to include data that was marked as deleted by third party webhooks. | [optional]
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]
 **include_remote_fields** | **bool**| Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format. | [optional]
 **page_size** | **int**| Number of results to return per page. | [optional]

### Return type

[**PaginatedRemoteFieldClassList**](PaginatedRemoteFieldClassList.md)

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

# **leads_retrieve**
> Lead leads_retrieve(id)



Returns a `Lead` object with the given `id`.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.crm
from MergePythonSDK.crm.api import leads_api
from MergePythonSDK.crm.model.lead import Lead
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
    api_instance = leads_api.LeadsApi(api_client)
    id = "id_example" # str | 
    expand = "owner,converted_contact,converted_account" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)
    include_remote_fields = True # bool | Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.leads_retrieve(id)
        pprint(api_response)
    except MergePythonSDK.crm.ApiException as e:
        print("Exception when calling LeadsApi->leads_retrieve: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.leads_retrieve(id, expand=expand, include_remote_data=include_remote_data, include_remote_fields=include_remote_fields)
        pprint(api_response)
    except MergePythonSDK.crm.ApiException as e:
        print("Exception when calling LeadsApi->leads_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional]
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]
 **include_remote_fields** | **bool**| Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format. | [optional]

### Return type

[**Lead**](Lead.md)

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

