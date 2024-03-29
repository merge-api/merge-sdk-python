"""
    Merge CRM API

    The unified API for building rich integrations with multiple CRM platforms.  # noqa: E501

    The version of the OpenAPI document: 1.0
    Contact: hello@merge.dev
    Generated by: https://openapi-generator.tech
"""


import unittest

import MergePythonSDK.crm
from MergePythonSDK.crm.api.association_types_api import AssociationTypesApi  # noqa: E501


class TestAssociationTypesApi(unittest.TestCase):
    """AssociationTypesApi unit test stubs"""

    def setUp(self):
        self.api = AssociationTypesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_custom_object_classes_association_types_create(self):
        """Test case for custom_object_classes_association_types_create

        """
        pass

    def test_custom_object_classes_association_types_list(self):
        """Test case for custom_object_classes_association_types_list

        """
        pass

    def test_custom_object_classes_association_types_meta_post_retrieve(self):
        """Test case for custom_object_classes_association_types_meta_post_retrieve

        """
        pass

    def test_custom_object_classes_association_types_retrieve(self):
        """Test case for custom_object_classes_association_types_retrieve

        """
        pass


if __name__ == '__main__':
    unittest.main()
