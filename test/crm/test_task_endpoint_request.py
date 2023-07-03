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
from MergePythonSDK.crm.model.task_request import TaskRequest
globals()['TaskRequest'] = TaskRequest
from MergePythonSDK.crm.model.task_endpoint_request import TaskEndpointRequest
from MergePythonSDK.shared.api_client import ApiClient


class TestTaskEndpointRequest(unittest.TestCase):
    """TaskEndpointRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTaskEndpointRequest(self):
        """Test TaskEndpointRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TaskEndpointRequest()  # noqa: E501

        """
        No test json responses were defined for TaskEndpointRequest
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (TaskEndpointRequest,), False)

        assert deserialized is not None

        assert deserialized.model is not None


if __name__ == '__main__':
    unittest.main()