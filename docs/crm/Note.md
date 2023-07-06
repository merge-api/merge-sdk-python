# Note

# The Note Object ### Description The `Note` object is used to represent a note on another object. ### Usage Example TODO

## Properties

| Name                   | Type                                                                 | Description                                                        | Notes                 |
| ---------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------ | --------------------- |
| **owner**              | **str, none_type**                                                   | The note&#39;s owner.                                              | [optional]            |
| **content**            | **str, none_type**                                                   | The note&#39;s content.                                            | [optional]            |
| **contact**            | **str, none_type**                                                   | The note&#39;s contact.                                            | [optional]            |
| **account**            | **str, none_type**                                                   | The note&#39;s account.                                            | [optional]            |
| **opportunity**        | **str, none_type**                                                   | The note&#39;s opportunity.                                        | [optional]            |
| **remote_updated_at**  | **datetime, none_type**                                              | When the third party&#39;s lead was updated.                       | [optional]            |
| **remote_created_at**  | **datetime, none_type**                                              | When the third party&#39;s lead was created.                       | [optional]            |
| **remote_was_deleted** | **bool**                                                             |                                                                    | [optional] [readonly] |
| **id**                 | **str**                                                              |                                                                    | [optional] [readonly] |
| **remote_id**          | **str, none_type**                                                   | The third-party API ID of the matching object.                     | [optional]            |
| **modified_at**        | **datetime**                                                         | This is the datetime that this object was last updated by Merge    | [optional] [readonly] |
| **field_mappings**     | **{str: (bool, dict, float, int, list, str, none_type)}, none_type** |                                                                    | [optional] [readonly] |
| **remote_data**        | [**[RemoteData], none_type**](RemoteData.md)                         |                                                                    | [optional] [readonly] |
| **remote_fields**      | [**[RemoteField]**](RemoteField.md)                                  |                                                                    | [optional] [readonly] |
| **any string name**    | **bool, dict, float, int, list, str, none_type**                     | any string name can be used but the value must be the correct type | [optional]            |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
