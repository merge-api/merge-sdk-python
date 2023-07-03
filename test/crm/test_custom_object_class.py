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
from MergePythonSDK.crm.model.remote_field_class_for_custom_object_class import RemoteFieldClassForCustomObjectClass
globals()['RemoteFieldClassForCustomObjectClass'] = RemoteFieldClassForCustomObjectClass
from MergePythonSDK.crm.model.custom_object_class import CustomObjectClass
from MergePythonSDK.shared.api_client import ApiClient


class TestCustomObjectClass(unittest.TestCase):
    """CustomObjectClass unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCustomObjectClass(self):
        """Test CustomObjectClass"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CustomObjectClass()  # noqa: E501

        """
        No test json responses were defined for CustomObjectClass
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (CustomObjectClass,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
