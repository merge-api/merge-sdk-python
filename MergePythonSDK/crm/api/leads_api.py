"""
    Merge CRM API

    The unified API for building rich integrations with multiple CRM platforms.  # noqa: E501

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
from MergePythonSDK.crm.model.lead import Lead
from MergePythonSDK.crm.model.lead_endpoint_request import LeadEndpointRequest
from MergePythonSDK.crm.model.lead_response import LeadResponse
from MergePythonSDK.crm.model.meta_response import MetaResponse
from MergePythonSDK.shared.model.merge_paginated_response import MergePaginatedResponse
from MergePythonSDK.crm.model.remote_field_class import RemoteFieldClass


class LeadsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.leads_create_endpoint = _Endpoint(
            settings={
                'response_type': (LeadResponse,),
                'auth': [
                    'tokenAuth'
                ],
                'endpoint_path': '/crm/v1/leads',
                'operation_id': 'leads_create',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_account_token',
                    'lead_endpoint_request',
                    'is_debug_mode',
                    'run_async',
                ],
                'required': [
                    'x_account_token',
                    'lead_endpoint_request',
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
                    'x_account_token':
                        (str,),
                    'lead_endpoint_request':
                        (LeadEndpointRequest,),
                    'is_debug_mode':
                        (bool,),
                    'run_async':
                        (bool,),
                },
                'attribute_map': {
                    'x_account_token': 'X-Account-Token',
                    'is_debug_mode': 'is_debug_mode',
                    'run_async': 'run_async',
                },
                'location_map': {
                    'x_account_token': 'header',
                    'lead_endpoint_request': 'body',
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
        self.leads_list_endpoint = _Endpoint(
            settings={
                'response_type': (MergePaginatedResponse(Lead),),
                'auth': [
                    'tokenAuth'
                ],
                'endpoint_path': '/crm/v1/leads',
                'operation_id': 'leads_list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_account_token',
                    'converted_account_id',
                    'converted_contact_id',
                    'created_after',
                    'created_before',
                    'cursor',
                    'expand',
                    'include_deleted_data',
                    'include_remote_data',
                    'include_remote_fields',
                    'modified_after',
                    'modified_before',
                    'owner_id',
                    'page_size',
                    'remote_id',
                ],
                'required': [
                    'x_account_token',
                ],
                'nullable': [
                    'remote_id',
                ],
                'enum': [
                    'expand',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('expand',): {

                        "CONVERTED_ACCOUNT": "converted_account",
                        "CONVERTED_CONTACT": "converted_contact",
                        "CONVERTED_CONTACT,CONVERTED_ACCOUNT": "converted_contact,converted_account",
                        "OWNER": "owner",
                        "OWNER,CONVERTED_ACCOUNT": "owner,converted_account",
                        "OWNER,CONVERTED_CONTACT": "owner,converted_contact",
                        "OWNER,CONVERTED_CONTACT,CONVERTED_ACCOUNT": "owner,converted_contact,converted_account"
                    },
                },
                'openapi_types': {
                    'x_account_token':
                        (str,),
                    'converted_account_id':
                        (str,),
                    'converted_contact_id':
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
                    'include_remote_fields':
                        (bool,),
                    'modified_after':
                        (datetime,),
                    'modified_before':
                        (datetime,),
                    'owner_id':
                        (str,),
                    'page_size':
                        (int,),
                    'remote_id':
                        (str, none_type,),
                },
                'attribute_map': {
                    'x_account_token': 'X-Account-Token',
                    'converted_account_id': 'converted_account_id',
                    'converted_contact_id': 'converted_contact_id',
                    'created_after': 'created_after',
                    'created_before': 'created_before',
                    'cursor': 'cursor',
                    'expand': 'expand',
                    'include_deleted_data': 'include_deleted_data',
                    'include_remote_data': 'include_remote_data',
                    'include_remote_fields': 'include_remote_fields',
                    'modified_after': 'modified_after',
                    'modified_before': 'modified_before',
                    'owner_id': 'owner_id',
                    'page_size': 'page_size',
                    'remote_id': 'remote_id',
                },
                'location_map': {
                    'x_account_token': 'header',
                    'converted_account_id': 'query',
                    'converted_contact_id': 'query',
                    'created_after': 'query',
                    'created_before': 'query',
                    'cursor': 'query',
                    'expand': 'query',
                    'include_deleted_data': 'query',
                    'include_remote_data': 'query',
                    'include_remote_fields': 'query',
                    'modified_after': 'query',
                    'modified_before': 'query',
                    'owner_id': 'query',
                    'page_size': 'query',
                    'remote_id': 'query',
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
        self.leads_meta_post_retrieve_endpoint = _Endpoint(
            settings={
                'response_type': (MetaResponse,),
                'auth': [
                    'tokenAuth'
                ],
                'endpoint_path': '/crm/v1/leads/meta/post',
                'operation_id': 'leads_meta_post_retrieve',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_account_token',
                ],
                'required': [
                    'x_account_token',
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
                    'x_account_token':
                        (str,),
                },
                'attribute_map': {
                    'x_account_token': 'X-Account-Token',
                },
                'location_map': {
                    'x_account_token': 'header',
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
        self.leads_remote_field_classes_list_endpoint = _Endpoint(
            settings={
                'response_type': (MergePaginatedResponse(RemoteFieldClass),),
                'auth': [
                    'tokenAuth'
                ],
                'endpoint_path': '/crm/v1/leads/remote-field-classes',
                'operation_id': 'leads_remote_field_classes_list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_account_token',
                    'cursor',
                    'include_deleted_data',
                    'include_remote_data',
                    'include_remote_fields',
                    'page_size',
                ],
                'required': [
                    'x_account_token',
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
                    'x_account_token':
                        (str,),
                    'cursor':
                        (str,),
                    'include_deleted_data':
                        (bool,),
                    'include_remote_data':
                        (bool,),
                    'include_remote_fields':
                        (bool,),
                    'page_size':
                        (int,),
                },
                'attribute_map': {
                    'x_account_token': 'X-Account-Token',
                    'cursor': 'cursor',
                    'include_deleted_data': 'include_deleted_data',
                    'include_remote_data': 'include_remote_data',
                    'include_remote_fields': 'include_remote_fields',
                    'page_size': 'page_size',
                },
                'location_map': {
                    'x_account_token': 'header',
                    'cursor': 'query',
                    'include_deleted_data': 'query',
                    'include_remote_data': 'query',
                    'include_remote_fields': 'query',
                    'page_size': 'query',
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
        self.leads_retrieve_endpoint = _Endpoint(
            settings={
                'response_type': (Lead,),
                'auth': [
                    'tokenAuth'
                ],
                'endpoint_path': '/crm/v1/leads/{id}',
                'operation_id': 'leads_retrieve',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_account_token',
                    'id',
                    'expand',
                    'include_remote_data',
                    'include_remote_fields',
                ],
                'required': [
                    'x_account_token',
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                    'expand',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('expand',): {

                        "CONVERTED_ACCOUNT": "converted_account",
                        "CONVERTED_CONTACT": "converted_contact",
                        "CONVERTED_CONTACT,CONVERTED_ACCOUNT": "converted_contact,converted_account",
                        "OWNER": "owner",
                        "OWNER,CONVERTED_ACCOUNT": "owner,converted_account",
                        "OWNER,CONVERTED_CONTACT": "owner,converted_contact",
                        "OWNER,CONVERTED_CONTACT,CONVERTED_ACCOUNT": "owner,converted_contact,converted_account"
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
                    'include_remote_fields':
                        (bool,),
                },
                'attribute_map': {
                    'x_account_token': 'X-Account-Token',
                    'id': 'id',
                    'expand': 'expand',
                    'include_remote_data': 'include_remote_data',
                    'include_remote_fields': 'include_remote_fields',
                },
                'location_map': {
                    'x_account_token': 'header',
                    'id': 'path',
                    'expand': 'query',
                    'include_remote_data': 'query',
                    'include_remote_fields': 'query',
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

    def leads_create(
        self,
        x_account_token,
        lead_endpoint_request,
        **kwargs
    ) -> "LeadResponse":
        """leads_create  # noqa: E501

        Creates a `Lead` object with the given values.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_create(x_account_token, lead_endpoint_request, async_req=True)
        >>> result = thread.get()

        Args:
            x_account_token (str): Token identifying the end user.
            lead_endpoint_request (LeadEndpointRequest):

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
            LeadResponse
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
        kwargs['lead_endpoint_request'] = \
            lead_endpoint_request
        return self.leads_create_endpoint.call_with_http_info(**kwargs)

    def leads_list(
        self,
        x_account_token,
        **kwargs
    ) -> "MergePaginatedResponse(Lead)":
        """leads_list  # noqa: E501

        Returns a list of `Lead` objects.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_list(x_account_token, async_req=True)
        >>> result = thread.get()

        Args:
            x_account_token (str): Token identifying the end user.

        Keyword Args:
            converted_account_id (str): If provided, will only return leads with this account.. [optional]
            converted_contact_id (str): If provided, will only return leads with this contact.. [optional]
            created_after (datetime): If provided, will only return objects created after this datetime.. [optional]
            created_before (datetime): If provided, will only return objects created before this datetime.. [optional]
            cursor (str): The pagination cursor value.. [optional]
            expand (str): Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.. [optional]
            include_deleted_data (bool): Whether to include data that was marked as deleted by third party webhooks.. [optional]
            include_remote_data (bool): Whether to include the original data Merge fetched from the third-party to produce these models.. [optional]
            include_remote_fields (bool): Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.. [optional]
            modified_after (datetime): If provided, only objects synced by Merge after this date time will be returned.. [optional]
            modified_before (datetime): If provided, only objects synced by Merge before this date time will be returned.. [optional]
            owner_id (str): If provided, will only return leads with this owner.. [optional]
            page_size (int): Number of results to return per page.. [optional]
            remote_id (str, none_type): The API provider's ID for the given object.. [optional]
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
            MergePaginatedResponse(Lead)
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
        return self.leads_list_endpoint.call_with_http_info(**kwargs)

    def leads_meta_post_retrieve(
        self,
        x_account_token,
        **kwargs
    ) -> "MetaResponse":
        """leads_meta_post_retrieve  # noqa: E501

        Returns metadata for `Lead` POSTs.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_meta_post_retrieve(x_account_token, async_req=True)
        >>> result = thread.get()

        Args:
            x_account_token (str): Token identifying the end user.

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
        kwargs['x_account_token'] = \
            x_account_token
        return self.leads_meta_post_retrieve_endpoint.call_with_http_info(**kwargs)

    def leads_remote_field_classes_list(
        self,
        x_account_token,
        **kwargs
    ) -> "MergePaginatedResponse(RemoteFieldClass)":
        """leads_remote_field_classes_list  # noqa: E501

        Returns a list of `RemoteFieldClass` objects.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_remote_field_classes_list(x_account_token, async_req=True)
        >>> result = thread.get()

        Args:
            x_account_token (str): Token identifying the end user.

        Keyword Args:
            cursor (str): The pagination cursor value.. [optional]
            include_deleted_data (bool): Whether to include data that was marked as deleted by third party webhooks.. [optional]
            include_remote_data (bool): Whether to include the original data Merge fetched from the third-party to produce these models.. [optional]
            include_remote_fields (bool): Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.. [optional]
            page_size (int): Number of results to return per page.. [optional]
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
            MergePaginatedResponse(RemoteFieldClass)
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
        return self.leads_remote_field_classes_list_endpoint.call_with_http_info(**kwargs)

    def leads_retrieve(
        self,
        x_account_token,
        id,
        **kwargs
    ) -> "Lead":
        """leads_retrieve  # noqa: E501

        Returns a `Lead` object with the given `id`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.leads_retrieve(x_account_token, id, async_req=True)
        >>> result = thread.get()

        Args:
            x_account_token (str): Token identifying the end user.
            id (str):

        Keyword Args:
            expand (str): Which relations should be returned in expanded form. Multiple relation names should be comma separated without spaces.. [optional]
            include_remote_data (bool): Whether to include the original data Merge fetched from the third-party to produce these models.. [optional]
            include_remote_fields (bool): Whether to include all remote fields, including fields that Merge did not map to common models, in a normalized format.. [optional]
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
            Lead
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
        return self.leads_retrieve_endpoint.call_with_http_info(**kwargs)

