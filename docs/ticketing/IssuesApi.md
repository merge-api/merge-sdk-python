# MergePythonSDK.ticketing.IssuesApi

All URIs are relative to *https://api.merge.dev/api/ticketing/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**issues_list**](IssuesApi.md#issues_list) | **GET** /issues | 
[**issues_retrieve**](IssuesApi.md#issues_retrieve) | **GET** /issues/{id} | 


# **issues_list**
> PaginatedIssueList issues_list()



Gets issues.

### Example

* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.ticketing
from MergePythonSDK.ticketing.api import issues_api

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

# Configure Bearer authorization: bearerAuth
configuration = MergePythonSDK.ticketing.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with MergePythonSDK.ticketing.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issues_api.IssuesApi(api_client)
    account_token = "account_token_example" # str |  (optional)
    cursor = "cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw" # str | The pagination cursor value. (optional)
    end_date = "end_date_example" # str | If included, will only include issues whose most recent action occurred before this time (optional)
    end_user_organization_name = "end_user_organization_name_example" # str |  (optional)
    first_incident_time_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type | If provided, will only return issues whose first incident time was after this datetime. (optional)
    first_incident_time_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type | If provided, will only return issues whose first incident time was before this datetime. (optional)
    include_muted = "include_muted_example" # str | If True, will include muted issues (optional)
    integration_name = "integration_name_example" # str |  (optional)
    last_incident_time_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type | If provided, will only return issues whose last incident time was after this datetime. (optional)
    last_incident_time_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type | If provided, will only return issues whose last incident time was before this datetime. (optional)
    page_size = 1 # int | Number of results to return per page. (optional)
    start_date = "start_date_example" # str | If included, will only include issues whose most recent action occurred after this time (optional)
    status = "ONGOING" # str | Status of the issue. Options: ('ONGOING', 'RESOLVED')  * `ONGOING` - ONGOING * `RESOLVED` - RESOLVED (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.issues_list(account_token=account_token, cursor=cursor, end_date=end_date, end_user_organization_name=end_user_organization_name, first_incident_time_after=first_incident_time_after, first_incident_time_before=first_incident_time_before, include_muted=include_muted, integration_name=integration_name, last_incident_time_after=last_incident_time_after, last_incident_time_before=last_incident_time_before, page_size=page_size, start_date=start_date, status=status)
        pprint(api_response)
    except MergePythonSDK.ticketing.ApiException as e:
        print("Exception when calling IssuesApi->issues_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_token** | **str**|  | [optional]
 **cursor** | **str**| The pagination cursor value. | [optional]
 **end_date** | **str**| If included, will only include issues whose most recent action occurred before this time | [optional]
 **end_user_organization_name** | **str**|  | [optional]
 **first_incident_time_after** | **datetime, none_type**| If provided, will only return issues whose first incident time was after this datetime. | [optional]
 **first_incident_time_before** | **datetime, none_type**| If provided, will only return issues whose first incident time was before this datetime. | [optional]
 **include_muted** | **str**| If True, will include muted issues | [optional]
 **integration_name** | **str**|  | [optional]
 **last_incident_time_after** | **datetime, none_type**| If provided, will only return issues whose last incident time was after this datetime. | [optional]
 **last_incident_time_before** | **datetime, none_type**| If provided, will only return issues whose last incident time was before this datetime. | [optional]
 **page_size** | **int**| Number of results to return per page. | [optional]
 **start_date** | **str**| If included, will only include issues whose most recent action occurred after this time | [optional]
 **status** | **str**| Status of the issue. Options: (&#39;ONGOING&#39;, &#39;RESOLVED&#39;)  * &#x60;ONGOING&#x60; - ONGOING * &#x60;RESOLVED&#x60; - RESOLVED | [optional]

### Return type

[**PaginatedIssueList**](PaginatedIssueList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issues_retrieve**
> Issue issues_retrieve(id)



Get a specific issue.

### Example

* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.ticketing
from MergePythonSDK.ticketing.api import issues_api
from MergePythonSDK.ticketing.model.issue import Issue
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

# Configure Bearer authorization: bearerAuth
configuration = MergePythonSDK.ticketing.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with MergePythonSDK.ticketing.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = issues_api.IssuesApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.issues_retrieve(id)
        pprint(api_response)
    except MergePythonSDK.ticketing.ApiException as e:
        print("Exception when calling IssuesApi->issues_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**Issue**](Issue.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

