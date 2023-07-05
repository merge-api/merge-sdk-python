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
from MergePythonSDK.ats.model.tag import Tag
globals()['Tag'] = Tag
from MergePythonSDK.ats.model.paginated_tag_list import PaginatedTagList
from MergePythonSDK.shared.api_client import ApiClient


class TestPaginatedTagList(unittest.TestCase):
    """PaginatedTagList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaginatedTagList(self):
        """Test PaginatedTagList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaginatedTagList()  # noqa: E501

        """
        No test json responses were defined for PaginatedTagList
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (PaginatedTagList,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
