"""
    Merge CRM API

    The unified API for building rich integrations with multiple CRM platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest
from unittest.mock import MagicMock

import MergePythonSDK.crm
from MergePythonSDK.crm.model.enabled_actions_enum import EnabledActionsEnum
globals()['EnabledActionsEnum'] = EnabledActionsEnum
from MergePythonSDK.crm.model.common_model_scopes_body_request import CommonModelScopesBodyRequest
from MergePythonSDK.shared.api_client import ApiClient


class TestCommonModelScopesBodyRequest(unittest.TestCase):
    """CommonModelScopesBodyRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCommonModelScopesBodyRequest(self):
        """Test CommonModelScopesBodyRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CommonModelScopesBodyRequest()  # noqa: E501

        """
        No test json responses were defined for CommonModelScopesBodyRequest
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (CommonModelScopesBodyRequest,), False)

        assert deserialized is not None

        assert deserialized.model_id is not None
        assert deserialized.enabled_actions is not None
        assert deserialized.disabled_fields is not None


if __name__ == '__main__':
    unittest.main()
