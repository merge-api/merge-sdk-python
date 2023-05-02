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
from MergePythonSDK.accounting.model.categories_enum import CategoriesEnum
from MergePythonSDK.accounting.model.model_operation import ModelOperation
globals()['CategoriesEnum'] = CategoriesEnum
globals()['ModelOperation'] = ModelOperation
from MergePythonSDK.accounting.model.account_details_and_actions_integration import AccountDetailsAndActionsIntegration
from MergePythonSDK.shared.api_client import ApiClient


class TestAccountDetailsAndActionsIntegration(unittest.TestCase):
    """AccountDetailsAndActionsIntegration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAccountDetailsAndActionsIntegration(self):
        """Test AccountDetailsAndActionsIntegration"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AccountDetailsAndActionsIntegration()  # noqa: E501

        """
        No test json responses were defined for AccountDetailsAndActionsIntegration
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (AccountDetailsAndActionsIntegration,), False)

        assert deserialized is not None

        assert deserialized.name is not None
        assert deserialized.categories is not None
        assert deserialized.color is not None
        assert deserialized.slug is not None
        assert deserialized.passthrough_available is not None


if __name__ == '__main__':
    unittest.main()
