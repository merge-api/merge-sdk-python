# EEOC

# The EEOC Object ### Description The `EEOC` object is used to represent the Equal Employment Opportunity Commission information for a candidate (race, gender, veteran status, disability status). ### Usage Example Fetch from the `LIST EEOCs` endpoint and filter by `candidate` to show all EEOC information for a candidate.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**candidate** | **str, none_type** | The candidate being represented. | [optional] 
**submitted_at** | **datetime, none_type** | When the information was submitted. | [optional] 
**race** | **bool, date, datetime, dict, float, int, list, str, none_type** | The candidate&#39;s race.  * &#x60;AMERICAN_INDIAN_OR_ALASKAN_NATIVE&#x60; - AMERICAN_INDIAN_OR_ALASKAN_NATIVE * &#x60;ASIAN&#x60; - ASIAN * &#x60;BLACK_OR_AFRICAN_AMERICAN&#x60; - BLACK_OR_AFRICAN_AMERICAN * &#x60;HISPANIC_OR_LATINO&#x60; - HISPANIC_OR_LATINO * &#x60;WHITE&#x60; - WHITE * &#x60;NATIVE_HAWAIIAN_OR_OTHER_PACIFIC_ISLANDER&#x60; - NATIVE_HAWAIIAN_OR_OTHER_PACIFIC_ISLANDER * &#x60;TWO_OR_MORE_RACES&#x60; - TWO_OR_MORE_RACES * &#x60;DECLINE_TO_SELF_IDENTIFY&#x60; - DECLINE_TO_SELF_IDENTIFY | [optional] 
**gender** | **bool, date, datetime, dict, float, int, list, str, none_type** | The candidate&#39;s gender.  * &#x60;MALE&#x60; - MALE * &#x60;FEMALE&#x60; - FEMALE * &#x60;NON-BINARY&#x60; - NON-BINARY * &#x60;OTHER&#x60; - OTHER * &#x60;DECLINE_TO_SELF_IDENTIFY&#x60; - DECLINE_TO_SELF_IDENTIFY | [optional] 
**veteran_status** | **bool, date, datetime, dict, float, int, list, str, none_type** | The candidate&#39;s veteran status.  * &#x60;I_AM_NOT_A_PROTECTED_VETERAN&#x60; - I_AM_NOT_A_PROTECTED_VETERAN * &#x60;I_IDENTIFY_AS_ONE_OR_MORE_OF_THE_CLASSIFICATIONS_OF_A_PROTECTED_VETERAN&#x60; - I_IDENTIFY_AS_ONE_OR_MORE_OF_THE_CLASSIFICATIONS_OF_A_PROTECTED_VETERAN * &#x60;I_DONT_WISH_TO_ANSWER&#x60; - I_DONT_WISH_TO_ANSWER | [optional] 
**disability_status** | **bool, date, datetime, dict, float, int, list, str, none_type** | The candidate&#39;s disability status.  * &#x60;YES_I_HAVE_A_DISABILITY_OR_PREVIOUSLY_HAD_A_DISABILITY&#x60; - YES_I_HAVE_A_DISABILITY_OR_PREVIOUSLY_HAD_A_DISABILITY * &#x60;NO_I_DONT_HAVE_A_DISABILITY&#x60; - NO_I_DONT_HAVE_A_DISABILITY * &#x60;I_DONT_WISH_TO_ANSWER&#x60; - I_DONT_WISH_TO_ANSWER | [optional] 
**remote_was_deleted** | **bool** | Indicates whether or not this object has been deleted by third party webhooks. | [optional] [readonly] 
**field_mappings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] [readonly] 
**modified_at** | **datetime** | This is the datetime that this object was last updated by Merge | [optional] [readonly] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


