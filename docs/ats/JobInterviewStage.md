# JobInterviewStage

# The JobInterviewStage Object ### Description The `JobInterviewStage` object is used to represent a particular recruiting stage for an `Application`. A given `Application` typically has the `JobInterviewStage` object represented in the current_stage field. ### Usage Example Fetch from the `LIST JobInterviewStages` endpoint and view the job interview stages used by a company.

## Properties

| Name                   | Type                                                                 | Description                                                                                                                                                   | Notes                 |
| ---------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| **id**                 | **str**                                                              |                                                                                                                                                               | [optional] [readonly] |
| **remote_id**          | **str, none_type**                                                   | The third-party API ID of the matching object.                                                                                                                | [optional]            |
| **name**               | **str, none_type**                                                   | Standard stage names are offered by ATS systems but can be modified by users.                                                                                 | [optional]            |
| **job**                | **str, none_type**                                                   | This field is populated only if the stage is specific to a particular job. If the stage is generic, this field will not be populated.                         | [optional]            |
| **stage_order**        | **int, none_type**                                                   | The stage’s order, with the lowest values ordered first. If the third-party does not return details on the order of stages, this field will not be populated. | [optional]            |
| **remote_was_deleted** | **bool**                                                             | Indicates whether or not this object has been deleted by third party webhooks.                                                                                | [optional] [readonly] |
| **modified_at**        | **datetime**                                                         | This is the datetime that this object was last updated by Merge                                                                                               | [optional] [readonly] |
| **field_mappings**     | **{str: (bool, dict, float, int, list, str, none_type)}, none_type** |                                                                                                                                                               | [optional] [readonly] |
| **remote_data**        | [**[RemoteData], none_type**](RemoteData.md)                         |                                                                                                                                                               | [optional] [readonly] |
| **any string name**    | **bool, dict, float, int, list, str, none_type**                     | any string name can be used but the value must be the correct type                                                                                            | [optional]            |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
