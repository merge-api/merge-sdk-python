# PurchaseOrderRequest

# The PurchaseOrder Object ### Description The `PurchaseOrder` object is used to represent a company's purchase orders.  ### Usage Example Fetch from the `LIST PurchaseOrders` endpoint and view a company's purchase orders.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**status** | **bool, dict, float, int, list, str, none_type** | The purchase order&#39;s status. | [optional] 
**issue_date** | **datetime, none_type** | The purchase order&#39;s issue date. | [optional] 
**delivery_date** | **datetime, none_type** | The purchase order&#39;s delivery date. | [optional] 
**delivery_address** | **str, none_type** | The purchase order&#39;s delivery address. | [optional] 
**customer** | **str, none_type** | The purchase order&#39;s customer. | [optional] 
**vendor** | **str, none_type** | The purchase_order&#39;s vendor. | [optional] 
**memo** | **str, none_type** | A memo attached to the purchase order. | [optional] 
**total_amount** | **float, none_type** | The purchase order&#39;s total amount. | [optional] 
**currency** | **bool, dict, float, int, list, str, none_type** | The purchase order&#39;s currency. | [optional] 
**remote_created_at** | **datetime, none_type** | When the third party&#39;s purchase order note was created. | [optional] 
**remote_updated_at** | **datetime, none_type** | When the third party&#39;s purchase order note was updated. | [optional] 
**integration_params** | **{str: (bool, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 
**linked_account_params** | **{str: (bool, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 
**any string name** | **bool, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


