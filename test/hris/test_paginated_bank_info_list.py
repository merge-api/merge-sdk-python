"""
    Merge HRIS API

    The unified API for building rich integrations with multiple HR Information System platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest
from unittest.mock import MagicMock

import MergePythonSDK.hris
from MergePythonSDK.hris.model.bank_info import BankInfo
globals()['BankInfo'] = BankInfo
from MergePythonSDK.hris.model.paginated_bank_info_list import PaginatedBankInfoList
from MergePythonSDK.shared.api_client import ApiClient


class TestPaginatedBankInfoList(unittest.TestCase):
    """PaginatedBankInfoList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaginatedBankInfoList(self):
        """Test PaginatedBankInfoList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaginatedBankInfoList()  # noqa: E501

        """
        No test json responses were defined for PaginatedBankInfoList
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (PaginatedBankInfoList,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
