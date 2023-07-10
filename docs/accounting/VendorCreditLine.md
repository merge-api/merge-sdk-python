# VendorCreditLine

# The VendorCreditLine Object ### Description The `VendorCreditLine` object is used to represent a vendor credit's line items. ### Usage Example Fetch from the `GET VendorCredit` endpoint and view the vendor credit's line items.

## Properties

| Name                    | Type                                             | Description                                                        | Notes                 |
| ----------------------- | ------------------------------------------------ | ------------------------------------------------------------------ | --------------------- |
| **tracking_categories** | **[str]**                                        | The line&#39;s associated tracking categories.                     |
| **remote_id**           | **str, none_type**                               | The third-party API ID of the matching object.                     | [optional]            |
| **net_amount**          | **float, none_type**                             | The full value of the credit.                                      | [optional]            |
| **tracking_category**   | **str, none_type**                               | The line&#39;s associated tracking category.                       | [optional]            |
| **description**         | **str, none_type**                               | The line&#39;s description.                                        | [optional]            |
| **account**             | **str, none_type**                               | The line&#39;s account.                                            | [optional]            |
| **company**             | **str, none_type**                               | The company the line belongs to.                                   | [optional]            |
| **exchange_rate**       | **str, none_type**                               | The vendor credit line item&#39;s exchange rate.                   | [optional]            |
| **modified_at**         | **datetime**                                     | This is the datetime that this object was last updated by Merge    | [optional] [readonly] |
| **any string name**     | **bool, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]            |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
