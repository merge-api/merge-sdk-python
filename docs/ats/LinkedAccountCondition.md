# LinkedAccountCondition

## Properties

| Name                    | Type                                             | Description                                                                                                                                 | Notes                 |
| ----------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| **condition_schema_id** | **str**                                          | The ID indicating which condition schema to use for a specific condition.                                                                   |
| **native_name**         | **str, none_type**                               | User-facing _native condition_ name. e.g. \&quot;Skip Manager\&quot;.                                                                       |
| **operator**            | **str**                                          | The operator for a specific condition.                                                                                                      |
| **field_name**          | **str, none_type**                               | The name of the field on the common model that this condition corresponds to, if they conceptually match. e.g. \&quot;location_type\&quot;. |
| **common_model**        | **str**                                          | The common model for a specific condition.                                                                                                  | [optional] [readonly] |
| **value**               | **bool, dict, float, int, list, str, none_type** | The value for a condition.                                                                                                                  | [optional] [readonly] |
| **any string name**     | **bool, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type                                                                          | [optional]            |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
