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
from MergePythonSDK.ats.model.job import Job
from MergePythonSDK.shared.model.merge_paginated_response import MergePaginatedResponse


class JobsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.jobs_list_endpoint = _Endpoint(
            settings={
                'response_type': (MergePaginatedResponse(Job),),
                'auth': [
                    'accountTokenAuth',
                    'bearerAuth'
                ],
                'endpoint_path': '/ats/v1/jobs',
                'operation_id': 'jobs_list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'code',
                    'created_after',
                    'created_before',
                    'cursor',
                    'expand',
                    'include_deleted_data',
                    'include_remote_data',
                    'modified_after',
                    'modified_before',
                    'offices',
                    'page_size',
                    'remote_fields',
                    'remote_id',
                    'show_enum_origins',
                    'status',
                ],
                'required': [],
                'nullable': [
                    'code',
                    'remote_id',
                    'status',
                ],
                'enum': [
                    'expand',
                    'remote_fields',
                    'show_enum_origins',
                    'status',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('expand',): {

                        "DEPARTMENTS": "departments",
                        "DEPARTMENTS,HIRING_MANAGERS": "departments,hiring_managers",
                        "DEPARTMENTS,HIRING_MANAGERS,RECRUITERS": "departments,hiring_managers,recruiters",
                        "DEPARTMENTS,OFFICES": "departments,offices",
                        "DEPARTMENTS,OFFICES,HIRING_MANAGERS": "departments,offices,hiring_managers",
                        "DEPARTMENTS,OFFICES,HIRING_MANAGERS,RECRUITERS": "departments,offices,hiring_managers,recruiters",
                        "DEPARTMENTS,OFFICES,RECRUITERS": "departments,offices,recruiters",
                        "DEPARTMENTS,RECRUITERS": "departments,recruiters",
                        "HIRING_MANAGERS": "hiring_managers",
                        "HIRING_MANAGERS,RECRUITERS": "hiring_managers,recruiters",
                        "OFFICES": "offices",
                        "OFFICES,HIRING_MANAGERS": "offices,hiring_managers",
                        "OFFICES,HIRING_MANAGERS,RECRUITERS": "offices,hiring_managers,recruiters",
                        "OFFICES,RECRUITERS": "offices,recruiters",
                        "RECRUITERS": "recruiters"
                    },
                    ('remote_fields',): {

                        "STATUS": "status"
                    },
                    ('show_enum_origins',): {

                        "STATUS": "status"
                    },
                    ('status',): {
                        'None': None,
                        "ARCHIVED": "ARCHIVED",
                        "CLOSED": "CLOSED",
                        "DRAFT": "DRAFT",
                        "OPEN": "OPEN",
                        "PENDING": "PENDING"
                    },
                },
                'openapi_types': {
                    'code':
                        (str, none_type,),
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
                    'offices':
                        (str,),
                    'page_size':
                        (int,),
                    'remote_fields':
                        (str,),
                    'remote_id':
                        (str, none_type,),
                    'show_enum_origins':
                        (str,),
                    'status':
                        (str, none_type,),
                },
                'attribute_map': {
                    'code': 'code',
                    'created_after': 'created_after',
                    'created_before': 'created_before',
                    'cursor': 'cursor',
                    'expand': 'expand',
                    'include_deleted_data': 'include_deleted_data',
                    'include_remote_data': 'include_remote_data',
                    'modified_after': 'modified_after',
                    'modified_before': 'modified_before',
                    'offices': 'offices',
                    'page_size': 'page_size',
                    'remote_fields': 'remote_fields',
                    'remote_id': 'remote_id',
                    'show_enum_origins': 'show_enum_origins',
                    'status': 'status',
                },
                'location_map': {
                    'code': 'query',
                    'created_after': 'query',
                    'created_before': 'query',
                    'cursor': 'query',
                    'expand': 'query',
                    'include_deleted_data': 'query',
                    'include_remote_data': 'query',
                    'modified_after': 'query',
                    'modified_before': 'query',
                    'offices': 'query',
                    'page_size': 'query',
                    'remote_fields': 'query',
                    'remote_id': 'query',
                    'show_enum_origins': 'query',
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
        self.jobs_retrieve_endpoint = _Endpoint(
            settings={
                'response_type': (Job,),
                'auth': [
                    'accountTokenAuth',
                    'bearerAuth'
                ],
                'endpoint_path': '/ats/v1/jobs/{id}',
                'operation_id': 'jobs_retrieve',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'expand',
                    'include_remote_data',
                    'remote_fields',
                    'show_enum_origins',
                ],
                'required': [
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

                        "DEPARTMENTS": "departments",
                        "DEPARTMENTS,HIRING_MANAGERS": "departments,hiring_managers",
                        "DEPARTMENTS,HIRING_MANAGERS,RECRUITERS": "departments,hiring_managers,recruiters",
                        "DEPARTMENTS,OFFICES": "departments,offices",
                        "DEPARTMENTS,OFFICES,HIRING_MANAGERS": "departments,offices,hiring_managers",
                        "DEPARTMENTS,OFFICES,HIRING_MANAGERS,RECRUITERS": "departments,offices,hiring_managers,recruiters",
                        "DEPARTMENTS,OFFICES,RECRUITERS": "departments,offices,recruiters",
                        "DEPARTMENTS,RECRUITERS": "departments,recruiters",
                        "HIRING_MANAGERS": "hiring_managers",
                        "HIRING_MANAGERS,RECRUITERS": "hiring_managers,recruiters",
                        "OFFICES": "offices",
                        "OFFICES,HIRING_MANAGERS": "offices,hiring_managers",
                        "OFFICES,HIRING_MANAGERS,RECRUITERS": "offices,hiring_managers,recruiters",
                        "OFFICES,RECRUITERS": "offices,recruiters",
                        "RECRUITERS": "recruiters"
                    },
                    ('remote_fields',): {

                        "STATUS": "status"
                    },
                    ('show_enum_origins',): {

                        "STATUS": "status"
                    },
                },
                'openapi_types': {
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
                    'id': 'id',
                    'expand': 'expand',
                    'include_remote_data': 'include_remote_data',
                    'remote_fields': 'remote_fields',
                    'show_enum_origins': 'show_enum_origins',
                },
                'location_map': {
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

    def jobs_list(
        self,
        **kwargs
    ) -> "MergePaginatedResponse(Job)":
        """jobs_list  # noqa: E501

        Returns a list of `Job` objects.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.jobs_list(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            code (str, none_type): If provided, will only return jobs with this code.. [optional]
            created_after (datetime): If provided, will only return objects created after this datetime.. [optional]
            created_before (datetime): If provided, will only return objects created before this datetime.. [optional]
            cursor (str): The pagination cursor value.. [optional]
            expand (str): Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.. [optional]
            include_deleted_data (bool): Whether to include data that was marked as deleted by third party webhooks.. [optional]
            include_remote_data (bool): Whether to include the original data Merge fetched from the third-party to produce these models.. [optional]
            modified_after (datetime): If provided, only objects synced by Merge after this date time will be returned.. [optional]
            modified_before (datetime): If provided, only objects synced by Merge before this date time will be returned.. [optional]
            offices (str): If provided, will only return jobs for this office; multiple offices can be separated by commas.. [optional]
            page_size (int): Number of results to return per page.. [optional]
            remote_fields (str): Deprecated. Use show_enum_origins.. [optional] if omitted the server will use the default value of "status"
            remote_id (str, none_type): The API provider's ID for the given object.. [optional]
            show_enum_origins (str): Which fields should be returned in non-normalized form.. [optional] if omitted the server will use the default value of "status"
            status (str, none_type): If provided, will only return jobs with this status. Options: ('OPEN', 'CLOSED', 'DRAFT', 'ARCHIVED', 'PENDING')  * `OPEN` - OPEN * `CLOSED` - CLOSED * `DRAFT` - DRAFT * `ARCHIVED` - ARCHIVED * `PENDING` - PENDING. [optional]
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
            MergePaginatedResponse(Job)
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
        return self.jobs_list_endpoint.call_with_http_info(**kwargs)

    def jobs_retrieve(
        self,
        id,
        **kwargs
    ) -> "Job":
        """jobs_retrieve  # noqa: E501

        Returns a `Job` object with the given `id`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.jobs_retrieve(id, async_req=True)
        >>> result = thread.get()

        Args:
            id (str):

        Keyword Args:
            expand (str): Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.. [optional]
            include_remote_data (bool): Whether to include the original data Merge fetched from the third-party to produce these models.. [optional]
            remote_fields (str): Deprecated. Use show_enum_origins.. [optional] if omitted the server will use the default value of "status"
            show_enum_origins (str): Which fields should be returned in non-normalized form.. [optional] if omitted the server will use the default value of "status"
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
            Job
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
        kwargs['id'] = \
            id
        return self.jobs_retrieve_endpoint.call_with_http_info(**kwargs)
