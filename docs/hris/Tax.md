# Tax

# The Tax Object ### Description The `Tax` object is used to represent an array of the tax deductions for a given employee's payroll run. ### Usage Example Fetch from the `LIST Taxes` endpoint and filter by `ID` to show all taxes.

## Properties

| Name                     | Type                                                                 | Description                                                                    | Notes                 |
| ------------------------ | -------------------------------------------------------------------- | ------------------------------------------------------------------------------ | --------------------- |
| **id**                   | **str**                                                              |                                                                                | [optional] [readonly] |
| **remote_id**            | **str, none_type**                                                   | The third-party API ID of the matching object.                                 | [optional]            |
| **employee_payroll_run** | **str, none_type**                                                   |                                                                                | [optional]            |
| **name**                 | **str, none_type**                                                   | The tax&#39;s name.                                                            | [optional]            |
| **amount**               | **float, none_type**                                                 | The tax amount.                                                                | [optional]            |
| **employer_tax**         | **bool, none_type**                                                  | Whether or not the employer is responsible for paying the tax.                 | [optional]            |
| **remote_was_deleted**   | **bool**                                                             | Indicates whether or not this object has been deleted by third party webhooks. | [optional]            |
| **modified_at**          | **datetime**                                                         | This is the datetime that this object was last updated by Merge                | [optional] [readonly] |
| **field_mappings**       | **{str: (bool, dict, float, int, list, str, none_type)}, none_type** |                                                                                | [optional] [readonly] |
| **remote_data**          | [**[RemoteData], none_type**](RemoteData.md)                         |                                                                                | [optional] [readonly] |
| **any string name**      | **bool, dict, float, int, list, str, none_type**                     | any string name can be used but the value must be the correct type             | [optional]            |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
