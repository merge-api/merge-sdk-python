# RemoteUser

# The RemoteUser Object ### Description The `RemoteUser` object is used to represent a user with a login to the ATS system. ### Usage Example Fetch from the `LIST RemoteUsers` endpoint to show all users for a third party.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**first_name** | **str, none_type** | The user&#39;s first name. | [optional] 
**last_name** | **str, none_type** | The user&#39;s last name. | [optional] 
**email** | **str, none_type** | The user&#39;s email. | [optional] 
**disabled** | **bool, none_type** | Whether the user&#39;s account had been disabled. | [optional] 
**remote_created_at** | **datetime, none_type** | When the third party&#39;s user was created. | [optional] 
**access_role** | **bool, date, datetime, dict, float, int, list, str, none_type** | The user&#39;s role.  * &#x60;SUPER_ADMIN&#x60; - SUPER_ADMIN * &#x60;ADMIN&#x60; - ADMIN * &#x60;TEAM_MEMBER&#x60; - TEAM_MEMBER * &#x60;LIMITED_TEAM_MEMBER&#x60; - LIMITED_TEAM_MEMBER * &#x60;INTERVIEWER&#x60; - INTERVIEWER | [optional] 
**remote_was_deleted** | **bool** | Indicates whether or not this object has been deleted by third party webhooks. | [optional] [readonly] 
**field_mappings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] [readonly] 
**modified_at** | **datetime** | This is the datetime that this object was last updated by Merge | [optional] [readonly] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

