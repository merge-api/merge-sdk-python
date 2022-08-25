# Account

# The Account Object ### Description The `Account` object is what businesses use to track transactions. Accountants often call accounts \"ledgers\".  ### Usage Example Fetch from the `LIST Accounts` endpoint and view a company's accounts.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**name** | **str, none_type** | The account&#39;s name. | [optional] 
**description** | **str, none_type** | The account&#39;s description. | [optional] 
**classification** | **bool, date, datetime, dict, float, int, list, str, none_type** | The account&#39;s classification. | [optional] 
**type** | **str, none_type** | The account&#39;s type. | [optional] 
**status** | **bool, date, datetime, dict, float, int, list, str, none_type** | The account&#39;s status. | [optional] 
**current_balance** | **float, none_type** | The account&#39;s current balance. | [optional] 
**currency** | **bool, date, datetime, dict, float, int, list, str, none_type** | The account&#39;s currency. | [optional] 
**account_number** | **str, none_type** | The account&#39;s number. | [optional] 
**remote_was_deleted** | **bool** | Indicates whether or not this object has been deleted by third party webhooks. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


