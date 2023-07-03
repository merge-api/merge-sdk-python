"""
    Merge Accounting API

    The unified API for building rich integrations with multiple Accounting & Finance platforms.  # noqa: E501

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
    from MergePythonSDK.accounting.model.accounting_phone_number import AccountingPhoneNumber
    from MergePythonSDK.shared.model.remote_remote_data import RemoteData
    from MergePythonSDK.accounting.model.status7d1_enum import Status7d1Enum
    globals()['AccountingPhoneNumber'] = AccountingPhoneNumber
    globals()['RemoteData'] = RemoteData
    globals()['Status7d1Enum'] = Status7d1Enum

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
            'id': (str, none_type,),  # noqa: E501
            'remote_id': (str, none_type, none_type,),  # noqa: E501
            'name': (str, none_type, none_type,),  # noqa: E501
            'is_supplier': (bool, none_type, none_type,),  # noqa: E501
            'is_customer': (bool, none_type, none_type,),  # noqa: E501
            'email_address': (str, none_type, none_type,),  # noqa: E501
            'tax_number': (str, none_type, none_type,),  # noqa: E501
            'status': (Status7d1Enum, str, none_type,),
            'currency': (str, none_type, none_type,),  # noqa: E501
            'remote_updated_at': (datetime, none_type, none_type,),  # noqa: E501
            'company': (str, none_type, none_type,),  # noqa: E501
            'addresses': ([str, none_type], none_type,),  # noqa: E501
            'phone_numbers': ([AccountingPhoneNumber], none_type,),  # noqa: E501
            'remote_was_deleted': (bool, none_type,),  # noqa: E501
            'modified_at': (datetime, none_type,),  # noqa: E501
            'field_mappings': ({str: (bool, dict, float, int, list, str, none_type)}, none_type, none_type,),  # noqa: E501
            'remote_data': ([RemoteData], none_type, none_type,),  # noqa: E501
        }
        expands_types = {"account": "Account"}

        # update types with expands
        for key, val in expands_types.items():
            if key in defined_types.keys():
                expands_model = import_model_by_name(val, "accounting")
                if len(defined_types[key]) > 0 and isinstance(defined_types[key][0], list):
                    defined_types[key][0].insert(0, expands_model)
                else:
                    defined_types[key] = (*defined_types[key], expands_model)
        return defined_types

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'remote_id': 'remote_id',  # noqa: E501
        'name': 'name',  # noqa: E501
        'is_supplier': 'is_supplier',  # noqa: E501
        'is_customer': 'is_customer',  # noqa: E501
        'email_address': 'email_address',  # noqa: E501
        'tax_number': 'tax_number',  # noqa: E501
        'status': 'status',  # noqa: E501
        'currency': 'currency',  # noqa: E501
        'remote_updated_at': 'remote_updated_at',  # noqa: E501
        'company': 'company',  # noqa: E501
        'addresses': 'addresses',  # noqa: E501
        'phone_numbers': 'phone_numbers',  # noqa: E501
        'remote_was_deleted': 'remote_was_deleted',  # noqa: E501
        'modified_at': 'modified_at',  # noqa: E501
        'field_mappings': 'field_mappings',  # noqa: E501
        'remote_data': 'remote_data',  # noqa: E501
    }

    read_only_vars = {
        'id',  # noqa: E501
        'remote_was_deleted',  # noqa: E501
        'modified_at',  # noqa: E501
        'field_mappings',  # noqa: E501
        'remote_data',  # noqa: E501
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
            id (str): [optional]  # noqa: E501
            remote_id (str, none_type): The third-party API ID of the matching object.. [optional]  # noqa: E501
            name (str, none_type): The contact's name.. [optional]  # noqa: E501
            is_supplier (bool, none_type): Whether the contact is a supplier.. [optional]  # noqa: E501
            is_customer (bool, none_type): Whether the contact is a customer.. [optional]  # noqa: E501
            email_address (str, none_type): The contact's email address.. [optional]  # noqa: E501
            tax_number (str, none_type): The contact's tax number.. [optional]  # noqa: E501
            status (bool, dict, float, int, list, str, none_type): The contact's status  * `ACTIVE` - ACTIVE * `ARCHIVED` - ARCHIVED. [optional]  # noqa: E501
            currency (str, none_type): The currency the contact's transactions are in.. [optional]  # noqa: E501
            remote_updated_at (datetime, none_type): When the third party's contact was updated.. [optional]  # noqa: E501
            company (str, none_type): The company the contact belongs to.. [optional]  # noqa: E501
            addresses ([str, none_type]): `Address` object IDs for the given `Contacts` object.. [optional]  # noqa: E501
            phone_numbers ([AccountingPhoneNumber]): `AccountingPhoneNumber` object for the given `Contacts` object.. [optional]  # noqa: E501
            remote_was_deleted (bool): Indicates whether or not this object has been deleted by third party webhooks.. [optional]  # noqa: E501
            modified_at (datetime): This is the datetime that this object was last updated by Merge. [optional]  # noqa: E501
            field_mappings ({str: (bool, dict, float, int, list, str, none_type)}, none_type): [optional]  # noqa: E501
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
        self.is_supplier = kwargs.get("is_supplier", None)
        self.is_customer = kwargs.get("is_customer", None)
        self.email_address = kwargs.get("email_address", None)
        self.tax_number = kwargs.get("tax_number", None)
        self.status = kwargs.get("status", None)
        self.currency = kwargs.get("currency", None)
        self.remote_updated_at = kwargs.get("remote_updated_at", None)
        self.company = kwargs.get("company", None)
        self.addresses = kwargs.get("addresses", None)
        self.phone_numbers = kwargs.get("phone_numbers", None)

        # Read only properties
        self._id = kwargs.get("id", str())
        self._remote_was_deleted = kwargs.get("remote_was_deleted", bool())
        self._modified_at = kwargs.get("modified_at", None)
        self._field_mappings = kwargs.get("field_mappings", None)
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
            id (str): [optional]  # noqa: E501
            remote_id (str, none_type): The third-party API ID of the matching object.. [optional]  # noqa: E501
            name (str, none_type): The contact's name.. [optional]  # noqa: E501
            is_supplier (bool, none_type): Whether the contact is a supplier.. [optional]  # noqa: E501
            is_customer (bool, none_type): Whether the contact is a customer.. [optional]  # noqa: E501
            email_address (str, none_type): The contact's email address.. [optional]  # noqa: E501
            tax_number (str, none_type): The contact's tax number.. [optional]  # noqa: E501
            status (bool, dict, float, int, list, str, none_type): The contact's status  * `ACTIVE` - ACTIVE * `ARCHIVED` - ARCHIVED. [optional]  # noqa: E501
            currency (str, none_type): The currency the contact's transactions are in.. [optional]  # noqa: E501
            remote_updated_at (datetime, none_type): When the third party's contact was updated.. [optional]  # noqa: E501
            company (str, none_type): The company the contact belongs to.. [optional]  # noqa: E501
            addresses ([str, none_type]): `Address` object IDs for the given `Contacts` object.. [optional]  # noqa: E501
            phone_numbers ([AccountingPhoneNumber]): `AccountingPhoneNumber` object for the given `Contacts` object.. [optional]  # noqa: E501
            remote_was_deleted (bool): Indicates whether or not this object has been deleted by third party webhooks.. [optional]  # noqa: E501
            modified_at (datetime): This is the datetime that this object was last updated by Merge. [optional]  # noqa: E501
            field_mappings ({str: (bool, dict, float, int, list, str, none_type)}, none_type): [optional]  # noqa: E501
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
        self.is_supplier: Union[bool, none_type] = kwargs.get("is_supplier", None)
        self.is_customer: Union[bool, none_type] = kwargs.get("is_customer", None)
        self.email_address: Union[str, none_type] = kwargs.get("email_address", None)
        self.tax_number: Union[str, none_type] = kwargs.get("tax_number", None)
        self.status: Union[bool, dict, float, int, list, str, none_type] = kwargs.get("status", None)
        self.currency: Union[str, none_type] = kwargs.get("currency", None)
        self.remote_updated_at: Union[datetime, none_type] = kwargs.get("remote_updated_at", None)
        self.company: Union[str, none_type] = kwargs.get("company", None)
        self.addresses: Union[List[str, none_type]] = kwargs.get("addresses", list())
        self.phone_numbers: Union[List["AccountingPhoneNumber"]] = kwargs.get("phone_numbers", None)

        # Read only properties
        self._id: Union[str] = kwargs.get("id", str())
        self._remote_was_deleted: Union[bool] = kwargs.get("remote_was_deleted", bool())
        self._modified_at: Union[datetime] = kwargs.get("modified_at", None)
        self._field_mappings: Union[Dict[str, bool, dict, float, int, list, str, none_type], none_type] = kwargs.get("field_mappings", None)
        self._remote_data: Union[List["RemoteData"]] = kwargs.get("remote_data", None)

    # Read only property getters
    @property
    def id(self):
        return self._id

    @property
    def remote_was_deleted(self):
        return self._remote_was_deleted

    @property
    def modified_at(self):
        return self._modified_at

    @property
    def field_mappings(self):
        return self._field_mappings

    @property
    def remote_data(self):
        return self._remote_data



