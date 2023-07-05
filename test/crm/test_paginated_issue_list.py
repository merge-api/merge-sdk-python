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
from MergePythonSDK.crm.model.issue import Issue
globals()['Issue'] = Issue
from MergePythonSDK.crm.model.paginated_issue_list import PaginatedIssueList
from MergePythonSDK.shared.api_client import ApiClient


class TestPaginatedIssueList(unittest.TestCase):
    """PaginatedIssueList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaginatedIssueList(self):
        """Test PaginatedIssueList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaginatedIssueList()  # noqa: E501

        """
        No test json responses were defined for PaginatedIssueList
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (PaginatedIssueList,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
