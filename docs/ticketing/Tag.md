# Tag

# The Tag Object ### Description The `Tag` object is used to represent a tag or label for a ticket. ### Usage Example TODO

## Properties

| Name                   | Type                                                                 | Description                                                                    | Notes                 |
| ---------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------ | --------------------- |
| **remote_id**          | **str, none_type**                                                   | The third-party API ID of the matching object.                                 | [optional]            |
| **name**               | **str, none_type**                                                   | The tag&#39;s name.                                                            | [optional]            |
| **remote_was_deleted** | **bool**                                                             | Indicates whether or not this object has been deleted by third party webhooks. | [optional]            |
| **modified_at**        | **datetime**                                                         | This is the datetime that this object was last updated by Merge                | [optional] [readonly] |
| **field_mappings**     | **{str: (bool, dict, float, int, list, str, none_type)}, none_type** |                                                                                | [optional] [readonly] |
| **remote_data**        | [**[RemoteData], none_type**](RemoteData.md)                         |                                                                                | [optional] [readonly] |
| **any string name**    | **bool, dict, float, int, list, str, none_type**                     | any string name can be used but the value must be the correct type             | [optional]            |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
