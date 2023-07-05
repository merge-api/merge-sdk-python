"""
    Merge Ticketing API

    The unified API for building rich integrations with multiple Ticketing platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest
from unittest.mock import MagicMock

import MergePythonSDK.ticketing
from MergePythonSDK.ticketing.model.priority_enum import PriorityEnum
from MergePythonSDK.ticketing.model.remote_data import RemoteData
from MergePythonSDK.ticketing.model.remote_field import RemoteField
from MergePythonSDK.ticketing.model.ticket_status_enum import TicketStatusEnum
globals()['PriorityEnum'] = PriorityEnum
globals()['RemoteData'] = RemoteData
globals()['RemoteField'] = RemoteField
globals()['TicketStatusEnum'] = TicketStatusEnum
from MergePythonSDK.ticketing.model.ticket import Ticket
from MergePythonSDK.shared.api_client import ApiClient


class TestTicket(unittest.TestCase):
    """Ticket unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTicket(self):
        """Test Ticket"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Ticket()  # noqa: E501

        """
        No test json responses were defined for Ticket
        """
        raw_json = None

        if raw_json is None:
            return

        response_mock = MagicMock()
        response_mock.data = raw_json

        deserialized = ApiClient().deserialize(response_mock, (Ticket,), False)

        assert deserialized is not None



if __name__ == '__main__':
    unittest.main()
