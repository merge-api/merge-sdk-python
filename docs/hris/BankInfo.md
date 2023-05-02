# BankInfo

# The BankInfo Object ### Description The `BankInfo` object is used to represent the Bank Account information for an Employee.  ### Usage Example Fetch from the `LIST BankInfo` endpoint and filter by `ID` to show all bank information.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**employee** | **str, none_type** | The employee with this bank account. | [optional] 
**account_number** | **str, none_type** | The account number. | [optional] 
**routing_number** | **str, none_type** | The routing number. | [optional] 
**bank_name** | **str, none_type** | The bank name. | [optional] 
**account_type** | **bool, date, datetime, dict, float, int, list, str, none_type** | The bank account type  * &#x60;SAVINGS&#x60; - SAVINGS * &#x60;CHECKING&#x60; - CHECKING | [optional] 
**remote_created_at** | **datetime, none_type** | When the matching bank object was created in the third party system. | [optional] 
**remote_was_deleted** | **bool** | Indicates whether or not this object has been deleted by third party webhooks. | [optional] [readonly] 
**field_mappings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] [readonly] 
**modified_at** | **datetime** | This is the datetime that this object was last updated by Merge | [optional] [readonly] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


