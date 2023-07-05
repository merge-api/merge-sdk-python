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
from MergePythonSDK.crm.model.remote_field_class import RemoteFieldClass
globals()['RemoteFieldClass'] = RemoteFieldClass
from MergePythonSDK.crm.model.remote_field import RemoteField
from MergePythonSDK.shared.api_client import ApiClient


class TestRemoteField(unittest.TestCase):
    """RemoteField unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRemoteField(self):
        """Test RemoteField"""
        # FIXME: construct object with mandatory attributes with example values
        # model = RemoteField()  # noqa: E501

        """
        No test json responses were defined for RemoteField
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (RemoteField,), False)

        assert deserialized is not None

        assert deserialized.remote_field_class is not None


if __name__ == '__main__':
    unittest.main()
