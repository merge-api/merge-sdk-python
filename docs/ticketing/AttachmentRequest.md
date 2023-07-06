# AttachmentRequest

# The Attachment Object ### Description The `Attachment` object is used to represent an attachment for a ticket. ### Usage Example TODO

## Properties

| Name                      | Type                                                                 | Description                                                                                           | Notes      |
| ------------------------- | -------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ---------- |
| **file_name**             | **str, none_type**                                                   | The attachment&#39;s name. It is required to include the file extension in the attachment&#39;s name. | [optional] |
| **ticket**                | **str, none_type**                                                   | The ticket associated with the attachment.                                                            | [optional] |
| **file_url**              | **str, none_type**                                                   | The attachment&#39;s url. It is required to include the file extension in the file&#39;s URL.         | [optional] |
| **content_type**          | **str, none_type**                                                   | The attachment&#39;s file format.                                                                     | [optional] |
| **uploaded_by**           | **str, none_type**                                                   | The user who uploaded the attachment.                                                                 | [optional] |
| **integration_params**    | **{str: (bool, dict, float, int, list, str, none_type)}, none_type** |                                                                                                       | [optional] |
| **linked_account_params** | **{str: (bool, dict, float, int, list, str, none_type)}, none_type** |                                                                                                       | [optional] |
| **any string name**       | **bool, dict, float, int, list, str, none_type**                     | any string name can be used but the value must be the correct type                                    | [optional] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
