# EngagementType

# The Engagement Type Object ### Description The `Engagement Type` object is used to represent an interaction activity. A given `Engagement` typically has an `Engagement Type` object represented in the engagement_type field. ### Usage Example TODO

## Properties

| Name                | Type                                             | Description                                                                                                                     | Notes                 |
| ------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| **activity_type**   | **bool, dict, float, int, list, str, none_type** | The engagement type&#39;s activity type. _ &#x60;CALL&#x60; - CALL _ &#x60;MEETING&#x60; - MEETING \* &#x60;EMAIL&#x60; - EMAIL | [optional]            |
| **name**            | **str, none_type**                               | The engagement type&#39;s name.                                                                                                 | [optional]            |
| **id**              | **str**                                          |                                                                                                                                 | [optional] [readonly] |
| **remote_id**       | **str, none_type**                               | The third-party API ID of the matching object.                                                                                  | [optional]            |
| **modified_at**     | **datetime**                                     | This is the datetime that this object was last updated by Merge                                                                 | [optional] [readonly] |
| **remote_fields**   | [**[RemoteField]**](RemoteField.md)              |                                                                                                                                 | [optional] [readonly] |
| **any string name** | **bool, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type                                                              | [optional]            |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
