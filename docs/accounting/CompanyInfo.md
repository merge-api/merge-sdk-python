# CompanyInfo

# The CompanyInfo Object ### Description The `CompanyInfo` object is used to represent a company's information.  ### Usage Example Fetch from the `GET CompanyInfo` endpoint and view a company's information.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**name** | **str, none_type** | The company&#39;s name. | [optional] 
**legal_name** | **str, none_type** | The company&#39;s legal name. | [optional] 
**tax_number** | **str, none_type** | The company&#39;s tax number. | [optional] 
**fiscal_year_end_month** | **int, none_type** | The company&#39;s fiscal year end month. | [optional] 
**fiscal_year_end_day** | **int, none_type** | The company&#39;s fiscal year end day. | [optional] 
**currency** | **bool, dict, float, int, list, str, none_type** | The currency set in the company&#39;s accounting platform. | [optional] 
**remote_created_at** | **datetime, none_type** | When the third party&#39;s company was created. | [optional] 
**urls** | **[str, none_type], none_type** | The company&#39;s urls. | [optional] 
**addresses** | [**[Address]**](Address.md) |  | [optional] 
**phone_numbers** | [**[AccountingPhoneNumber]**](AccountingPhoneNumber.md) |  | [optional] 
**remote_was_deleted** | **bool** | Indicates whether or not this object has been deleted by third party webhooks. | [optional] [readonly] 
**any string name** | **bool, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


