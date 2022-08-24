# VendorCredit

# The VendorCredit Object ### Description The `VendorCredit` object is used to represent a company's vendor credits.  ### Usage Example Fetch from the `GET VendorCredit` endpoint and view a company's vendor credits.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**number** | **str, none_type** | The vendor credit&#39;s number. | [optional] 
**transaction_date** | **datetime, none_type** | The vendor credit&#39;s transaction date. | [optional] 
**vendor** | **str, none_type** |  | [optional] 
**total_amount** | **float, none_type** | The vendor credit&#39;s total amount. | [optional] 
**currency** | **bool, date, datetime, dict, float, int, list, str, none_type** | The vendor credit&#39;s currency. | [optional] 
**lines** | [**[VendorCreditLine]**](VendorCreditLine.md) |  | [optional] [readonly] 
**remote_was_deleted** | **bool** | Indicates whether or not this object has been deleted by third party webhooks. | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


