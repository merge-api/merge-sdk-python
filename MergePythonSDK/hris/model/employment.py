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
    from MergePythonSDK.hris.model.employment_type_enum import EmploymentTypeEnum
    from MergePythonSDK.hris.model.flsa_status_enum import FlsaStatusEnum
    from MergePythonSDK.hris.model.pay_currency_enum import PayCurrencyEnum
    from MergePythonSDK.hris.model.pay_frequency_enum import PayFrequencyEnum
    from MergePythonSDK.hris.model.pay_period_enum import PayPeriodEnum
    from MergePythonSDK.shared.model.remote_data import RemoteData
    globals()['EmploymentTypeEnum'] = EmploymentTypeEnum
    globals()['FlsaStatusEnum'] = FlsaStatusEnum
    globals()['PayCurrencyEnum'] = PayCurrencyEnum
    globals()['PayFrequencyEnum'] = PayFrequencyEnum
    globals()['PayPeriodEnum'] = PayPeriodEnum
    globals()['RemoteData'] = RemoteData

class Employment(ModelNormal):
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
            'remote_id': (str, none_type, none_type,),  # noqa: E501
            'employee': (str, none_type, none_type,),  # noqa: E501
            'job_title': (str, none_type, none_type,),  # noqa: E501
            'pay_rate': (float, none_type, none_type,),  # noqa: E501
            'pay_period': (PayPeriodEnum, str, none_type,),
            'pay_frequency': (PayFrequencyEnum, str, none_type,),
            'pay_currency': (PayCurrencyEnum, str, none_type,),
            'pay_group': (str, none_type, none_type,),  # noqa: E501
            'flsa_status': (FlsaStatusEnum, str, none_type,),
            'effective_date': (datetime, none_type, none_type,),  # noqa: E501
            'employment_type': (EmploymentTypeEnum, str, none_type,),
            'remote_data': ([RemoteData], none_type, none_type,),  # noqa: E501
            'remote_was_deleted': (bool, none_type,),  # noqa: E501
        }
        expands_types = {"employee": "Employee", "pay_group": "PayGroup"}

        # update types with expands
        for key, val in expands_types.items():
            if key in defined_types.keys():
                expands_model = import_model_by_name(val, "hris")
                if len(defined_types[key]) > 0 and isinstance(defined_types[key][0], list):
                    defined_types[key][0].insert(0, expands_model)
                defined_types[key] = (*defined_types[key], expands_model)
        return defined_types

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'remote_id': 'remote_id',  # noqa: E501
        'employee': 'employee',  # noqa: E501
        'job_title': 'job_title',  # noqa: E501
        'pay_rate': 'pay_rate',  # noqa: E501
        'pay_period': 'pay_period',  # noqa: E501
        'pay_frequency': 'pay_frequency',  # noqa: E501
        'pay_currency': 'pay_currency',  # noqa: E501
        'pay_group': 'pay_group',  # noqa: E501
        'flsa_status': 'flsa_status',  # noqa: E501
        'effective_date': 'effective_date',  # noqa: E501
        'employment_type': 'employment_type',  # noqa: E501
        'remote_data': 'remote_data',  # noqa: E501
        'remote_was_deleted': 'remote_was_deleted',  # noqa: E501
    }

    read_only_vars = {
        'id',  # noqa: E501
        'remote_data',  # noqa: E501
        'remote_was_deleted',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Employment - a model defined in OpenAPI

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
            employee (str, none_type): [optional]  # noqa: E501
            job_title (str, none_type): The position's title.. [optional]  # noqa: E501
            pay_rate (float, none_type): The position's pay rate in dollars.. [optional]  # noqa: E501
            pay_period (bool, date, datetime, dict, float, int, list, str, none_type): The time period this pay rate encompasses.. [optional]  # noqa: E501
            pay_frequency (bool, date, datetime, dict, float, int, list, str, none_type): The position's pay frequency.. [optional]  # noqa: E501
            pay_currency (bool, date, datetime, dict, float, int, list, str, none_type): The position's currency code.. [optional]  # noqa: E501
            pay_group (str, none_type): [optional]  # noqa: E501
            flsa_status (bool, date, datetime, dict, float, int, list, str, none_type): The position's FLSA status.. [optional]  # noqa: E501
            effective_date (datetime, none_type): The position's effective date.. [optional]  # noqa: E501
            employment_type (bool, date, datetime, dict, float, int, list, str, none_type): The position's type of employment.. [optional]  # noqa: E501
            remote_data ([RemoteData], none_type): [optional]  # noqa: E501
            remote_was_deleted (bool): Indicates whether or not this object has been deleted by third party webhooks.. [optional]  # noqa: E501
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
        self.employee = kwargs.get("employee", None)
        self.job_title = kwargs.get("job_title", None)
        self.pay_rate = kwargs.get("pay_rate", None)
        self.pay_period = kwargs.get("pay_period", None)
        self.pay_frequency = kwargs.get("pay_frequency", None)
        self.pay_currency = kwargs.get("pay_currency", None)
        self.pay_group = kwargs.get("pay_group", None)
        self.flsa_status = kwargs.get("flsa_status", None)
        self.effective_date = kwargs.get("effective_date", None)
        self.employment_type = kwargs.get("employment_type", None)

        # Read only properties
        self._id = kwargs.get("id", str())
        self._remote_data = kwargs.get("remote_data", None)
        self._remote_was_deleted = kwargs.get("remote_was_deleted", bool())
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
        """Employment - a model defined in OpenAPI

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
            employee (str, none_type): [optional]  # noqa: E501
            job_title (str, none_type): The position's title.. [optional]  # noqa: E501
            pay_rate (float, none_type): The position's pay rate in dollars.. [optional]  # noqa: E501
            pay_period (bool, date, datetime, dict, float, int, list, str, none_type): The time period this pay rate encompasses.. [optional]  # noqa: E501
            pay_frequency (bool, date, datetime, dict, float, int, list, str, none_type): The position's pay frequency.. [optional]  # noqa: E501
            pay_currency (bool, date, datetime, dict, float, int, list, str, none_type): The position's currency code.. [optional]  # noqa: E501
            pay_group (str, none_type): [optional]  # noqa: E501
            flsa_status (bool, date, datetime, dict, float, int, list, str, none_type): The position's FLSA status.. [optional]  # noqa: E501
            effective_date (datetime, none_type): The position's effective date.. [optional]  # noqa: E501
            employment_type (bool, date, datetime, dict, float, int, list, str, none_type): The position's type of employment.. [optional]  # noqa: E501
            remote_data ([RemoteData], none_type): [optional]  # noqa: E501
            remote_was_deleted (bool): Indicates whether or not this object has been deleted by third party webhooks.. [optional]  # noqa: E501
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
        self.employee: Union[str, none_type] = kwargs.get("employee", None)
        self.job_title: Union[str, none_type] = kwargs.get("job_title", None)
        self.pay_rate: Union[float, none_type] = kwargs.get("pay_rate", None)
        self.pay_period: Union[bool, date, datetime, dict, float, int, list, str, none_type] = kwargs.get("pay_period", None)
        self.pay_frequency: Union[bool, date, datetime, dict, float, int, list, str, none_type] = kwargs.get("pay_frequency", None)
        self.pay_currency: Union[bool, date, datetime, dict, float, int, list, str, none_type] = kwargs.get("pay_currency", None)
        self.pay_group: Union[str, none_type] = kwargs.get("pay_group", None)
        self.flsa_status: Union[bool, date, datetime, dict, float, int, list, str, none_type] = kwargs.get("flsa_status", None)
        self.effective_date: Union[datetime, none_type] = kwargs.get("effective_date", None)
        self.employment_type: Union[bool, date, datetime, dict, float, int, list, str, none_type] = kwargs.get("employment_type", None)

        # Read only properties
        self._id: Union[str] = kwargs.get("id", str())
        self._remote_data: Union[List["RemoteData"]] = kwargs.get("remote_data", None)
        self._remote_was_deleted: Union[bool] = kwargs.get("remote_was_deleted", bool())

    # Read only property getters
    @property
    def id(self):
        return self._id

    @property
    def remote_data(self):
        return self._remote_data

    @property
    def remote_was_deleted(self):
        return self._remote_was_deleted



