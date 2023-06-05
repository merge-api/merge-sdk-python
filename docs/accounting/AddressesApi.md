# MergePythonSDK.accounting.AddressesApi

All URIs are relative to *https://api.merge.dev/api/accounting/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addresses_retrieve**](AddressesApi.md#addresses_retrieve) | **GET** /addresses/{id} | 


# **addresses_retrieve**
> Address addresses_retrieve(x_account_token, id)



Returns an `Address` object with the given `id`.

### Example

* Api Key Authentication (tokenAuth):

```python
import time
import MergePythonSDK.accounting
from MergePythonSDK.accounting.api import addresses_api
from MergePythonSDK.accounting.model.address import Address
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

# Configure API key authorization: tokenAuth
configuration.api_key['tokenAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with MergePythonSDK.accounting.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = addresses_api.AddressesApi(api_client)
    x_account_token = "X-Account-Token_example" # str | Token identifying the end user.
    id = "id_example" # str | 
    include_remote_data = True # bool | Whether to include the original data Merge fetched from the third-party to produce these models. (optional)
    remote_fields = "type" # str | Deprecated. Use show_enum_origins. (optional) if omitted the server will use the default value of "type"
    show_enum_origins = "type" # str | Which fields should be returned in non-normalized form. (optional) if omitted the server will use the default value of "type"

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.addresses_retrieve(x_account_token, id)
        pprint(api_response)
    except MergePythonSDK.accounting.ApiException as e:
        print("Exception when calling AddressesApi->addresses_retrieve: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.addresses_retrieve(x_account_token, id, include_remote_data=include_remote_data, remote_fields=remote_fields, show_enum_origins=show_enum_origins)
        pprint(api_response)
    except MergePythonSDK.accounting.ApiException as e:
        print("Exception when calling AddressesApi->addresses_retrieve: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_account_token** | **str**| Token identifying the end user. |
 **id** | **str**|  |
 **include_remote_data** | **bool**| Whether to include the original data Merge fetched from the third-party to produce these models. | [optional]
 **remote_fields** | **str**| Deprecated. Use show_enum_origins. | [optional] if omitted the server will use the default value of "type"
 **show_enum_origins** | **str**| Which fields should be returned in non-normalized form. | [optional] if omitted the server will use the default value of "type"

### Return type

[**Address**](Address.md)

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

