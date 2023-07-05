# CustomObjectClass

# The Custom Object Class Object ### Description The `Custom Object Class` object is used to represent a Custom Object Schema in the remote system. ### Usage Example TODO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** |  | [optional] 
**description** | **str, none_type** |  | [optional] 
**labels** | **{str: (str, none_type)}** |  | [optional] [readonly] 
**fields** | [**[RemoteFieldClassForCustomObjectClass]**](RemoteFieldClassForCustomObjectClass.md) |  | [optional] [readonly] 
**association_types** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}], none_type** |  | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**modified_at** | **datetime** |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


