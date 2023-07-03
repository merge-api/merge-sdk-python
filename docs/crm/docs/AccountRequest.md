# AccountRequest

# The Account Object ### Description The `Account` object is used to represent a company in a CRM system. ### Usage Example TODO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner** | **str, none_type** | The account&#39;s owner. | [optional] 
**name** | **str, none_type** | The account&#39;s name. | [optional] 
**description** | **str, none_type** | The account&#39;s description. | [optional] 
**industry** | **str, none_type** | The account&#39;s industry. | [optional] 
**website** | **str, none_type** | The account&#39;s website. | [optional] 
**number_of_employees** | **int, none_type** | The account&#39;s number of employees. | [optional] 
**last_activity_at** | **datetime, none_type** | The last date (either most recent or furthest in the future) of when an activity occurs in an account. | [optional] 
**integration_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 
**linked_account_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 
**remote_fields** | [**[RemoteFieldRequest]**](RemoteFieldRequest.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


