# IncomeStatement

# The IncomeStatement Object ### Description The `IncomeStatement` object is used to represent a company's income statements.  ### Usage Example Fetch from the `GET IncomeStatement` endpoint and view a company's income statement for a given period.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**name** | **str, none_type** | The income statement&#39;s name. | [optional] 
**currency** | **bool, dict, float, int, list, str, none_type** | The income statement&#39;s currency. | [optional] 
**start_period** | **datetime, none_type** | The income statement&#39;s start period. | [optional] 
**end_period** | **datetime, none_type** | The income statement&#39;s end period. | [optional] 
**income** | [**[ReportItem]**](ReportItem.md) |  | [optional] [readonly] 
**cost_of_sales** | [**[ReportItem]**](ReportItem.md) |  | [optional] [readonly] 
**gross_profit** | **float, none_type** | The income statement&#39;s gross profit. | [optional] 
**operating_expenses** | [**[ReportItem]**](ReportItem.md) |  | [optional] [readonly] 
**net_operating_income** | **float, none_type** | The income statement&#39;s net operating profit. | [optional] 
**non_operating_expenses** | [**[ReportItem]**](ReportItem.md) |  | [optional] [readonly] 
**net_income** | **float, none_type** | The income statement&#39;s net income. | [optional] 
**remote_was_deleted** | **bool** | Indicates whether or not this object has been deleted by third party webhooks. | [optional] [readonly] 
**any string name** | **bool, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


