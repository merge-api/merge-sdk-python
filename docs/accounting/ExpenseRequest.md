# ExpenseRequest

# The Expense Object ### Description The `Expense` object is used to represent a company's expenses  ### Usage Example Fetch from the `GET Expense` endpoint and view a company's expense.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**transaction_date** | **datetime, none_type** | When the transaction occurred. | [optional] 
**remote_created_at** | **datetime, none_type** | When the expense was created. | [optional] 
**account** | **str, none_type** |  | [optional] 
**contact** | **str, none_type** |  | [optional] 
**total_amount** | **float, none_type** | The expense&#39;s total amount. | [optional] 
**currency** | **bool, date, datetime, dict, float, int, list, str, none_type** | The expense&#39;s currency. | [optional] 
**memo** | **str, none_type** | The expense&#39;s private note. | [optional] 
**integration_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 
**linked_account_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


