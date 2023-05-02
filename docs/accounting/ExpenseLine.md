# ExpenseLine

# The ExpenseLine Object ### Description The `ExpenseLine` object is used to represent an expense's line items.  ### Usage Example Fetch from the `GET Expense` endpoint and view the expense's line items.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**item** | **str, none_type** | The line&#39;s item. | [optional] 
**net_amount** | **float, none_type** | The line&#39;s net amount. | [optional] 
**tracking_category** | **str, none_type** |  | [optional] 
**tracking_categories** | **[str, none_type]** |  | [optional] 
**company** | **str, none_type** | The company the line belongs to. | [optional] 
**account** | **str, none_type** | The expense&#39;s payment account. | [optional] 
**contact** | **str, none_type** | The expense&#39;s contact. | [optional] 
**description** | **str, none_type** | The description of the item that was purchased by the company. | [optional] 
**exchange_rate** | **str, none_type** | The expense line item&#39;s exchange rate. | [optional] 
**modified_at** | **datetime** | This is the datetime that this object was last updated by Merge | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


