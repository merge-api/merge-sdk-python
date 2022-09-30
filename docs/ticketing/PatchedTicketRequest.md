# PatchedTicketRequest

# The Ticket Object ### Description The `Ticket` object is used to represent a ticket or a task within a system.  ### Usage Example TODO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | The ticket&#39;s name. | [optional] 
**assignees** | **[str, none_type]** |  | [optional] 
**due_date** | **datetime, none_type** | The ticket&#39;s due date. | [optional] 
**status** | **bool, dict, float, int, list, str, none_type** | The current status of the ticket. | [optional] 
**description** | **str, none_type** | The ticket&#39;s description. | [optional] 
**project** | **str, none_type** |  | [optional] 
**ticket_type** | **str, none_type** | The ticket&#39;s type. | [optional] 
**account** | **str, none_type** |  | [optional] 
**contact** | **str, none_type** |  | [optional] 
**parent_ticket** | **str, none_type** |  | [optional] 
**tags** | **[str]** |  | [optional] 
**remote_created_at** | **datetime, none_type** | When the third party&#39;s ticket was created. | [optional] 
**remote_updated_at** | **datetime, none_type** | When the third party&#39;s ticket was updated. | [optional] 
**completed_at** | **datetime, none_type** | When the ticket was completed. | [optional] 
**ticket_url** | **str, none_type** | The 3rd party url of the Ticket. | [optional] 
**priority** | **bool, dict, float, int, list, str, none_type** | The priority or urgency of the Ticket. Possible values include: URGENT, HIGH, NORMAL, LOW - in cases where there is no clear mapping - the original value passed through. | [optional] 
**any string name** | **bool, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


