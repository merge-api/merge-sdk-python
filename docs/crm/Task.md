# Task

# The Task Object ### Description The `Task` object is used to represent a task in the remote system. ### Usage Example TODO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**subject** | **str, none_type** | The task&#39;s subject. | [optional] 
**content** | **str, none_type** | The task&#39;s content. | [optional] 
**owner** | **str, none_type** |  | [optional] 
**account** | **str, none_type** |  | [optional] 
**completed_date** | **datetime, none_type** | When the task is completed. | [optional] 
**due_date** | **datetime, none_type** | When the task is due. | [optional] 
**status** | **bool, date, datetime, dict, float, int, list, str, none_type** | The task&#39;s status. | [optional] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**remote_was_deleted** | **bool** | Indicates whether or not this object has been deleted by third party webhooks. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


