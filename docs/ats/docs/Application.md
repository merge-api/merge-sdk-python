# Application

# The Application Object ### Description The Application Object is used to represent a candidate's journey through a particular Job's recruiting process. If a Candidate applies for multiple Jobs, there will be a separate Application for each Job if the third-party integration allows it.  ### Usage Example Fetch from the `LIST Applications` endpoint and filter by `ID` to show all applications.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**candidate** | **str, none_type** | The candidate applying. | [optional] 
**job** | **str, none_type** | The job being applied for. | [optional] 
**applied_at** | **datetime, none_type** | When the application was submitted. | [optional] 
**rejected_at** | **datetime, none_type** | When the application was rejected. | [optional] 
**source** | **str, none_type** | The application&#39;s source. | [optional] 
**credited_to** | **str, none_type** | The user credited for this application. | [optional] 
**current_stage** | **str, none_type** | The application&#39;s current stage. | [optional] 
**reject_reason** | **str, none_type** | The application&#39;s reason for rejection. | [optional] 
**remote_was_deleted** | **bool** |  | [optional] [readonly] 
**modified_at** | **datetime** | This is the datetime that this object was last updated by Merge | [optional] [readonly] 
**field_mappings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] [readonly] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


