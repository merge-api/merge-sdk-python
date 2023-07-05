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
from MergePythonSDK.accounting.model.vendor_credit import VendorCredit
globals()['VendorCredit'] = VendorCredit
from MergePythonSDK.accounting.model.paginated_vendor_credit_list import PaginatedVendorCreditList
from MergePythonSDK.shared.api_client import ApiClient


class TestPaginatedVendorCreditList(unittest.TestCase):
    """PaginatedVendorCreditList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaginatedVendorCreditList(self):
        """Test PaginatedVendorCreditList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaginatedVendorCreditList()  # noqa: E501

        """
        No test json responses were defined for PaginatedVendorCreditList
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (PaginatedVendorCreditList,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()