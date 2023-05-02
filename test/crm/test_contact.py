"""
    Merge CRM API

    The unified API for building rich integrations with multiple CRM platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest
from unittest.mock import MagicMock

import MergePythonSDK.crm
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
from MergePythonSDK.crm.model.contact import Contact
from MergePythonSDK.shared.api_client import ApiClient


class TestContact(unittest.TestCase):
    """Contact unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testContact(self):
        """Test Contact"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Contact()  # noqa: E501

        """
        No test json responses were defined for Contact
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (Contact,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
