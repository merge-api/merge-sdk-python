"""
    Merge Accounting API

    The unified API for building rich integrations with multiple Accounting & Finance platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import unittest

import MergePythonSDK.accounting
from MergePythonSDK.accounting.api.purchase_orders_api import PurchaseOrdersApi  # noqa: E501


class TestPurchaseOrdersApi(unittest.TestCase):
    """PurchaseOrdersApi unit test stubs"""

    def setUp(self):
        self.api = PurchaseOrdersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_purchase_orders_create(self):
        """Test case for purchase_orders_create

        """
        pass

    def test_purchase_orders_list(self):
        """Test case for purchase_orders_list

        """
        pass

    def test_purchase_orders_meta_post_retrieve(self):
        """Test case for purchase_orders_meta_post_retrieve

        """
        pass

    def test_purchase_orders_retrieve(self):
        """Test case for purchase_orders_retrieve

        """
        pass


if __name__ == '__main__':
    unittest.main()
