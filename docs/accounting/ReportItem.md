# ReportItem

# The ReportItem Object ### Description The `ReportItem` object is used to represent a report item for a Balance Sheet, Cash Flow Statement or Profit and Loss Report. ### Usage Example Fetch from the `GET BalanceSheet` endpoint and view the balance sheet's report items.

## Properties

| Name                | Type                                                      | Description                                                        | Notes                 |
| ------------------- | --------------------------------------------------------- | ------------------------------------------------------------------ | --------------------- |
| **remote_id**       | **str, none_type**                                        | The third-party API ID of the matching object.                     | [optional]            |
| **name**            | **str, none_type**                                        | The report item&#39;s name.                                        | [optional]            |
| **value**           | **float, none_type**                                      | The report item&#39;s value.                                       | [optional]            |
| **sub_items**       | **{str: (bool, dict, float, int, list, str, none_type)}** |                                                                    | [optional] [readonly] |
| **company**         | **str, none_type**                                        | The company the report item belongs to.                            | [optional]            |
| **modified_at**     | **datetime**                                              | This is the datetime that this object was last updated by Merge    | [optional] [readonly] |
| **any string name** | **bool, dict, float, int, list, str, none_type**          | any string name can be used but the value must be the correct type | [optional]            |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
