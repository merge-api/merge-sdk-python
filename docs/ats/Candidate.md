# Candidate

# The Candidate Object ### Description The `Candidate` object is used to represent profile information about a given Candidate. Because it is specific to a Candidate, this information stays constant across applications. ### Usage Example Fetch from the `LIST Candidates` endpoint and filter by `ID` to show all candidates.

## Properties

| Name                    | Type                                                                 | Description                                                        | Notes                 |
| ----------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------ | --------------------- |
| **id**                  | **str**                                                              |                                                                    | [optional] [readonly] |
| **remote_id**           | **str, none_type**                                                   | The third-party API ID of the matching object.                     | [optional]            |
| **first_name**          | **str, none_type**                                                   | The candidate&#39;s first name.                                    | [optional]            |
| **last_name**           | **str, none_type**                                                   | The candidate&#39;s last name.                                     | [optional]            |
| **company**             | **str, none_type**                                                   | The candidate&#39;s current company.                               | [optional]            |
| **title**               | **str, none_type**                                                   | The candidate&#39;s current title.                                 | [optional]            |
| **remote_created_at**   | **datetime, none_type**                                              | When the third party&#39;s candidate was created.                  | [optional]            |
| **remote_updated_at**   | **datetime, none_type**                                              | When the third party&#39;s candidate was updated.                  | [optional]            |
| **last_interaction_at** | **datetime, none_type**                                              | When the most recent interaction with the candidate occurred.      | [optional]            |
| **is_private**          | **bool, none_type**                                                  | Whether or not the candidate is private.                           | [optional]            |
| **can_email**           | **bool, none_type**                                                  | Whether or not the candidate can be emailed.                       | [optional]            |
| **locations**           | **[str, none_type], none_type**                                      | The candidate&#39;s locations.                                     | [optional]            |
| **phone_numbers**       | [**[PhoneNumber]**](PhoneNumber.md)                                  |                                                                    | [optional]            |
| **email_addresses**     | [**[EmailAddress]**](EmailAddress.md)                                |                                                                    | [optional]            |
| **urls**                | [**[Url]**](Url.md)                                                  |                                                                    | [optional]            |
| **tags**                | **[str, none_type]**                                                 | Array of &#x60;Tag&#x60; names as strings.                         | [optional]            |
| **applications**        | **[str, none_type]**                                                 | Array of &#x60;Application&#x60; object IDs.                       | [optional]            |
| **attachments**         | **[str, none_type]**                                                 | Array of &#x60;Attachment&#x60; object IDs.                        | [optional]            |
| **remote_was_deleted**  | **bool**                                                             |                                                                    | [optional] [readonly] |
| **modified_at**         | **datetime**                                                         | This is the datetime that this object was last updated by Merge    | [optional] [readonly] |
| **field_mappings**      | **{str: (bool, dict, float, int, list, str, none_type)}, none_type** |                                                                    | [optional] [readonly] |
| **remote_data**         | [**[RemoteData], none_type**](RemoteData.md)                         |                                                                    | [optional] [readonly] |
| **any string name**     | **bool, dict, float, int, list, str, none_type**                     | any string name can be used but the value must be the correct type | [optional]            |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
