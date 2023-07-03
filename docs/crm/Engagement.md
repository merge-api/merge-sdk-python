# Engagement

# The Engagement Object ### Description The `Engagement` object is used to represent an interaction noted in a CRM system. ### Usage Example TODO

## Properties

| Name                   | Type                                                                 | Description                                                                                       | Notes                 |
| ---------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | --------------------- |
| **owner**              | **str, none_type**                                                   | The engagement&#39;s owner.                                                                       | [optional]            |
| **content**            | **str, none_type**                                                   | The engagement&#39;s content.                                                                     | [optional]            |
| **subject**            | **str, none_type**                                                   | The engagement&#39;s subject.                                                                     | [optional]            |
| **direction**          | **bool, dict, float, int, list, str, none_type**                     | The engagement&#39;s direction. _ &#x60;INBOUND&#x60; - INBOUND _ &#x60;OUTBOUND&#x60; - OUTBOUND | [optional]            |
| **engagement_type**    | **str, none_type**                                                   | The engagement type of the engagement.                                                            | [optional]            |
| **start_time**         | **datetime, none_type**                                              | The time at which the engagement started.                                                         | [optional]            |
| **end_time**           | **datetime, none_type**                                              | The time at which the engagement ended.                                                           | [optional]            |
| **account**            | **str, none_type**                                                   | The account of the engagement.                                                                    | [optional]            |
| **contacts**           | **[str, none_type]**                                                 |                                                                                                   | [optional]            |
| **remote_was_deleted** | **bool**                                                             | Indicates whether or not this object has been deleted by third party webhooks.                    | [optional] [readonly] |
| **id**                 | **str**                                                              |                                                                                                   | [optional] [readonly] |
| **remote_id**          | **str, none_type**                                                   | The third-party API ID of the matching object.                                                    | [optional]            |
| **modified_at**        | **datetime**                                                         | This is the datetime that this object was last updated by Merge                                   | [optional] [readonly] |
| **field_mappings**     | **{str: (bool, dict, float, int, list, str, none_type)}, none_type** |                                                                                                   | [optional] [readonly] |
| **remote_data**        | [**[RemoteData], none_type**](RemoteData.md)                         |                                                                                                   | [optional] [readonly] |
| **remote_fields**      | [**[RemoteField]**](RemoteField.md)                                  |                                                                                                   | [optional] [readonly] |
| **any string name**    | **bool, dict, float, int, list, str, none_type**                     | any string name can be used but the value must be the correct type                                | [optional]            |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
