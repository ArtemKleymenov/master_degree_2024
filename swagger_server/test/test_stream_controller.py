# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestStreamController(BaseTestCase):
    """StreamController integration test stubs"""

    def test_get_stream_frame(self):
        """Test case for get_stream_frame

        Returns last frame in stream
        """
        response = self.client.open(
            '/api/v1//Stream/getFrame',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_stream_url(self):
        """Test case for get_stream_url

        Returns stream URL
        """
        response = self.client.open(
            '/api/v1//Stream',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_stream_url(self):
        """Test case for update_stream_url

        Updates a camera source URL
        """
        query_string = [('url', 'url_example')]
        response = self.client.open(
            '/api/v1//Stream',
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
