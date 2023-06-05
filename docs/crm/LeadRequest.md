# LeadRequest

# The Lead Object ### Description The `Lead` object is used to represent an individual who is a potential customer. ### Usage Example TODO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner** | **str, none_type** | The lead&#39;s owner. | [optional] 
**lead_source** | **str, none_type** | The lead&#39;s source. | [optional] 
**title** | **str, none_type** | The lead&#39;s title. | [optional] 
**company** | **str, none_type** | The lead&#39;s company. | [optional] 
**first_name** | **str, none_type** | The lead&#39;s first name. | [optional] 
**last_name** | **str, none_type** | The lead&#39;s last name. | [optional] 
**addresses** | [**[AddressRequest]**](AddressRequest.md) |  | [optional] 
**email_addresses** | [**[EmailAddressRequest]**](EmailAddressRequest.md) |  | [optional] 
**phone_numbers** | [**[PhoneNumberRequest]**](PhoneNumberRequest.md) |  | [optional] 
**converted_date** | **datetime, none_type** | When the lead was converted. | [optional] 
**converted_contact** | **str, none_type** | The contact of the converted lead. | [optional] 
**converted_account** | **str, none_type** | The account of the converted lead. | [optional] 
**integration_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 
**linked_account_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 
**remote_fields** | [**[RemoteFieldRequest]**](RemoteFieldRequest.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


