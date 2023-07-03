# AssociationType

# The AssociationType Object ### Description The `Association Type` object represents the relationship between two objects. ### Usage Example TODO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_object_class** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] [readonly] 
**target_object_classes** | [**[AssociationSubType]**](AssociationSubType.md) |  | [optional] [readonly] 
**remote_key_name** | **str, none_type** |  | [optional] 
**display_name** | **str, none_type** |  | [optional] 
**cardinality** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**is_required** | **bool** |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**modified_at** | **datetime** | This is the datetime that this object was last updated by Merge | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


