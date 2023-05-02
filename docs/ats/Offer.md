# Offer

# The Offer Object ### Description The `Offer` object is used to represent an offer for a candidate's application specific to a job. ### Usage Example Fetch from the `LIST Offers` endpoint and filter by `ID` to show all offers.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**application** | **str, none_type** | The application who is receiving the offer. | [optional] 
**creator** | **str, none_type** | The user who created the offer. | [optional] 
**remote_created_at** | **datetime, none_type** | When the third party&#39;s offer was created. | [optional] 
**closed_at** | **datetime, none_type** | When the offer was closed. | [optional] 
**sent_at** | **datetime, none_type** | When the offer was sent. | [optional] 
**start_date** | **datetime, none_type** | The employment start date on the offer. | [optional] 
**status** | **bool, date, datetime, dict, float, int, list, str, none_type** | The offer&#39;s status.  * &#x60;DRAFT&#x60; - DRAFT * &#x60;APPROVAL-SENT&#x60; - APPROVAL-SENT * &#x60;APPROVED&#x60; - APPROVED * &#x60;SENT&#x60; - SENT * &#x60;SENT-MANUALLY&#x60; - SENT-MANUALLY * &#x60;OPENED&#x60; - OPENED * &#x60;DENIED&#x60; - DENIED * &#x60;SIGNED&#x60; - SIGNED * &#x60;DEPRECATED&#x60; - DEPRECATED | [optional] 
**remote_was_deleted** | **bool** | Indicates whether or not this object has been deleted by third party webhooks. | [optional] [readonly] 
**field_mappings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] [readonly] 
**modified_at** | **datetime** | This is the datetime that this object was last updated by Merge | [optional] [readonly] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


