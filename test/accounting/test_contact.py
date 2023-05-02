"""
    Merge Accounting API

    The unified API for building rich integrations with multiple Accounting & Finance platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest
from unittest.mock import MagicMock

import MergePythonSDK.accounting
from MergePythonSDK.accounting.model.accounting_phone_number import AccountingPhoneNumber
from MergePythonSDK.shared.model.remote_data import RemoteData
from MergePythonSDK.accounting.model.status7d1_enum import Status7d1Enum
globals()['AccountingPhoneNumber'] = AccountingPhoneNumber
globals()['RemoteData'] = RemoteData
globals()['Status7d1Enum'] = Status7d1Enum
from MergePythonSDK.accounting.model.contact import Contact
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
