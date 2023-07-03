# Role

# The Role Object ### Description The `Role` object is used to represent the set of actions & access that a user with this role is allowed to perform.  ### Usage Example TODO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**name** | **str, none_type** | The name of the Role. | [optional] 
**ticket_actions** | **[bool, date, datetime, dict, float, int, list, str, none_type], none_type** | The set of actions that a User with this Role can perform. Possible enum values include: &#x60;VIEW&#x60;, &#x60;CREATE&#x60;, &#x60;EDIT&#x60;, &#x60;DELETE&#x60;, &#x60;CLOSE&#x60;, and &#x60;ASSIGN&#x60;. | [optional] 
**ticket_access** | **bool, date, datetime, dict, float, int, list, str, none_type** | The level of Ticket access that a User with this Role can perform.  * &#x60;ALL&#x60; - ALL * &#x60;ASSIGNED_ONLY&#x60; - ASSIGNED_ONLY * &#x60;TEAM_ONLY&#x60; - TEAM_ONLY | [optional] 
**remote_was_deleted** | **bool** | Indicates whether or not this object has been deleted by third party webhooks. | [optional] 
**modified_at** | **datetime** | This is the datetime that this object was last updated by Merge | [optional] [readonly] 
**field_mappings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] [readonly] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


