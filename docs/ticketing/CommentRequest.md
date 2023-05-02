# CommentRequest

# The Comment Object ### Description The `Comment` object is used to represent a comment on a ticket.  ### Usage Example TODO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str, none_type** | The author of the Comment, if the author is a User. | [optional] 
**contact** | **str, none_type** | The author of the Comment, if the author is a Contact. | [optional] 
**body** | **str, none_type** | The comment&#39;s text body. | [optional] 
**html_body** | **str, none_type** | The comment&#39;s text body formatted as html. | [optional] 
**ticket** | **str, none_type** | The ticket associated with the comment.  | [optional] 
**is_private** | **bool, none_type** | Whether or not the comment is internal. | [optional] 
**integration_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 
**linked_account_params** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


