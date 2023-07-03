"""
    Merge HRIS API

    The unified API for building rich integrations with multiple HR Information System platforms.  # noqa: E501

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
    from MergePythonSDK.hris.model.issue_status_enum import IssueStatusEnum
    globals()['IssueStatusEnum'] = IssueStatusEnum

class Issue(ModelNormal):
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
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, dict, float, int, list, str, none_type,)  # noqa: E501

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
            'error_description': (str,),  # noqa: E501
            'id': (str, none_type,),  # noqa: E501
            'status': (IssueStatusEnum, str, none_type,),
            'end_user': ({str: (bool, dict, float, int, list, str, none_type)}, none_type,),  # noqa: E501
            'first_incident_time': (datetime, none_type, none_type,),  # noqa: E501
            'last_incident_time': (datetime, none_type, none_type,),  # noqa: E501
            'is_muted': (bool, none_type,),  # noqa: E501
            'error_details': ([str], none_type,),  # noqa: E501
        }
        return defined_types

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'error_description': 'error_description',  # noqa: E501
        'id': 'id',  # noqa: E501
        'status': 'status',  # noqa: E501
        'end_user': 'end_user',  # noqa: E501
        'first_incident_time': 'first_incident_time',  # noqa: E501
        'last_incident_time': 'last_incident_time',  # noqa: E501
        'is_muted': 'is_muted',  # noqa: E501
        'error_details': 'error_details',  # noqa: E501
    }

    read_only_vars = {
        'id',  # noqa: E501
        'end_user',  # noqa: E501
        'is_muted',  # noqa: E501
        'error_details',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, error_description, *args, **kwargs):  # noqa: E501
        """Issue - a model defined in OpenAPI

        Args:
            error_description (str):

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
            id (str): [optional]  # noqa: E501
            status (bool, dict, float, int, list, str, none_type): Status of the issue. Options: ('ONGOING', 'RESOLVED')  * `ONGOING` - ONGOING * `RESOLVED` - RESOLVED. [optional]  # noqa: E501
            end_user ({str: (bool, dict, float, int, list, str, none_type)}): [optional]  # noqa: E501
            first_incident_time (datetime, none_type): [optional]  # noqa: E501
            last_incident_time (datetime, none_type): [optional]  # noqa: E501
            is_muted (bool): [optional]  # noqa: E501
            error_details ([str]): [optional]  # noqa: E501
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


        self.error_description = error_description
        self.status = kwargs.get("status", None)
        self.first_incident_time = kwargs.get("first_incident_time", None)
        self.last_incident_time = kwargs.get("last_incident_time", None)

        # Read only properties
        self._id = kwargs.get("id", str())
        self._end_user = kwargs.get("end_user", dict())
        self._is_muted = kwargs.get("is_muted", bool())
        self._error_details = kwargs.get("error_details", list())
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
    def __init__(self, error_description, *args, **kwargs):  # noqa: E501
        """Issue - a model defined in OpenAPI

        Args:
            error_description (str):

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
            id (str): [optional]  # noqa: E501
            status (bool, dict, float, int, list, str, none_type): Status of the issue. Options: ('ONGOING', 'RESOLVED')  * `ONGOING` - ONGOING * `RESOLVED` - RESOLVED. [optional]  # noqa: E501
            end_user ({str: (bool, dict, float, int, list, str, none_type)}): [optional]  # noqa: E501
            first_incident_time (datetime, none_type): [optional]  # noqa: E501
            last_incident_time (datetime, none_type): [optional]  # noqa: E501
            is_muted (bool): [optional]  # noqa: E501
            error_details ([str]): [optional]  # noqa: E501
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

        self.error_description: Union[str] = error_description
        self.status: Union[bool, dict, float, int, list, str, none_type] = kwargs.get("status", None)
        self.first_incident_time: Union[datetime, none_type] = kwargs.get("first_incident_time", None)
        self.last_incident_time: Union[datetime, none_type] = kwargs.get("last_incident_time", None)

        # Read only properties
        self._id: Union[str] = kwargs.get("id", str())
        self._end_user: Union[Dict[str, bool, dict, float, int, list, str, none_type]] = kwargs.get("end_user", dict())
        self._is_muted: Union[bool] = kwargs.get("is_muted", bool())
        self._error_details: Union[List[str]] = kwargs.get("error_details", list())

    # Read only property getters
    @property
    def id(self):
        return self._id

    @property
    def end_user(self):
        return self._end_user

    @property
    def is_muted(self):
        return self._is_muted

    @property
    def error_details(self):
        return self._error_details



