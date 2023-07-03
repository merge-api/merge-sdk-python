# PatchedTaskRequest

# The Task Object ### Description The `Task` object is used to represent a task, such as a to-do item. ### Usage Example TODO

## Properties

| Name                      | Type                                                                 | Description                                                                    | Notes      |
| ------------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ---------- |
| **subject**               | **str, none_type**                                                   | The task&#39;s subject.                                                        | [optional] |
| **content**               | **str, none_type**                                                   | The task&#39;s content.                                                        | [optional] |
| **owner**                 | **str, none_type**                                                   | The task&#39;s owner.                                                          | [optional] |
| **account**               | **str, none_type**                                                   | The task&#39;s account.                                                        | [optional] |
| **opportunity**           | **str, none_type**                                                   | The task&#39;s opportunity.                                                    | [optional] |
| **completed_date**        | **datetime, none_type**                                              | When the task is completed.                                                    | [optional] |
| **due_date**              | **datetime, none_type**                                              | When the task is due.                                                          | [optional] |
| **status**                | **bool, dict, float, int, list, str, none_type**                     | The task&#39;s status. _ &#x60;OPEN&#x60; - OPEN _ &#x60;CLOSED&#x60; - CLOSED | [optional] |
| **integration_params**    | **{str: (bool, dict, float, int, list, str, none_type)}, none_type** |                                                                                | [optional] |
| **linked_account_params** | **{str: (bool, dict, float, int, list, str, none_type)}, none_type** |                                                                                | [optional] |
| **remote_fields**         | [**[RemoteFieldRequest]**](RemoteFieldRequest.md)                    |                                                                                | [optional] |
| **any string name**       | **bool, dict, float, int, list, str, none_type**                     | any string name can be used but the value must be the correct type             | [optional] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
