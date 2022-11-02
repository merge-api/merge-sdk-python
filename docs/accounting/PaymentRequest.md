# PaymentRequest

# The Payment Object ### Description The `Payment` object is used to represent a invoice's payment.  ### Usage Example Fetch from the `GET Payment` endpoint and view an invoice's payment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**transaction_date** | **datetime, none_type** | The payment&#39;s transaction date. | [optional] 
**contact** | **str, none_type** |  | [optional] 
**account** | **str, none_type** |  | [optional] 
**total_amount** | **float, none_type** | The payment&#39;s total amount. | [optional] 
**remote_updated_at** | **datetime, none_type** | When the third party&#39;s payment entry was updated. | [optional] 
**integration_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 
**linked_account_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


