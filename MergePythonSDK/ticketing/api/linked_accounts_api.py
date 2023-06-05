"""
    Merge Ticketing API

    The unified API for building rich integrations with multiple Ticketing platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from MergePythonSDK.shared.api_client import ApiClient, Endpoint as _Endpoint
from MergePythonSDK.shared.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from MergePythonSDK.shared.model.merge_paginated_response import MergePaginatedResponse
from MergePythonSDK.ticketing.model.account_details_and_actions import AccountDetailsAndActions


class LinkedAccountsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.linked_accounts_list_endpoint = _Endpoint(
            settings={
                'response_type': (MergePaginatedResponse(AccountDetailsAndActions),),
                'auth': [
                    'tokenAuth'
                ],
                'endpoint_path': '/ticketing/v1/linked-accounts',
                'operation_id': 'linked_accounts_list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'category',
                    'cursor',
                    'end_user_email_address',
                    'end_user_organization_name',
                    'end_user_origin_id',
                    'end_user_origin_ids',
                    'id',
                    'ids',
                    'include_duplicates',
                    'integration_name',
                    'is_test_account',
                    'page_size',
                    'status',
                ],
                'required': [],
                'nullable': [
                    'category',
                ],
                'enum': [
                    'category',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('category',): {
                        'None': None,
                        "ACCOUNTING": "accounting",
                        "ATS": "ats",
                        "CRM": "crm",
                        "FILESTORAGE": "filestorage",
                        "HRIS": "hris",
                        "MKTG": "mktg",
                        "TICKETING": "ticketing"
                    },
                },
                'openapi_types': {
                    'category':
                        (str, none_type,),
                    'cursor':
                        (str,),
                    'end_user_email_address':
                        (str,),
                    'end_user_organization_name':
                        (str,),
                    'end_user_origin_id':
                        (str,),
                    'end_user_origin_ids':
                        (str,),
                    'id':
                        (str,),
                    'ids':
                        (str,),
                    'include_duplicates':
                        (bool,),
                    'integration_name':
                        (str,),
                    'is_test_account':
                        (str,),
                    'page_size':
                        (int,),
                    'status':
                        (str,),
                },
                'attribute_map': {
                    'category': 'category',
                    'cursor': 'cursor',
                    'end_user_email_address': 'end_user_email_address',
                    'end_user_organization_name': 'end_user_organization_name',
                    'end_user_origin_id': 'end_user_origin_id',
                    'end_user_origin_ids': 'end_user_origin_ids',
                    'id': 'id',
                    'ids': 'ids',
                    'include_duplicates': 'include_duplicates',
                    'integration_name': 'integration_name',
                    'is_test_account': 'is_test_account',
                    'page_size': 'page_size',
                    'status': 'status',
                },
                'location_map': {
                    'category': 'query',
                    'cursor': 'query',
                    'end_user_email_address': 'query',
                    'end_user_organization_name': 'query',
                    'end_user_origin_id': 'query',
                    'end_user_origin_ids': 'query',
                    'id': 'query',
                    'ids': 'query',
                    'include_duplicates': 'query',
                    'integration_name': 'query',
                    'is_test_account': 'query',
                    'page_size': 'query',
                    'status': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def linked_accounts_list(
        self,
        **kwargs
    ) -> "MergePaginatedResponse(AccountDetailsAndActions)":
        """linked_accounts_list  # noqa: E501

        List linked accounts for your organization.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.linked_accounts_list(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            category (str, none_type): Options: ('hris', 'ats', 'accounting', 'ticketing', 'crm', 'mktg', 'filestorage')  * `hris` - hris * `ats` - ats * `accounting` - accounting * `ticketing` - ticketing * `crm` - crm * `mktg` - mktg * `filestorage` - filestorage. [optional]
            cursor (str): The pagination cursor value.. [optional]
            end_user_email_address (str): If provided, will only return linked accounts associated with the given email address.. [optional]
            end_user_organization_name (str): If provided, will only return linked accounts associated with the given organization name.. [optional]
            end_user_origin_id (str): If provided, will only return linked accounts associated with the given origin ID.. [optional]
            end_user_origin_ids (str): Comma-separated list of EndUser origin IDs, making it possible to specify multiple EndUsers at once.. [optional]
            id (str): [optional]
            ids (str): Comma-separated list of LinkedAccount IDs, making it possible to specify multiple LinkedAccounts at once.. [optional]
            include_duplicates (bool): If `true`, will include complete production duplicates of the account specified by the `id` query parameter in the response. `id` must be for a complete production linked account.. [optional]
            integration_name (str): If provided, will only return linked accounts associated with the given integration name.. [optional]
            is_test_account (str): If included, will only include test linked accounts. If not included, will only include non-test linked accounts.. [optional]
            page_size (int): Number of results to return per page.. [optional]
            status (str): Filter by status. Options: `COMPLETE`, `INCOMPLETE`, `RELINK_NEEDED`. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            MergePaginatedResponse(AccountDetailsAndActions)
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.linked_accounts_list_endpoint.call_with_http_info(**kwargs)

