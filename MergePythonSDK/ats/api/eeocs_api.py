"""
    Merge ATS API

    The unified API for building rich integrations with multiple Applicant Tracking System platforms.  # noqa: E501

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
from MergePythonSDK.ats.model.eeoc import EEOC
from MergePythonSDK.shared.model.merge_paginated_response import MergePaginatedResponse


class EeocsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.eeocs_list_endpoint = _Endpoint(
            settings={
                'response_type': (MergePaginatedResponse(EEOC),),
                'auth': [
                    'tokenAuth'
                ],
                'endpoint_path': '/ats/v1/eeocs',
                'operation_id': 'eeocs_list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_account_token',
                    'candidate_id',
                    'created_after',
                    'created_before',
                    'cursor',
                    'expand',
                    'include_deleted_data',
                    'include_remote_data',
                    'modified_after',
                    'modified_before',
                    'page_size',
                    'remote_fields',
                    'remote_id',
                    'show_enum_origins',
                ],
                'required': [
                    'x_account_token',
                ],
                'nullable': [
                    'remote_id',
                ],
                'enum': [
                    'expand',
                    'remote_fields',
                    'show_enum_origins',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('expand',): {

                        "CANDIDATE": "candidate"
                    },
                    ('remote_fields',): {

                        "DISABILITY_STATUS": "disability_status",
                        "DISABILITY_STATUS,GENDER": "disability_status,gender",
                        "DISABILITY_STATUS,GENDER,RACE": "disability_status,gender,race",
                        "DISABILITY_STATUS,GENDER,RACE,VETERAN_STATUS": "disability_status,gender,race,veteran_status",
                        "DISABILITY_STATUS,GENDER,VETERAN_STATUS": "disability_status,gender,veteran_status",
                        "DISABILITY_STATUS,RACE": "disability_status,race",
                        "DISABILITY_STATUS,RACE,VETERAN_STATUS": "disability_status,race,veteran_status",
                        "DISABILITY_STATUS,VETERAN_STATUS": "disability_status,veteran_status",
                        "GENDER": "gender",
                        "GENDER,RACE": "gender,race",
                        "GENDER,RACE,VETERAN_STATUS": "gender,race,veteran_status",
                        "GENDER,VETERAN_STATUS": "gender,veteran_status",
                        "RACE": "race",
                        "RACE,VETERAN_STATUS": "race,veteran_status",
                        "VETERAN_STATUS": "veteran_status"
                    },
                    ('show_enum_origins',): {

                        "DISABILITY_STATUS": "disability_status",
                        "DISABILITY_STATUS,GENDER": "disability_status,gender",
                        "DISABILITY_STATUS,GENDER,RACE": "disability_status,gender,race",
                        "DISABILITY_STATUS,GENDER,RACE,VETERAN_STATUS": "disability_status,gender,race,veteran_status",
                        "DISABILITY_STATUS,GENDER,VETERAN_STATUS": "disability_status,gender,veteran_status",
                        "DISABILITY_STATUS,RACE": "disability_status,race",
                        "DISABILITY_STATUS,RACE,VETERAN_STATUS": "disability_status,race,veteran_status",
                        "DISABILITY_STATUS,VETERAN_STATUS": "disability_status,veteran_status",
                        "GENDER": "gender",
                        "GENDER,RACE": "gender,race",
                        "GENDER,RACE,VETERAN_STATUS": "gender,race,veteran_status",
                        "GENDER,VETERAN_STATUS": "gender,veteran_status",
                        "RACE": "race",
                        "RACE,VETERAN_STATUS": "race,veteran_status",
                        "VETERAN_STATUS": "veteran_status"
                    },
                },
                'openapi_types': {
                    'x_account_token':
                        (str,),
                    'candidate_id':
                        (str,),
                    'created_after':
                        (datetime,),
                    'created_before':
                        (datetime,),
                    'cursor':
                        (str,),
                    'expand':
                        (str,),
                    'include_deleted_data':
                        (bool,),
                    'include_remote_data':
                        (bool,),
                    'modified_after':
                        (datetime,),
                    'modified_before':
                        (datetime,),
                    'page_size':
                        (int,),
                    'remote_fields':
                        (str,),
                    'remote_id':
                        (str, none_type,),
                    'show_enum_origins':
                        (str,),
                },
                'attribute_map': {
                    'x_account_token': 'X-Account-Token',
                    'candidate_id': 'candidate_id',
                    'created_after': 'created_after',
                    'created_before': 'created_before',
                    'cursor': 'cursor',
                    'expand': 'expand',
                    'include_deleted_data': 'include_deleted_data',
                    'include_remote_data': 'include_remote_data',
                    'modified_after': 'modified_after',
                    'modified_before': 'modified_before',
                    'page_size': 'page_size',
                    'remote_fields': 'remote_fields',
                    'remote_id': 'remote_id',
                    'show_enum_origins': 'show_enum_origins',
                },
                'location_map': {
                    'x_account_token': 'header',
                    'candidate_id': 'query',
                    'created_after': 'query',
                    'created_before': 'query',
                    'cursor': 'query',
                    'expand': 'query',
                    'include_deleted_data': 'query',
                    'include_remote_data': 'query',
                    'modified_after': 'query',
                    'modified_before': 'query',
                    'page_size': 'query',
                    'remote_fields': 'query',
                    'remote_id': 'query',
                    'show_enum_origins': 'query',
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
        self.eeocs_retrieve_endpoint = _Endpoint(
            settings={
                'response_type': (EEOC,),
                'auth': [
                    'tokenAuth'
                ],
                'endpoint_path': '/ats/v1/eeocs/{id}',
                'operation_id': 'eeocs_retrieve',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_account_token',
                    'id',
                    'expand',
                    'include_remote_data',
                    'remote_fields',
                    'show_enum_origins',
                ],
                'required': [
                    'x_account_token',
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                    'expand',
                    'remote_fields',
                    'show_enum_origins',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('expand',): {

                        "CANDIDATE": "candidate"
                    },
                    ('remote_fields',): {

                        "DISABILITY_STATUS": "disability_status",
                        "DISABILITY_STATUS,GENDER": "disability_status,gender",
                        "DISABILITY_STATUS,GENDER,RACE": "disability_status,gender,race",
                        "DISABILITY_STATUS,GENDER,RACE,VETERAN_STATUS": "disability_status,gender,race,veteran_status",
                        "DISABILITY_STATUS,GENDER,VETERAN_STATUS": "disability_status,gender,veteran_status",
                        "DISABILITY_STATUS,RACE": "disability_status,race",
                        "DISABILITY_STATUS,RACE,VETERAN_STATUS": "disability_status,race,veteran_status",
                        "DISABILITY_STATUS,VETERAN_STATUS": "disability_status,veteran_status",
                        "GENDER": "gender",
                        "GENDER,RACE": "gender,race",
                        "GENDER,RACE,VETERAN_STATUS": "gender,race,veteran_status",
                        "GENDER,VETERAN_STATUS": "gender,veteran_status",
                        "RACE": "race",
                        "RACE,VETERAN_STATUS": "race,veteran_status",
                        "VETERAN_STATUS": "veteran_status"
                    },
                    ('show_enum_origins',): {

                        "DISABILITY_STATUS": "disability_status",
                        "DISABILITY_STATUS,GENDER": "disability_status,gender",
                        "DISABILITY_STATUS,GENDER,RACE": "disability_status,gender,race",
                        "DISABILITY_STATUS,GENDER,RACE,VETERAN_STATUS": "disability_status,gender,race,veteran_status",
                        "DISABILITY_STATUS,GENDER,VETERAN_STATUS": "disability_status,gender,veteran_status",
                        "DISABILITY_STATUS,RACE": "disability_status,race",
                        "DISABILITY_STATUS,RACE,VETERAN_STATUS": "disability_status,race,veteran_status",
                        "DISABILITY_STATUS,VETERAN_STATUS": "disability_status,veteran_status",
                        "GENDER": "gender",
                        "GENDER,RACE": "gender,race",
                        "GENDER,RACE,VETERAN_STATUS": "gender,race,veteran_status",
                        "GENDER,VETERAN_STATUS": "gender,veteran_status",
                        "RACE": "race",
                        "RACE,VETERAN_STATUS": "race,veteran_status",
                        "VETERAN_STATUS": "veteran_status"
                    },
                },
                'openapi_types': {
                    'x_account_token':
                        (str,),
                    'id':
                        (str,),
                    'expand':
                        (str,),
                    'include_remote_data':
                        (bool,),
                    'remote_fields':
                        (str,),
                    'show_enum_origins':
                        (str,),
                },
                'attribute_map': {
                    'x_account_token': 'X-Account-Token',
                    'id': 'id',
                    'expand': 'expand',
                    'include_remote_data': 'include_remote_data',
                    'remote_fields': 'remote_fields',
                    'show_enum_origins': 'show_enum_origins',
                },
                'location_map': {
                    'x_account_token': 'header',
                    'id': 'path',
                    'expand': 'query',
                    'include_remote_data': 'query',
                    'remote_fields': 'query',
                    'show_enum_origins': 'query',
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

    def eeocs_list(
        self,
        x_account_token,
        **kwargs
    ) -> "MergePaginatedResponse(EEOC)":
        """eeocs_list  # noqa: E501

        Returns a list of `EEOC` objects.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.eeocs_list(x_account_token, async_req=True)
        >>> result = thread.get()

        Args:
            x_account_token (str): Token identifying the end user.

        Keyword Args:
            candidate_id (str): If provided, will only return EEOC info for this candidate.. [optional]
            created_after (datetime): If provided, will only return objects created after this datetime.. [optional]
            created_before (datetime): If provided, will only return objects created before this datetime.. [optional]
            cursor (str): The pagination cursor value.. [optional]
            expand (str): Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.. [optional] if omitted the server will use the default value of "candidate"
            include_deleted_data (bool): Whether to include data that was marked as deleted by third party webhooks.. [optional]
            include_remote_data (bool): Whether to include the original data Merge fetched from the third-party to produce these models.. [optional]
            modified_after (datetime): If provided, only objects synced by Merge after this date time will be returned.. [optional]
            modified_before (datetime): If provided, only objects synced by Merge before this date time will be returned.. [optional]
            page_size (int): Number of results to return per page.. [optional]
            remote_fields (str): Deprecated. Use show_enum_origins.. [optional]
            remote_id (str, none_type): The API provider's ID for the given object.. [optional]
            show_enum_origins (str): Which fields should be returned in non-normalized form.. [optional]
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
            MergePaginatedResponse(EEOC)
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
        kwargs['x_account_token'] = \
            x_account_token
        return self.eeocs_list_endpoint.call_with_http_info(**kwargs)

    def eeocs_retrieve(
        self,
        x_account_token,
        id,
        **kwargs
    ) -> "EEOC":
        """eeocs_retrieve  # noqa: E501

        Returns an `EEOC` object with the given `id`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.eeocs_retrieve(x_account_token, id, async_req=True)
        >>> result = thread.get()

        Args:
            x_account_token (str): Token identifying the end user.
            id (str):

        Keyword Args:
            expand (str): Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.. [optional] if omitted the server will use the default value of "candidate"
            include_remote_data (bool): Whether to include the original data Merge fetched from the third-party to produce these models.. [optional]
            remote_fields (str): Deprecated. Use show_enum_origins.. [optional]
            show_enum_origins (str): Which fields should be returned in non-normalized form.. [optional]
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
            EEOC
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
        kwargs['x_account_token'] = \
            x_account_token
        kwargs['id'] = \
            id
        return self.eeocs_retrieve_endpoint.call_with_http_info(**kwargs)

