# Deduction

# The Deduction Object ### Description The `Deduction` object is used to represent an array of the wages withheld from total earnings for the purpose of paying taxes.  ### Usage Example Fetch from the `LIST Deductions` endpoint and filter by `ID` to show all deductions.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**employee_payroll_run** | **str, none_type** |  | [optional] 
**name** | **str, none_type** | The deduction&#39;s name. | [optional] 
**employee_deduction** | **float, none_type** | The amount of money that is withheld from an employee&#39;s gross pay by the employee. | [optional] 
**company_deduction** | **float, none_type** | The amount of money that is withheld on behalf of an employee by the company. | [optional] 
**remote_was_deleted** | **bool** | Indicates whether or not this object has been deleted by third party webhooks. | [optional] 
**field_mappings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] [readonly] 
**modified_at** | **datetime** | This is the datetime that this object was last updated by Merge | [optional] [readonly] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


