# JournalLineRequest

# The JournalLine Object ### Description The `JournalLine` object is used to represent a journal entry's line items.  ### Usage Example Fetch from the `GET JournalEntry` endpoint and view the journal entry's line items.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**account** | **str, none_type** |  | [optional] 
**net_amount** | **float, none_type** | The line&#39;s net amount. | [optional] 
**tracking_category** | **str, none_type** |  | [optional] 
**contact** | **str, none_type** |  | [optional] 
**description** | **str, none_type** | The line&#39;s description. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


