# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.output import OUTPUT  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_list_objects(self):
        """Test case for list_objects

        List objects by bucket name
        """
        response = self.client.open(
            '/v2/listObjects/{bucketName}'.format(bucketName='bucketName_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
