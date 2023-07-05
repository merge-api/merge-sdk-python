"""
    Merge ATS API

    The unified API for building rich integrations with multiple Applicant Tracking System platforms.  # noqa: E501

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
    from MergePythonSDK.shared.model.category_enum import CategoryEnum
    globals()['CategoryEnum'] = CategoryEnum

class AccountDetails(ModelNormal):
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
            'id': (str, none_type,),  # noqa: E501
            'integration': (str, none_type,),  # noqa: E501
            'integration_slug': (str, none_type,),  # noqa: E501
            'category': (CategoryEnum, str, none_type,),
            'end_user_origin_id': (str, none_type,),  # noqa: E501
            'end_user_organization_name': (str, none_type,),  # noqa: E501
            'end_user_email_address': (str, none_type,),  # noqa: E501
            'status': (str, none_type,),  # noqa: E501
            'webhook_listener_url': (str, none_type,),  # noqa: E501
            'is_duplicate': (bool, none_type, none_type,),  # noqa: E501
        }
        return defined_types

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'integration': 'integration',  # noqa: E501
        'integration_slug': 'integration_slug',  # noqa: E501
        'category': 'category',  # noqa: E501
        'end_user_origin_id': 'end_user_origin_id',  # noqa: E501
        'end_user_organization_name': 'end_user_organization_name',  # noqa: E501
        'end_user_email_address': 'end_user_email_address',  # noqa: E501
        'status': 'status',  # noqa: E501
        'webhook_listener_url': 'webhook_listener_url',  # noqa: E501
        'is_duplicate': 'is_duplicate',  # noqa: E501
    }

    read_only_vars = {
        'id',  # noqa: E501
        'integration',  # noqa: E501
        'integration_slug',  # noqa: E501
        'end_user_origin_id',  # noqa: E501
        'end_user_organization_name',  # noqa: E501
        'end_user_email_address',  # noqa: E501
        'status',  # noqa: E501
        'webhook_listener_url',  # noqa: E501
        'is_duplicate',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """AccountDetails - a model defined in OpenAPI

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
            integration (str): [optional]  # noqa: E501
            integration_slug (str): [optional]  # noqa: E501
            category (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            end_user_origin_id (str): [optional]  # noqa: E501
            end_user_organization_name (str): [optional]  # noqa: E501
            end_user_email_address (str): [optional]  # noqa: E501
            status (str): [optional]  # noqa: E501
            webhook_listener_url (str): [optional]  # noqa: E501
            is_duplicate (bool, none_type): Whether a Production Linked Account's credentials match another existing Production Linked Account. This field is `null` for Test Linked Accounts, incomplete Production Linked Accounts, and ignored duplicate Production Linked Account sets.. [optional]  # noqa: E501
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


        self.category = kwargs.get("category", None)

        # Read only properties
        self._id = kwargs.get("id", str())
        self._integration = kwargs.get("integration", str())
        self._integration_slug = kwargs.get("integration_slug", str())
        self._end_user_origin_id = kwargs.get("end_user_origin_id", str())
        self._end_user_organization_name = kwargs.get("end_user_organization_name", str())
        self._end_user_email_address = kwargs.get("end_user_email_address", str())
        self._status = kwargs.get("status", str())
        self._webhook_listener_url = kwargs.get("webhook_listener_url", str())
        self._is_duplicate = kwargs.get("is_duplicate", None)
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
        """AccountDetails - a model defined in OpenAPI

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
            integration (str): [optional]  # noqa: E501
            integration_slug (str): [optional]  # noqa: E501
            category (bool, date, datetime, dict, float, int, list, str, none_type): [optional]  # noqa: E501
            end_user_origin_id (str): [optional]  # noqa: E501
            end_user_organization_name (str): [optional]  # noqa: E501
            end_user_email_address (str): [optional]  # noqa: E501
            status (str): [optional]  # noqa: E501
            webhook_listener_url (str): [optional]  # noqa: E501
            is_duplicate (bool, none_type): Whether a Production Linked Account's credentials match another existing Production Linked Account. This field is `null` for Test Linked Accounts, incomplete Production Linked Accounts, and ignored duplicate Production Linked Account sets.. [optional]  # noqa: E501
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

        self.category: Union[bool, date, datetime, dict, float, int, list, str, none_type] = kwargs.get("category", None)

        # Read only properties
        self._id: Union[str] = kwargs.get("id", str())
        self._integration: Union[str] = kwargs.get("integration", str())
        self._integration_slug: Union[str] = kwargs.get("integration_slug", str())
        self._end_user_origin_id: Union[str] = kwargs.get("end_user_origin_id", str())
        self._end_user_organization_name: Union[str] = kwargs.get("end_user_organization_name", str())
        self._end_user_email_address: Union[str] = kwargs.get("end_user_email_address", str())
        self._status: Union[str] = kwargs.get("status", str())
        self._webhook_listener_url: Union[str] = kwargs.get("webhook_listener_url", str())
        self._is_duplicate: Union[bool, none_type] = kwargs.get("is_duplicate", None)

    # Read only property getters
    @property
    def id(self):
        return self._id

    @property
    def integration(self):
        return self._integration

    @property
    def integration_slug(self):
        return self._integration_slug

    @property
    def end_user_origin_id(self):
        return self._end_user_origin_id

    @property
    def end_user_organization_name(self):
        return self._end_user_organization_name

    @property
    def end_user_email_address(self):
        return self._end_user_email_address

    @property
    def status(self):
        return self._status

    @property
    def webhook_listener_url(self):
        return self._webhook_listener_url

    @property
    def is_duplicate(self):
        return self._is_duplicate



