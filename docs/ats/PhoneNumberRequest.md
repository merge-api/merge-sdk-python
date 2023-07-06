# PhoneNumberRequest

# The PhoneNumber Object ### Description The `PhoneNumber` object is used to represent a candidate's phone number. ### Usage Example Fetch from the `GET Candidate` endpoint and view their phone numbers.

## Properties

| Name                      | Type                                                                 | Description                                                                                                                                                          | Notes      |
| ------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **value**                 | **str, none_type**                                                   | The phone number.                                                                                                                                                    | [optional] |
| **phone_number_type**     | **bool, dict, float, int, list, str, none_type**                     | The type of phone number. _ &#x60;HOME&#x60; - HOME _ &#x60;WORK&#x60; - WORK _ &#x60;MOBILE&#x60; - MOBILE _ &#x60;SKYPE&#x60; - SKYPE \* &#x60;OTHER&#x60; - OTHER | [optional] |
| **integration_params**    | **{str: (bool, dict, float, int, list, str, none_type)}, none_type** |                                                                                                                                                                      | [optional] |
| **linked_account_params** | **{str: (bool, dict, float, int, list, str, none_type)}, none_type** |                                                                                                                                                                      | [optional] |
| **any string name**       | **bool, dict, float, int, list, str, none_type**                     | any string name can be used but the value must be the correct type                                                                                                   | [optional] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
