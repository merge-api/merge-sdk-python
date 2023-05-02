"""
    Merge Ticketing API

    The unified API for building rich integrations with multiple Ticketing platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from typing import (
    Optional,
    Union,
    List,
    Dict,
)

from MergePythonSDK.shared.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    OpenApiModel,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from MergePythonSDK.shared.exceptions import ApiAttributeError
from MergePythonSDK.shared.model_utils import import_model_by_name


def lazy_import():
    from MergePythonSDK.ticketing.model.method_enum import MethodEnum
    from MergePythonSDK.ticketing.model.multipart_form_field_request import MultipartFormFieldRequest
    from MergePythonSDK.ticketing.model.request_format_enum import RequestFormatEnum
    globals()['MethodEnum'] = MethodEnum
    globals()['MultipartFormFieldRequest'] = MultipartFormFieldRequest
    globals()['RequestFormatEnum'] = RequestFormatEnum

class DataPassthroughRequest(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('path',): {
            'min_length': 1,
        },
        ('base_url_override',): {
            'min_length': 1,
        },
        ('data',): {
            'min_length': 1,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()

        defined_types = {
            'method': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'path': (str,),  # noqa: E501
            'base_url_override': (str, none_type, none_type,),  # noqa: E501
            'data': (str, none_type, none_type,),  # noqa: E501
            'multipart_form_data': ([MultipartFormFieldRequest], none_type, none_type,),  # noqa: E501
            'headers': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type, none_type,),  # noqa: E501
            'request_format': (RequestFormatEnum, str, none_type,),
            'normalize_response': (bool, none_type,),  # noqa: E501
        }
        return defined_types

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'method': 'method',  # noqa: E501
        'path': 'path',  # noqa: E501
        'base_url_override': 'base_url_override',  # noqa: E501
        'data': 'data',  # noqa: E501
        'multipart_form_data': 'multipart_form_data',  # noqa: E501
        'headers': 'headers',  # noqa: E501
        'request_format': 'request_format',  # noqa: E501
        'normalize_response': 'normalize_response',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, method, path, *args, **kwargs):  # noqa: E501
        """DataPassthroughRequest - a model defined in OpenAPI

        Args:
            method (bool, date, datetime, dict, float, int, list, str, none_type):
            path (str):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            base_url_override (str, none_type): [optional]  # noqa: E501
            data (str, none_type): [optional]  # noqa: E501
            multipart_form_data ([MultipartFormFieldRequest], none_type): Pass an array of `MultipartFormField` objects in here instead of using the `data` param if `request_format` is set to `MULTIPART`.. [optional]  # noqa: E501
            headers ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): The headers to use for the request (Merge will handle the account's authorization headers). `Content-Type` header is required for passthrough. Choose content type corresponding to expected format of receiving server.. [optional]  # noqa: E501
            request_format (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            normalize_response (bool): Optional. If true, the response will always be an object of the form `{\"type\": T, \"value\": ...}` where `T` will be one of `string, boolean, number, null, array, object`.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)


        self.method = method
        self.path = path
        self.base_url_override = kwargs.get("base_url_override", None)
        self.data = kwargs.get("data", None)
        self.multipart_form_data = kwargs.get("multipart_form_data", None)
        self.headers = kwargs.get("headers", None)
        self.request_format = kwargs.get("request_format", None)
        self.normalize_response = kwargs.get("normalize_response", None)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, method, path, *args, **kwargs):  # noqa: E501
        """DataPassthroughRequest - a model defined in OpenAPI

        Args:
            method (bool, date, datetime, dict, float, int, list, str, none_type):
            path (str):

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            base_url_override (str, none_type): [optional]  # noqa: E501
            data (str, none_type): [optional]  # noqa: E501
            multipart_form_data ([MultipartFormFieldRequest], none_type): Pass an array of `MultipartFormField` objects in here instead of using the `data` param if `request_format` is set to `MULTIPART`.. [optional]  # noqa: E501
            headers ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): The headers to use for the request (Merge will handle the account's authorization headers). `Content-Type` header is required for passthrough. Choose content type corresponding to expected format of receiving server.. [optional]  # noqa: E501
            request_format (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            normalize_response (bool): Optional. If true, the response will always be an object of the form `{\"type\": T, \"value\": ...}` where `T` will be one of `string, boolean, number, null, array, object`.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.method: Union[bool, date, datetime, dict, float, int, list, str, none_type] = method
        self.path: Union[str] = path
        self.base_url_override: Union[str, none_type] = kwargs.get("base_url_override", None)
        self.data: Union[str, none_type] = kwargs.get("data", None)
        self.multipart_form_data: Union[List["MultipartFormFieldRequest"]] = kwargs.get("multipart_form_data", None)
        self.headers: Union[Dict[str, bool, date, datetime, dict, float, int, list, str, none_type], none_type] = kwargs.get("headers", None)
        self.request_format: Union[bool, date, datetime, dict, float, int, list, str, none_type] = kwargs.get("request_format", None)
        self.normalize_response: Union[bool] = kwargs.get("normalize_response", bool())


