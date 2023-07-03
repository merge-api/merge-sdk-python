# ActivityRequest

# The Activity Object ### Description The `Activity` object is used to represent an activity for a candidate performed by a user. ### Usage Example Fetch from the `LIST Activities` endpoint and filter by `ID` to show all activities.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str, none_type** | The user that performed the action. | [optional] 
**activity_type** | **bool, date, datetime, dict, float, int, list, str, none_type** | The activity&#39;s type.  * &#x60;NOTE&#x60; - NOTE * &#x60;EMAIL&#x60; - EMAIL * &#x60;OTHER&#x60; - OTHER | [optional] 
**subject** | **str, none_type** | The activity&#39;s subject. | [optional] 
**body** | **str, none_type** | The activity&#39;s body. | [optional] 
**visibility** | **bool, date, datetime, dict, float, int, list, str, none_type** | The activity&#39;s visibility.  * &#x60;ADMIN_ONLY&#x60; - ADMIN_ONLY * &#x60;PUBLIC&#x60; - PUBLIC * &#x60;PRIVATE&#x60; - PRIVATE | [optional] 
**candidate** | **str, none_type** | The activity’s candidate. | [optional] 
**integration_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 
**linked_account_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


