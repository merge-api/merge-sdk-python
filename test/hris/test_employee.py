"""
    Merge HRIS API

    The unified API for building rich integrations with multiple HR Information System platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest
from unittest.mock import MagicMock

import MergePythonSDK.hris
from MergePythonSDK.hris.model.employment_status_enum import EmploymentStatusEnum
from MergePythonSDK.hris.model.ethnicity_enum import EthnicityEnum
from MergePythonSDK.hris.model.gender_enum import GenderEnum
from MergePythonSDK.hris.model.marital_status_enum import MaritalStatusEnum
from MergePythonSDK.shared.model.remote_data import RemoteData
globals()['EmploymentStatusEnum'] = EmploymentStatusEnum
globals()['EthnicityEnum'] = EthnicityEnum
globals()['GenderEnum'] = GenderEnum
globals()['MaritalStatusEnum'] = MaritalStatusEnum
globals()['RemoteData'] = RemoteData
from MergePythonSDK.hris.model.employee import Employee
from MergePythonSDK.shared.api_client import ApiClient


class TestEmployee(unittest.TestCase):
    """Employee unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEmployee(self):
        """Test Employee"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Employee()  # noqa: E501

        """
        No test json responses were defined for Employee
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (Employee,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
