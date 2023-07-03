# CustomObject

# The CustomObject Object ### Description The `Custom Object` record refers to an instance of a Custom Object Class. ### Usage Example TODO

## Properties

| Name                | Type                                                      | Description                                                        | Notes                 |
| ------------------- | --------------------------------------------------------- | ------------------------------------------------------------------ | --------------------- |
| **object_class**    | **str, none_type**                                        |                                                                    | [optional]            |
| **fields**          | **{str: (bool, dict, float, int, list, str, none_type)}** |                                                                    | [optional] [readonly] |
| **remote_id**       | **str, none_type**                                        | The third-party API ID of the matching object.                     | [optional]            |
| **id**              | **str**                                                   |                                                                    | [optional] [readonly] |
| **modified_at**     | **datetime**                                              | This is the datetime that this object was last updated by Merge    | [optional] [readonly] |
| **remote_fields**   | [**[RemoteField]**](RemoteField.md)                       |                                                                    | [optional] [readonly] |
| **any string name** | **bool, dict, float, int, list, str, none_type**          | any string name can be used but the value must be the correct type | [optional]            |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
