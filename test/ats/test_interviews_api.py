"""
    Merge ATS API

    The unified API for building rich integrations with multiple Applicant Tracking System platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import unittest

import MergePythonSDK.ats
from MergePythonSDK.ats.api.interviews_api import InterviewsApi  # noqa: E501


class TestInterviewsApi(unittest.TestCase):
    """InterviewsApi unit test stubs"""

    def setUp(self):
        self.api = InterviewsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_interviews_create(self):
        """Test case for interviews_create

        """
        pass

    def test_interviews_list(self):
        """Test case for interviews_list

        """
        pass

    def test_interviews_meta_post_retrieve(self):
        """Test case for interviews_meta_post_retrieve

        """
        pass

    def test_interviews_retrieve(self):
        """Test case for interviews_retrieve

        """
        pass


if __name__ == '__main__':
    unittest.main()
