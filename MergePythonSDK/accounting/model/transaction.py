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
    from MergePythonSDK.shared.model.remote_data import RemoteData
    from MergePythonSDK.accounting.model.transaction_line_item import TransactionLineItem
    globals()['CurrencyEnum'] = CurrencyEnum
    globals()['RemoteData'] = RemoteData
    globals()['TransactionLineItem'] = TransactionLineItem

class Transaction(ModelNormal):
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
        ('total_amount',): {
            'regex': {
                'pattern': r'^-?\d{0,32}(?:\.\d{0,16})?$',  # noqa: E501
            },
        },
        ('exchange_rate',): {
            'regex': {
                'pattern': r'^-?\d{0,32}(?:\.\d{0,16})?$',  # noqa: E501
            },
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
            'transaction_type': (str, none_type, none_type,),  # noqa: E501
            'number': (str, none_type, none_type,),  # noqa: E501
            'transaction_date': (datetime, none_type, none_type,),  # noqa: E501
            'account': (str, none_type, none_type,),  # noqa: E501
            'contact': (str, none_type, none_type,),  # noqa: E501
            'total_amount': (str, none_type, none_type,),  # noqa: E501
            'currency': (CurrencyEnum, str, none_type,),
            'exchange_rate': (str, none_type, none_type,),  # noqa: E501
            'company': (str, none_type, none_type,),  # noqa: E501
            'tracking_categories': ([str, none_type], none_type,),  # noqa: E501
            'line_items': ([TransactionLineItem], none_type,),  # noqa: E501
            'remote_was_deleted': (bool, none_type,),  # noqa: E501
            'id': (str, none_type,),  # noqa: E501
            'remote_id': (str, none_type, none_type,),  # noqa: E501
            'modified_at': (datetime, none_type,),  # noqa: E501
            'field_mappings': ({str: (bool, dict, float, int, list, str, none_type)}, none_type, none_type,),  # noqa: E501
            'remote_data': ([RemoteData], none_type, none_type,),  # noqa: E501
        }
        expands_types = {"account": "Account", "contact": "Contact", "line_items": "TransactionLineItem", "tracking_categories": "TrackingCategory"}

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
        'transaction_type': 'transaction_type',  # noqa: E501
        'number': 'number',  # noqa: E501
        'transaction_date': 'transaction_date',  # noqa: E501
        'account': 'account',  # noqa: E501
        'contact': 'contact',  # noqa: E501
        'total_amount': 'total_amount',  # noqa: E501
        'currency': 'currency',  # noqa: E501
        'exchange_rate': 'exchange_rate',  # noqa: E501
        'company': 'company',  # noqa: E501
        'tracking_categories': 'tracking_categories',  # noqa: E501
        'line_items': 'line_items',  # noqa: E501
        'remote_was_deleted': 'remote_was_deleted',  # noqa: E501
        'id': 'id',  # noqa: E501
        'remote_id': 'remote_id',  # noqa: E501
        'modified_at': 'modified_at',  # noqa: E501
        'field_mappings': 'field_mappings',  # noqa: E501
        'remote_data': 'remote_data',  # noqa: E501
    }

    read_only_vars = {
        'line_items',  # noqa: E501
        'remote_was_deleted',  # noqa: E501
        'id',  # noqa: E501
        'modified_at',  # noqa: E501
        'field_mappings',  # noqa: E501
        'remote_data',  # noqa: E501
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Transaction - a model defined in OpenAPI

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
            transaction_type (str, none_type): The type of transaction, which can by any transaction object not already included in Merge’s common model.. [optional]  # noqa: E501
            number (str, none_type): The transaction's number used for identifying purposes.. [optional]  # noqa: E501
            transaction_date (datetime, none_type): The date upon which the transaction occurred.. [optional]  # noqa: E501
            account (str, none_type): The transaction's account.. [optional]  # noqa: E501
            contact (str, none_type): The contact to whom the transaction relates to.. [optional]  # noqa: E501
            total_amount (str, none_type): The total amount being paid after taxes.. [optional]  # noqa: E501
            currency (bool, dict, float, int, list, str, none_type): The transaction's currency.  * `XUA` - ADB Unit of Account * `AFN` - Afghan Afghani * `AFA` - Afghan Afghani (1927–2002) * `ALL` - Albanian Lek * `ALK` - Albanian Lek (1946–1965) * `DZD` - Algerian Dinar * `ADP` - Andorran Peseta * `AOA` - Angolan Kwanza * `AOK` - Angolan Kwanza (1977–1991) * `AON` - Angolan New Kwanza (1990–2000) * `AOR` - Angolan Readjusted Kwanza (1995–1999) * `ARA` - Argentine Austral * `ARS` - Argentine Peso * `ARM` - Argentine Peso (1881–1970) * `ARP` - Argentine Peso (1983–1985) * `ARL` - Argentine Peso Ley (1970–1983) * `AMD` - Armenian Dram * `AWG` - Aruban Florin * `AUD` - Australian Dollar * `ATS` - Austrian Schilling * `AZN` - Azerbaijani Manat * `AZM` - Azerbaijani Manat (1993–2006) * `BSD` - Bahamian Dollar * `BHD` - Bahraini Dinar * `BDT` - Bangladeshi Taka * `BBD` - Barbadian Dollar * `BYN` - Belarusian Ruble * `BYB` - Belarusian Ruble (1994–1999) * `BYR` - Belarusian Ruble (2000–2016) * `BEF` - Belgian Franc * `BEC` - Belgian Franc (convertible) * `BEL` - Belgian Franc (financial) * `BZD` - Belize Dollar * `BMD` - Bermudan Dollar * `BTN` - Bhutanese Ngultrum * `BOB` - Bolivian Boliviano * `BOL` - Bolivian Boliviano (1863–1963) * `BOV` - Bolivian Mvdol * `BOP` - Bolivian Peso * `BAM` - Bosnia-Herzegovina Convertible Mark * `BAD` - Bosnia-Herzegovina Dinar (1992–1994) * `BAN` - Bosnia-Herzegovina New Dinar (1994–1997) * `BWP` - Botswanan Pula * `BRC` - Brazilian Cruzado (1986–1989) * `BRZ` - Brazilian Cruzeiro (1942–1967) * `BRE` - Brazilian Cruzeiro (1990–1993) * `BRR` - Brazilian Cruzeiro (1993–1994) * `BRN` - Brazilian New Cruzado (1989–1990) * `BRB` - Brazilian New Cruzeiro (1967–1986) * `BRL` - Brazilian Real * `GBP` - British Pound * `BND` - Brunei Dollar * `BGL` - Bulgarian Hard Lev * `BGN` - Bulgarian Lev * `BGO` - Bulgarian Lev (1879–1952) * `BGM` - Bulgarian Socialist Lev * `BUK` - Burmese Kyat * `BIF` - Burundian Franc * `XPF` - CFP Franc * `KHR` - Cambodian Riel * `CAD` - Canadian Dollar * `CVE` - Cape Verdean Escudo * `KYD` - Cayman Islands Dollar * `XAF` - Central African CFA Franc * `CLE` - Chilean Escudo * `CLP` - Chilean Peso * `CLF` - Chilean Unit of Account (UF) * `CNX` - Chinese People’s Bank Dollar * `CNY` - Chinese Yuan * `CNH` - Chinese Yuan (offshore) * `COP` - Colombian Peso * `COU` - Colombian Real Value Unit * `KMF` - Comorian Franc * `CDF` - Congolese Franc * `CRC` - Costa Rican Colón * `HRD` - Croatian Dinar * `HRK` - Croatian Kuna * `CUC` - Cuban Convertible Peso * `CUP` - Cuban Peso * `CYP` - Cypriot Pound * `CZK` - Czech Koruna * `CSK` - Czechoslovak Hard Koruna * `DKK` - Danish Krone * `DJF` - Djiboutian Franc * `DOP` - Dominican Peso * `NLG` - Dutch Guilder * `XCD` - East Caribbean Dollar * `DDM` - East German Mark * `ECS` - Ecuadorian Sucre * `ECV` - Ecuadorian Unit of Constant Value * `EGP` - Egyptian Pound * `GQE` - Equatorial Guinean Ekwele * `ERN` - Eritrean Nakfa * `EEK` - Estonian Kroon * `ETB` - Ethiopian Birr * `EUR` - Euro * `XBA` - European Composite Unit * `XEU` - European Currency Unit * `XBB` - European Monetary Unit * `XBC` - European Unit of Account (XBC) * `XBD` - European Unit of Account (XBD) * `FKP` - Falkland Islands Pound * `FJD` - Fijian Dollar * `FIM` - Finnish Markka * `FRF` - French Franc * `XFO` - French Gold Franc * `XFU` - French UIC-Franc * `GMD` - Gambian Dalasi * `GEK` - Georgian Kupon Larit * `GEL` - Georgian Lari * `DEM` - German Mark * `GHS` - Ghanaian Cedi * `GHC` - Ghanaian Cedi (1979–2007) * `GIP` - Gibraltar Pound * `XAU` - Gold * `GRD` - Greek Drachma * `GTQ` - Guatemalan Quetzal * `GWP` - Guinea-Bissau Peso * `GNF` - Guinean Franc * `GNS` - Guinean Syli * `GYD` - Guyanaese Dollar * `HTG` - Haitian Gourde * `HNL` - Honduran Lempira * `HKD` - Hong Kong Dollar * `HUF` - Hungarian Forint * `IMP` - IMP * `ISK` - Icelandic Króna * `ISJ` - Icelandic Króna (1918–1981) * `INR` - Indian Rupee * `IDR` - Indonesian Rupiah * `IRR` - Iranian Rial * `IQD` - Iraqi Dinar * `IEP` - Irish Pound * `ILS` - Israeli New Shekel * `ILP` - Israeli Pound * `ILR` - Israeli Shekel (1980–1985) * `ITL` - Italian Lira * `JMD` - Jamaican Dollar * `JPY` - Japanese Yen * `JOD` - Jordanian Dinar * `KZT` - Kazakhstani Tenge * `KES` - Kenyan Shilling * `KWD` - Kuwaiti Dinar * `KGS` - Kyrgystani Som * `LAK` - Laotian Kip * `LVL` - Latvian Lats * `LVR` - Latvian Ruble * `LBP` - Lebanese Pound * `LSL` - Lesotho Loti * `LRD` - Liberian Dollar * `LYD` - Libyan Dinar * `LTL` - Lithuanian Litas * `LTT` - Lithuanian Talonas * `LUL` - Luxembourg Financial Franc * `LUC` - Luxembourgian Convertible Franc * `LUF` - Luxembourgian Franc * `MOP` - Macanese Pataca * `MKD` - Macedonian Denar * `MKN` - Macedonian Denar (1992–1993) * `MGA` - Malagasy Ariary * `MGF` - Malagasy Franc * `MWK` - Malawian Kwacha * `MYR` - Malaysian Ringgit * `MVR` - Maldivian Rufiyaa * `MVP` - Maldivian Rupee (1947–1981) * `MLF` - Malian Franc * `MTL` - Maltese Lira * `MTP` - Maltese Pound * `MRU` - Mauritanian Ouguiya * `MRO` - Mauritanian Ouguiya (1973–2017) * `MUR` - Mauritian Rupee * `MXV` - Mexican Investment Unit * `MXN` - Mexican Peso * `MXP` - Mexican Silver Peso (1861–1992) * `MDC` - Moldovan Cupon * `MDL` - Moldovan Leu * `MCF` - Monegasque Franc * `MNT` - Mongolian Tugrik * `MAD` - Moroccan Dirham * `MAF` - Moroccan Franc * `MZE` - Mozambican Escudo * `MZN` - Mozambican Metical * `MZM` - Mozambican Metical (1980–2006) * `MMK` - Myanmar Kyat * `NAD` - Namibian Dollar * `NPR` - Nepalese Rupee * `ANG` - Netherlands Antillean Guilder * `TWD` - New Taiwan Dollar * `NZD` - New Zealand Dollar * `NIO` - Nicaraguan Córdoba * `NIC` - Nicaraguan Córdoba (1988–1991) * `NGN` - Nigerian Naira * `KPW` - North Korean Won * `NOK` - Norwegian Krone * `OMR` - Omani Rial * `PKR` - Pakistani Rupee * `XPD` - Palladium * `PAB` - Panamanian Balboa * `PGK` - Papua New Guinean Kina * `PYG` - Paraguayan Guarani * `PEI` - Peruvian Inti * `PEN` - Peruvian Sol * `PES` - Peruvian Sol (1863–1965) * `PHP` - Philippine Peso * `XPT` - Platinum * `PLN` - Polish Zloty * `PLZ` - Polish Zloty (1950–1995) * `PTE` - Portuguese Escudo * `GWE` - Portuguese Guinea Escudo * `QAR` - Qatari Rial * `XRE` - RINET Funds * `RHD` - Rhodesian Dollar * `RON` - Romanian Leu * `ROL` - Romanian Leu (1952–2006) * `RUB` - Russian Ruble * `RUR` - Russian Ruble (1991–1998) * `RWF` - Rwandan Franc * `SVC` - Salvadoran Colón * `WST` - Samoan Tala * `SAR` - Saudi Riyal * `RSD` - Serbian Dinar * `CSD` - Serbian Dinar (2002–2006) * `SCR` - Seychellois Rupee * `SLL` - Sierra Leonean Leone * `XAG` - Silver * `SGD` - Singapore Dollar * `SKK` - Slovak Koruna * `SIT` - Slovenian Tolar * `SBD` - Solomon Islands Dollar * `SOS` - Somali Shilling * `ZAR` - South African Rand * `ZAL` - South African Rand (financial) * `KRH` - South Korean Hwan (1953–1962) * `KRW` - South Korean Won * `KRO` - South Korean Won (1945–1953) * `SSP` - South Sudanese Pound * `SUR` - Soviet Rouble * `ESP` - Spanish Peseta * `ESA` - Spanish Peseta (A account) * `ESB` - Spanish Peseta (convertible account) * `XDR` - Special Drawing Rights * `LKR` - Sri Lankan Rupee * `SHP` - St. Helena Pound * `XSU` - Sucre * `SDD` - Sudanese Dinar (1992–2007) * `SDG` - Sudanese Pound * `SDP` - Sudanese Pound (1957–1998) * `SRD` - Surinamese Dollar * `SRG` - Surinamese Guilder * `SZL` - Swazi Lilangeni * `SEK` - Swedish Krona * `CHF` - Swiss Franc * `SYP` - Syrian Pound * `STN` - São Tomé & Príncipe Dobra * `STD` - São Tomé & Príncipe Dobra (1977–2017) * `TVD` - TVD * `TJR` - Tajikistani Ruble * `TJS` - Tajikistani Somoni * `TZS` - Tanzanian Shilling * `XTS` - Testing Currency Code * `THB` - Thai Baht * `XXX` - The codes assigned for transactions where no currency is involved * `TPE` - Timorese Escudo * `TOP` - Tongan Paʻanga * `TTD` - Trinidad & Tobago Dollar * `TND` - Tunisian Dinar * `TRY` - Turkish Lira * `TRL` - Turkish Lira (1922–2005) * `TMT` - Turkmenistani Manat * `TMM` - Turkmenistani Manat (1993–2009) * `USD` - US Dollar * `USN` - US Dollar (Next day) * `USS` - US Dollar (Same day) * `UGX` - Ugandan Shilling * `UGS` - Ugandan Shilling (1966–1987) * `UAH` - Ukrainian Hryvnia * `UAK` - Ukrainian Karbovanets * `AED` - United Arab Emirates Dirham * `UYW` - Uruguayan Nominal Wage Index Unit * `UYU` - Uruguayan Peso * `UYP` - Uruguayan Peso (1975–1993) * `UYI` - Uruguayan Peso (Indexed Units) * `UZS` - Uzbekistani Som * `VUV` - Vanuatu Vatu * `VES` - Venezuelan Bolívar * `VEB` - Venezuelan Bolívar (1871–2008) * `VEF` - Venezuelan Bolívar (2008–2018) * `VND` - Vietnamese Dong * `VNN` - Vietnamese Dong (1978–1985) * `CHE` - WIR Euro * `CHW` - WIR Franc * `XOF` - West African CFA Franc * `YDD` - Yemeni Dinar * `YER` - Yemeni Rial * `YUN` - Yugoslavian Convertible Dinar (1990–1992) * `YUD` - Yugoslavian Hard Dinar (1966–1990) * `YUM` - Yugoslavian New Dinar (1994–2002) * `YUR` - Yugoslavian Reformed Dinar (1992–1993) * `ZWN` - ZWN * `ZRN` - Zairean New Zaire (1993–1998) * `ZRZ` - Zairean Zaire (1971–1993) * `ZMW` - Zambian Kwacha * `ZMK` - Zambian Kwacha (1968–2012) * `ZWD` - Zimbabwean Dollar (1980–2008) * `ZWR` - Zimbabwean Dollar (2008) * `ZWL` - Zimbabwean Dollar (2009). [optional]  # noqa: E501
            exchange_rate (str, none_type): The transaction's exchange rate.. [optional]  # noqa: E501
            company (str, none_type): The company the transaction belongs to.. [optional]  # noqa: E501
            tracking_categories ([str, none_type]): [optional]  # noqa: E501
            line_items ([TransactionLineItem]): [optional]  # noqa: E501
            remote_was_deleted (bool): Indicates whether or not this object has been deleted by third party webhooks.. [optional]  # noqa: E501
            id (str): [optional]  # noqa: E501
            remote_id (str, none_type): The third-party API ID of the matching object.. [optional]  # noqa: E501
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


        self.transaction_type = kwargs.get("transaction_type", None)
        self.number = kwargs.get("number", None)
        self.transaction_date = kwargs.get("transaction_date", None)
        self.account = kwargs.get("account", None)
        self.contact = kwargs.get("contact", None)
        self.total_amount = kwargs.get("total_amount", None)
        self.currency = kwargs.get("currency", None)
        self.exchange_rate = kwargs.get("exchange_rate", None)
        self.company = kwargs.get("company", None)
        self.tracking_categories = kwargs.get("tracking_categories", None)
        self.remote_id = kwargs.get("remote_id", None)
        self._line_items = kwargs.get("line_items", None)
        self._remote_was_deleted = kwargs.get("remote_was_deleted", bool())
        self._id = kwargs.get("id", str())
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
        """Transaction - a model defined in OpenAPI

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
            transaction_type (str, none_type): The type of transaction, which can by any transaction object not already included in Merge’s common model.. [optional]  # noqa: E501
            number (str, none_type): The transaction's number used for identifying purposes.. [optional]  # noqa: E501
            transaction_date (datetime, none_type): The date upon which the transaction occurred.. [optional]  # noqa: E501
            account (str, none_type): The transaction's account.. [optional]  # noqa: E501
            contact (str, none_type): The contact to whom the transaction relates to.. [optional]  # noqa: E501
            total_amount (str, none_type): The total amount being paid after taxes.. [optional]  # noqa: E501
            currency (bool, dict, float, int, list, str, none_type): The transaction's currency.  * `XUA` - ADB Unit of Account * `AFN` - Afghan Afghani * `AFA` - Afghan Afghani (1927–2002) * `ALL` - Albanian Lek * `ALK` - Albanian Lek (1946–1965) * `DZD` - Algerian Dinar * `ADP` - Andorran Peseta * `AOA` - Angolan Kwanza * `AOK` - Angolan Kwanza (1977–1991) * `AON` - Angolan New Kwanza (1990–2000) * `AOR` - Angolan Readjusted Kwanza (1995–1999) * `ARA` - Argentine Austral * `ARS` - Argentine Peso * `ARM` - Argentine Peso (1881–1970) * `ARP` - Argentine Peso (1983–1985) * `ARL` - Argentine Peso Ley (1970–1983) * `AMD` - Armenian Dram * `AWG` - Aruban Florin * `AUD` - Australian Dollar * `ATS` - Austrian Schilling * `AZN` - Azerbaijani Manat * `AZM` - Azerbaijani Manat (1993–2006) * `BSD` - Bahamian Dollar * `BHD` - Bahraini Dinar * `BDT` - Bangladeshi Taka * `BBD` - Barbadian Dollar * `BYN` - Belarusian Ruble * `BYB` - Belarusian Ruble (1994–1999) * `BYR` - Belarusian Ruble (2000–2016) * `BEF` - Belgian Franc * `BEC` - Belgian Franc (convertible) * `BEL` - Belgian Franc (financial) * `BZD` - Belize Dollar * `BMD` - Bermudan Dollar * `BTN` - Bhutanese Ngultrum * `BOB` - Bolivian Boliviano * `BOL` - Bolivian Boliviano (1863–1963) * `BOV` - Bolivian Mvdol * `BOP` - Bolivian Peso * `BAM` - Bosnia-Herzegovina Convertible Mark * `BAD` - Bosnia-Herzegovina Dinar (1992–1994) * `BAN` - Bosnia-Herzegovina New Dinar (1994–1997) * `BWP` - Botswanan Pula * `BRC` - Brazilian Cruzado (1986–1989) * `BRZ` - Brazilian Cruzeiro (1942–1967) * `BRE` - Brazilian Cruzeiro (1990–1993) * `BRR` - Brazilian Cruzeiro (1993–1994) * `BRN` - Brazilian New Cruzado (1989–1990) * `BRB` - Brazilian New Cruzeiro (1967–1986) * `BRL` - Brazilian Real * `GBP` - British Pound * `BND` - Brunei Dollar * `BGL` - Bulgarian Hard Lev * `BGN` - Bulgarian Lev * `BGO` - Bulgarian Lev (1879–1952) * `BGM` - Bulgarian Socialist Lev * `BUK` - Burmese Kyat * `BIF` - Burundian Franc * `XPF` - CFP Franc * `KHR` - Cambodian Riel * `CAD` - Canadian Dollar * `CVE` - Cape Verdean Escudo * `KYD` - Cayman Islands Dollar * `XAF` - Central African CFA Franc * `CLE` - Chilean Escudo * `CLP` - Chilean Peso * `CLF` - Chilean Unit of Account (UF) * `CNX` - Chinese People’s Bank Dollar * `CNY` - Chinese Yuan * `CNH` - Chinese Yuan (offshore) * `COP` - Colombian Peso * `COU` - Colombian Real Value Unit * `KMF` - Comorian Franc * `CDF` - Congolese Franc * `CRC` - Costa Rican Colón * `HRD` - Croatian Dinar * `HRK` - Croatian Kuna * `CUC` - Cuban Convertible Peso * `CUP` - Cuban Peso * `CYP` - Cypriot Pound * `CZK` - Czech Koruna * `CSK` - Czechoslovak Hard Koruna * `DKK` - Danish Krone * `DJF` - Djiboutian Franc * `DOP` - Dominican Peso * `NLG` - Dutch Guilder * `XCD` - East Caribbean Dollar * `DDM` - East German Mark * `ECS` - Ecuadorian Sucre * `ECV` - Ecuadorian Unit of Constant Value * `EGP` - Egyptian Pound * `GQE` - Equatorial Guinean Ekwele * `ERN` - Eritrean Nakfa * `EEK` - Estonian Kroon * `ETB` - Ethiopian Birr * `EUR` - Euro * `XBA` - European Composite Unit * `XEU` - European Currency Unit * `XBB` - European Monetary Unit * `XBC` - European Unit of Account (XBC) * `XBD` - European Unit of Account (XBD) * `FKP` - Falkland Islands Pound * `FJD` - Fijian Dollar * `FIM` - Finnish Markka * `FRF` - French Franc * `XFO` - French Gold Franc * `XFU` - French UIC-Franc * `GMD` - Gambian Dalasi * `GEK` - Georgian Kupon Larit * `GEL` - Georgian Lari * `DEM` - German Mark * `GHS` - Ghanaian Cedi * `GHC` - Ghanaian Cedi (1979–2007) * `GIP` - Gibraltar Pound * `XAU` - Gold * `GRD` - Greek Drachma * `GTQ` - Guatemalan Quetzal * `GWP` - Guinea-Bissau Peso * `GNF` - Guinean Franc * `GNS` - Guinean Syli * `GYD` - Guyanaese Dollar * `HTG` - Haitian Gourde * `HNL` - Honduran Lempira * `HKD` - Hong Kong Dollar * `HUF` - Hungarian Forint * `IMP` - IMP * `ISK` - Icelandic Króna * `ISJ` - Icelandic Króna (1918–1981) * `INR` - Indian Rupee * `IDR` - Indonesian Rupiah * `IRR` - Iranian Rial * `IQD` - Iraqi Dinar * `IEP` - Irish Pound * `ILS` - Israeli New Shekel * `ILP` - Israeli Pound * `ILR` - Israeli Shekel (1980–1985) * `ITL` - Italian Lira * `JMD` - Jamaican Dollar * `JPY` - Japanese Yen * `JOD` - Jordanian Dinar * `KZT` - Kazakhstani Tenge * `KES` - Kenyan Shilling * `KWD` - Kuwaiti Dinar * `KGS` - Kyrgystani Som * `LAK` - Laotian Kip * `LVL` - Latvian Lats * `LVR` - Latvian Ruble * `LBP` - Lebanese Pound * `LSL` - Lesotho Loti * `LRD` - Liberian Dollar * `LYD` - Libyan Dinar * `LTL` - Lithuanian Litas * `LTT` - Lithuanian Talonas * `LUL` - Luxembourg Financial Franc * `LUC` - Luxembourgian Convertible Franc * `LUF` - Luxembourgian Franc * `MOP` - Macanese Pataca * `MKD` - Macedonian Denar * `MKN` - Macedonian Denar (1992–1993) * `MGA` - Malagasy Ariary * `MGF` - Malagasy Franc * `MWK` - Malawian Kwacha * `MYR` - Malaysian Ringgit * `MVR` - Maldivian Rufiyaa * `MVP` - Maldivian Rupee (1947–1981) * `MLF` - Malian Franc * `MTL` - Maltese Lira * `MTP` - Maltese Pound * `MRU` - Mauritanian Ouguiya * `MRO` - Mauritanian Ouguiya (1973–2017) * `MUR` - Mauritian Rupee * `MXV` - Mexican Investment Unit * `MXN` - Mexican Peso * `MXP` - Mexican Silver Peso (1861–1992) * `MDC` - Moldovan Cupon * `MDL` - Moldovan Leu * `MCF` - Monegasque Franc * `MNT` - Mongolian Tugrik * `MAD` - Moroccan Dirham * `MAF` - Moroccan Franc * `MZE` - Mozambican Escudo * `MZN` - Mozambican Metical * `MZM` - Mozambican Metical (1980–2006) * `MMK` - Myanmar Kyat * `NAD` - Namibian Dollar * `NPR` - Nepalese Rupee * `ANG` - Netherlands Antillean Guilder * `TWD` - New Taiwan Dollar * `NZD` - New Zealand Dollar * `NIO` - Nicaraguan Córdoba * `NIC` - Nicaraguan Córdoba (1988–1991) * `NGN` - Nigerian Naira * `KPW` - North Korean Won * `NOK` - Norwegian Krone * `OMR` - Omani Rial * `PKR` - Pakistani Rupee * `XPD` - Palladium * `PAB` - Panamanian Balboa * `PGK` - Papua New Guinean Kina * `PYG` - Paraguayan Guarani * `PEI` - Peruvian Inti * `PEN` - Peruvian Sol * `PES` - Peruvian Sol (1863–1965) * `PHP` - Philippine Peso * `XPT` - Platinum * `PLN` - Polish Zloty * `PLZ` - Polish Zloty (1950–1995) * `PTE` - Portuguese Escudo * `GWE` - Portuguese Guinea Escudo * `QAR` - Qatari Rial * `XRE` - RINET Funds * `RHD` - Rhodesian Dollar * `RON` - Romanian Leu * `ROL` - Romanian Leu (1952–2006) * `RUB` - Russian Ruble * `RUR` - Russian Ruble (1991–1998) * `RWF` - Rwandan Franc * `SVC` - Salvadoran Colón * `WST` - Samoan Tala * `SAR` - Saudi Riyal * `RSD` - Serbian Dinar * `CSD` - Serbian Dinar (2002–2006) * `SCR` - Seychellois Rupee * `SLL` - Sierra Leonean Leone * `XAG` - Silver * `SGD` - Singapore Dollar * `SKK` - Slovak Koruna * `SIT` - Slovenian Tolar * `SBD` - Solomon Islands Dollar * `SOS` - Somali Shilling * `ZAR` - South African Rand * `ZAL` - South African Rand (financial) * `KRH` - South Korean Hwan (1953–1962) * `KRW` - South Korean Won * `KRO` - South Korean Won (1945–1953) * `SSP` - South Sudanese Pound * `SUR` - Soviet Rouble * `ESP` - Spanish Peseta * `ESA` - Spanish Peseta (A account) * `ESB` - Spanish Peseta (convertible account) * `XDR` - Special Drawing Rights * `LKR` - Sri Lankan Rupee * `SHP` - St. Helena Pound * `XSU` - Sucre * `SDD` - Sudanese Dinar (1992–2007) * `SDG` - Sudanese Pound * `SDP` - Sudanese Pound (1957–1998) * `SRD` - Surinamese Dollar * `SRG` - Surinamese Guilder * `SZL` - Swazi Lilangeni * `SEK` - Swedish Krona * `CHF` - Swiss Franc * `SYP` - Syrian Pound * `STN` - São Tomé & Príncipe Dobra * `STD` - São Tomé & Príncipe Dobra (1977–2017) * `TVD` - TVD * `TJR` - Tajikistani Ruble * `TJS` - Tajikistani Somoni * `TZS` - Tanzanian Shilling * `XTS` - Testing Currency Code * `THB` - Thai Baht * `XXX` - The codes assigned for transactions where no currency is involved * `TPE` - Timorese Escudo * `TOP` - Tongan Paʻanga * `TTD` - Trinidad & Tobago Dollar * `TND` - Tunisian Dinar * `TRY` - Turkish Lira * `TRL` - Turkish Lira (1922–2005) * `TMT` - Turkmenistani Manat * `TMM` - Turkmenistani Manat (1993–2009) * `USD` - US Dollar * `USN` - US Dollar (Next day) * `USS` - US Dollar (Same day) * `UGX` - Ugandan Shilling * `UGS` - Ugandan Shilling (1966–1987) * `UAH` - Ukrainian Hryvnia * `UAK` - Ukrainian Karbovanets * `AED` - United Arab Emirates Dirham * `UYW` - Uruguayan Nominal Wage Index Unit * `UYU` - Uruguayan Peso * `UYP` - Uruguayan Peso (1975–1993) * `UYI` - Uruguayan Peso (Indexed Units) * `UZS` - Uzbekistani Som * `VUV` - Vanuatu Vatu * `VES` - Venezuelan Bolívar * `VEB` - Venezuelan Bolívar (1871–2008) * `VEF` - Venezuelan Bolívar (2008–2018) * `VND` - Vietnamese Dong * `VNN` - Vietnamese Dong (1978–1985) * `CHE` - WIR Euro * `CHW` - WIR Franc * `XOF` - West African CFA Franc * `YDD` - Yemeni Dinar * `YER` - Yemeni Rial * `YUN` - Yugoslavian Convertible Dinar (1990–1992) * `YUD` - Yugoslavian Hard Dinar (1966–1990) * `YUM` - Yugoslavian New Dinar (1994–2002) * `YUR` - Yugoslavian Reformed Dinar (1992–1993) * `ZWN` - ZWN * `ZRN` - Zairean New Zaire (1993–1998) * `ZRZ` - Zairean Zaire (1971–1993) * `ZMW` - Zambian Kwacha * `ZMK` - Zambian Kwacha (1968–2012) * `ZWD` - Zimbabwean Dollar (1980–2008) * `ZWR` - Zimbabwean Dollar (2008) * `ZWL` - Zimbabwean Dollar (2009). [optional]  # noqa: E501
            exchange_rate (str, none_type): The transaction's exchange rate.. [optional]  # noqa: E501
            company (str, none_type): The company the transaction belongs to.. [optional]  # noqa: E501
            tracking_categories ([str, none_type]): [optional]  # noqa: E501
            line_items ([TransactionLineItem]): [optional]  # noqa: E501
            remote_was_deleted (bool): Indicates whether or not this object has been deleted by third party webhooks.. [optional]  # noqa: E501
            id (str): [optional]  # noqa: E501
            remote_id (str, none_type): The third-party API ID of the matching object.. [optional]  # noqa: E501
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

        self.transaction_type: Union[str, none_type] = kwargs.get("transaction_type", None)
        self.number: Union[str, none_type] = kwargs.get("number", None)
        self.transaction_date: Union[datetime, none_type] = kwargs.get("transaction_date", None)
        self.account: Union[str, none_type] = kwargs.get("account", None)
        self.contact: Union[str, none_type] = kwargs.get("contact", None)
        self.total_amount: Union[str, none_type] = kwargs.get("total_amount", None)
        self.currency: Union[bool, dict, float, int, list, str, none_type] = kwargs.get("currency", None)
        self.exchange_rate: Union[str, none_type] = kwargs.get("exchange_rate", None)
        self.company: Union[str, none_type] = kwargs.get("company", None)
        self.tracking_categories: Union[List[str, none_type]] = kwargs.get("tracking_categories", list())
        self.remote_id: Union[str, none_type] = kwargs.get("remote_id", None)
        self._line_items: Union[List["TransactionLineItem"]] = kwargs.get("line_items", None)
        self._remote_was_deleted: Union[bool] = kwargs.get("remote_was_deleted", bool())
        self._id: Union[str] = kwargs.get("id", str())
        self._modified_at: Union[datetime] = kwargs.get("modified_at", None)
        self._field_mappings: Union[Dict[str, bool, dict, float, int, list, str, none_type], none_type] = kwargs.get("field_mappings", None)
        self._remote_data: Union[List["RemoteData"]] = kwargs.get("remote_data", None)
    @property
    def line_items(self):
        return self._line_items

    @property
    def remote_was_deleted(self):
        return self._remote_was_deleted

    @property
    def id(self):
        return self._id

    @property
    def modified_at(self):
        return self._modified_at

    @property
    def field_mappings(self):
        return self._field_mappings

    @property
    def remote_data(self):
        return self._remote_data



