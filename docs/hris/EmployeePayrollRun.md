# EmployeePayrollRun

# The EmployeePayrollRun Object ### Description The `EmployeePayrollRun` object is used to represent a payroll run for a specific employee.  ### Usage Example Fetch from the `LIST EmployeePayrollRun` endpoint and filter by `ID` to show all employee payroll runs.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**employee** | **str, none_type** |  | [optional] 
**payroll_run** | **str, none_type** |  | [optional] 
**gross_pay** | **float, none_type** | The gross pay from the run. | [optional] 
**net_pay** | **float, none_type** | The net pay from the run. | [optional] 
**start_date** | **datetime, none_type** | The day and time the payroll run started. | [optional] 
**end_date** | **datetime, none_type** | The day and time the payroll run ended. | [optional] 
**check_date** | **datetime, none_type** | The day and time the payroll run was checked. | [optional] 
**earnings** | [**[Earning]**](Earning.md) |  | [optional] [readonly] 
**deductions** | [**[Deduction]**](Deduction.md) |  | [optional] [readonly] 
**taxes** | [**[Tax]**](Tax.md) |  | [optional] [readonly] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**remote_was_deleted** | **bool** | Indicates whether or not this object has been deleted by third party webhooks. | [optional] [readonly] 
**any string name** | **bool, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


