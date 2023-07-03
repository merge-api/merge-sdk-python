# Lead

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
**addresses** | [**[Address]**](Address.md) |  | [optional] [readonly] 
**email_addresses** | [**[EmailAddress]**](EmailAddress.md) |  | [optional] [readonly] 
**phone_numbers** | [**[PhoneNumber]**](PhoneNumber.md) |  | [optional] [readonly] 
**remote_updated_at** | **datetime, none_type** | When the third party&#39;s lead was updated. | [optional] 
**remote_created_at** | **datetime, none_type** | When the third party&#39;s lead was created. | [optional] 
**converted_date** | **datetime, none_type** | When the lead was converted. | [optional] 
**converted_contact** | **str, none_type** | The contact of the converted lead. | [optional] 
**converted_account** | **str, none_type** | The account of the converted lead. | [optional] 
**remote_was_deleted** | **bool** |  | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**modified_at** | **datetime** | This is the datetime that this object was last updated by Merge | [optional] [readonly] 
**field_mappings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] [readonly] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**remote_fields** | [**[RemoteField]**](RemoteField.md) |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


