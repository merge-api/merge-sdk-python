"""
    Merge ATS API

    The unified API for building rich integrations with multiple Applicant Tracking System platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest
from unittest.mock import MagicMock

import MergePythonSDK.ats
from MergePythonSDK.ats.model.activity_request import ActivityRequest
globals()['ActivityRequest'] = ActivityRequest
from MergePythonSDK.ats.model.activity_endpoint_request import ActivityEndpointRequest
from MergePythonSDK.shared.api_client import ApiClient


class TestActivityEndpointRequest(unittest.TestCase):
    """ActivityEndpointRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testActivityEndpointRequest(self):
        """Test ActivityEndpointRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ActivityEndpointRequest()  # noqa: E501

        """
        No test json responses were defined for ActivityEndpointRequest
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (ActivityEndpointRequest,), False)

        assert deserialized is not None

        assert deserialized.model is not None
        assert deserialized.remote_user_id is not None


if __name__ == '__main__':
    unittest.main()
