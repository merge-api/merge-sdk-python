# Engagement

# The Engagement Object ### Description The `Engagement` object is used to represent an engagement in the remote system. ### Usage Example TODO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**owner** | **str, none_type** |  | [optional] 
**content** | **str, none_type** | The engagement&#39;s content. | [optional] 
**subject** | **str, none_type** | The engagement&#39;s subject. | [optional] 
**direction** | **bool, dict, float, int, list, str, none_type** | The engagement&#39;s direction. | [optional] 
**engagement_type** | **str, none_type** |  | [optional] 
**start_time** | **datetime, none_type** | The time at which the engagement started. | [optional] 
**end_time** | **datetime, none_type** | The time at which the engagement ended. | [optional] 
**account** | **str, none_type** |  | [optional] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**remote_was_deleted** | **bool** | Indicates whether or not this object has been deleted by third party webhooks. | [optional] [readonly] 
**any string name** | **bool, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


