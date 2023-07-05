"""
    Merge Ticketing API

    The unified API for building rich integrations with multiple Ticketing platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest
from unittest.mock import MagicMock

import MergePythonSDK.ticketing
from MergePythonSDK.ticketing.model.remote_data import RemoteData
globals()['RemoteData'] = RemoteData
from MergePythonSDK.ticketing.model.attachment import Attachment
from MergePythonSDK.shared.api_client import ApiClient


class TestAttachment(unittest.TestCase):
    """Attachment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAttachment(self):
        """Test Attachment"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Attachment()  # noqa: E501

        """
        No test json responses were defined for Attachment
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (Attachment,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
