# PatchedEngagementRequest

# The Engagement Object ### Description The `Engagement` object is used to represent an interaction noted in a CRM system. ### Usage Example TODO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner** | **str, none_type** | The engagement&#39;s owner. | [optional] 
**content** | **str, none_type** | The engagement&#39;s content. | [optional] 
**subject** | **str, none_type** | The engagement&#39;s subject. | [optional] 
**direction** | **bool, date, datetime, dict, float, int, list, str, none_type** | The engagement&#39;s direction.  * &#x60;INBOUND&#x60; - INBOUND * &#x60;OUTBOUND&#x60; - OUTBOUND | [optional] 
**engagement_type** | **str, none_type** | The engagement type of the engagement. | [optional] 
**start_time** | **datetime, none_type** | The time at which the engagement started. | [optional] 
**end_time** | **datetime, none_type** | The time at which the engagement ended. | [optional] 
**account** | **str, none_type** | The account of the engagement. | [optional] 
**contacts** | **[str, none_type]** |  | [optional] 
**integration_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 
**linked_account_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 
**remote_fields** | [**[RemoteFieldRequest]**](RemoteFieldRequest.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


