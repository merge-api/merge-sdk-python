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
from MergePythonSDK.crm.model.patched_contact_request import PatchedContactRequest
globals()['PatchedContactRequest'] = PatchedContactRequest
from MergePythonSDK.crm.model.patched_crm_contact_endpoint_request import PatchedCRMContactEndpointRequest
from MergePythonSDK.shared.api_client import ApiClient


class TestPatchedCRMContactEndpointRequest(unittest.TestCase):
    """PatchedCRMContactEndpointRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPatchedCRMContactEndpointRequest(self):
        """Test PatchedCRMContactEndpointRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PatchedCRMContactEndpointRequest()  # noqa: E501

        """
        No test json responses were defined for PatchedCRMContactEndpointRequest
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (PatchedCRMContactEndpointRequest,), False)

        assert deserialized is not None

        assert deserialized.model is not None


if __name__ == '__main__':
    unittest.main()
