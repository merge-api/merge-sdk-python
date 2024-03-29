# MergePythonSDK.ats.LinkTokenApi

All URIs are relative to *https://api.merge.dev/api/ats/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**link_token_create**](LinkTokenApi.md#link_token_create) | **POST** /link-token | 


# **link_token_create**
> LinkToken link_token_create(end_user_details_request)



Creates a link token to be used when linking a new end user.

### Example

* Bearer Authentication (bearerAuth):

```python
import time
import MergePythonSDK.ats
from MergePythonSDK.ats.api import link_token_api
from MergePythonSDK.ats.model.end_user_details_request import EndUserDetailsRequest
from MergePythonSDK.ats.model.link_token import LinkToken
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

# Configure Bearer authorization: bearerAuth
configuration = MergePythonSDK.ats.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with MergePythonSDK.ats.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = link_token_api.LinkTokenApi(api_client)
    end_user_details_request = EndUserDetailsRequest(
        end_user_email_address="end_user_email_address_example",
        end_user_organization_name="end_user_organization_name_example",
        end_user_origin_id="end_user_origin_id_example",
        categories=[
            CategoriesEnum("hris"),
        ],
        integration="integration_example",
        link_expiry_mins=30,
        should_create_magic_link_url=False,
        common_models=[
            CommonModelScopesBodyRequest(
                model_id="hris.Employee",
                enabled_actions=[
                    EnabledActionsEnum("["READ","WRITE"]"),
                ],
                disabled_fields=["first_name"],
            ),
        ],
    ) # EndUserDetailsRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.link_token_create(end_user_details_request)
        pprint(api_response)
    except MergePythonSDK.ats.ApiException as e:
        print("Exception when calling LinkTokenApi->link_token_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_user_details_request** | [**EndUserDetailsRequest**](EndUserDetailsRequest.md)|  |

### Return type

[**LinkToken**](LinkToken.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

