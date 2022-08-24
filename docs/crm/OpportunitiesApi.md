# MergePythonSDK.crm.OpportunitiesApi

All URIs are relative to *https://api.merge.dev/api/crm/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**opportunities_create**](OpportunitiesApi.md#opportunities_create) | **POST** /opportunities | 
[**opportunities_list**](OpportunitiesApi.md#opportunities_list) | **GET** /opportunities | 
[**opportunities_meta_post_retrieve**](OpportunitiesApi.md#opportunities_meta_post_retrieve) | **GET** /opportunities/meta/post | 
[**opportunities_retrieve**](OpportunitiesApi.md#opportunities_retrieve) | **GET** /opportunities/{id} | 


# **opportunities_create**
> OpportunityResponse opportunities_create(x_account_token, opportunity_endpoint_request)



Creates an `Opportunity` object with the given values.

### Example

* Api Key Authentication (tokenAuth):

```python
import time
import MergePythonSDK.crm
from MergePythonSDK.crm.api import opportunities_api
from MergePythonSDK.crm.model.opportunity_endpoint_request import OpportunityEndpointRequest
from MergePythonSDK.crm.model.opportunity_response import OpportunityResponse
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
    api_instance = opportunities_api.OpportunitiesApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    opportunity_endpoint_request = OpportunityEndpointRequest(
        model=OpportunityRequest(
            remote_id="19202938",
            name="Needs Integrations",
            description="Needs a Unified API for Integrations!",
            amount=100000,
            owner="0358cbc6-2040-430a-848e-aafacbadf3aa",
            account="0958cbc6-6040-430a-848e-aafacbadf4ae",
            stage="1968cbc6-6040-430a-848e-aafacbadf4ad",
            status=None,
            last_activity_at=dateutil_parser('2022-02-10T00:00:00Z'),
            close_date=dateutil_parser('2022-02-10T00:00:00Z'),
            remote_created_at=dateutil_parser('2021-11-10T00:00:00Z'),
            integration_params={
                "key": None,
            },
            linked_account_params={
                "key": None,
            },
        ),
    ) # OpportunityEndpointRequest | 
    is_debug_mode = True # bool | Whether to include debug fields (such as log file links) in the response. (optional)
    run_async = True # bool | Whether or not third-party updates should be run asynchronously. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.opportunities_create(x_account_token, opportunity_endpoint_request)
        pprint(api_response)
    except MergePythonSDK.crm.ApiException as e:
        print("Exception when calling OpportunitiesApi->opportunities_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.opportunities_create(x_account_token, opportunity_endpoint_request, is_debug_mode=is_debug_mode, run_async=run_async)
        pprint(api_response)
    except MergePythonSDK.crm.ApiException as e:
        print("Exception when calling OpportunitiesApi->opportunities_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **opportunity_endpoint_request** | [**OpportunityEndpointRequest**](OpportunityEndpointRequest.md)|  |
 **is_debug_mode** | **bool**| Whether to include debug fields (such as log file links) in the response. | [optional]
 **run_async** | **bool**| Whether or not third-party updates should be run asynchronously. | [optional]

### Return type

[**OpportunityResponse**](OpportunityResponse.md)

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

# **opportunities_list**
> PaginatedOpportunityList opportunities_list(x_account_token)



Returns a list of `Opportunity` objects.

### Example

* Api Key Authentication (tokenAuth):

```python
import time
import MergePythonSDK.crm
from MergePythonSDK.crm.api import opportunities_api
from MergePythonSDK.crm.model.paginated_opportunity_list import PaginatedOpportunityList
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
    api_instance = opportunities_api.OpportunitiesApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    account_id = "account_id_example" # str | If provided, will only return opportunities with this account. (optional)
    created_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created after this datetime. (optional)
    created_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created before this datetime. (optional)
    cursor = "cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw" # str | The pagination cursor value. (optional)
    expand = "owner,stage,account" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)
    include_deleted_data = True # bool | Whether to include data that was marked as deleted by third party webhooks. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)
    modified_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects modified after this datetime. (optional)
    modified_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects modified before this datetime. (optional)
    owner_id = "owner_id_example" # str | If provided, will only return opportunities with this owner. (optional)
    page_size = 1 # int | Number of results to return per page. (optional)
    remote_fields = "status" # str | Which fields should be returned in non-normalized form. (optional) if omitted the server will use the default value of "status"
    remote_id = "remote_id_example" # str, none_type | The API provider's ID for the given object. (optional)
    stage_id = "stage_id_example" # str | If provided, will only return opportunities with this stage. (optional)
    status = "LOST" # str, none_type | If provided, will only return opportunities with this status. Options: ('OPEN', 'WON', 'LOST') (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.opportunities_list(x_account_token)
        pprint(api_response)
    except MergePythonSDK.crm.ApiException as e:
        print("Exception when calling OpportunitiesApi->opportunities_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.opportunities_list(x_account_token, account_id=account_id, created_after=created_after, created_before=created_before, cursor=cursor, expand=expand, include_deleted_data=include_deleted_data, include_remote_data=include_remote_data, modified_after=modified_after, modified_before=modified_before, owner_id=owner_id, page_size=page_size, remote_fields=remote_fields, remote_id=remote_id, stage_id=stage_id, status=status)
        pprint(api_response)
    except MergePythonSDK.crm.ApiException as e:
        print("Exception when calling OpportunitiesApi->opportunities_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **account_id** | **str**| If provided, will only return opportunities with this account. | [optional]
 **created_after** | **datetime**| If provided, will only return objects created after this datetime. | [optional]
 **created_before** | **datetime**| If provided, will only return objects created before this datetime. | [optional]
 **cursor** | **str**| The pagination cursor value. | [optional]
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional]
 **include_deleted_data** | **bool**| Whether to include data that was marked as deleted by third party webhooks. | [optional]
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]
 **modified_after** | **datetime**| If provided, will only return objects modified after this datetime. | [optional]
 **modified_before** | **datetime**| If provided, will only return objects modified before this datetime. | [optional]
 **owner_id** | **str**| If provided, will only return opportunities with this owner. | [optional]
 **page_size** | **int**| Number of results to return per page. | [optional]
 **remote_fields** | **str**| Which fields should be returned in non-normalized form. | [optional] if omitted the server will use the default value of "status"
 **remote_id** | **str, none_type**| The API provider&#39;s ID for the given object. | [optional]
 **stage_id** | **str**| If provided, will only return opportunities with this stage. | [optional]
 **status** | **str, none_type**| If provided, will only return opportunities with this status. Options: (&#39;OPEN&#39;, &#39;WON&#39;, &#39;LOST&#39;) | [optional]

### Return type

[**PaginatedOpportunityList**](PaginatedOpportunityList.md)

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

# **opportunities_meta_post_retrieve**
> MetaResponse opportunities_meta_post_retrieve(x_account_token)



Returns metadata for `Opportunity` POSTs.

### Example

* Api Key Authentication (tokenAuth):

```python
import time
import MergePythonSDK.crm
from MergePythonSDK.crm.api import opportunities_api
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
    api_instance = opportunities_api.OpportunitiesApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.opportunities_meta_post_retrieve(x_account_token)
        pprint(api_response)
    except MergePythonSDK.crm.ApiException as e:
        print("Exception when calling OpportunitiesApi->opportunities_meta_post_retrieve: %s\n" % e)
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

# **opportunities_retrieve**
> Opportunity opportunities_retrieve(x_account_token, id)



Returns an `Opportunity` object with the given `id`.

### Example

* Api Key Authentication (tokenAuth):

```python
import time
import MergePythonSDK.crm
from MergePythonSDK.crm.api import opportunities_api
from MergePythonSDK.crm.model.opportunity import Opportunity
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
    api_instance = opportunities_api.OpportunitiesApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    id = "id_example" # str | 
    expand = "owner,stage,account" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)
    remote_fields = "status" # str | Which fields should be returned in non-normalized form. (optional) if omitted the server will use the default value of "status"

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.opportunities_retrieve(x_account_token, id)
        pprint(api_response)
    except MergePythonSDK.crm.ApiException as e:
        print("Exception when calling OpportunitiesApi->opportunities_retrieve: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.opportunities_retrieve(x_account_token, id, expand=expand, include_remote_data=include_remote_data, remote_fields=remote_fields)
        pprint(api_response)
    except MergePythonSDK.crm.ApiException as e:
        print("Exception when calling OpportunitiesApi->opportunities_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **id** | **str**|  |
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional]
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]
 **remote_fields** | **str**| Which fields should be returned in non-normalized form. | [optional] if omitted the server will use the default value of "status"

### Return type

[**Opportunity**](Opportunity.md)

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

