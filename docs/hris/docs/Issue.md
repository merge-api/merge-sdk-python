# Issue

## Properties

| Name                    | Type                                                      | Description                                                                                                                             | Notes                 |
| ----------------------- | --------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| **error_description**   | **str**                                                   |                                                                                                                                         |
| **id**                  | **str**                                                   |                                                                                                                                         | [optional] [readonly] |
| **status**              | **bool, dict, float, int, list, str, none_type**          | Status of the issue. Options: (&#39;ONGOING&#39;, &#39;RESOLVED&#39;) _ &#x60;ONGOING&#x60; - ONGOING _ &#x60;RESOLVED&#x60; - RESOLVED | [optional]            |
| **end_user**            | **{str: (bool, dict, float, int, list, str, none_type)}** |                                                                                                                                         | [optional] [readonly] |
| **first_incident_time** | **datetime, none_type**                                   |                                                                                                                                         | [optional]            |
| **last_incident_time**  | **datetime, none_type**                                   |                                                                                                                                         | [optional]            |
| **is_muted**            | **bool**                                                  |                                                                                                                                         | [optional] [readonly] |
| **error_details**       | **[str]**                                                 |                                                                                                                                         | [optional] [readonly] |
| **any string name**     | **bool, dict, float, int, list, str, none_type**          | any string name can be used but the value must be the correct type                                                                      | [optional]            |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
