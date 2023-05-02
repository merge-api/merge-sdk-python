# MergePythonSDK.hris.TeamsApi

All URIs are relative to *https://api.merge.dev/api/hris/v1*

| Method                                           | HTTP request        | Description |
| ------------------------------------------------ | ------------------- | ----------- |
| [**teams_list**](TeamsApi.md#teams_list)         | **GET** /teams      |
| [**teams_retrieve**](TeamsApi.md#teams_retrieve) | **GET** /teams/{id} |

# **teams_list**

> PaginatedTeamList teams_list()

Returns a list of `Team` objects.

### Example

- Api Key Authentication (accountTokenAuth):
- Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.hris
from MergePythonSDK.hris.api import teams_api
from MergePythonSDK.hris.model.paginated_team_list import PaginatedTeamList
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
    api_instance = teams_api.TeamsApi(api_client)
    created_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created after this datetime. (optional)
    created_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, will only return objects created before this datetime. (optional)
    cursor = "cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw" # str | The pagination cursor value. (optional)
    expand = "parent_team" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional) if omitted the server will use the default value of "parent_team"
    include_deleted_data = True # bool | Whether to include data that was marked as deleted by third party webhooks. (optional)
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)
    modified_after = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, only objects synced by Merge after this date time will be returned. (optional)
    modified_before = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | If provided, only objects synced by Merge before this date time will be returned. (optional)
    page_size = 1 # int | Number of results to return per page. (optional)
    parent_team_id = "parent_team_id_example" # str | If provided, will only return teams with this parent team. (optional)
    remote_id = "remote_id_example" # str, none_type | The API provider's ID for the given object. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.teams_list(created_after=created_after, created_before=created_before, cursor=cursor, expand=expand, include_deleted_data=include_deleted_data, include_remote_data=include_remote_data, modified_after=modified_after, modified_before=modified_before, page_size=page_size, parent_team_id=parent_team_id, remote_id=remote_id)
        pprint(api_response)
    except MergePythonSDK.hris.ApiException as e:
        print("Exception when calling TeamsApi->teams_list: %s\n" % e)
```

### Parameters

| Name                     | Type               | Description                                                                                                            | Notes                                                                        |
| ------------------------ | ------------------ | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **created_after**        | **datetime**       | If provided, will only return objects created after this datetime.                                                     | [optional]                                                                   |
| **created_before**       | **datetime**       | If provided, will only return objects created before this datetime.                                                    | [optional]                                                                   |
| **cursor**               | **str**            | The pagination cursor value.                                                                                           | [optional]                                                                   |
| **expand**               | **str**            | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional] if omitted the server will use the default value of "parent_team" |
| **include_deleted_data** | **bool**           | Whether to include data that was marked as deleted by third party webhooks.                                            | [optional]                                                                   |
| **include_remote_data**  | **bool**           | Whether to include the original data Merge fetched from the third-party to produce these models.                       | [optional]                                                                   |
| **modified_after**       | **datetime**       | If provided, only objects synced by Merge after this date time will be returned.                                       | [optional]                                                                   |
| **modified_before**      | **datetime**       | If provided, only objects synced by Merge before this date time will be returned.                                      | [optional]                                                                   |
| **page_size**            | **int**            | Number of results to return per page.                                                                                  | [optional]                                                                   |
| **parent_team_id**       | **str**            | If provided, will only return teams with this parent team.                                                             | [optional]                                                                   |
| **remote_id**            | **str, none_type** | The API provider&#39;s ID for the given object.                                                                        | [optional]                                                                   |

### Return type

[**PaginatedTeamList**](PaginatedTeamList.md)

### Authorization

[accountTokenAuth](../README.md#accountTokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
| ----------- | ----------- | ---------------- |
| **200**     |             | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **teams_retrieve**

> Team teams_retrieve(id)

Returns a `Team` object with the given `id`.

### Example

- Api Key Authentication (accountTokenAuth):
- Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.hris
from MergePythonSDK.hris.api import teams_api
from MergePythonSDK.hris.model.team import Team
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
    api_instance = teams_api.TeamsApi(api_client)
    id = "id_example" # str |
    expand = "parent_team" # str | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. (optional) if omitted the server will use the default value of "parent_team"
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.teams_retrieve(id)
        pprint(api_response)
    except MergePythonSDK.hris.ApiException as e:
        print("Exception when calling TeamsApi->teams_retrieve: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.teams_retrieve(id, expand=expand, include_remote_data=include_remote_data)
        pprint(api_response)
    except MergePythonSDK.hris.ApiException as e:
        print("Exception when calling TeamsApi->teams_retrieve: %s\n" % e)
```

### Parameters

| Name                    | Type     | Description                                                                                                            | Notes                                                                        |
| ----------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **id**                  | **str**  |                                                                                                                        |
| **expand**              | **str**  | Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces. | [optional] if omitted the server will use the default value of "parent_team" |
| **include_remote_data** | **bool** | Whether to include the original data Merge fetched from the third-party to produce these models.                       | [optional]                                                                   |

### Return type

[**Team**](Team.md)

### Authorization

[accountTokenAuth](../README.md#accountTokenAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
| ----------- | ----------- | ---------------- |
| **200**     |             | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
