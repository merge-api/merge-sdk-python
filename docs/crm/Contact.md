# Contact

# The Contact Object ### Description The `Contact` object is used to represent an existing point of contact at a company in a CRM system. ### Usage Example TODO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str, none_type** | The contact&#39;s first name. | [optional] 
**last_name** | **str, none_type** | The contact&#39;s last name. | [optional] 
**account** | **str, none_type** | The contact&#39;s account. | [optional] 
**addresses** | [**[Address]**](Address.md) |  | [optional] 
**email_addresses** | [**[EmailAddress]**](EmailAddress.md) |  | [optional] 
**phone_numbers** | [**[PhoneNumber]**](PhoneNumber.md) |  | [optional] 
**last_activity_at** | **datetime, none_type** | When the contact&#39;s last activity occurred. | [optional] 
**remote_created_at** | **datetime, none_type** | When the third party&#39;s contact was created. | [optional] 
**remote_was_deleted** | **bool** |  | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**field_mappings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] [readonly] 
**modified_at** | **datetime** | This is the datetime that this object was last updated by Merge | [optional] [readonly] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**remote_fields** | [**[RemoteField]**](RemoteField.md) |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


