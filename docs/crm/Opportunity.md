# Opportunity

# The Opportunity Object ### Description The `Opportunity` object is used to represent a deal opportunity in a CRM system. ### Usage Example TODO

## Properties

| Name                   | Type                                                                 | Description                                                                                                | Notes                 |
| ---------------------- | -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | --------------------- |
| **name**               | **str, none_type**                                                   | The opportunity&#39;s name.                                                                                | [optional]            |
| **description**        | **str, none_type**                                                   | The opportunity&#39;s description.                                                                         | [optional]            |
| **amount**             | **int, none_type**                                                   | The opportunity&#39;s amount.                                                                              | [optional]            |
| **owner**              | **str, none_type**                                                   | The opportunity&#39;s owner.                                                                               | [optional]            |
| **account**            | **str, none_type**                                                   | The account of the opportunity.                                                                            | [optional]            |
| **stage**              | **str, none_type**                                                   | The stage of the opportunity.                                                                              | [optional]            |
| **status**             | **bool, dict, float, int, list, str, none_type**                     | The opportunity&#39;s status. _ &#x60;OPEN&#x60; - OPEN _ &#x60;WON&#x60; - WON \* &#x60;LOST&#x60; - LOST | [optional]            |
| **last_activity_at**   | **datetime, none_type**                                              | When the opportunity&#39;s last activity occurred.                                                         | [optional]            |
| **close_date**         | **datetime, none_type**                                              | When the opportunity was closed.                                                                           | [optional]            |
| **remote_created_at**  | **datetime, none_type**                                              | When the third party&#39;s opportunity was created.                                                        | [optional]            |
| **remote_was_deleted** | **bool**                                                             |                                                                                                            | [optional] [readonly] |
| **id**                 | **str**                                                              |                                                                                                            | [optional] [readonly] |
| **remote_id**          | **str, none_type**                                                   | The third-party API ID of the matching object.                                                             | [optional]            |
| **modified_at**        | **datetime**                                                         | This is the datetime that this object was last updated by Merge                                            | [optional] [readonly] |
| **field_mappings**     | **{str: (bool, dict, float, int, list, str, none_type)}, none_type** |                                                                                                            | [optional] [readonly] |
| **remote_data**        | [**[RemoteData], none_type**](RemoteData.md)                         |                                                                                                            | [optional] [readonly] |
| **remote_fields**      | [**[RemoteField]**](RemoteField.md)                                  |                                                                                                            | [optional] [readonly] |
| **any string name**    | **bool, dict, float, int, list, str, none_type**                     | any string name can be used but the value must be the correct type                                         | [optional]            |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
