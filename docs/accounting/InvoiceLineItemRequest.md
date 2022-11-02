# InvoiceLineItemRequest

# The InvoiceLineItem Object ### Description The `InvoiceLineItem` object is used to represent an invoice's line items.  ### Usage Example Fetch from the `GET Invoice` endpoint and view the invoice's line items.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**description** | **str, none_type** | The line item&#39;s description. | [optional] 
**unit_price** | **float, none_type** | The line item&#39;s unit price. | [optional] 
**quantity** | **float, none_type** | The line item&#39;s quantity. | [optional] 
**total_amount** | **float, none_type** | The line item&#39;s total amount. | [optional] 
**item** | **str, none_type** |  | [optional] 
**account** | **str, none_type** |  | [optional] 
**tracking_category** | **str, none_type** |  | [optional] 
**integration_params** | **{str: (bool, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 
**linked_account_params** | **{str: (bool, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 
**any string name** | **bool, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


