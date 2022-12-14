"""
    Merge Accounting API

    The unified API for building rich integrations with multiple Accounting & Finance platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import unittest

import MergePythonSDK.accounting
from MergePythonSDK.accounting.api.tax_rates_api import TaxRatesApi  # noqa: E501


class TestTaxRatesApi(unittest.TestCase):
    """TaxRatesApi unit test stubs"""

    def setUp(self):
        self.api = TaxRatesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_tax_rates_list(self):
        """Test case for tax_rates_list

        """
        pass

    def test_tax_rates_retrieve(self):
        """Test case for tax_rates_retrieve

        """
        pass


if __name__ == '__main__':
    unittest.main()
