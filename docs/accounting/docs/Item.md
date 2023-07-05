# Item

# The Item Object ### Description The `Item` object refers to the goods involved in a transaction.  ### Usage Example Fetch from the `LIST Items` endpoint and view a company's items.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**name** | **str, none_type** | The item&#39;s name. | [optional] 
**status** | **bool, date, datetime, dict, float, int, list, str, none_type** | The item&#39;s status.  * &#x60;ACTIVE&#x60; - ACTIVE * &#x60;ARCHIVED&#x60; - ARCHIVED | [optional] 
**unit_price** | **float, none_type** | The item&#39;s unit price. | [optional] 
**purchase_price** | **float, none_type** | The price at which the item is purchased from a vendor. | [optional] 
**purchase_account** | **str, none_type** | References the default account used to record a purchase of the item. | [optional] 
**sales_account** | **str, none_type** | References the default account used to record a sale. | [optional] 
**company** | **str, none_type** | The company the item belongs to. | [optional] 
**remote_updated_at** | **datetime, none_type** | When the third party&#39;s item note was updated. | [optional] 
**remote_was_deleted** | **bool** | Indicates whether or not this object has been deleted by third party webhooks. | [optional] [readonly] 
**modified_at** | **datetime** | This is the datetime that this object was last updated by Merge | [optional] [readonly] 
**field_mappings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] [readonly] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


