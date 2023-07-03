# MergePythonSDK.hris.EmployeesApi

All URIs are relative to *https://api.merge.dev/api/hris/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**employees_create**](EmployeesApi.md#employees_create) | **POST** /employees | 
[**employees_ignore_create**](EmployeesApi.md#employees_ignore_create) | **POST** /employees/ignore/{model_id} | 
[**employees_list**](EmployeesApi.md#employees_list) | **GET** /employees | 
[**employees_meta_post_retrieve**](EmployeesApi.md#employees_meta_post_retrieve) | **GET** /employees/meta/post | 
[**employees_retrieve**](EmployeesApi.md#employees_retrieve) | **GET** /employees/{id} | 


# **employees_create**
> EmployeeResponse employees_create(employee_endpoint_request)



Creates an `Employee` object with the given values.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.hris
from MergePythonSDK.hris.api import employees_api
from MergePythonSDK.hris.model.employee_response import EmployeeResponse
from MergePythonSDK.hris.model.employee_endpoint_request import EmployeeEndpointRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.merge.dev/api/hris/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = MergePythonSDK.hris.Configuration(
    host = "https://api.merge.dev/api/hris/v1"
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
configuration = MergePythonSDK.hris.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with MergePythonSDK.hris.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = employees_api.EmployeesApi(api_client)
    employee_endpoint_request = EmployeeEndpointRequest(
        model=EmployeeRequest(
            employee_number="2",
            company="8d9fd929-436c-4fd4-a48b-0c61f68d6178",
            first_name="Greg",
            last_name="Hirsch",
            display_full_name="Cousin Greg Hirsch",
            username="cousingreg",
            groups=["21a54124-397f-494d-985e-3c5b330b8a68"],
            work_email="greg@merge.dev",
            personal_email="greg@gmail.com",
            mobile_phone_number="+1234567890",
            employments=["17a54124-287f-494d-965e-3c5b330c9a68"],
            home_location="d2f972d0-2526-434b-9409-4c3b468e08f0",
            work_location="9efbc633-3387-4306-aa55-e2c635e6bb4f",
            manager="0048ea5b-911e-4dff-9364-92070dea62ff",
            team="249c9faa-3045-4a31-953b-8f22d3613301",
            pay_group="ad1264e2-39be-4787-b749-f1aade9e3405",
            ssn="1234567890",
            gender=None,
            ethnicity=None,
            marital_status=None,
            date_of_birth=dateutil_parser('1990-11-10T00:00:00Z'),
            hire_date=dateutil_parser('2020-10-10T00:00:00Z'),
            start_date=dateutil_parser('2020-10-11T00:00:00Z'),
            employment_status=None,
            termination_date=dateutil_parser('2021-10-12T00:00:00Z'),
            avatar="http://alturl.com/h2h8m",
            integration_params={
                "key": None,
            },
            linked_account_params={
                "key": None,
            },
        ),
    ) # EmployeeEndpointRequest | 
    is_debug_mode = True # bool | Whether to include debug fields (such as log file links) in the response. (optional)
    run_async = True # bool | Whether or not third-party updates should be run asynchronously. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.employees_create(employee_endpoint_request)
        pprint(api_response)
    except MergePythonSDK.hris.ApiException as e:
        print("Exception when calling EmployeesApi->employees_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.employees_create(employee_endpoint_request, is_debug_mode=is_debug_mode, run_async=run_async)
        pprint(api_response)
    except MergePythonSDK.hris.ApiException as e:
        print("Exception when calling EmployeesApi->employees_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_endpoint_request** | [**EmployeeEndpointRequest**](EmployeeEndpointRequest.md)|  |
 **is_debug_mode** | **bool**| Whether to include debug fields (such as log file links) in the response. | [optional]
 **run_async** | **bool**| Whether or not third-party updates should be run asynchronously. | [optional]

### Return type

[**EmployeeResponse**](EmployeeResponse.md)

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

# **employees_ignore_create**
> employees_ignore_create(model_id, ignore_common_model_request)



Ignores a specific row based on the `model_id` in the url. These records will have their properties set to null, and will not be updated in future syncs. The \"reason\" and \"message\" fields in the request body will be stored for audit purposes.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.hris
from MergePythonSDK.hris.api import employees_api
from MergePythonSDK.hris.model.ignore_common_model_request import IgnoreCommonModelRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.merge.dev/api/hris/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = MergePythonSDK.hris.Configuration(
    host = "https://api.merge.dev/api/hris/v1"
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
configuration = MergePythonSDK.hris.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with MergePythonSDK.hris.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = employees_api.EmployeesApi(api_client)
    model_id = "model_id_example" # str | 
    ignore_common_model_request = IgnoreCommonModelRequest(
        reason=None,
        message="deletion request by user id 51903790-7dfe-4053-8d63-5a10cc4ffd39",
    ) # IgnoreCommonModelRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.employees_ignore_create(model_id, ignore_common_model_request)
    except MergePythonSDK.hris.ApiException as e:
        print("Exception when calling EmployeesApi->employees_ignore_create: %s\n" % e)
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

# **employees_list**
> PaginatedEmployeeList employees_list()



Returns a list of `Employee` objects.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.hris
from MergePythonSDK.hris.api import employees_api

from pprint import pprint
# Defining the host is optional and defaults to https://api.merge.dev/api/hris/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = MergePythonSDK.hris.Configuration(
    host = "https://api.merge.dev/api/hris/v1"
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
configuration = MergePythonSDK.hris.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with MergePythonSDK.hris.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = employees_api.EmployeesApi(api_client)
    company_id = "company_id_example" # str | If provided, will only return employees for this company. (optional)
    created_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created after this datetime. (optional)
    created_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created before this datetime. (optional)
    cursor = "cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw" # str | The pagination cursor value. (optional)
    display_full_name = "display_full_name_example" # str, none_type | If provided, will only return employees with this display name. (optional)
    employment_status = "ACTIVE" # str, none_type | If provided, will only return employees with this employment status.  * `ACTIVE` - ACTIVE * `PENDING` - PENDING * `INACTIVE` - INACTIVE (optional)
    expand = "employments,groups,home_location,work_location,manager,team,company,pay_group" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)
    first_name = "first_name_example" # str, none_type | If provided, will only return employees with this first name. (optional)
    groups = "groups_example" # str | If provided, will only return employees matching the group ids; multiple groups can be separated by commas. (optional)
    include_deleted_data = True # bool | Whether to include data that was marked as deleted by third party webhooks. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)
    include_sensitive_fields = True # bool | Whether to include sensitive fields (such as social security numbers) in the response. (optional)
    last_name = "last_name_example" # str, none_type | If provided, will only return employees with this last name. (optional)
    manager_id = "manager_id_example" # str | If provided, will only return employees for this manager. (optional)
    modified_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, only objects synced by Merge after this date time will be returned. (optional)
    modified_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, only objects synced by Merge before this date time will be returned. (optional)
    page_size = 1 # int | Number of results to return per page. (optional)
    pay_group_id = "pay_group_id_example" # str | If provided, will only return employees for this pay group (optional)
    personal_email = "personal_email_example" # str, none_type | If provided, will only return Employees with this personal email (optional)
    remote_fields = "employment_status,ethnicity,gender,marital_status" # str | Deprecated. Use show_enum_origins. (optional)
    remote_id = "remote_id_example" # str, none_type | The API provider's ID for the given object. (optional)
    show_enum_origins = "employment_status,ethnicity,gender,marital_status" # str | Which fields should be returned in non-normalized form. (optional)
    started_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type | If provided, will only return employees that started after this datetime. (optional)
    started_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type | If provided, will only return employees that started before this datetime. (optional)
    team_id = "team_id_example" # str | If provided, will only return employees for this team. (optional)
    terminated_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type | If provided, will only return employees that were terminated after this datetime. (optional)
    terminated_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime, none_type | If provided, will only return employees that were terminated before this datetime. (optional)
    work_email = "work_email_example" # str, none_type | If provided, will only return Employees with this work email (optional)
    work_location_id = "work_location_id_example" # str | If provided, will only return employees for this location. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.employees_list(company_id=company_id, created_after=created_after, created_before=created_before, cursor=cursor, display_full_name=display_full_name, employment_status=employment_status, expand=expand, first_name=first_name, groups=groups, include_deleted_data=include_deleted_data, include_remote_data=include_remote_data, include_sensitive_fields=include_sensitive_fields, last_name=last_name, manager_id=manager_id, modified_after=modified_after, modified_before=modified_before, page_size=page_size, pay_group_id=pay_group_id, personal_email=personal_email, remote_fields=remote_fields, remote_id=remote_id, show_enum_origins=show_enum_origins, started_after=started_after, started_before=started_before, team_id=team_id, terminated_after=terminated_after, terminated_before=terminated_before, work_email=work_email, work_location_id=work_location_id)
        pprint(api_response)
    except MergePythonSDK.hris.ApiException as e:
        print("Exception when calling EmployeesApi->employees_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| If provided, will only return employees for this company. | [optional]
 **created_after** | **datetime**| If provided, will only return objects created after this datetime. | [optional]
 **created_before** | **datetime**| If provided, will only return objects created before this datetime. | [optional]
 **cursor** | **str**| The pagination cursor value. | [optional]
 **display_full_name** | **str, none_type**| If provided, will only return employees with this display name. | [optional]
 **employment_status** | **str, none_type**| If provided, will only return employees with this employment status.  * &#x60;ACTIVE&#x60; - ACTIVE * &#x60;PENDING&#x60; - PENDING * &#x60;INACTIVE&#x60; - INACTIVE | [optional]
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional]
 **first_name** | **str, none_type**| If provided, will only return employees with this first name. | [optional]
 **groups** | **str**| If provided, will only return employees matching the group ids; multiple groups can be separated by commas. | [optional]
 **include_deleted_data** | **bool**| Whether to include data that was marked as deleted by third party webhooks. | [optional]
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]
 **include_sensitive_fields** | **bool**| Whether to include sensitive fields (such as social security numbers) in the response. | [optional]
 **last_name** | **str, none_type**| If provided, will only return employees with this last name. | [optional]
 **manager_id** | **str**| If provided, will only return employees for this manager. | [optional]
 **modified_after** | **datetime**| If provided, only objects synced by Merge after this date time will be returned. | [optional]
 **modified_before** | **datetime**| If provided, only objects synced by Merge before this date time will be returned. | [optional]
 **page_size** | **int**| Number of results to return per page. | [optional]
 **pay_group_id** | **str**| If provided, will only return employees for this pay group | [optional]
 **personal_email** | **str, none_type**| If provided, will only return Employees with this personal email | [optional]
 **remote_fields** | **str**| Deprecated. Use show_enum_origins. | [optional]
 **remote_id** | **str, none_type**| The API provider&#39;s ID for the given object. | [optional]
 **show_enum_origins** | **str**| Which fields should be returned in non-normalized form. | [optional]
 **started_after** | **datetime, none_type**| If provided, will only return employees that started after this datetime. | [optional]
 **started_before** | **datetime, none_type**| If provided, will only return employees that started before this datetime. | [optional]
 **team_id** | **str**| If provided, will only return employees for this team. | [optional]
 **terminated_after** | **datetime, none_type**| If provided, will only return employees that were terminated after this datetime. | [optional]
 **terminated_before** | **datetime, none_type**| If provided, will only return employees that were terminated before this datetime. | [optional]
 **work_email** | **str, none_type**| If provided, will only return Employees with this work email | [optional]
 **work_location_id** | **str**| If provided, will only return employees for this location. | [optional]

### Return type

[**PaginatedEmployeeList**](PaginatedEmployeeList.md)

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

# **employees_meta_post_retrieve**
> MetaResponse employees_meta_post_retrieve()



Returns metadata for `Employee` POSTs.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.hris
from MergePythonSDK.hris.api import employees_api
from MergePythonSDK.hris.model.meta_response import MetaResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.merge.dev/api/hris/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = MergePythonSDK.hris.Configuration(
    host = "https://api.merge.dev/api/hris/v1"
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
configuration = MergePythonSDK.hris.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with MergePythonSDK.hris.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = employees_api.EmployeesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.employees_meta_post_retrieve()
        pprint(api_response)
    except MergePythonSDK.hris.ApiException as e:
        print("Exception when calling EmployeesApi->employees_meta_post_retrieve: %s\n" % e)
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

# **employees_retrieve**
> Employee employees_retrieve(id)



Returns an `Employee` object with the given `id`.

### Example

* Api Key Authentication (accountTokenAuth):
* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.hris
from MergePythonSDK.hris.api import employees_api
from MergePythonSDK.hris.model.employee import Employee
from pprint import pprint
# Defining the host is optional and defaults to https://api.merge.dev/api/hris/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = MergePythonSDK.hris.Configuration(
    host = "https://api.merge.dev/api/hris/v1"
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
configuration = MergePythonSDK.hris.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with MergePythonSDK.hris.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = employees_api.EmployeesApi(api_client)
    id = "id_example" # str | 
    expand = "employments,groups,home_location,work_location,manager,team,company,pay_group" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)
    include_sensitive_fields = True # bool | Whether to include sensitive fields (such as social security numbers) in the response. (optional)
    remote_fields = "employment_status,ethnicity,gender,marital_status" # str | Deprecated. Use show_enum_origins. (optional)
    show_enum_origins = "employment_status,ethnicity,gender,marital_status" # str | Which fields should be returned in non-normalized form. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.employees_retrieve(id)
        pprint(api_response)
    except MergePythonSDK.hris.ApiException as e:
        print("Exception when calling EmployeesApi->employees_retrieve: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.employees_retrieve(id, expand=expand, include_remote_data=include_remote_data, include_sensitive_fields=include_sensitive_fields, remote_fields=remote_fields, show_enum_origins=show_enum_origins)
        pprint(api_response)
    except MergePythonSDK.hris.ApiException as e:
        print("Exception when calling EmployeesApi->employees_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **expand** | **str**| Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional]
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]
 **include_sensitive_fields** | **bool**| Whether to include sensitive fields (such as social security numbers) in the response. | [optional]
 **remote_fields** | **str**| Deprecated. Use show_enum_origins. | [optional]
 **show_enum_origins** | **str**| Which fields should be returned in non-normalized form. | [optional]

### Return type

[**Employee**](Employee.md)

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

