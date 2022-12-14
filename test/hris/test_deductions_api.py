"""
    Merge HRIS API

    The unified API for building rich integrations with multiple HR Information System platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import unittest

import MergePythonSDK.hris
from MergePythonSDK.hris.api.deductions_api import DeductionsApi  # noqa: E501


class TestDeductionsApi(unittest.TestCase):
    """DeductionsApi unit test stubs"""

    def setUp(self):
        self.api = DeductionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_deductions_list(self):
        """Test case for deductions_list

        """
        pass

    def test_deductions_retrieve(self):
        """Test case for deductions_retrieve

        """
        pass


if __name__ == '__main__':
    unittest.main()
