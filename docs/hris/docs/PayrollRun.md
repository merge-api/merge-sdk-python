# PayrollRun

# The PayrollRun Object ### Description The `PayrollRun` object is used to represent a group of pay statements for a specific pay schedule.  ### Usage Example Fetch from the `LIST PayrollRuns` endpoint and filter by `ID` to show all payroll runs.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**run_state** | **bool, date, datetime, dict, float, int, list, str, none_type** | The state of the payroll run  * &#x60;PAID&#x60; - PAID * &#x60;DRAFT&#x60; - DRAFT * &#x60;APPROVED&#x60; - APPROVED * &#x60;FAILED&#x60; - FAILED * &#x60;CLOSED&#x60; - CLOSED | [optional] 
**run_type** | **bool, date, datetime, dict, float, int, list, str, none_type** | The type of the payroll run  * &#x60;REGULAR&#x60; - REGULAR * &#x60;OFF_CYCLE&#x60; - OFF_CYCLE * &#x60;CORRECTION&#x60; - CORRECTION * &#x60;TERMINATION&#x60; - TERMINATION * &#x60;SIGN_ON_BONUS&#x60; - SIGN_ON_BONUS | [optional] 
**start_date** | **datetime, none_type** | The day and time the payroll run started. | [optional] 
**end_date** | **datetime, none_type** | The day and time the payroll run ended. | [optional] 
**check_date** | **datetime, none_type** | The day and time the payroll run was checked. | [optional] 
**remote_was_deleted** | **bool** | Indicates whether or not this object has been deleted by third party webhooks. | [optional] [readonly] 
**field_mappings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] [readonly] 
**modified_at** | **datetime** | This is the datetime that this object was last updated by Merge | [optional] [readonly] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

