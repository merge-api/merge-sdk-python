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
from MergePythonSDK.ats.model.overall_recommendation_enum import OverallRecommendationEnum
from MergePythonSDK.ats.model.remote_data import RemoteData
globals()['OverallRecommendationEnum'] = OverallRecommendationEnum
globals()['RemoteData'] = RemoteData
from MergePythonSDK.ats.model.scorecard import Scorecard
from MergePythonSDK.shared.api_client import ApiClient


class TestScorecard(unittest.TestCase):
    """Scorecard unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testScorecard(self):
        """Test Scorecard"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Scorecard()  # noqa: E501

        """
        No test json responses were defined for Scorecard
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (Scorecard,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
