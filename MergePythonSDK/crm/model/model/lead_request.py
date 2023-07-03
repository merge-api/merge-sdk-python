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
    from MergePythonSDK.crm.model.address_request import AddressRequest
    from MergePythonSDK.crm.model.email_address_request import EmailAddressRequest
    from MergePythonSDK.crm.model.phone_number_request import PhoneNumberRequest
    from MergePythonSDK.crm.model.remote_field_request import RemoteFieldRequest
    globals()['AddressRequest'] = AddressRequest
    globals()['EmailAddressRequest'] = EmailAddressRequest
    globals()['PhoneNumberRequest'] = PhoneNumberRequest
    globals()['RemoteFieldRequest'] = RemoteFieldRequest

class LeadRequest(ModelNormal):
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
            'owner': (str, none_type, none_type,),  # noqa: E501
            'lead_source': (str, none_type, none_type,),  # noqa: E501
            'title': (str, none_type, none_type,),  # noqa: E501
            'company': (str, none_type, none_type,),  # noqa: E501
            'first_name': (str, none_type, none_type,),  # noqa: E501
            'last_name': (str, none_type, none_type,),  # noqa: E501
            'addresses': ([AddressRequest], none_type,),  # noqa: E501
            'email_addresses': ([EmailAddressRequest], none_type,),  # noqa: E501
            'phone_numbers': ([PhoneNumberRequest], none_type,),  # noqa: E501
            'converted_date': (datetime, none_type, none_type,),  # noqa: E501
            'converted_contact': (str, none_type, none_type,),  # noqa: E501
            'converted_account': (str, none_type, none_type,),  # noqa: E501
            'integration_params': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type, none_type,),  # noqa: E501
            'linked_account_params': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type, none_type,),  # noqa: E501
            'remote_fields': ([RemoteFieldRequest], none_type,),  # noqa: E501
        }
        expands_types = {"converted_account": "Account", "converted_contact": "Contact", "owner": "User"}

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
        'owner': 'owner',  # noqa: E501
        'lead_source': 'lead_source',  # noqa: E501
        'title': 'title',  # noqa: E501
        'company': 'company',  # noqa: E501
        'first_name': 'first_name',  # noqa: E501
        'last_name': 'last_name',  # noqa: E501
        'addresses': 'addresses',  # noqa: E501
        'email_addresses': 'email_addresses',  # noqa: E501
        'phone_numbers': 'phone_numbers',  # noqa: E501
        'converted_date': 'converted_date',  # noqa: E501
        'converted_contact': 'converted_contact',  # noqa: E501
        'converted_account': 'converted_account',  # noqa: E501
        'integration_params': 'integration_params',  # noqa: E501
        'linked_account_params': 'linked_account_params',  # noqa: E501
        'remote_fields': 'remote_fields',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """LeadRequest - a model defined in OpenAPI

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
            owner (str, none_type): The lead's owner.. [optional]  # noqa: E501
            lead_source (str, none_type): The lead's source.. [optional]  # noqa: E501
            title (str, none_type): The lead's title.. [optional]  # noqa: E501
            company (str, none_type): The lead's company.. [optional]  # noqa: E501
            first_name (str, none_type): The lead's first name.. [optional]  # noqa: E501
            last_name (str, none_type): The lead's last name.. [optional]  # noqa: E501
            addresses ([AddressRequest]): [optional]  # noqa: E501
            email_addresses ([EmailAddressRequest]): [optional]  # noqa: E501
            phone_numbers ([PhoneNumberRequest]): [optional]  # noqa: E501
            converted_date (datetime, none_type): When the lead was converted.. [optional]  # noqa: E501
            converted_contact (str, none_type): The contact of the converted lead.. [optional]  # noqa: E501
            converted_account (str, none_type): The account of the converted lead.. [optional]  # noqa: E501
            integration_params ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): [optional]  # noqa: E501
            linked_account_params ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): [optional]  # noqa: E501
            remote_fields ([RemoteFieldRequest]): [optional]  # noqa: E501
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


        self.owner = kwargs.get("owner", None)
        self.lead_source = kwargs.get("lead_source", None)
        self.title = kwargs.get("title", None)
        self.company = kwargs.get("company", None)
        self.first_name = kwargs.get("first_name", None)
        self.last_name = kwargs.get("last_name", None)
        self.addresses = kwargs.get("addresses", None)
        self.email_addresses = kwargs.get("email_addresses", None)
        self.phone_numbers = kwargs.get("phone_numbers", None)
        self.converted_date = kwargs.get("converted_date", None)
        self.converted_contact = kwargs.get("converted_contact", None)
        self.converted_account = kwargs.get("converted_account", None)
        self.integration_params = kwargs.get("integration_params", None)
        self.linked_account_params = kwargs.get("linked_account_params", None)
        self.remote_fields = kwargs.get("remote_fields", None)
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
        """LeadRequest - a model defined in OpenAPI

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
            owner (str, none_type): The lead's owner.. [optional]  # noqa: E501
            lead_source (str, none_type): The lead's source.. [optional]  # noqa: E501
            title (str, none_type): The lead's title.. [optional]  # noqa: E501
            company (str, none_type): The lead's company.. [optional]  # noqa: E501
            first_name (str, none_type): The lead's first name.. [optional]  # noqa: E501
            last_name (str, none_type): The lead's last name.. [optional]  # noqa: E501
            addresses ([AddressRequest]): [optional]  # noqa: E501
            email_addresses ([EmailAddressRequest]): [optional]  # noqa: E501
            phone_numbers ([PhoneNumberRequest]): [optional]  # noqa: E501
            converted_date (datetime, none_type): When the lead was converted.. [optional]  # noqa: E501
            converted_contact (str, none_type): The contact of the converted lead.. [optional]  # noqa: E501
            converted_account (str, none_type): The account of the converted lead.. [optional]  # noqa: E501
            integration_params ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): [optional]  # noqa: E501
            linked_account_params ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): [optional]  # noqa: E501
            remote_fields ([RemoteFieldRequest]): [optional]  # noqa: E501
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

        self.owner: Union[str, none_type] = kwargs.get("owner", None)
        self.lead_source: Union[str, none_type] = kwargs.get("lead_source", None)
        self.title: Union[str, none_type] = kwargs.get("title", None)
        self.company: Union[str, none_type] = kwargs.get("company", None)
        self.first_name: Union[str, none_type] = kwargs.get("first_name", None)
        self.last_name: Union[str, none_type] = kwargs.get("last_name", None)
        self.addresses: Union[List["AddressRequest"]] = kwargs.get("addresses", None)
        self.email_addresses: Union[List["EmailAddressRequest"]] = kwargs.get("email_addresses", None)
        self.phone_numbers: Union[List["PhoneNumberRequest"]] = kwargs.get("phone_numbers", None)
        self.converted_date: Union[datetime, none_type] = kwargs.get("converted_date", None)
        self.converted_contact: Union[str, none_type] = kwargs.get("converted_contact", None)
        self.converted_account: Union[str, none_type] = kwargs.get("converted_account", None)
        self.integration_params: Union[Dict[str, bool, date, datetime, dict, float, int, list, str, none_type], none_type] = kwargs.get("integration_params", None)
        self.linked_account_params: Union[Dict[str, bool, date, datetime, dict, float, int, list, str, none_type], none_type] = kwargs.get("linked_account_params", None)
        self.remote_fields: Union[List["RemoteFieldRequest"]] = kwargs.get("remote_fields", None)

