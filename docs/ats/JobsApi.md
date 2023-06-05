# MergePythonSDK.ats.JobsApi

All URIs are relative to *https://api.merge.dev/api/ats/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jobs_list**](JobsApi.md#jobs_list) | **GET** /jobs | 
[**jobs_retrieve**](JobsApi.md#jobs_retrieve) | **GET** /jobs/{id} | 


# **jobs_list**
> PaginatedJobList jobs_list(x_account_token)



Returns a list of `Job` objects.

### Example

* Api Key Authentication (tokenAuth):

```python
import time
import MergePythonSDK.ats
from MergePythonSDK.ats.api import jobs_api

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

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with MergePythonSDK.ats.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jobs_api.JobsApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    code = "code_example" # str, none_type | If provided, will only return jobs with this code. (optional)
    created_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created after this datetime. (optional)
    created_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created before this datetime. (optional)
    cursor = "cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw" # str | The pagination cursor value. (optional)
    expand = "departments,offices,hiring_managers,recruiters" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)
    include_deleted_data = True # bool | Whether to include data that was marked as deleted by third party webhooks. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)
    modified_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, only objects synced by Merge after this date time will be returned. (optional)
    modified_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, only objects synced by Merge before this date time will be returned. (optional)
    offices = "offices_example" # str | If provided, will only return jobs for this office; multiple offices can be separated by commas. (optional)
    page_size = 1 # int | Number of results to return per page. (optional)
    remote_fields = "status" # str | Deprecated. Use show_enum_origins. (optional) if omitted the server will use the default value of "status"
    remote_id = "remote_id_example" # str, none_type | The API provider's ID for the given object. (optional)
    show_enum_origins = "status" # str | Which fields should be returned in non-normalized form. (optional) if omitted the server will use the default value of "status"
    status = "ARCHIVED" # str, none_type | If provided, will only return jobs with this status. Options: ('OPEN', 'CLOSED', 'DRAFT', 'ARCHIVED', 'PENDING')  * `OPEN` - OPEN * `CLOSED` - CLOSED * `DRAFT` - DRAFT * `ARCHIVED` - ARCHIVED * `PENDING` - PENDING (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.jobs_list(x_account_token)
        pprint(api_response)
    except MergePythonSDK.ats.ApiException as e:
        print("Exception when calling JobsApi->jobs_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.jobs_list(x_account_token, code=code, created_after=created_after, created_before=created_before, cursor=cursor, expand=expand, include_deleted_data=include_deleted_data, include_remote_data=include_remote_data, modified_after=modified_after, modified_before=modified_before, offices=offices, page_size=page_size, remote_fields=remote_fields, remote_id=remote_id, show_enum_origins=show_enum_origins, status=status)
        pprint(api_response)
    except MergePythonSDK.ats.ApiException as e:
        print("Exception when calling JobsApi->jobs_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **code** | **str, none_type**| If provided, will only return jobs with this code. | [optional]
 **created_after** | **datetime**| If provided, will only return objects created after this datetime. | [optional]
 **created_before** | **datetime**| If provided, will only return objects created before this datetime. | [optional]
 **cursor** | **str**| The pagination cursor value. | [optional]
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional]
 **include_deleted_data** | **bool**| Whether to include data that was marked as deleted by third party webhooks. | [optional]
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]
 **modified_after** | **datetime**| If provided, only objects synced by Merge after this date time will be returned. | [optional]
 **modified_before** | **datetime**| If provided, only objects synced by Merge before this date time will be returned. | [optional]
 **offices** | **str**| If provided, will only return jobs for this office; multiple offices can be separated by commas. | [optional]
 **page_size** | **int**| Number of results to return per page. | [optional]
 **remote_fields** | **str**| Deprecated. Use show_enum_origins. | [optional] if omitted the server will use the default value of "status"
 **remote_id** | **str, none_type**| The API provider&#39;s ID for the given object. | [optional]
 **show_enum_origins** | **str**| Which fields should be returned in non-normalized form. | [optional] if omitted the server will use the default value of "status"
 **status** | **str, none_type**| If provided, will only return jobs with this status. Options: (&#39;OPEN&#39;, &#39;CLOSED&#39;, &#39;DRAFT&#39;, &#39;ARCHIVED&#39;, &#39;PENDING&#39;)  * &#x60;OPEN&#x60; - OPEN * &#x60;CLOSED&#x60; - CLOSED * &#x60;DRAFT&#x60; - DRAFT * &#x60;ARCHIVED&#x60; - ARCHIVED * &#x60;PENDING&#x60; - PENDING | [optional]

### Return type

[**PaginatedJobList**](PaginatedJobList.md)

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

# **jobs_retrieve**
> Job jobs_retrieve(x_account_token, id)



Returns a `Job` object with the given `id`.

### Example

* Api Key Authentication (tokenAuth):

```python
import time
import MergePythonSDK.ats
from MergePythonSDK.ats.api import jobs_api
from MergePythonSDK.ats.model.job import Job
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

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with MergePythonSDK.ats.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jobs_api.JobsApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    id = "id_example" # str | 
    expand = "departments,offices,hiring_managers,recruiters" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)
    remote_fields = "status" # str | Deprecated. Use show_enum_origins. (optional) if omitted the server will use the default value of "status"
    show_enum_origins = "status" # str | Which fields should be returned in non-normalized form. (optional) if omitted the server will use the default value of "status"

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.jobs_retrieve(x_account_token, id)
        pprint(api_response)
    except MergePythonSDK.ats.ApiException as e:
        print("Exception when calling JobsApi->jobs_retrieve: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.jobs_retrieve(x_account_token, id, expand=expand, include_remote_data=include_remote_data, remote_fields=remote_fields, show_enum_origins=show_enum_origins)
        pprint(api_response)
    except MergePythonSDK.ats.ApiException as e:
        print("Exception when calling JobsApi->jobs_retrieve: %s\n" % e)
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

[**Job**](Job.md)

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

