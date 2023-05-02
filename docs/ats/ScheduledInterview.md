# ScheduledInterview

# The ScheduledInterview Object ### Description The `ScheduledInterview` object is used to represent a scheduled interview for a given candidate’s application to a job. An `Application` can have multiple `ScheduledInterview`s depending on the particular hiring process. ### Usage Example Fetch from the `LIST ScheduledInterviews` endpoint and filter by `interviewers` to show all office locations.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**application** | **str, none_type** | The application being interviewed. | [optional] 
**job_interview_stage** | **str, none_type** | The stage of the interview. | [optional] 
**organizer** | **str, none_type** | The user organizing the interview. | [optional] 
**interviewers** | **[str, none_type]** | Array of &#x60;RemoteUser&#x60; IDs. | [optional] 
**location** | **str, none_type** | The interview&#39;s location. | [optional] 
**start_at** | **datetime, none_type** | When the interview was started. | [optional] 
**end_at** | **datetime, none_type** | When the interview was ended. | [optional] 
**remote_created_at** | **datetime, none_type** | When the third party&#39;s interview was created. | [optional] 
**remote_updated_at** | **datetime, none_type** | When the third party&#39;s interview was updated. | [optional] 
**status** | **bool, date, datetime, dict, float, int, list, str, none_type** | The interview&#39;s status.  * &#x60;SCHEDULED&#x60; - SCHEDULED * &#x60;AWAITING_FEEDBACK&#x60; - AWAITING_FEEDBACK * &#x60;COMPLETE&#x60; - COMPLETE | [optional] 
**remote_was_deleted** | **bool** | Indicates whether or not this object has been deleted by third party webhooks. | [optional] [readonly] 
**field_mappings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] [readonly] 
**modified_at** | **datetime** | This is the datetime that this object was last updated by Merge | [optional] [readonly] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


