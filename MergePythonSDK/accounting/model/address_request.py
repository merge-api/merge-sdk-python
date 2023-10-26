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
    from MergePythonSDK.accounting.model.address_type_enum import AddressTypeEnum
    from MergePythonSDK.accounting.model.country_enum import CountryEnum
    globals()['AddressTypeEnum'] = AddressTypeEnum
    globals()['CountryEnum'] = CountryEnum

class AddressRequest(ModelNormal):
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
            'type': (AddressTypeEnum, str, none_type,),
            'street_1': (str, none_type, none_type,),  # noqa: E501
            'street_2': (str, none_type, none_type,),  # noqa: E501
            'city': (str, none_type, none_type,),  # noqa: E501
            'country_subdivision': (str, none_type, none_type,),  # noqa: E501
            'country': (CountryEnum, str, none_type,),
            'zip_code': (str, none_type, none_type,),  # noqa: E501
            'integration_params': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type, none_type,),  # noqa: E501
            'linked_account_params': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type, none_type,),  # noqa: E501
        }
        return defined_types

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'type': 'type',  # noqa: E501
        'street_1': 'street_1',  # noqa: E501
        'street_2': 'street_2',  # noqa: E501
        'city': 'city',  # noqa: E501
        'country_subdivision': 'country_subdivision',  # noqa: E501
        'country': 'country',  # noqa: E501
        'zip_code': 'zip_code',  # noqa: E501
        'integration_params': 'integration_params',  # noqa: E501
        'linked_account_params': 'linked_account_params',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """AddressRequest - a model defined in OpenAPI

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
            type (bool, date, datetime, dict, float, int, list, str, none_type): The address type.  * `BILLING` - BILLING * `SHIPPING` - SHIPPING. [optional]  # noqa: E501
            street_1 (str, none_type): Line 1 of the address's street.. [optional]  # noqa: E501
            street_2 (str, none_type): Line 2 of the address's street.. [optional]  # noqa: E501
            city (str, none_type): The address's city.. [optional]  # noqa: E501
            country_subdivision (str, none_type): The address's state or region.. [optional]  # noqa: E501
            country (bool, date, datetime, dict, float, int, list, str, none_type): The address's country.  * `AF` - Afghanistan * `AX` - Åland Islands * `AL` - Albania * `DZ` - Algeria * `AS` - American Samoa * `AD` - Andorra * `AO` - Angola * `AI` - Anguilla * `AQ` - Antarctica * `AG` - Antigua and Barbuda * `AR` - Argentina * `AM` - Armenia * `AW` - Aruba * `AU` - Australia * `AT` - Austria * `AZ` - Azerbaijan * `BS` - Bahamas * `BH` - Bahrain * `BD` - Bangladesh * `BB` - Barbados * `BY` - Belarus * `BE` - Belgium * `BZ` - Belize * `BJ` - Benin * `BM` - Bermuda * `BT` - Bhutan * `BO` - Bolivia * `BQ` - Bonaire, Sint Eustatius and Saba * `BA` - Bosnia and Herzegovina * `BW` - Botswana * `BV` - Bouvet Island * `BR` - Brazil * `IO` - British Indian Ocean Territory * `BN` - Brunei * `BG` - Bulgaria * `BF` - Burkina Faso * `BI` - Burundi * `CV` - Cabo Verde * `KH` - Cambodia * `CM` - Cameroon * `CA` - Canada * `KY` - Cayman Islands * `CF` - Central African Republic * `TD` - Chad * `CL` - Chile * `CN` - China * `CX` - Christmas Island * `CC` - Cocos (Keeling) Islands * `CO` - Colombia * `KM` - Comoros * `CG` - Congo * `CD` - Congo (the Democratic Republic of the) * `CK` - Cook Islands * `CR` - Costa Rica * `CI` - Côte d'Ivoire * `HR` - Croatia * `CU` - Cuba * `CW` - Curaçao * `CY` - Cyprus * `CZ` - Czechia * `DK` - Denmark * `DJ` - Djibouti * `DM` - Dominica * `DO` - Dominican Republic * `EC` - Ecuador * `EG` - Egypt * `SV` - El Salvador * `GQ` - Equatorial Guinea * `ER` - Eritrea * `EE` - Estonia * `SZ` - Eswatini * `ET` - Ethiopia * `FK` - Falkland Islands (Malvinas) * `FO` - Faroe Islands * `FJ` - Fiji * `FI` - Finland * `FR` - France * `GF` - French Guiana * `PF` - French Polynesia * `TF` - French Southern Territories * `GA` - Gabon * `GM` - Gambia * `GE` - Georgia * `DE` - Germany * `GH` - Ghana * `GI` - Gibraltar * `GR` - Greece * `GL` - Greenland * `GD` - Grenada * `GP` - Guadeloupe * `GU` - Guam * `GT` - Guatemala * `GG` - Guernsey * `GN` - Guinea * `GW` - Guinea-Bissau * `GY` - Guyana * `HT` - Haiti * `HM` - Heard Island and McDonald Islands * `VA` - Holy See * `HN` - Honduras * `HK` - Hong Kong * `HU` - Hungary * `IS` - Iceland * `IN` - India * `ID` - Indonesia * `IR` - Iran * `IQ` - Iraq * `IE` - Ireland * `IM` - Isle of Man * `IL` - Israel * `IT` - Italy * `JM` - Jamaica * `JP` - Japan * `JE` - Jersey * `JO` - Jordan * `KZ` - Kazakhstan * `KE` - Kenya * `KI` - Kiribati * `KW` - Kuwait * `KG` - Kyrgyzstan * `LA` - Laos * `LV` - Latvia * `LB` - Lebanon * `LS` - Lesotho * `LR` - Liberia * `LY` - Libya * `LI` - Liechtenstein * `LT` - Lithuania * `LU` - Luxembourg * `MO` - Macao * `MG` - Madagascar * `MW` - Malawi * `MY` - Malaysia * `MV` - Maldives * `ML` - Mali * `MT` - Malta * `MH` - Marshall Islands * `MQ` - Martinique * `MR` - Mauritania * `MU` - Mauritius * `YT` - Mayotte * `MX` - Mexico * `FM` - Micronesia (Federated States of) * `MD` - Moldova * `MC` - Monaco * `MN` - Mongolia * `ME` - Montenegro * `MS` - Montserrat * `MA` - Morocco * `MZ` - Mozambique * `MM` - Myanmar * `NA` - Namibia * `NR` - Nauru * `NP` - Nepal * `NL` - Netherlands * `NC` - New Caledonia * `NZ` - New Zealand * `NI` - Nicaragua * `NE` - Niger * `NG` - Nigeria * `NU` - Niue * `NF` - Norfolk Island * `KP` - North Korea * `MK` - North Macedonia * `MP` - Northern Mariana Islands * `NO` - Norway * `OM` - Oman * `PK` - Pakistan * `PW` - Palau * `PS` - Palestine, State of * `PA` - Panama * `PG` - Papua New Guinea * `PY` - Paraguay * `PE` - Peru * `PH` - Philippines * `PN` - Pitcairn * `PL` - Poland * `PT` - Portugal * `PR` - Puerto Rico * `QA` - Qatar * `RE` - Réunion * `RO` - Romania * `RU` - Russia * `RW` - Rwanda * `BL` - Saint Barthélemy * `SH` - Saint Helena, Ascension and Tristan da Cunha * `KN` - Saint Kitts and Nevis * `LC` - Saint Lucia * `MF` - Saint Martin (French part) * `PM` - Saint Pierre and Miquelon * `VC` - Saint Vincent and the Grenadines * `WS` - Samoa * `SM` - San Marino * `ST` - Sao Tome and Principe * `SA` - Saudi Arabia * `SN` - Senegal * `RS` - Serbia * `SC` - Seychelles * `SL` - Sierra Leone * `SG` - Singapore * `SX` - Sint Maarten (Dutch part) * `SK` - Slovakia * `SI` - Slovenia * `SB` - Solomon Islands * `SO` - Somalia * `ZA` - South Africa * `GS` - South Georgia and the South Sandwich Islands * `KR` - South Korea * `SS` - South Sudan * `ES` - Spain * `LK` - Sri Lanka * `SD` - Sudan * `SR` - Suriname * `SJ` - Svalbard and Jan Mayen * `SE` - Sweden * `CH` - Switzerland * `SY` - Syria * `TW` - Taiwan * `TJ` - Tajikistan * `TZ` - Tanzania * `TH` - Thailand * `TL` - Timor-Leste * `TG` - Togo * `TK` - Tokelau * `TO` - Tonga * `TT` - Trinidad and Tobago * `TN` - Tunisia * `TR` - Turkey * `TM` - Turkmenistan * `TC` - Turks and Caicos Islands * `TV` - Tuvalu * `UG` - Uganda * `UA` - Ukraine * `AE` - United Arab Emirates * `GB` - United Kingdom * `UM` - United States Minor Outlying Islands * `US` - United States of America * `UY` - Uruguay * `UZ` - Uzbekistan * `VU` - Vanuatu * `VE` - Venezuela * `VN` - Vietnam * `VG` - Virgin Islands (British) * `VI` - Virgin Islands (U.S.) * `WF` - Wallis and Futuna * `EH` - Western Sahara * `YE` - Yemen * `ZM` - Zambia * `ZW` - Zimbabwe. [optional]  # noqa: E501
            zip_code (str, none_type): The address's zip code.. [optional]  # noqa: E501
            integration_params ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): [optional]  # noqa: E501
            linked_account_params ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): [optional]  # noqa: E501
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


        self.type = kwargs.get("type", None)
        self.street_1 = kwargs.get("street_1", None)
        self.street_2 = kwargs.get("street_2", None)
        self.city = kwargs.get("city", None)
        self.country_subdivision = kwargs.get("country_subdivision", None)
        self.country = kwargs.get("country", None)
        self.zip_code = kwargs.get("zip_code", None)
        self.integration_params = kwargs.get("integration_params", None)
        self.linked_account_params = kwargs.get("linked_account_params", None)
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
        """AddressRequest - a model defined in OpenAPI

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
            type (bool, date, datetime, dict, float, int, list, str, none_type): The address type.  * `BILLING` - BILLING * `SHIPPING` - SHIPPING. [optional]  # noqa: E501
            street_1 (str, none_type): Line 1 of the address's street.. [optional]  # noqa: E501
            street_2 (str, none_type): Line 2 of the address's street.. [optional]  # noqa: E501
            city (str, none_type): The address's city.. [optional]  # noqa: E501
            country_subdivision (str, none_type): The address's state or region.. [optional]  # noqa: E501
            country (bool, date, datetime, dict, float, int, list, str, none_type): The address's country.  * `AF` - Afghanistan * `AX` - Åland Islands * `AL` - Albania * `DZ` - Algeria * `AS` - American Samoa * `AD` - Andorra * `AO` - Angola * `AI` - Anguilla * `AQ` - Antarctica * `AG` - Antigua and Barbuda * `AR` - Argentina * `AM` - Armenia * `AW` - Aruba * `AU` - Australia * `AT` - Austria * `AZ` - Azerbaijan * `BS` - Bahamas * `BH` - Bahrain * `BD` - Bangladesh * `BB` - Barbados * `BY` - Belarus * `BE` - Belgium * `BZ` - Belize * `BJ` - Benin * `BM` - Bermuda * `BT` - Bhutan * `BO` - Bolivia * `BQ` - Bonaire, Sint Eustatius and Saba * `BA` - Bosnia and Herzegovina * `BW` - Botswana * `BV` - Bouvet Island * `BR` - Brazil * `IO` - British Indian Ocean Territory * `BN` - Brunei * `BG` - Bulgaria * `BF` - Burkina Faso * `BI` - Burundi * `CV` - Cabo Verde * `KH` - Cambodia * `CM` - Cameroon * `CA` - Canada * `KY` - Cayman Islands * `CF` - Central African Republic * `TD` - Chad * `CL` - Chile * `CN` - China * `CX` - Christmas Island * `CC` - Cocos (Keeling) Islands * `CO` - Colombia * `KM` - Comoros * `CG` - Congo * `CD` - Congo (the Democratic Republic of the) * `CK` - Cook Islands * `CR` - Costa Rica * `CI` - Côte d'Ivoire * `HR` - Croatia * `CU` - Cuba * `CW` - Curaçao * `CY` - Cyprus * `CZ` - Czechia * `DK` - Denmark * `DJ` - Djibouti * `DM` - Dominica * `DO` - Dominican Republic * `EC` - Ecuador * `EG` - Egypt * `SV` - El Salvador * `GQ` - Equatorial Guinea * `ER` - Eritrea * `EE` - Estonia * `SZ` - Eswatini * `ET` - Ethiopia * `FK` - Falkland Islands (Malvinas) * `FO` - Faroe Islands * `FJ` - Fiji * `FI` - Finland * `FR` - France * `GF` - French Guiana * `PF` - French Polynesia * `TF` - French Southern Territories * `GA` - Gabon * `GM` - Gambia * `GE` - Georgia * `DE` - Germany * `GH` - Ghana * `GI` - Gibraltar * `GR` - Greece * `GL` - Greenland * `GD` - Grenada * `GP` - Guadeloupe * `GU` - Guam * `GT` - Guatemala * `GG` - Guernsey * `GN` - Guinea * `GW` - Guinea-Bissau * `GY` - Guyana * `HT` - Haiti * `HM` - Heard Island and McDonald Islands * `VA` - Holy See * `HN` - Honduras * `HK` - Hong Kong * `HU` - Hungary * `IS` - Iceland * `IN` - India * `ID` - Indonesia * `IR` - Iran * `IQ` - Iraq * `IE` - Ireland * `IM` - Isle of Man * `IL` - Israel * `IT` - Italy * `JM` - Jamaica * `JP` - Japan * `JE` - Jersey * `JO` - Jordan * `KZ` - Kazakhstan * `KE` - Kenya * `KI` - Kiribati * `KW` - Kuwait * `KG` - Kyrgyzstan * `LA` - Laos * `LV` - Latvia * `LB` - Lebanon * `LS` - Lesotho * `LR` - Liberia * `LY` - Libya * `LI` - Liechtenstein * `LT` - Lithuania * `LU` - Luxembourg * `MO` - Macao * `MG` - Madagascar * `MW` - Malawi * `MY` - Malaysia * `MV` - Maldives * `ML` - Mali * `MT` - Malta * `MH` - Marshall Islands * `MQ` - Martinique * `MR` - Mauritania * `MU` - Mauritius * `YT` - Mayotte * `MX` - Mexico * `FM` - Micronesia (Federated States of) * `MD` - Moldova * `MC` - Monaco * `MN` - Mongolia * `ME` - Montenegro * `MS` - Montserrat * `MA` - Morocco * `MZ` - Mozambique * `MM` - Myanmar * `NA` - Namibia * `NR` - Nauru * `NP` - Nepal * `NL` - Netherlands * `NC` - New Caledonia * `NZ` - New Zealand * `NI` - Nicaragua * `NE` - Niger * `NG` - Nigeria * `NU` - Niue * `NF` - Norfolk Island * `KP` - North Korea * `MK` - North Macedonia * `MP` - Northern Mariana Islands * `NO` - Norway * `OM` - Oman * `PK` - Pakistan * `PW` - Palau * `PS` - Palestine, State of * `PA` - Panama * `PG` - Papua New Guinea * `PY` - Paraguay * `PE` - Peru * `PH` - Philippines * `PN` - Pitcairn * `PL` - Poland * `PT` - Portugal * `PR` - Puerto Rico * `QA` - Qatar * `RE` - Réunion * `RO` - Romania * `RU` - Russia * `RW` - Rwanda * `BL` - Saint Barthélemy * `SH` - Saint Helena, Ascension and Tristan da Cunha * `KN` - Saint Kitts and Nevis * `LC` - Saint Lucia * `MF` - Saint Martin (French part) * `PM` - Saint Pierre and Miquelon * `VC` - Saint Vincent and the Grenadines * `WS` - Samoa * `SM` - San Marino * `ST` - Sao Tome and Principe * `SA` - Saudi Arabia * `SN` - Senegal * `RS` - Serbia * `SC` - Seychelles * `SL` - Sierra Leone * `SG` - Singapore * `SX` - Sint Maarten (Dutch part) * `SK` - Slovakia * `SI` - Slovenia * `SB` - Solomon Islands * `SO` - Somalia * `ZA` - South Africa * `GS` - South Georgia and the South Sandwich Islands * `KR` - South Korea * `SS` - South Sudan * `ES` - Spain * `LK` - Sri Lanka * `SD` - Sudan * `SR` - Suriname * `SJ` - Svalbard and Jan Mayen * `SE` - Sweden * `CH` - Switzerland * `SY` - Syria * `TW` - Taiwan * `TJ` - Tajikistan * `TZ` - Tanzania * `TH` - Thailand * `TL` - Timor-Leste * `TG` - Togo * `TK` - Tokelau * `TO` - Tonga * `TT` - Trinidad and Tobago * `TN` - Tunisia * `TR` - Turkey * `TM` - Turkmenistan * `TC` - Turks and Caicos Islands * `TV` - Tuvalu * `UG` - Uganda * `UA` - Ukraine * `AE` - United Arab Emirates * `GB` - United Kingdom * `UM` - United States Minor Outlying Islands * `US` - United States of America * `UY` - Uruguay * `UZ` - Uzbekistan * `VU` - Vanuatu * `VE` - Venezuela * `VN` - Vietnam * `VG` - Virgin Islands (British) * `VI` - Virgin Islands (U.S.) * `WF` - Wallis and Futuna * `EH` - Western Sahara * `YE` - Yemen * `ZM` - Zambia * `ZW` - Zimbabwe. [optional]  # noqa: E501
            zip_code (str, none_type): The address's zip code.. [optional]  # noqa: E501
            integration_params ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): [optional]  # noqa: E501
            linked_account_params ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): [optional]  # noqa: E501
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

        self.type: Union[bool, date, datetime, dict, float, int, list, str, none_type] = kwargs.get("type", None)
        self.street_1: Union[str, none_type] = kwargs.get("street_1", None)
        self.street_2: Union[str, none_type] = kwargs.get("street_2", None)
        self.city: Union[str, none_type] = kwargs.get("city", None)
        self.country_subdivision: Union[str, none_type] = kwargs.get("country_subdivision", None)
        self.country: Union[bool, date, datetime, dict, float, int, list, str, none_type] = kwargs.get("country", None)
        self.zip_code: Union[str, none_type] = kwargs.get("zip_code", None)
        self.integration_params: Union[Dict[str, bool, date, datetime, dict, float, int, list, str, none_type], none_type] = kwargs.get("integration_params", None)
        self.linked_account_params: Union[Dict[str, bool, date, datetime, dict, float, int, list, str, none_type], none_type] = kwargs.get("linked_account_params", None)


