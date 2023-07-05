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
from MergePythonSDK.crm.model.association_type import AssociationType
globals()['AssociationType'] = AssociationType
from MergePythonSDK.crm.model.paginated_association_type_list import PaginatedAssociationTypeList
from MergePythonSDK.shared.api_client import ApiClient


class TestPaginatedAssociationTypeList(unittest.TestCase):
    """PaginatedAssociationTypeList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaginatedAssociationTypeList(self):
        """Test PaginatedAssociationTypeList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaginatedAssociationTypeList()  # noqa: E501

        """
        No test json responses were defined for PaginatedAssociationTypeList
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (PaginatedAssociationTypeList,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()