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
    from MergePythonSDK.shared.model.remote_data import RemoteData
    globals()['RemoteData'] = RemoteData

class Tag(ModelNormal):
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
            'remote_id': (str, none_type, none_type,),  # noqa: E501
            'name': (str, none_type, none_type,),  # noqa: E501
            'remote_was_deleted': (bool, none_type,),  # noqa: E501
            'field_mappings': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type, none_type,),  # noqa: E501
            'modified_at': (datetime, none_type,),  # noqa: E501
            'remote_data': ([RemoteData], none_type, none_type,),  # noqa: E501
        }
        return defined_types

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'remote_id': 'remote_id',  # noqa: E501
        'name': 'name',  # noqa: E501
        'remote_was_deleted': 'remote_was_deleted',  # noqa: E501
        'field_mappings': 'field_mappings',  # noqa: E501
        'modified_at': 'modified_at',  # noqa: E501
        'remote_data': 'remote_data',  # noqa: E501
    }

    read_only_vars = {
        'field_mappings',  # noqa: E501
        'modified_at',  # noqa: E501
        'remote_data',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Tag - a model defined in OpenAPI

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
            remote_id (str, none_type): The third-party API ID of the matching object.. [optional]  # noqa: E501
            name (str, none_type): The tag's name.. [optional]  # noqa: E501
            remote_was_deleted (bool): Indicates whether or not this object has been deleted by third party webhooks.. [optional]  # noqa: E501
            field_mappings ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): [optional]  # noqa: E501
            modified_at (datetime): This is the datetime that this object was last updated by Merge. [optional]  # noqa: E501
            remote_data ([RemoteData], none_type): [optional]  # noqa: E501
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


        self.remote_id = kwargs.get("remote_id", None)
        self.name = kwargs.get("name", None)
        self.remote_was_deleted = kwargs.get("remote_was_deleted", None)
        self._field_mappings = kwargs.get("field_mappings", None)
        self._modified_at = kwargs.get("modified_at", None)
        self._remote_data = kwargs.get("remote_data", None)
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
    def __init__(self, *args, **kwargs):  # noqa: E501
        """Tag - a model defined in OpenAPI

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
            remote_id (str, none_type): The third-party API ID of the matching object.. [optional]  # noqa: E501
            name (str, none_type): The tag's name.. [optional]  # noqa: E501
            remote_was_deleted (bool): Indicates whether or not this object has been deleted by third party webhooks.. [optional]  # noqa: E501
            field_mappings ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): [optional]  # noqa: E501
            modified_at (datetime): This is the datetime that this object was last updated by Merge. [optional]  # noqa: E501
            remote_data ([RemoteData], none_type): [optional]  # noqa: E501
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

        self.remote_id: Union[str, none_type] = kwargs.get("remote_id", None)
        self.name: Union[str, none_type] = kwargs.get("name", None)
        self.remote_was_deleted: Union[bool] = kwargs.get("remote_was_deleted", bool())
        self._field_mappings: Union[Dict[str, bool, date, datetime, dict, float, int, list, str, none_type], none_type] = kwargs.get("field_mappings", None)
        self._modified_at: Union[datetime] = kwargs.get("modified_at", None)
        self._remote_data: Union[List["RemoteData"]] = kwargs.get("remote_data", None)
    @property
    def field_mappings(self):
        return self._field_mappings

    @property
    def modified_at(self):
        return self._modified_at

    @property
    def remote_data(self):
        return self._remote_data



