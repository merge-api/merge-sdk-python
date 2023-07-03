# ConditionSchema


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the condition schema. This ID is used when updating selective syncs for a linked account. | 
**native_name** | **str, none_type** | User-facing *native condition* name. e.g. \&quot;Skip Manager\&quot;. | 
**field_name** | **str, none_type** | The name of the field on the common model that this condition corresponds to, if they conceptually match. e.g. \&quot;location_type\&quot;. | 
**condition_type** | **bool, date, datetime, dict, float, int, list, str, none_type** | The type of value(s) that can be set for this condition.  * &#x60;BOOLEAN&#x60; - BOOLEAN * &#x60;DATE&#x60; - DATE * &#x60;DATE_TIME&#x60; - DATE_TIME * &#x60;INTEGER&#x60; - INTEGER * &#x60;FLOAT&#x60; - FLOAT * &#x60;STRING&#x60; - STRING * &#x60;LIST_OF_STRINGS&#x60; - LIST_OF_STRINGS | 
**operators** | [**[OperatorSchema]**](OperatorSchema.md) | The schemas for the operators that can be used on a condition. | 
**common_model** | **str** | The common model for which a condition schema is defined. | [optional] [readonly] 
**is_unique** | **bool** | Whether this condition can only be applied once. If false, the condition can be AND&#39;d together multiple times. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


