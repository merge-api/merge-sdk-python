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
    from MergePythonSDK.accounting.model.currency_enum import CurrencyEnum
    from MergePythonSDK.accounting.model.purchase_order_line_item import PurchaseOrderLineItem
    from MergePythonSDK.accounting.model.purchase_order_status_enum import PurchaseOrderStatusEnum
    from MergePythonSDK.shared.model.remote_data import RemoteData
    globals()['CurrencyEnum'] = CurrencyEnum
    globals()['PurchaseOrderLineItem'] = PurchaseOrderLineItem
    globals()['PurchaseOrderStatusEnum'] = PurchaseOrderStatusEnum
    globals()['RemoteData'] = RemoteData

class PurchaseOrder(ModelNormal):
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
            'remote_data': ([RemoteData], none_type, none_type,),  # noqa: E501
            'status': (PurchaseOrderStatusEnum, str, none_type,),
            'issue_date': (datetime, none_type, none_type,),  # noqa: E501
            'delivery_date': (datetime, none_type, none_type,),  # noqa: E501
            'delivery_address': (str, none_type, none_type,),  # noqa: E501
            'customer': (str, none_type, none_type,),  # noqa: E501
            'vendor': (str, none_type, none_type,),  # noqa: E501
            'memo': (str, none_type, none_type,),  # noqa: E501
            'total_amount': (float, none_type, none_type,),  # noqa: E501
            'currency': (CurrencyEnum, str, none_type,),
            'line_items': ([PurchaseOrderLineItem], none_type,),  # noqa: E501
            'remote_created_at': (datetime, none_type, none_type,),  # noqa: E501
            'remote_updated_at': (datetime, none_type, none_type,),  # noqa: E501
            'remote_was_deleted': (bool, none_type,),  # noqa: E501
        }
        expands_types = {"delivery_address": "Address", "line_items": "PurchaseOrderLineItem"}

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
        'remote_data': 'remote_data',  # noqa: E501
        'status': 'status',  # noqa: E501
        'issue_date': 'issue_date',  # noqa: E501
        'delivery_date': 'delivery_date',  # noqa: E501
        'delivery_address': 'delivery_address',  # noqa: E501
        'customer': 'customer',  # noqa: E501
        'vendor': 'vendor',  # noqa: E501
        'memo': 'memo',  # noqa: E501
        'total_amount': 'total_amount',  # noqa: E501
        'currency': 'currency',  # noqa: E501
        'line_items': 'line_items',  # noqa: E501
        'remote_created_at': 'remote_created_at',  # noqa: E501
        'remote_updated_at': 'remote_updated_at',  # noqa: E501
        'remote_was_deleted': 'remote_was_deleted',  # noqa: E501
    }

    read_only_vars = {
        'id',  # noqa: E501
        'remote_data',  # noqa: E501
        'line_items',  # noqa: E501
        'remote_was_deleted',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """PurchaseOrder - a model defined in OpenAPI

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
            remote_data ([RemoteData], none_type): [optional]  # noqa: E501
            status (bool, dict, float, int, list, str, none_type): The purchase order's status.. [optional]  # noqa: E501
            issue_date (datetime, none_type): The purchase order's issue date.. [optional]  # noqa: E501
            delivery_date (datetime, none_type): The purchase order's delivery date.. [optional]  # noqa: E501
            delivery_address (str, none_type): The purchase order's delivery address.. [optional]  # noqa: E501
            customer (str, none_type): The purchase order's customer.. [optional]  # noqa: E501
            vendor (str, none_type): The purchase_order's vendor.. [optional]  # noqa: E501
            memo (str, none_type): A memo attached to the purchase order.. [optional]  # noqa: E501
            total_amount (float, none_type): The purchase order's total amount.. [optional]  # noqa: E501
            currency (bool, dict, float, int, list, str, none_type): The purchase order's currency.. [optional]  # noqa: E501
            line_items ([PurchaseOrderLineItem]): [optional]  # noqa: E501
            remote_created_at (datetime, none_type): When the third party's purchase order note was created.. [optional]  # noqa: E501
            remote_updated_at (datetime, none_type): When the third party's purchase order note was updated.. [optional]  # noqa: E501
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
        self.status = kwargs.get("status", None)
        self.issue_date = kwargs.get("issue_date", None)
        self.delivery_date = kwargs.get("delivery_date", None)
        self.delivery_address = kwargs.get("delivery_address", None)
        self.customer = kwargs.get("customer", None)
        self.vendor = kwargs.get("vendor", None)
        self.memo = kwargs.get("memo", None)
        self.total_amount = kwargs.get("total_amount", None)
        self.currency = kwargs.get("currency", None)
        self.remote_created_at = kwargs.get("remote_created_at", None)
        self.remote_updated_at = kwargs.get("remote_updated_at", None)

        # Read only properties
        self._id = kwargs.get("id", str())
        self._remote_data = kwargs.get("remote_data", None)
        self._line_items = kwargs.get("line_items", None)
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
        """PurchaseOrder - a model defined in OpenAPI

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
            remote_data ([RemoteData], none_type): [optional]  # noqa: E501
            status (bool, dict, float, int, list, str, none_type): The purchase order's status.. [optional]  # noqa: E501
            issue_date (datetime, none_type): The purchase order's issue date.. [optional]  # noqa: E501
            delivery_date (datetime, none_type): The purchase order's delivery date.. [optional]  # noqa: E501
            delivery_address (str, none_type): The purchase order's delivery address.. [optional]  # noqa: E501
            customer (str, none_type): The purchase order's customer.. [optional]  # noqa: E501
            vendor (str, none_type): The purchase_order's vendor.. [optional]  # noqa: E501
            memo (str, none_type): A memo attached to the purchase order.. [optional]  # noqa: E501
            total_amount (float, none_type): The purchase order's total amount.. [optional]  # noqa: E501
            currency (bool, dict, float, int, list, str, none_type): The purchase order's currency.. [optional]  # noqa: E501
            line_items ([PurchaseOrderLineItem]): [optional]  # noqa: E501
            remote_created_at (datetime, none_type): When the third party's purchase order note was created.. [optional]  # noqa: E501
            remote_updated_at (datetime, none_type): When the third party's purchase order note was updated.. [optional]  # noqa: E501
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
        self.status: Union[bool, dict, float, int, list, str, none_type] = kwargs.get("status", None)
        self.issue_date: Union[datetime, none_type] = kwargs.get("issue_date", None)
        self.delivery_date: Union[datetime, none_type] = kwargs.get("delivery_date", None)
        self.delivery_address: Union[str, none_type] = kwargs.get("delivery_address", None)
        self.customer: Union[str, none_type] = kwargs.get("customer", None)
        self.vendor: Union[str, none_type] = kwargs.get("vendor", None)
        self.memo: Union[str, none_type] = kwargs.get("memo", None)
        self.total_amount: Union[float, none_type] = kwargs.get("total_amount", None)
        self.currency: Union[bool, dict, float, int, list, str, none_type] = kwargs.get("currency", None)
        self.remote_created_at: Union[datetime, none_type] = kwargs.get("remote_created_at", None)
        self.remote_updated_at: Union[datetime, none_type] = kwargs.get("remote_updated_at", None)

        # Read only properties
        self._id: Union[str] = kwargs.get("id", str())
        self._remote_data: Union[List["RemoteData"]] = kwargs.get("remote_data", None)
        self._line_items: Union[List["PurchaseOrderLineItem"]] = kwargs.get("line_items", None)
        self._remote_was_deleted: Union[bool] = kwargs.get("remote_was_deleted", bool())

    # Read only property getters
    @property
    def id(self):
        return self._id

    @property
    def remote_data(self):
        return self._remote_data

    @property
    def line_items(self):
        return self._line_items

    @property
    def remote_was_deleted(self):
        return self._remote_was_deleted



