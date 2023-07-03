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
    from MergePythonSDK.shared.model.categories_enum import CategoriesEnum
    from MergePythonSDK.crm.model.common_model_scopes_body_request import CommonModelScopesBodyRequest
    globals()['CategoriesEnum'] = CategoriesEnum
    globals()['CommonModelScopesBodyRequest'] = CommonModelScopesBodyRequest

class EndUserDetailsRequest(ModelNormal):
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
        ('end_user_email_address',): {
            'max_length': 100,
            'min_length': 1,
        },
        ('end_user_organization_name',): {
            'max_length': 100,
            'min_length': 1,
        },
        ('end_user_origin_id',): {
            'max_length': 100,
            'min_length': 1,
        },
        ('integration',): {
            'min_length': 1,
        },
        ('link_expiry_mins',): {
            'inclusive_maximum': 10080,
            'inclusive_minimum': 30,
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
            'end_user_email_address': (str,),  # noqa: E501
            'end_user_organization_name': (str,),  # noqa: E501
            'end_user_origin_id': (str,),  # noqa: E501
            'categories': ([CategoriesEnum],),  # noqa: E501
            'integration': (str, none_type, none_type,),  # noqa: E501
            'link_expiry_mins': (int, none_type,),  # noqa: E501
            'should_create_magic_link_url': (bool, none_type, none_type,),  # noqa: E501
            'common_models': ([CommonModelScopesBodyRequest], none_type, none_type,),  # noqa: E501
        }
        return defined_types

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'end_user_email_address': 'end_user_email_address',  # noqa: E501
        'end_user_organization_name': 'end_user_organization_name',  # noqa: E501
        'end_user_origin_id': 'end_user_origin_id',  # noqa: E501
        'categories': 'categories',  # noqa: E501
        'integration': 'integration',  # noqa: E501
        'link_expiry_mins': 'link_expiry_mins',  # noqa: E501
        'should_create_magic_link_url': 'should_create_magic_link_url',  # noqa: E501
        'common_models': 'common_models',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, end_user_email_address, end_user_organization_name, end_user_origin_id, categories, *args, **kwargs):  # noqa: E501
        """EndUserDetailsRequest - a model defined in OpenAPI

        Args:
            end_user_email_address (str): Your end user's email address. This is purely for identification purposes - setting this value will not cause any emails to be sent.
            end_user_organization_name (str): Your end user's organization.
            end_user_origin_id (str): This unique identifier typically represents the ID for your end user in your product's database. This value must be distinct from other Linked Accounts' unique identifiers.
            categories ([CategoriesEnum]): The integration categories to show in Merge Link.

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
            integration (str, none_type): The slug of a specific pre-selected integration for this linking flow token. For examples of slugs, see https://www.merge.dev/docs/basics/integration-metadata/.. [optional]  # noqa: E501
            link_expiry_mins (int): An integer number of minutes between [30, 720 or 10080 if for a Magic Link URL] for how long this token is valid. Defaults to 30.. [optional] if omitted the server will use the default value of 30  # noqa: E501
            should_create_magic_link_url (bool, none_type): Whether to generate a Magic Link URL. Defaults to false. For more information on Magic Link, see https://merge.dev/blog/product/integrations,-fast.-say-hello-to-magic-link/.. [optional] if omitted the server will use the default value of False  # noqa: E501
            common_models ([CommonModelScopesBodyRequest], none_type): An array of objects to specify the models and fields that will be disabled for a given Linked Account. Each object uses model_id, enabled_actions, and disabled_fields to specify the model, method, and fields that are scoped for a given Linked Account.. [optional]  # noqa: E501
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


        self.end_user_email_address = end_user_email_address
        self.end_user_organization_name = end_user_organization_name
        self.end_user_origin_id = end_user_origin_id
        self.categories = categories
        self.integration = kwargs.get("integration", None)
        self.link_expiry_mins = kwargs.get("link_expiry_mins", 30)
        self.should_create_magic_link_url = kwargs.get("should_create_magic_link_url", False)
        self.common_models = kwargs.get("common_models", None)
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
    def __init__(self, end_user_email_address, end_user_organization_name, end_user_origin_id, categories, *args, **kwargs):  # noqa: E501
        """EndUserDetailsRequest - a model defined in OpenAPI

        Args:
            end_user_email_address (str): Your end user's email address. This is purely for identification purposes - setting this value will not cause any emails to be sent.
            end_user_organization_name (str): Your end user's organization.
            end_user_origin_id (str): This unique identifier typically represents the ID for your end user in your product's database. This value must be distinct from other Linked Accounts' unique identifiers.
            categories ([CategoriesEnum]): The integration categories to show in Merge Link.

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
            integration (str, none_type): The slug of a specific pre-selected integration for this linking flow token. For examples of slugs, see https://www.merge.dev/docs/basics/integration-metadata/.. [optional]  # noqa: E501
            link_expiry_mins (int): An integer number of minutes between [30, 720 or 10080 if for a Magic Link URL] for how long this token is valid. Defaults to 30.. [optional] if omitted the server will use the default value of 30  # noqa: E501
            should_create_magic_link_url (bool, none_type): Whether to generate a Magic Link URL. Defaults to false. For more information on Magic Link, see https://merge.dev/blog/product/integrations,-fast.-say-hello-to-magic-link/.. [optional] if omitted the server will use the default value of False  # noqa: E501
            common_models ([CommonModelScopesBodyRequest], none_type): An array of objects to specify the models and fields that will be disabled for a given Linked Account. Each object uses model_id, enabled_actions, and disabled_fields to specify the model, method, and fields that are scoped for a given Linked Account.. [optional]  # noqa: E501
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

        self.end_user_email_address: Union[str] = end_user_email_address
        self.end_user_organization_name: Union[str] = end_user_organization_name
        self.end_user_origin_id: Union[str] = end_user_origin_id
        self.categories: Union[List["CategoriesEnum"]] = categories
        self.integration: Union[str, none_type] = kwargs.get("integration", None)
        self.link_expiry_mins: Union[int] = kwargs.get("link_expiry_mins", 30)
        self.should_create_magic_link_url: Union[bool, none_type] = kwargs.get("should_create_magic_link_url", False)
        self.common_models: Union[List["CommonModelScopesBodyRequest"]] = kwargs.get("common_models", None)


