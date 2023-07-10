# PatchedContactRequest

# The Contact Object ### Description The `Contact` object is used to represent an existing point of contact at a company in a CRM system. ### Usage Example TODO

## Properties

| Name                      | Type                                                                 | Description                                                        | Notes      |
| ------------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------ | ---------- |
| **first_name**            | **str, none_type**                                                   | The contact&#39;s first name.                                      | [optional] |
| **last_name**             | **str, none_type**                                                   | The contact&#39;s last name.                                       | [optional] |
| **account**               | **str, none_type**                                                   | The contact&#39;s account.                                         | [optional] |
| **addresses**             | [**[AddressRequest]**](AddressRequest.md)                            |                                                                    | [optional] |
| **email_addresses**       | [**[EmailAddressRequest]**](EmailAddressRequest.md)                  |                                                                    | [optional] |
| **phone_numbers**         | [**[PhoneNumberRequest]**](PhoneNumberRequest.md)                    |                                                                    | [optional] |
| **last_activity_at**      | **datetime, none_type**                                              | When the contact&#39;s last activity occurred.                     | [optional] |
| **integration_params**    | **{str: (bool, dict, float, int, list, str, none_type)}, none_type** |                                                                    | [optional] |
| **linked_account_params** | **{str: (bool, dict, float, int, list, str, none_type)}, none_type** |                                                                    | [optional] |
| **remote_fields**         | [**[RemoteFieldRequest]**](RemoteFieldRequest.md)                    |                                                                    | [optional] |
| **any string name**       | **bool, dict, float, int, list, str, none_type**                     | any string name can be used but the value must be the correct type | [optional] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
