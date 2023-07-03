# TaxRate

# The TaxRate Object ### Description The `TaxRate` object is used to represent a tax rate.  ### Usage Example Fetch from the `LIST TaxRates` endpoint and view tax rates relevant to a company.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str, none_type** | The tax rate&#39;s description. | [optional] 
**total_tax_rate** | **float, none_type** | The tax rate&#39;s total tax rate. | [optional] 
**effective_tax_rate** | **float, none_type** | The tax rate&#39;s effective tax rate. | [optional] 
**company** | **str, none_type** | The company the tax rate belongs to. | [optional] 
**remote_was_deleted** | **bool** | Indicates whether or not this object has been deleted by third party webhooks. | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**field_mappings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] [readonly] 
**modified_at** | **datetime** | This is the datetime that this object was last updated by Merge | [optional] [readonly] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


