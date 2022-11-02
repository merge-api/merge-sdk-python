# Note

# The Note Object ### Description The `Note` object is used to represent a note in the remote system. ### Usage Example TODO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**owner** | **str, none_type** |  | [optional] 
**content** | **str, none_type** | The note&#39;s content. | [optional] 
**contact** | **str, none_type** |  | [optional] 
**account** | **str, none_type** |  | [optional] 
**opportunity** | **str, none_type** |  | [optional] 
**remote_updated_at** | **datetime, none_type** | When the third party&#39;s lead was updated. | [optional] 
**remote_created_at** | **datetime, none_type** | When the third party&#39;s lead was created. | [optional] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**remote_was_deleted** | **bool** |  | [optional] [readonly] 
**any string name** | **bool, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


