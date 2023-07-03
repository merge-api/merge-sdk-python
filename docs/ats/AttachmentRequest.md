# AttachmentRequest

# The Attachment Object ### Description The `Attachment` object is used to represent a file attached to a candidate. ### Usage Example Fetch from the `LIST Attachments` endpoint and view attachments accessible by a company.

## Properties

| Name                      | Type                                                                 | Description                                                                                                                                                              | Notes      |
| ------------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| **file_name**             | **str, none_type**                                                   | The attachment&#39;s name.                                                                                                                                               | [optional] |
| **file_url**              | **str, none_type**                                                   | The attachment&#39;s url.                                                                                                                                                | [optional] |
| **candidate**             | **str, none_type**                                                   |                                                                                                                                                                          | [optional] |
| **attachment_type**       | **bool, dict, float, int, list, str, none_type**                     | The attachment&#39;s type. _ &#x60;RESUME&#x60; - RESUME _ &#x60;COVER_LETTER&#x60; - COVER_LETTER _ &#x60;OFFER_LETTER&#x60; - OFFER_LETTER _ &#x60;OTHER&#x60; - OTHER | [optional] |
| **integration_params**    | **{str: (bool, dict, float, int, list, str, none_type)}, none_type** |                                                                                                                                                                          | [optional] |
| **linked_account_params** | **{str: (bool, dict, float, int, list, str, none_type)}, none_type** |                                                                                                                                                                          | [optional] |
| **any string name**       | **bool, dict, float, int, list, str, none_type**                     | any string name can be used but the value must be the correct type                                                                                                       | [optional] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
