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
from MergePythonSDK.accounting.model.currency_enum import CurrencyEnum
from MergePythonSDK.accounting.model.remote_data import RemoteData
from MergePythonSDK.accounting.model.report_item import ReportItem
globals()['CurrencyEnum'] = CurrencyEnum
globals()['RemoteData'] = RemoteData
globals()['ReportItem'] = ReportItem
from MergePythonSDK.accounting.model.income_statement import IncomeStatement
from MergePythonSDK.shared.api_client import ApiClient


class TestIncomeStatement(unittest.TestCase):
    """IncomeStatement unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIncomeStatement(self):
        """Test IncomeStatement"""
        # FIXME: construct object with mandatory attributes with example values
        # model = IncomeStatement()  # noqa: E501

        """
        No test json responses were defined for IncomeStatement
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (IncomeStatement,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
