# MergePythonSDK.ats.CandidatesApi

All URIs are relative to *https://api.merge.dev/api/ats/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**candidates_create**](CandidatesApi.md#candidates_create) | **POST** /candidates | 
[**candidates_ignore_create**](CandidatesApi.md#candidates_ignore_create) | **POST** /candidates/ignore/{model_id} | 
[**candidates_list**](CandidatesApi.md#candidates_list) | **GET** /candidates | 
[**candidates_meta_patch_retrieve**](CandidatesApi.md#candidates_meta_patch_retrieve) | **GET** /candidates/meta/patch/{id} | 
[**candidates_meta_post_retrieve**](CandidatesApi.md#candidates_meta_post_retrieve) | **GET** /candidates/meta/post | 
[**candidates_partial_update**](CandidatesApi.md#candidates_partial_update) | **PATCH** /candidates/{id} | 
[**candidates_retrieve**](CandidatesApi.md#candidates_retrieve) | **GET** /candidates/{id} | 


# **candidates_create**
> CandidateResponse candidates_create(candidate_endpoint_request)



Creates a `Candidate` object with the given values.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.ats
from MergePythonSDK.ats.api import candidates_api
from MergePythonSDK.ats.model.candidate_endpoint_request import CandidateEndpointRequest
from MergePythonSDK.ats.model.candidate_response import CandidateResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.merge.dev/api/ats/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = MergePythonSDK.ats.Configuration(
    host = "https://api.merge.dev/api/ats/v1"
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
configuration = MergePythonSDK.ats.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with MergePythonSDK.ats.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = candidates_api.CandidatesApi(api_client)
    candidate_endpoint_request = CandidateEndpointRequest(
        model=CandidateRequest(
            first_name="Gil",
            last_name="Feig",
            company="Columbia Dining App.",
            title="Software Engineer",
            last_interaction_at=dateutil_parser('2021-10-17T00:00:00Z'),
            is_private=True,
            can_email=True,
            locations=["San Francisco","New York","Miami"],
            phone_numbers=[
                PhoneNumberRequest(
                    value="+3198675309",
                    phone_number_type=None,
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
                    value="merge_is_hiring@merge.dev",
                    email_address_type=None,
                    integration_params={
                        "key": None,
                    },
                    linked_account_params={
                        "key": None,
                    },
                ),
            ],
            urls=[
                UrlRequest(
                    value="http://alturl.com/p749b",
                    url_type=None,
                    integration_params={
                        "key": None,
                    },
                    linked_account_params={
                        "key": None,
                    },
                ),
            ],
            tags=["High-Priority"],
            applications=["29eb9867-ce2a-403f-b8ce-f2844b89f078","b4d08e5c-de00-4d64-a29f-66addac9af99","4ff877d2-fb3e-4a5b-a7a5-168ddf2ffa56"],
            attachments=["bea08964-32b4-4a20-8bb4-2612ba09de1d"],
            remote_template_id="92830948203",
            integration_params={
                "key": None,
            },
            linked_account_params={
                "key": None,
            },
        ),
        remote_user_id="remote_user_id_example",
    ) # CandidateEndpointRequest | 
    is_debug_mode = True # bool | Whether to include debug fields (such as log file links) in the response. (optional)
    run_async = True # bool | Whether or not third-party updates should be run asynchronously. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.candidates_create(candidate_endpoint_request)
        pprint(api_response)
    except MergePythonSDK.ats.ApiException as e:
        print("Exception when calling CandidatesApi->candidates_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.candidates_create(candidate_endpoint_request, is_debug_mode=is_debug_mode, run_async=run_async)
        pprint(api_response)
    except MergePythonSDK.ats.ApiException as e:
        print("Exception when calling CandidatesApi->candidates_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **candidate_endpoint_request** | [**CandidateEndpointRequest**](CandidateEndpointRequest.md)|  |
 **is_debug_mode** | **bool**| Whether to include debug fields (such as log file links) in the response. | [optional]
 **run_async** | **bool**| Whether or not third-party updates should be run asynchronously. | [optional]

### Return type

[**CandidateResponse**](CandidateResponse.md)

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

# **candidates_ignore_create**
> candidates_ignore_create(model_id, ignore_common_model_request)



Ignores a specific row based on the `model_id` in the url. These records will have their properties set to null, and will not be updated in future syncs. The \"reason\" and \"message\" fields in the request body will be stored for audit purposes.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.ats
from MergePythonSDK.ats.api import candidates_api
from MergePythonSDK.ats.model.ignore_common_model_request import IgnoreCommonModelRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.merge.dev/api/ats/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = MergePythonSDK.ats.Configuration(
    host = "https://api.merge.dev/api/ats/v1"
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
configuration = MergePythonSDK.ats.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with MergePythonSDK.ats.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = candidates_api.CandidatesApi(api_client)
    model_id = "model_id_example" # str | 
    ignore_common_model_request = IgnoreCommonModelRequest(
        reason=None,
        message="deletion request by user id 51903790-7dfe-4053-8d63-5a10cc4ffd39",
    ) # IgnoreCommonModelRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.candidates_ignore_create(model_id, ignore_common_model_request)
    except MergePythonSDK.ats.ApiException as e:
        print("Exception when calling CandidatesApi->candidates_ignore_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **str**|  |
 **ignore_common_model_request** | [**IgnoreCommonModelRequest**](IgnoreCommonModelRequest.md)|  |

### Return type

void (empty response body)

### Authorization

[accountTokenAuth](../README.md#accountTokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No response body |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **candidates_list**
> PaginatedCandidateList candidates_list()



Returns a list of `Candidate` objects.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.ats
from MergePythonSDK.ats.api import candidates_api
from MergePythonSDK.ats.model.paginated_candidate_list import PaginatedCandidateList
from pprint import pprint
# Defining the host is optional and defaults to https://api.merge.dev/api/ats/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = MergePythonSDK.ats.Configuration(
    host = "https://api.merge.dev/api/ats/v1"
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
configuration = MergePythonSDK.ats.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with MergePythonSDK.ats.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = candidates_api.CandidatesApi(api_client)
    created_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created after this datetime. (optional)
    created_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created before this datetime. (optional)
    cursor = "cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw" # str | The pagination cursor value. (optional)
    email_addresses = "email_addresses_example" # str | If provided, will only return candidates with these email addresses; multiple addresses can be separated by commas. (optional)
    expand = "applications,attachments" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)
    first_name = "first_name_example" # str, none_type | If provided, will only return candidates with this first name. (optional)
    include_deleted_data = True # bool | Whether to include data that was marked as deleted by third party webhooks. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)
    last_name = "last_name_example" # str, none_type | If provided, will only return candidates with this last name. (optional)
    modified_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, only objects synced by Merge after this date time will be returned. (optional)
    modified_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, only objects synced by Merge before this date time will be returned. (optional)
    page_size = 1 # int | Number of results to return per page. (optional)
    remote_id = "remote_id_example" # str, none_type | The API provider's ID for the given object. (optional)
    tags = "tags_example" # str | If provided, will only return candidates with these tags; multiple tags can be separated by commas. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.candidates_list(created_after=created_after, created_before=created_before, cursor=cursor, email_addresses=email_addresses, expand=expand, first_name=first_name, include_deleted_data=include_deleted_data, include_remote_data=include_remote_data, last_name=last_name, modified_after=modified_after, modified_before=modified_before, page_size=page_size, remote_id=remote_id, tags=tags)
        pprint(api_response)
    except MergePythonSDK.ats.ApiException as e:
        print("Exception when calling CandidatesApi->candidates_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **created_after** | **datetime**| If provided, will only return objects created after this datetime. | [optional]
 **created_before** | **datetime**| If provided, will only return objects created before this datetime. | [optional]
 **cursor** | **str**| The pagination cursor value. | [optional]
 **email_addresses** | **str**| If provided, will only return candidates with these email addresses; multiple addresses can be separated by commas. | [optional]
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional]
 **first_name** | **str, none_type**| If provided, will only return candidates with this first name. | [optional]
 **include_deleted_data** | **bool**| Whether to include data that was marked as deleted by third party webhooks. | [optional]
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]
 **last_name** | **str, none_type**| If provided, will only return candidates with this last name. | [optional]
 **modified_after** | **datetime**| If provided, only objects synced by Merge after this date time will be returned. | [optional]
 **modified_before** | **datetime**| If provided, only objects synced by Merge before this date time will be returned. | [optional]
 **page_size** | **int**| Number of results to return per page. | [optional]
 **remote_id** | **str, none_type**| The API provider&#39;s ID for the given object. | [optional]
 **tags** | **str**| If provided, will only return candidates with these tags; multiple tags can be separated by commas. | [optional]

### Return type

[**PaginatedCandidateList**](PaginatedCandidateList.md)

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

# **candidates_meta_patch_retrieve**
> MetaResponse candidates_meta_patch_retrieve(id)



Returns metadata for `Candidate` PATCHs.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.ats
from MergePythonSDK.ats.api import candidates_api
from MergePythonSDK.ats.model.meta_response import MetaResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.merge.dev/api/ats/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = MergePythonSDK.ats.Configuration(
    host = "https://api.merge.dev/api/ats/v1"
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
configuration = MergePythonSDK.ats.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with MergePythonSDK.ats.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = candidates_api.CandidatesApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.candidates_meta_patch_retrieve(id)
        pprint(api_response)
    except MergePythonSDK.ats.ApiException as e:
        print("Exception when calling CandidatesApi->candidates_meta_patch_retrieve: %s\n" % e)
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

# **candidates_meta_post_retrieve**
> MetaResponse candidates_meta_post_retrieve()



Returns metadata for `Candidate` POSTs.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.ats
from MergePythonSDK.ats.api import candidates_api
from MergePythonSDK.ats.model.meta_response import MetaResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.merge.dev/api/ats/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = MergePythonSDK.ats.Configuration(
    host = "https://api.merge.dev/api/ats/v1"
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
configuration = MergePythonSDK.ats.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with MergePythonSDK.ats.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = candidates_api.CandidatesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.candidates_meta_post_retrieve()
        pprint(api_response)
    except MergePythonSDK.ats.ApiException as e:
        print("Exception when calling CandidatesApi->candidates_meta_post_retrieve: %s\n" % e)
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

# **candidates_partial_update**
> CandidateResponse candidates_partial_update(id, patched_candidate_endpoint_request)



Updates a `Candidate` object with the given `id`.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.ats
from MergePythonSDK.ats.api import candidates_api
from MergePythonSDK.ats.model.patched_candidate_endpoint_request import PatchedCandidateEndpointRequest
from MergePythonSDK.ats.model.candidate_response import CandidateResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.merge.dev/api/ats/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = MergePythonSDK.ats.Configuration(
    host = "https://api.merge.dev/api/ats/v1"
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
configuration = MergePythonSDK.ats.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with MergePythonSDK.ats.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = candidates_api.CandidatesApi(api_client)
    id = "id_example" # str | 
    patched_candidate_endpoint_request = PatchedCandidateEndpointRequest(
        model=PatchedCandidateRequest(
            first_name="Gil",
            last_name="Feig",
            company="Columbia Dining App.",
            title="Software Engineer",
            last_interaction_at=dateutil_parser('2021-10-17T00:00:00Z'),
            is_private=True,
            can_email=True,
            locations=["San Francisco","New York","Miami"],
            phone_numbers=[
                PhoneNumberRequest(
                    value="+3198675309",
                    phone_number_type=None,
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
                    value="merge_is_hiring@merge.dev",
                    email_address_type=None,
                    integration_params={
                        "key": None,
                    },
                    linked_account_params={
                        "key": None,
                    },
                ),
            ],
            urls=[
                UrlRequest(
                    value="http://alturl.com/p749b",
                    url_type=None,
                    integration_params={
                        "key": None,
                    },
                    linked_account_params={
                        "key": None,
                    },
                ),
            ],
            tags=["High-Priority"],
            applications=["29eb9867-ce2a-403f-b8ce-f2844b89f078","b4d08e5c-de00-4d64-a29f-66addac9af99","4ff877d2-fb3e-4a5b-a7a5-168ddf2ffa56"],
            attachments=["bea08964-32b4-4a20-8bb4-2612ba09de1d"],
            remote_template_id="92830948203",
            integration_params={
                "key": None,
            },
            linked_account_params={
                "key": None,
            },
        ),
        remote_user_id="remote_user_id_example",
    ) # PatchedCandidateEndpointRequest | 
    is_debug_mode = True # bool | Whether to include debug fields (such as log file links) in the response. (optional)
    run_async = True # bool | Whether or not third-party updates should be run asynchronously. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.candidates_partial_update(id, patched_candidate_endpoint_request)
        pprint(api_response)
    except MergePythonSDK.ats.ApiException as e:
        print("Exception when calling CandidatesApi->candidates_partial_update: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.candidates_partial_update(id, patched_candidate_endpoint_request, is_debug_mode=is_debug_mode, run_async=run_async)
        pprint(api_response)
    except MergePythonSDK.ats.ApiException as e:
        print("Exception when calling CandidatesApi->candidates_partial_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **patched_candidate_endpoint_request** | [**PatchedCandidateEndpointRequest**](PatchedCandidateEndpointRequest.md)|  |
 **is_debug_mode** | **bool**| Whether to include debug fields (such as log file links) in the response. | [optional]
 **run_async** | **bool**| Whether or not third-party updates should be run asynchronously. | [optional]

### Return type

[**CandidateResponse**](CandidateResponse.md)

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

# **candidates_retrieve**
> Candidate candidates_retrieve(id)



Returns a `Candidate` object with the given `id`.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.ats
from MergePythonSDK.ats.api import candidates_api
from MergePythonSDK.ats.model.candidate import Candidate
from pprint import pprint
# Defining the host is optional and defaults to https://api.merge.dev/api/ats/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = MergePythonSDK.ats.Configuration(
    host = "https://api.merge.dev/api/ats/v1"
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
configuration = MergePythonSDK.ats.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with MergePythonSDK.ats.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = candidates_api.CandidatesApi(api_client)
    id = "id_example" # str | 
    expand = "applications,attachments" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.candidates_retrieve(id)
        pprint(api_response)
    except MergePythonSDK.ats.ApiException as e:
        print("Exception when calling CandidatesApi->candidates_retrieve: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.candidates_retrieve(id, expand=expand, include_remote_data=include_remote_data)
        pprint(api_response)
    except MergePythonSDK.ats.ApiException as e:
        print("Exception when calling CandidatesApi->candidates_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional]
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]

### Return type

[**Candidate**](Candidate.md)

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

