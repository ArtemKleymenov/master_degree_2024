# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestThresholdController(BaseTestCase):
    """ThresholdController integration test stubs"""

    def test_get_threshold(self):
        """Test case for get_threshold

        Returns Threshold value
        """
        response = self.client.open(
            '/api/v1//Threshold',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_threhold(self):
        """Test case for update_threhold

        Updates a service threshold
        """
        query_string = [('url', 1.2)]
        response = self.client.open(
            '/api/v1//Threshold',
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
