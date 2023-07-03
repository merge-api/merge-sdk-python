# EmailAddress

# The EmailAddress Object ### Description The `EmailAddress` object is used to represent a candidate's email address. ### Usage Example Fetch from the `GET Candidate` endpoint and view their email addresses.

## Properties

| Name                   | Type                                             | Description                                                                                                         | Notes                 |
| ---------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------- | --------------------- |
| **value**              | **str, none_type**                               | The email address.                                                                                                  | [optional]            |
| **email_address_type** | **bool, dict, float, int, list, str, none_type** | The type of email address. _ &#x60;PERSONAL&#x60; - PERSONAL _ &#x60;WORK&#x60; - WORK \* &#x60;OTHER&#x60; - OTHER | [optional]            |
| **modified_at**        | **datetime**                                     | This is the datetime that this object was last updated by Merge                                                     | [optional] [readonly] |
| **any string name**    | **bool, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type                                                  | [optional]            |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
