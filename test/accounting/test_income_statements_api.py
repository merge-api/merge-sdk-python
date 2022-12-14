"""
    Merge Accounting API

    The unified API for building rich integrations with multiple Accounting & Finance platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import unittest

import MergePythonSDK.accounting
from MergePythonSDK.accounting.api.income_statements_api import IncomeStatementsApi  # noqa: E501


class TestIncomeStatementsApi(unittest.TestCase):
    """IncomeStatementsApi unit test stubs"""

    def setUp(self):
        self.api = IncomeStatementsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_income_statements_list(self):
        """Test case for income_statements_list

        """
        pass

    def test_income_statements_retrieve(self):
        """Test case for income_statements_retrieve

        """
        pass


if __name__ == '__main__':
    unittest.main()
