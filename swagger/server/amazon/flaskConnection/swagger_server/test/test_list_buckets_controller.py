# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.output import OUTPUT  # noqa: E501
from swagger_server.test import BaseTestCase


class TestListBucketsController(BaseTestCase):
    """ListBucketsController integration test stubs"""

    def test_list_buckets(self):
        """Test case for list_buckets

        Get all buckets
        """
        response = self.client.open(
            '/v2/listBuckets',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
