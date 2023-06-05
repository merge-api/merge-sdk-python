"""
    Merge CRM API

    The unified API for building rich integrations with multiple CRM platforms.  # noqa: E501

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
    from MergePythonSDK.crm.model.address import Address
    from MergePythonSDK.crm.model.email_address import EmailAddress
    from MergePythonSDK.crm.model.phone_number import PhoneNumber
    from MergePythonSDK.shared.model.remote_data import RemoteData
    from MergePythonSDK.crm.model.remote_field import RemoteField
    globals()['Address'] = Address
    globals()['EmailAddress'] = EmailAddress
    globals()['PhoneNumber'] = PhoneNumber
    globals()['RemoteData'] = RemoteData
    globals()['RemoteField'] = RemoteField

class Contact(ModelNormal):
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
            'first_name': (str, none_type, none_type,),  # noqa: E501
            'last_name': (str, none_type, none_type,),  # noqa: E501
            'account': (str, none_type, none_type,),  # noqa: E501
            'addresses': ([Address], none_type,),  # noqa: E501
            'email_addresses': ([EmailAddress], none_type,),  # noqa: E501
            'phone_numbers': ([PhoneNumber], none_type,),  # noqa: E501
            'last_activity_at': (datetime, none_type, none_type,),  # noqa: E501
            'remote_created_at': (datetime, none_type, none_type,),  # noqa: E501
            'remote_was_deleted': (bool, none_type,),  # noqa: E501
            'id': (str, none_type,),  # noqa: E501
            'remote_id': (str, none_type, none_type,),  # noqa: E501
            'field_mappings': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type, none_type,),  # noqa: E501
            'modified_at': (datetime, none_type,),  # noqa: E501
            'remote_data': ([RemoteData], none_type, none_type,),  # noqa: E501
            'remote_fields': ([RemoteField], none_type,),  # noqa: E501
        }
        expands_types = {"account": "Account"}

        # update types with expands
        for key, val in expands_types.items():
            if key in defined_types.keys():
                expands_model = import_model_by_name(val, "crm")
                if len(defined_types[key]) > 0 and isinstance(defined_types[key][0], list):
                    defined_types[key][0].insert(0, expands_model)
                else:
                    defined_types[key] = (*defined_types[key], expands_model)
        return defined_types

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'first_name': 'first_name',  # noqa: E501
        'last_name': 'last_name',  # noqa: E501
        'account': 'account',  # noqa: E501
        'addresses': 'addresses',  # noqa: E501
        'email_addresses': 'email_addresses',  # noqa: E501
        'phone_numbers': 'phone_numbers',  # noqa: E501
        'last_activity_at': 'last_activity_at',  # noqa: E501
        'remote_created_at': 'remote_created_at',  # noqa: E501
        'remote_was_deleted': 'remote_was_deleted',  # noqa: E501
        'id': 'id',  # noqa: E501
        'remote_id': 'remote_id',  # noqa: E501
        'field_mappings': 'field_mappings',  # noqa: E501
        'modified_at': 'modified_at',  # noqa: E501
        'remote_data': 'remote_data',  # noqa: E501
        'remote_fields': 'remote_fields',  # noqa: E501
    }

    read_only_vars = {
        'remote_was_deleted',  # noqa: E501
        'id',  # noqa: E501
        'field_mappings',  # noqa: E501
        'modified_at',  # noqa: E501
        'remote_data',  # noqa: E501
        'remote_fields',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Contact - a model defined in OpenAPI

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
            first_name (str, none_type): The contact's first name.. [optional]  # noqa: E501
            last_name (str, none_type): The contact's last name.. [optional]  # noqa: E501
            account (str, none_type): The contact's account.. [optional]  # noqa: E501
            addresses ([Address]): [optional]  # noqa: E501
            email_addresses ([EmailAddress]): [optional]  # noqa: E501
            phone_numbers ([PhoneNumber]): [optional]  # noqa: E501
            last_activity_at (datetime, none_type): When the contact's last activity occurred.. [optional]  # noqa: E501
            remote_created_at (datetime, none_type): When the third party's contact was created.. [optional]  # noqa: E501
            remote_was_deleted (bool): [optional]  # noqa: E501
            id (str): [optional]  # noqa: E501
            remote_id (str, none_type): The third-party API ID of the matching object.. [optional]  # noqa: E501
            field_mappings ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): [optional]  # noqa: E501
            modified_at (datetime): This is the datetime that this object was last updated by Merge. [optional]  # noqa: E501
            remote_data ([RemoteData], none_type): [optional]  # noqa: E501
            remote_fields ([RemoteField]): [optional]  # noqa: E501
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


        self.first_name = kwargs.get("first_name", None)
        self.last_name = kwargs.get("last_name", None)
        self.account = kwargs.get("account", None)
        self.addresses = kwargs.get("addresses", None)
        self.email_addresses = kwargs.get("email_addresses", None)
        self.phone_numbers = kwargs.get("phone_numbers", None)
        self.last_activity_at = kwargs.get("last_activity_at", None)
        self.remote_created_at = kwargs.get("remote_created_at", None)
        self.remote_id = kwargs.get("remote_id", None)
        self._remote_was_deleted = kwargs.get("remote_was_deleted", bool())
        self._id = kwargs.get("id", str())
        self._field_mappings = kwargs.get("field_mappings", None)
        self._modified_at = kwargs.get("modified_at", None)
        self._remote_data = kwargs.get("remote_data", None)
        self._remote_fields = kwargs.get("remote_fields", None)
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
        """Contact - a model defined in OpenAPI

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
            first_name (str, none_type): The contact's first name.. [optional]  # noqa: E501
            last_name (str, none_type): The contact's last name.. [optional]  # noqa: E501
            account (str, none_type): The contact's account.. [optional]  # noqa: E501
            addresses ([Address]): [optional]  # noqa: E501
            email_addresses ([EmailAddress]): [optional]  # noqa: E501
            phone_numbers ([PhoneNumber]): [optional]  # noqa: E501
            last_activity_at (datetime, none_type): When the contact's last activity occurred.. [optional]  # noqa: E501
            remote_created_at (datetime, none_type): When the third party's contact was created.. [optional]  # noqa: E501
            remote_was_deleted (bool): [optional]  # noqa: E501
            id (str): [optional]  # noqa: E501
            remote_id (str, none_type): The third-party API ID of the matching object.. [optional]  # noqa: E501
            field_mappings ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): [optional]  # noqa: E501
            modified_at (datetime): This is the datetime that this object was last updated by Merge. [optional]  # noqa: E501
            remote_data ([RemoteData], none_type): [optional]  # noqa: E501
            remote_fields ([RemoteField]): [optional]  # noqa: E501
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

        self.first_name: Union[str, none_type] = kwargs.get("first_name", None)
        self.last_name: Union[str, none_type] = kwargs.get("last_name", None)
        self.account: Union[str, none_type] = kwargs.get("account", None)
        self.addresses: Union[List["Address"]] = kwargs.get("addresses", None)
        self.email_addresses: Union[List["EmailAddress"]] = kwargs.get("email_addresses", None)
        self.phone_numbers: Union[List["PhoneNumber"]] = kwargs.get("phone_numbers", None)
        self.last_activity_at: Union[datetime, none_type] = kwargs.get("last_activity_at", None)
        self.remote_created_at: Union[datetime, none_type] = kwargs.get("remote_created_at", None)
        self.remote_id: Union[str, none_type] = kwargs.get("remote_id", None)
        self._remote_was_deleted: Union[bool] = kwargs.get("remote_was_deleted", bool())
        self._id: Union[str] = kwargs.get("id", str())
        self._field_mappings: Union[Dict[str, bool, date, datetime, dict, float, int, list, str, none_type], none_type] = kwargs.get("field_mappings", None)
        self._modified_at: Union[datetime] = kwargs.get("modified_at", None)
        self._remote_data: Union[List["RemoteData"]] = kwargs.get("remote_data", None)
        self._remote_fields: Union[List["RemoteField"]] = kwargs.get("remote_fields", None)
    @property
    def remote_was_deleted(self):
        return self._remote_was_deleted

    @property
    def id(self):
        return self._id

    @property
    def field_mappings(self):
        return self._field_mappings

    @property
    def modified_at(self):
        return self._modified_at

    @property
    def remote_data(self):
        return self._remote_data

    @property
    def remote_fields(self):
        return self._remote_fields



