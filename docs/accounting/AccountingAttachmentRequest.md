# AccountingAttachmentRequest

# The Accounting Attachment Object ### Description The `AccountingAttachment` object is used to represent a company's attachments. ### Usage Example Fetch from the `LIST AccountingAttachments` endpoint and view a company's attachments.

## Properties

| Name                      | Type                                                                 | Description                                                        | Notes      |
| ------------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------ | ---------- |
| **file_name**             | **str, none_type**                                                   | The attachment&#39;s name.                                         | [optional] |
| **file_url**              | **str, none_type**                                                   | The attachment&#39;s url.                                          | [optional] |
| **company**               | **str, none_type**                                                   | The company the accounting attachment belongs to.                  | [optional] |
| **integration_params**    | **{str: (bool, dict, float, int, list, str, none_type)}, none_type** |                                                                    | [optional] |
| **linked_account_params** | **{str: (bool, dict, float, int, list, str, none_type)}, none_type** |                                                                    | [optional] |
| **any string name**       | **bool, dict, float, int, list, str, none_type**                     | any string name can be used but the value must be the correct type | [optional] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
