# Employee

# The Employee Object ### Description The `Employee` object is used to represent any person who has been employed by a company.  ### Usage Example Fetch from the `LIST Employee` endpoint and filter by `ID` to show all employees.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**remote_id** | **str, none_type** | The third-party API ID of the matching object. | [optional] 
**employee_number** | **str, none_type** | The employee&#39;s number that appears in the third-party integration&#39;s UI. | [optional] 
**company** | **str, none_type** | The ID of the employee&#39;s company. | [optional] 
**first_name** | **str, none_type** | The employee&#39;s first name. | [optional] 
**last_name** | **str, none_type** | The employee&#39;s last name. | [optional] 
**display_full_name** | **str, none_type** | The employee&#39;s full name, to use for display purposes. If a preferred first name is available, the full name will include the preferred first name. | [optional] 
**username** | **str, none_type** | The employee&#39;s username that appears in the remote UI. | [optional] 
**groups** | **[str, none_type]** |  | [optional] 
**work_email** | **str, none_type** | The employee&#39;s work email. | [optional] 
**personal_email** | **str, none_type** | The employee&#39;s personal email. | [optional] 
**mobile_phone_number** | **str, none_type** | The employee&#39;s mobile phone number. | [optional] 
**employments** | **[str, none_type]** | Array of &#x60;Employment&#x60; IDs for this Employee. | [optional] 
**home_location** | **str, none_type** | The employee&#39;s home address. | [optional] 
**work_location** | **str, none_type** | The employee&#39;s work address. | [optional] 
**manager** | **str, none_type** | The employee ID of the employee&#39;s manager. | [optional] 
**team** | **str, none_type** | The employee&#39;s team. | [optional] 
**pay_group** | **str, none_type** | The employee&#39;s pay group | [optional] 
**ssn** | **str, none_type** | The employee&#39;s social security number. | [optional] 
**gender** | **bool, date, datetime, dict, float, int, list, str, none_type** | The employee&#39;s gender.  * &#x60;MALE&#x60; - MALE * &#x60;FEMALE&#x60; - FEMALE * &#x60;NON-BINARY&#x60; - NON-BINARY * &#x60;OTHER&#x60; - OTHER * &#x60;PREFER_NOT_TO_DISCLOSE&#x60; - PREFER_NOT_TO_DISCLOSE | [optional] 
**ethnicity** | **bool, date, datetime, dict, float, int, list, str, none_type** | The employee&#39;s ethnicity.  * &#x60;AMERICAN_INDIAN_OR_ALASKA_NATIVE&#x60; - AMERICAN_INDIAN_OR_ALASKA_NATIVE * &#x60;ASIAN_OR_INDIAN_SUBCONTINENT&#x60; - ASIAN_OR_INDIAN_SUBCONTINENT * &#x60;BLACK_OR_AFRICAN_AMERICAN&#x60; - BLACK_OR_AFRICAN_AMERICAN * &#x60;HISPANIC_OR_LATINO&#x60; - HISPANIC_OR_LATINO * &#x60;NATIVE_HAWAIIAN_OR_OTHER_PACIFIC_ISLANDER&#x60; - NATIVE_HAWAIIAN_OR_OTHER_PACIFIC_ISLANDER * &#x60;TWO_OR_MORE_RACES&#x60; - TWO_OR_MORE_RACES * &#x60;WHITE&#x60; - WHITE * &#x60;PREFER_NOT_TO_DISCLOSE&#x60; - PREFER_NOT_TO_DISCLOSE | [optional] 
**marital_status** | **bool, date, datetime, dict, float, int, list, str, none_type** | The employee&#39;s filing status as related to marital status.  * &#x60;SINGLE&#x60; - SINGLE * &#x60;MARRIED_FILING_JOINTLY&#x60; - MARRIED_FILING_JOINTLY * &#x60;MARRIED_FILING_SEPARATELY&#x60; - MARRIED_FILING_SEPARATELY * &#x60;HEAD_OF_HOUSEHOLD&#x60; - HEAD_OF_HOUSEHOLD * &#x60;QUALIFYING_WIDOW_OR_WIDOWER_WITH_DEPENDENT_CHILD&#x60; - QUALIFYING_WIDOW_OR_WIDOWER_WITH_DEPENDENT_CHILD | [optional] 
**date_of_birth** | **datetime, none_type** | The employee&#39;s date of birth. | [optional] 
**hire_date** | **datetime, none_type** | The date that the employee was hired, usually the day that an offer letter is signed. If an employee has multiple hire dates from previous employments, this represents the most recent hire date. Note: If you&#39;re looking for the employee&#39;s start date, refer to the start_date field. | [optional] 
**start_date** | **datetime, none_type** | The date that the employee started working. If an employee was rehired, the most recent start date will be returned. | [optional] 
**remote_created_at** | **datetime, none_type** | When the third party&#39;s employee was created. | [optional] 
**employment_status** | **bool, date, datetime, dict, float, int, list, str, none_type** | The employment status of the employee.  * &#x60;ACTIVE&#x60; - ACTIVE * &#x60;PENDING&#x60; - PENDING * &#x60;INACTIVE&#x60; - INACTIVE | [optional] 
**termination_date** | **datetime, none_type** | The employee&#39;s termination date. | [optional] 
**avatar** | **str, none_type** | The URL of the employee&#39;s avatar image. | [optional] 
**custom_fields** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Custom fields configured for a given model. | [optional] 
**remote_was_deleted** | **bool** |  | [optional] [readonly] 
**field_mappings** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] [readonly] 
**modified_at** | **datetime** | This is the datetime that this object was last updated by Merge | [optional] [readonly] 
**remote_data** | [**[RemoteData], none_type**](RemoteData.md) |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

