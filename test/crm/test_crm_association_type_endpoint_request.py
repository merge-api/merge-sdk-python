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
from MergePythonSDK.crm.model.association_type_request_request import AssociationTypeRequestRequest
globals()['AssociationTypeRequestRequest'] = AssociationTypeRequestRequest
from MergePythonSDK.crm.model.crm_association_type_endpoint_request import CRMAssociationTypeEndpointRequest
from MergePythonSDK.shared.api_client import ApiClient


class TestCRMAssociationTypeEndpointRequest(unittest.TestCase):
    """CRMAssociationTypeEndpointRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCRMAssociationTypeEndpointRequest(self):
        """Test CRMAssociationTypeEndpointRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CRMAssociationTypeEndpointRequest()  # noqa: E501

        """
        No test json responses were defined for CRMAssociationTypeEndpointRequest
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (CRMAssociationTypeEndpointRequest,), False)

        assert deserialized is not None

        assert deserialized.model is not None


if __name__ == '__main__':
    unittest.main()
