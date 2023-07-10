# User

# The User Object ### Description The `User` object is used to represent a user with a login to the CRM system. ### Usage Example TODO

## Properties

| Name                   | Type                                                                 | Description                                                                    | Notes                 |
| ---------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------ | --------------------- |
| **name**               | **str, none_type**                                                   | The user&#39;s name.                                                           | [optional]            |
| **email**              | **str, none_type**                                                   | The user&#39;s email address.                                                  | [optional]            |
| **is_active**          | **bool, none_type**                                                  | Whether or not the user is active.                                             | [optional]            |
| **remote_was_deleted** | **bool**                                                             | Indicates whether or not this object has been deleted by third party webhooks. | [optional] [readonly] |
| **id**                 | **str**                                                              |                                                                                | [optional] [readonly] |
| **remote_id**          | **str, none_type**                                                   | The third-party API ID of the matching object.                                 | [optional]            |
| **modified_at**        | **datetime**                                                         | This is the datetime that this object was last updated by Merge                | [optional] [readonly] |
| **field_mappings**     | **{str: (bool, dict, float, int, list, str, none_type)}, none_type** |                                                                                | [optional] [readonly] |
| **remote_data**        | [**[RemoteData], none_type**](RemoteData.md)                         |                                                                                | [optional] [readonly] |
| **remote_fields**      | [**[RemoteField]**](RemoteField.md)                                  |                                                                                | [optional] [readonly] |
| **any string name**    | **bool, dict, float, int, list, str, none_type**                     | any string name can be used but the value must be the correct type             | [optional]            |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
