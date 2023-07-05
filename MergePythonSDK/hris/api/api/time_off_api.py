"""
    Merge HRIS API

    The unified API for building rich integrations with multiple HR Information System platforms.  # noqa: E501

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
from MergePythonSDK.hris.model.meta_response import MetaResponse
from MergePythonSDK.shared.model.merge_paginated_response import MergePaginatedResponse
from MergePythonSDK.hris.model.time_off import TimeOff
from MergePythonSDK.hris.model.time_off_endpoint_request import TimeOffEndpointRequest
from MergePythonSDK.hris.model.time_off_response import TimeOffResponse


class TimeOffApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.time_off_create_endpoint = _Endpoint(
            settings={
                'response_type': (TimeOffResponse,),
                'auth': [
                    'accountTokenAuth',
                    'bearerAuth'
                ],
                'endpoint_path': '/hris/v1/time-off',
                'operation_id': 'time_off_create',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'time_off_endpoint_request',
                    'is_debug_mode',
                    'run_async',
                ],
                'required': [
                    'time_off_endpoint_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'time_off_endpoint_request':
                        (TimeOffEndpointRequest,),
                    'is_debug_mode':
                        (bool,),
                    'run_async':
                        (bool,),
                },
                'attribute_map': {
                    'is_debug_mode': 'is_debug_mode',
                    'run_async': 'run_async',
                },
                'location_map': {
                    'time_off_endpoint_request': 'body',
                    'is_debug_mode': 'query',
                    'run_async': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json',
                    'application/x-www-form-urlencoded',
                    'multipart/form-data'
                ]
            },
            api_client=api_client
        )
        self.time_off_list_endpoint = _Endpoint(
            settings={
                'response_type': (MergePaginatedResponse(TimeOff),),
                'auth': [
                    'accountTokenAuth',
                    'bearerAuth'
                ],
                'endpoint_path': '/hris/v1/time-off',
                'operation_id': 'time_off_list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'approver_id',
                    'created_after',
                    'created_before',
                    'cursor',
                    'employee_id',
                    'expand',
                    'include_deleted_data',
                    'include_remote_data',
                    'modified_after',
                    'modified_before',
                    'page_size',
                    'remote_fields',
                    'remote_id',
                    'request_type',
                    'show_enum_origins',
                    'status',
                ],
                'required': [],
                'nullable': [
                    'remote_id',
                    'request_type',
                    'status',
                ],
                'enum': [
                    'expand',
                    'remote_fields',
                    'request_type',
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

                        "APPROVER": "approver",
                        "EMPLOYEE": "employee",
                        "EMPLOYEE,APPROVER": "employee,approver"
                    },
                    ('remote_fields',): {

                        "REQUEST_TYPE": "request_type",
                        "REQUEST_TYPE,STATUS": "request_type,status",
                        "REQUEST_TYPE,STATUS,UNITS": "request_type,status,units",
                        "REQUEST_TYPE,UNITS": "request_type,units",
                        "STATUS": "status",
                        "STATUS,UNITS": "status,units",
                        "UNITS": "units"
                    },
                    ('request_type',): {
                        'None': None,
                        "BEREAVEMENT": "BEREAVEMENT",
                        "JURY_DUTY": "JURY_DUTY",
                        "PERSONAL": "PERSONAL",
                        "SICK": "SICK",
                        "VACATION": "VACATION",
                        "VOLUNTEER": "VOLUNTEER"
                    },
                    ('show_enum_origins',): {

                        "REQUEST_TYPE": "request_type",
                        "REQUEST_TYPE,STATUS": "request_type,status",
                        "REQUEST_TYPE,STATUS,UNITS": "request_type,status,units",
                        "REQUEST_TYPE,UNITS": "request_type,units",
                        "STATUS": "status",
                        "STATUS,UNITS": "status,units",
                        "UNITS": "units"
                    },
                    ('status',): {
                        'None': None,
                        "APPROVED": "APPROVED",
                        "CANCELLED": "CANCELLED",
                        "DECLINED": "DECLINED",
                        "DELETED": "DELETED",
                        "REQUESTED": "REQUESTED"
                    },
                },
                'openapi_types': {
                    'approver_id':
                        (str,),
                    'created_after':
                        (datetime,),
                    'created_before':
                        (datetime,),
                    'cursor':
                        (str,),
                    'employee_id':
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
                    'request_type':
                        (str, none_type,),
                    'show_enum_origins':
                        (str,),
                    'status':
                        (str, none_type,),
                },
                'attribute_map': {
                    'approver_id': 'approver_id',
                    'created_after': 'created_after',
                    'created_before': 'created_before',
                    'cursor': 'cursor',
                    'employee_id': 'employee_id',
                    'expand': 'expand',
                    'include_deleted_data': 'include_deleted_data',
                    'include_remote_data': 'include_remote_data',
                    'modified_after': 'modified_after',
                    'modified_before': 'modified_before',
                    'page_size': 'page_size',
                    'remote_fields': 'remote_fields',
                    'remote_id': 'remote_id',
                    'request_type': 'request_type',
                    'show_enum_origins': 'show_enum_origins',
                    'status': 'status',
                },
                'location_map': {
                    'approver_id': 'query',
                    'created_after': 'query',
                    'created_before': 'query',
                    'cursor': 'query',
                    'employee_id': 'query',
                    'expand': 'query',
                    'include_deleted_data': 'query',
                    'include_remote_data': 'query',
                    'modified_after': 'query',
                    'modified_before': 'query',
                    'page_size': 'query',
                    'remote_fields': 'query',
                    'remote_id': 'query',
                    'request_type': 'query',
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
        self.time_off_meta_post_retrieve_endpoint = _Endpoint(
            settings={
                'response_type': (MetaResponse,),
                'auth': [
                    'accountTokenAuth',
                    'bearerAuth'
                ],
                'endpoint_path': '/hris/v1/time-off/meta/post',
                'operation_id': 'time_off_meta_post_retrieve',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                },
                'attribute_map': {
                },
                'location_map': {
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
        self.time_off_retrieve_endpoint = _Endpoint(
            settings={
                'response_type': (TimeOff,),
                'auth': [
                    'accountTokenAuth',
                    'bearerAuth'
                ],
                'endpoint_path': '/hris/v1/time-off/{id}',
                'operation_id': 'time_off_retrieve',
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

                        "APPROVER": "approver",
                        "EMPLOYEE": "employee",
                        "EMPLOYEE,APPROVER": "employee,approver"
                    },
                    ('remote_fields',): {

                        "REQUEST_TYPE": "request_type",
                        "REQUEST_TYPE,STATUS": "request_type,status",
                        "REQUEST_TYPE,STATUS,UNITS": "request_type,status,units",
                        "REQUEST_TYPE,UNITS": "request_type,units",
                        "STATUS": "status",
                        "STATUS,UNITS": "status,units",
                        "UNITS": "units"
                    },
                    ('show_enum_origins',): {

                        "REQUEST_TYPE": "request_type",
                        "REQUEST_TYPE,STATUS": "request_type,status",
                        "REQUEST_TYPE,STATUS,UNITS": "request_type,status,units",
                        "REQUEST_TYPE,UNITS": "request_type,units",
                        "STATUS": "status",
                        "STATUS,UNITS": "status,units",
                        "UNITS": "units"
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

    def time_off_create(
        self,
        time_off_endpoint_request,
        **kwargs
    ) -> "TimeOffResponse":
        """time_off_create  # noqa: E501

        Creates a `TimeOff` object with the given values.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.time_off_create(time_off_endpoint_request, async_req=True)
        >>> result = thread.get()

        Args:
            time_off_endpoint_request (TimeOffEndpointRequest):

        Keyword Args:
            is_debug_mode (bool): Whether to include debug fields (such as log file links) in the response.. [optional]
            run_async (bool): Whether or not third-party updates should be run asynchronously.. [optional]
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
            TimeOffResponse
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
        kwargs['time_off_endpoint_request'] = \
            time_off_endpoint_request
        return self.time_off_create_endpoint.call_with_http_info(**kwargs)

    def time_off_list(
        self,
        **kwargs
    ) -> "MergePaginatedResponse(TimeOff)":
        """time_off_list  # noqa: E501

        Returns a list of `TimeOff` objects.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.time_off_list(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            approver_id (str): If provided, will only return time off for this approver.. [optional]
            created_after (datetime): If provided, will only return objects created after this datetime.. [optional]
            created_before (datetime): If provided, will only return objects created before this datetime.. [optional]
            cursor (str): The pagination cursor value.. [optional]
            employee_id (str): If provided, will only return time off for this employee.. [optional]
            expand (str): Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.. [optional]
            include_deleted_data (bool): Whether to include data that was marked as deleted by third party webhooks.. [optional]
            include_remote_data (bool): Whether to include the original data Merge fetched from the third-party to produce these models.. [optional]
            modified_after (datetime): If provided, only objects synced by Merge after this date time will be returned.. [optional]
            modified_before (datetime): If provided, only objects synced by Merge before this date time will be returned.. [optional]
            page_size (int): Number of results to return per page.. [optional]
            remote_fields (str): Deprecated. Use show_enum_origins.. [optional]
            remote_id (str, none_type): The API provider's ID for the given object.. [optional]
            request_type (str, none_type): If provided, will only return TimeOff with this request type. Options: ('VACATION', 'SICK', 'PERSONAL', 'JURY_DUTY', 'VOLUNTEER', 'BEREAVEMENT')  * `VACATION` - VACATION * `SICK` - SICK * `PERSONAL` - PERSONAL * `JURY_DUTY` - JURY_DUTY * `VOLUNTEER` - VOLUNTEER * `BEREAVEMENT` - BEREAVEMENT. [optional]
            show_enum_origins (str): Which fields should be returned in non-normalized form.. [optional]
            status (str, none_type): If provided, will only return TimeOff with this status. Options: ('REQUESTED', 'APPROVED', 'DECLINED', 'CANCELLED', 'DELETED')  * `REQUESTED` - REQUESTED * `APPROVED` - APPROVED * `DECLINED` - DECLINED * `CANCELLED` - CANCELLED * `DELETED` - DELETED. [optional]
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
            MergePaginatedResponse(TimeOff)
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
        return self.time_off_list_endpoint.call_with_http_info(**kwargs)

    def time_off_meta_post_retrieve(
        self,
        **kwargs
    ) -> "MetaResponse":
        """time_off_meta_post_retrieve  # noqa: E501

        Returns metadata for `TimeOff` POSTs.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.time_off_meta_post_retrieve(async_req=True)
        >>> result = thread.get()


        Keyword Args:
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
            MetaResponse
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
        return self.time_off_meta_post_retrieve_endpoint.call_with_http_info(**kwargs)

    def time_off_retrieve(
        self,
        id,
        **kwargs
    ) -> "TimeOff":
        """time_off_retrieve  # noqa: E501

        Returns a `TimeOff` object with the given `id`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.time_off_retrieve(id, async_req=True)
        >>> result = thread.get()

        Args:
            id (str):

        Keyword Args:
            expand (str): Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.. [optional]
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
            TimeOff
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
        return self.time_off_retrieve_endpoint.call_with_http_info(**kwargs)

