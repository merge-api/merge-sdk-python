# TicketRequest

# The Ticket Object ### Description The `Ticket` object is used to represent a ticket or a task within a system.  ### Usage Example TODO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | The ticket&#39;s name. | [optional] 
**assignees** | **[str, none_type]** |  | [optional] 
**creator** | **str, none_type** | The user who created this ticket. | [optional] 
**due_date** | **datetime, none_type** | The ticket&#39;s due date. | [optional] 
**status** | **bool, date, datetime, dict, float, int, list, str, none_type** | The current status of the ticket.  * &#x60;OPEN&#x60; - OPEN * &#x60;CLOSED&#x60; - CLOSED * &#x60;IN_PROGRESS&#x60; - IN_PROGRESS * &#x60;ON_HOLD&#x60; - ON_HOLD | [optional] 
**description** | **str, none_type** | The ticket’s description. HTML version of description is mapped if supported by the third-party platform. | [optional] 
**project** | **str, none_type** | The project the ticket belongs to. | [optional] 
**collections** | **[str, none_type]** |  | [optional] 
**ticket_type** | **str, none_type** | The ticket&#39;s type. | [optional] 
**account** | **str, none_type** | The account associated with the ticket. | [optional] 
**contact** | **str, none_type** | The contact associated with the ticket. | [optional] 
**parent_ticket** | **str, none_type** | The ticket&#39;s parent ticket. | [optional] 
**attachments** | **[str, none_type]** |  | [optional] 
**tags** | **[str, none_type]** |  | [optional] 
**completed_at** | **datetime, none_type** | When the ticket was completed. | [optional] 
**ticket_url** | **str, none_type** | The 3rd party url of the Ticket. | [optional] 
**priority** | **bool, date, datetime, dict, float, int, list, str, none_type** | The priority or urgency of the Ticket.  * &#x60;URGENT&#x60; - URGENT * &#x60;HIGH&#x60; - HIGH * &#x60;NORMAL&#x60; - NORMAL * &#x60;LOW&#x60; - LOW | [optional] 
**integration_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 
**linked_account_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 
**remote_fields** | [**[RemoteFieldRequest]**](RemoteFieldRequest.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


