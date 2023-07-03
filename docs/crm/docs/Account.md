# Account

# The Account Object ### Description The `Account` object is used to represent a company in a CRM system. ### Usage Example TODO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner** | **str, none_type** | The account&#39;s owner. | [optional] 
**name** | **str, none_type** | The account&#39;s name. | [optional] 
**description** | **str, none_type** | The account&#39;s description. | [optional] 
**industry** | **str, none_type** | The account&#39;s industry. | [optional] 
**website** | **str, none_type** | The account&#39;s website. | [optional] 
**number_of_employees** | **int, none_type** | The account&#39;s number of employees. | [optional] 
**addresses** | [**[Address]**](Address.md) |  | [optional] [readonly] 
**phone_numbers** | [**[PhoneNumber]**](PhoneNumber.md) |  | [optional] [readonly] 
**last_activity_at** | **datetime, none_type** | The last date (either most recent or furthest in the future) of when an activity occurs in an account. | [optional] 
**remote_updated_at** | **datetime, none_type** | When the CRM system account data was last modified by a user with a login. | [optional] 
**remote_created_at** | **datetime, none_type** | When the third party&#39;s account was created. | [optional] 
**remote_was_deleted** | **bool** |  | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**field_mappings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] [readonly] 
**modified_at** | **datetime** | This is the datetime that this object was last updated by Merge | [optional] [readonly] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**remote_fields** | [**[RemoteField]**](RemoteField.md) |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


