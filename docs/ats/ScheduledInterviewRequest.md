# ScheduledInterviewRequest

# The ScheduledInterview Object ### Description The `ScheduledInterview` object is used to represent a scheduled interview for a given candidate’s application to a job. An `Application` can have multiple `ScheduledInterview`s depending on the particular hiring process. ### Usage Example Fetch from the `LIST ScheduledInterviews` endpoint and filter by `interviewers` to show all office locations.

## Properties

| Name                      | Type                                                                 | Description                                                                                                                                            | Notes      |
| ------------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| **application**           | **str, none_type**                                                   | The application being interviewed.                                                                                                                     | [optional] |
| **job_interview_stage**   | **str, none_type**                                                   | The stage of the interview.                                                                                                                            | [optional] |
| **organizer**             | **str, none_type**                                                   | The user organizing the interview.                                                                                                                     | [optional] |
| **interviewers**          | **[str, none_type]**                                                 | Array of &#x60;RemoteUser&#x60; IDs.                                                                                                                   | [optional] |
| **location**              | **str, none_type**                                                   | The interview&#39;s location.                                                                                                                          | [optional] |
| **start_at**              | **datetime, none_type**                                              | When the interview was started.                                                                                                                        | [optional] |
| **end_at**                | **datetime, none_type**                                              | When the interview was ended.                                                                                                                          | [optional] |
| **status**                | **bool, dict, float, int, list, str, none_type**                     | The interview&#39;s status. _ &#x60;SCHEDULED&#x60; - SCHEDULED _ &#x60;AWAITING_FEEDBACK&#x60; - AWAITING_FEEDBACK \* &#x60;COMPLETE&#x60; - COMPLETE | [optional] |
| **integration_params**    | **{str: (bool, dict, float, int, list, str, none_type)}, none_type** |                                                                                                                                                        | [optional] |
| **linked_account_params** | **{str: (bool, dict, float, int, list, str, none_type)}, none_type** |                                                                                                                                                        | [optional] |
| **any string name**       | **bool, dict, float, int, list, str, none_type**                     | any string name can be used but the value must be the correct type                                                                                     | [optional] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
