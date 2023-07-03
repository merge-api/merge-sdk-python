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
    from MergePythonSDK.crm.model.opportunity_status_enum import OpportunityStatusEnum
    from MergePythonSDK.crm.model.remote_field_request import RemoteFieldRequest
    globals()['OpportunityStatusEnum'] = OpportunityStatusEnum
    globals()['RemoteFieldRequest'] = RemoteFieldRequest

class OpportunityRequest(ModelNormal):
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
        ('amount',): {
            'inclusive_maximum': 2147483647,
            'inclusive_minimum': -2147483648,
        },
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
            'name': (str, none_type, none_type,),  # noqa: E501
            'description': (str, none_type, none_type,),  # noqa: E501
            'amount': (int, none_type, none_type,),  # noqa: E501
            'owner': (str, none_type, none_type,),  # noqa: E501
            'account': (str, none_type, none_type,),  # noqa: E501
            'stage': (str, none_type, none_type,),  # noqa: E501
            'status': (OpportunityStatusEnum, str, none_type,),
            'last_activity_at': (datetime, none_type, none_type,),  # noqa: E501
            'close_date': (datetime, none_type, none_type,),  # noqa: E501
            'integration_params': ({str: (bool, dict, float, int, list, str, none_type)}, none_type, none_type,),  # noqa: E501
            'linked_account_params': ({str: (bool, dict, float, int, list, str, none_type)}, none_type, none_type,),  # noqa: E501
            'remote_fields': ([RemoteFieldRequest], none_type,),  # noqa: E501
        }
        expands_types = {"account": "Account", "owner": "User", "stage": "Stage"}

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
        'name': 'name',  # noqa: E501
        'description': 'description',  # noqa: E501
        'amount': 'amount',  # noqa: E501
        'owner': 'owner',  # noqa: E501
        'account': 'account',  # noqa: E501
        'stage': 'stage',  # noqa: E501
        'status': 'status',  # noqa: E501
        'last_activity_at': 'last_activity_at',  # noqa: E501
        'close_date': 'close_date',  # noqa: E501
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
        """OpportunityRequest - a model defined in OpenAPI

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
            name (str, none_type): The opportunity's name.. [optional]  # noqa: E501
            description (str, none_type): The opportunity's description.. [optional]  # noqa: E501
            amount (int, none_type): The opportunity's amount.. [optional]  # noqa: E501
            owner (str, none_type): The opportunity's owner.. [optional]  # noqa: E501
            account (str, none_type): The account of the opportunity.. [optional]  # noqa: E501
            stage (str, none_type): The stage of the opportunity.. [optional]  # noqa: E501
            status (bool, dict, float, int, list, str, none_type): The opportunity's status.  * `OPEN` - OPEN * `WON` - WON * `LOST` - LOST. [optional]  # noqa: E501
            last_activity_at (datetime, none_type): When the opportunity's last activity occurred.. [optional]  # noqa: E501
            close_date (datetime, none_type): When the opportunity was closed.. [optional]  # noqa: E501
            integration_params ({str: (bool, dict, float, int, list, str, none_type)}, none_type): [optional]  # noqa: E501
            linked_account_params ({str: (bool, dict, float, int, list, str, none_type)}, none_type): [optional]  # noqa: E501
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


        self.name = kwargs.get("name", None)
        self.description = kwargs.get("description", None)
        self.amount = kwargs.get("amount", None)
        self.owner = kwargs.get("owner", None)
        self.account = kwargs.get("account", None)
        self.stage = kwargs.get("stage", None)
        self.status = kwargs.get("status", None)
        self.last_activity_at = kwargs.get("last_activity_at", None)
        self.close_date = kwargs.get("close_date", None)
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
        """OpportunityRequest - a model defined in OpenAPI

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
            name (str, none_type): The opportunity's name.. [optional]  # noqa: E501
            description (str, none_type): The opportunity's description.. [optional]  # noqa: E501
            amount (int, none_type): The opportunity's amount.. [optional]  # noqa: E501
            owner (str, none_type): The opportunity's owner.. [optional]  # noqa: E501
            account (str, none_type): The account of the opportunity.. [optional]  # noqa: E501
            stage (str, none_type): The stage of the opportunity.. [optional]  # noqa: E501
            status (bool, dict, float, int, list, str, none_type): The opportunity's status.  * `OPEN` - OPEN * `WON` - WON * `LOST` - LOST. [optional]  # noqa: E501
            last_activity_at (datetime, none_type): When the opportunity's last activity occurred.. [optional]  # noqa: E501
            close_date (datetime, none_type): When the opportunity was closed.. [optional]  # noqa: E501
            integration_params ({str: (bool, dict, float, int, list, str, none_type)}, none_type): [optional]  # noqa: E501
            linked_account_params ({str: (bool, dict, float, int, list, str, none_type)}, none_type): [optional]  # noqa: E501
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

        self.name: Union[str, none_type] = kwargs.get("name", None)
        self.description: Union[str, none_type] = kwargs.get("description", None)
        self.amount: Union[int, none_type] = kwargs.get("amount", None)
        self.owner: Union[str, none_type] = kwargs.get("owner", None)
        self.account: Union[str, none_type] = kwargs.get("account", None)
        self.stage: Union[str, none_type] = kwargs.get("stage", None)
        self.status: Union[bool, dict, float, int, list, str, none_type] = kwargs.get("status", None)
        self.last_activity_at: Union[datetime, none_type] = kwargs.get("last_activity_at", None)
        self.close_date: Union[datetime, none_type] = kwargs.get("close_date", None)
        self.integration_params: Union[Dict[str, bool, dict, float, int, list, str, none_type], none_type] = kwargs.get("integration_params", None)
        self.linked_account_params: Union[Dict[str, bool, dict, float, int, list, str, none_type], none_type] = kwargs.get("linked_account_params", None)
        self.remote_fields: Union[List["RemoteFieldRequest"]] = kwargs.get("remote_fields", None)


