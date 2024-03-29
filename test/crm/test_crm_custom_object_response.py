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
from MergePythonSDK.crm.model.custom_object import CustomObject
from MergePythonSDK.crm.model.debug_mode_log import DebugModeLog
from MergePythonSDK.crm.model.error_validation_problem import ErrorValidationProblem
from MergePythonSDK.crm.model.warning_validation_problem import WarningValidationProblem
globals()['CustomObject'] = CustomObject
globals()['DebugModeLog'] = DebugModeLog
globals()['ErrorValidationProblem'] = ErrorValidationProblem
globals()['WarningValidationProblem'] = WarningValidationProblem
from MergePythonSDK.crm.model.crm_custom_object_response import CRMCustomObjectResponse
from MergePythonSDK.shared.api_client import ApiClient


class TestCRMCustomObjectResponse(unittest.TestCase):
    """CRMCustomObjectResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCRMCustomObjectResponse(self):
        """Test CRMCustomObjectResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CRMCustomObjectResponse()  # noqa: E501

        """
        No test json responses were defined for CRMCustomObjectResponse
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (CRMCustomObjectResponse,), False)

        assert deserialized is not None

        assert deserialized.model is not None
        assert deserialized.warnings is not None
        assert deserialized.errors is not None


if __name__ == '__main__':
    unittest.main()
