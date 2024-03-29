"""
    Merge ATS API

    The unified API for building rich integrations with multiple Applicant Tracking System platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import unittest

import MergePythonSDK.ats
from MergePythonSDK.ats.api.activities_api import ActivitiesApi  # noqa: E501


class TestActivitiesApi(unittest.TestCase):
    """ActivitiesApi unit test stubs"""

    def setUp(self):
        self.api = ActivitiesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_activities_create(self):
        """Test case for activities_create

        """
        pass

    def test_activities_list(self):
        """Test case for activities_list

        """
        pass

    def test_activities_meta_post_retrieve(self):
        """Test case for activities_meta_post_retrieve

        """
        pass

    def test_activities_retrieve(self):
        """Test case for activities_retrieve

        """
        pass


if __name__ == '__main__':
    unittest.main()
