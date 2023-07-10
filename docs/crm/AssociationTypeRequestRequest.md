# AssociationTypeRequestRequest

## Properties

| Name                      | Type                                                                    | Description                                                        | Notes                                                                |
| ------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------ | -------------------------------------------------------------------- |
| **source_object_class**   | [**ObjectClassDescriptionRequest**](ObjectClassDescriptionRequest.md)   |                                                                    |
| **target_object_classes** | [**[ObjectClassDescriptionRequest]**](ObjectClassDescriptionRequest.md) |                                                                    |
| **remote_key_name**       | **str**                                                                 |                                                                    |
| **display_name**          | **str**                                                                 |                                                                    | [optional]                                                           |
| **cardinality**           | [**CardinalityEnum**](CardinalityEnum.md)                               |                                                                    | [optional]                                                           |
| **is_required**           | **bool**                                                                |                                                                    | [optional] if omitted the server will use the default value of False |
| **any string name**       | **bool, dict, float, int, list, str, none_type**                        | any string name can be used but the value must be the correct type | [optional]                                                           |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
