# CreditNote

# The CreditNote Object ### Description The `CreditNote` object is used to represent a refund or credit of payment.  ### Usage Example Fetch from the `LIST CreditNotes` endpoint and view a company's credit notes.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**transaction_date** | **datetime, none_type** | The credit note&#39;s transaction date. | [optional] 
**status** | **bool, dict, float, int, list, str, none_type** | The credit note&#39;s status. | [optional] 
**number** | **str, none_type** | The credit note&#39;s number. | [optional] 
**contact** | **str, none_type** | The credit note&#39;s contact. | [optional] 
**total_amount** | **float, none_type** | The credit note&#39;s total amount. | [optional] 
**remaining_credit** | **float, none_type** | The credit note&#39;s remaining credit. | [optional] 
**line_items** | [**[CreditNoteLineItem]**](CreditNoteLineItem.md) |  | [optional] [readonly] 
**currency** | **bool, dict, float, int, list, str, none_type** | The credit note&#39;s currency. | [optional] 
**remote_created_at** | **datetime, none_type** | When the third party&#39;s credit note was created. | [optional] 
**remote_updated_at** | **datetime, none_type** | When the third party&#39;s credit note was updated. | [optional] 
**payments** | **[str, none_type]** | Array of &#x60;Payment&#x60; object IDs | [optional] 
**remote_was_deleted** | **bool** | Indicates whether or not this object has been deleted by third party webhooks. | [optional] [readonly] 
**any string name** | **bool, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


