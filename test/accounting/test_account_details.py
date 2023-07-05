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
from MergePythonSDK.accounting.model.category_enum import CategoryEnum
globals()['CategoryEnum'] = CategoryEnum
from MergePythonSDK.accounting.model.account_details import AccountDetails
from MergePythonSDK.shared.api_client import ApiClient


class TestAccountDetails(unittest.TestCase):
    """AccountDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAccountDetails(self):
        """Test AccountDetails"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AccountDetails()  # noqa: E501

        """
        No test json responses were defined for AccountDetails
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (AccountDetails,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
