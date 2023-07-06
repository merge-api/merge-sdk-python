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
from MergePythonSDK.shared.model.remote_data import RemoteData
globals()['RemoteData'] = RemoteData
from MergePythonSDK.ats.model.reject_reason import RejectReason
from MergePythonSDK.shared.api_client import ApiClient


class TestRejectReason(unittest.TestCase):
    """RejectReason unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRejectReason(self):
        """Test RejectReason"""
        # FIXME: construct object with mandatory attributes with example values
        # model = RejectReason()  # noqa: E501

        """
        No test json responses were defined for RejectReason
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (RejectReason,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
