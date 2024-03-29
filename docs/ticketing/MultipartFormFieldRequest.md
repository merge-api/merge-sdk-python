# MultipartFormFieldRequest

# The MultipartFormField Object ### Description The `MultipartFormField` object is used to represent fields in an HTTP request using `multipart/form-data`. ### Usage Example Create a `MultipartFormField` to define a multipart form entry.

## Properties

| Name                | Type                                             | Description                                                                                                                                                                               | Notes      |
| ------------------- | ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **name**            | **str**                                          | The name of the form field                                                                                                                                                                |
| **data**            | **str**                                          | The data for the form field.                                                                                                                                                              |
| **encoding**        | **bool, dict, float, int, list, str, none_type** | The encoding of the value of &#x60;data&#x60;. Defaults to &#x60;RAW&#x60; if not defined. _ &#x60;RAW&#x60; - RAW _ &#x60;BASE64&#x60; - BASE64 \* &#x60;GZIP_BASE64&#x60; - GZIP_BASE64 | [optional] |
| **file_name**       | **str, none_type**                               | The file name of the form field, if the field is for a file.                                                                                                                              | [optional] |
| **content_type**    | **str, none_type**                               | The MIME type of the file, if the field is for a file.                                                                                                                                    | [optional] |
| **any string name** | **bool, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type                                                                                                                        | [optional] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
