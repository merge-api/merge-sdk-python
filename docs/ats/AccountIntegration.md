# AccountIntegration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Company name. | 
**categories** | [**[CategoriesEnum]**](CategoriesEnum.md) | Category or categories this integration belongs to. Multiple categories should be comma separated, i.e. [ats, hris]. | [optional] 
**image** | **str, none_type** | Company logo in rectangular shape. &lt;b&gt;Upload an image with a clear background.&lt;/b&gt; | [optional] 
**square_image** | **str, none_type** | Company logo in square shape. &lt;b&gt;Upload an image with a white background.&lt;/b&gt; | [optional] 
**color** | **str** | The color of this integration used for buttons and text throughout the app and landing pages. &lt;b&gt;Choose a darker, saturated color.&lt;/b&gt; | [optional] 
**slug** | **str** |  | [optional] [readonly] 
**is_in_beta** | **bool** | If checked, this integration will not appear in the linking flow, and will appear elsewhere with a Beta tag. | [optional] 
**api_endpoints_to_documentation_urls** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Mapping of API endpoints to documentation urls for support. Example: {&#39;GET&#39;: [[&#39;/common-model-scopes&#39;, &#39;https://docs.merge.dev/accounting/common-model-scopes/#common_model_scopes_retrieve&#39;],[&#39;/common-model-actions&#39;, &#39;https://docs.merge.dev/accounting/common-model-actions/#common_model_actions_retrieve&#39;]], &#39;POST&#39;: []} | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


