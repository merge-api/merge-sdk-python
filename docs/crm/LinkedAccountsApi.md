# MergePythonSDK.crm.LinkedAccountsApi

All URIs are relative to *https://api.merge.dev/api/crm/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**linked_accounts_list**](LinkedAccountsApi.md#linked_accounts_list) | **GET** /linked-accounts | 


# **linked_accounts_list**
> PaginatedAccountDetailsAndActionsList linked_accounts_list()



List linked accounts for your organization.

### Example

* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.crm
from MergePythonSDK.crm.api import linked_accounts_api
from MergePythonSDK.crm.model.paginated_account_details_and_actions_list import PaginatedAccountDetailsAndActionsList
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

# Configure Bearer authorization: bearerAuth
configuration = MergePythonSDK.crm.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with MergePythonSDK.crm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = linked_accounts_api.LinkedAccountsApi(api_client)
    category = "accounting" # str, none_type | Options: ('hris', 'ats', 'accounting', 'ticketing', 'crm', 'mktg', 'filestorage')  * `hris` - hris * `ats` - ats * `accounting` - accounting * `ticketing` - ticketing * `crm` - crm * `mktg` - mktg * `filestorage` - filestorage (optional)
    cursor = "cD0yMDIxLTAxLTA2KzAzJTNBMjQlM0E1My40MzQzMjYlMkIwMCUzQTAw" # str | The pagination cursor value. (optional)
    end_user_email_address = "end_user_email_address_example" # str | If provided, will only return linked accounts associated with the given email address. (optional)
    end_user_organization_name = "end_user_organization_name_example" # str | If provided, will only return linked accounts associated with the given organization name. (optional)
    end_user_origin_id = "end_user_origin_id_example" # str | If provided, will only return linked accounts associated with the given origin ID. (optional)
    end_user_origin_ids = "end_user_origin_ids_example" # str | Comma-separated list of EndUser origin IDs, making it possible to specify multiple EndUsers at once. (optional)
    id = "id_example" # str |  (optional)
    ids = "ids_example" # str | Comma-separated list of LinkedAccount IDs, making it possible to specify multiple LinkedAccounts at once. (optional)
    include_duplicates = True # bool | If `true`, will include complete production duplicates of the account specified by the `id` query parameter in the response. `id` must be for a complete production linked account. (optional)
    integration_name = "integration_name_example" # str | If provided, will only return linked accounts associated with the given integration name. (optional)
    is_test_account = "is_test_account_example" # str | If included, will only include test linked accounts. If not included, will only include non-test linked accounts. (optional)
    page_size = 1 # int | Number of results to return per page. (optional)
    status = "status_example" # str | Filter by status. Options: `COMPLETE`, `INCOMPLETE`, `RELINK_NEEDED` (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.linked_accounts_list(category=category, cursor=cursor, end_user_email_address=end_user_email_address, end_user_organization_name=end_user_organization_name, end_user_origin_id=end_user_origin_id, end_user_origin_ids=end_user_origin_ids, id=id, ids=ids, include_duplicates=include_duplicates, integration_name=integration_name, is_test_account=is_test_account, page_size=page_size, status=status)
        pprint(api_response)
    except MergePythonSDK.crm.ApiException as e:
        print("Exception when calling LinkedAccountsApi->linked_accounts_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str, none_type**| Options: (&#39;hris&#39;, &#39;ats&#39;, &#39;accounting&#39;, &#39;ticketing&#39;, &#39;crm&#39;, &#39;mktg&#39;, &#39;filestorage&#39;)  * &#x60;hris&#x60; - hris * &#x60;ats&#x60; - ats * &#x60;accounting&#x60; - accounting * &#x60;ticketing&#x60; - ticketing * &#x60;crm&#x60; - crm * &#x60;mktg&#x60; - mktg * &#x60;filestorage&#x60; - filestorage | [optional]
 **cursor** | **str**| The pagination cursor value. | [optional]
 **end_user_email_address** | **str**| If provided, will only return linked accounts associated with the given email address. | [optional]
 **end_user_organization_name** | **str**| If provided, will only return linked accounts associated with the given organization name. | [optional]
 **end_user_origin_id** | **str**| If provided, will only return linked accounts associated with the given origin ID. | [optional]
 **end_user_origin_ids** | **str**| Comma-separated list of EndUser origin IDs, making it possible to specify multiple EndUsers at once. | [optional]
 **id** | **str**|  | [optional]
 **ids** | **str**| Comma-separated list of LinkedAccount IDs, making it possible to specify multiple LinkedAccounts at once. | [optional]
 **include_duplicates** | **bool**| If &#x60;true&#x60;, will include complete production duplicates of the account specified by the &#x60;id&#x60; query parameter in the response. &#x60;id&#x60; must be for a complete production linked account. | [optional]
 **integration_name** | **str**| If provided, will only return linked accounts associated with the given integration name. | [optional]
 **is_test_account** | **str**| If included, will only include test linked accounts. If not included, will only include non-test linked accounts. | [optional]
 **page_size** | **int**| Number of results to return per page. | [optional]
 **status** | **str**| Filter by status. Options: &#x60;COMPLETE&#x60;, &#x60;INCOMPLETE&#x60;, &#x60;RELINK_NEEDED&#x60; | [optional]

### Return type

[**PaginatedAccountDetailsAndActionsList**](PaginatedAccountDetailsAndActionsList.md)

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

