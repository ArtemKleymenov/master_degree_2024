# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.person import Person  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDatabaseController(BaseTestCase):
    """DatabaseController integration test stubs"""

    def test_create_persons_with_list_input(self):
        """Test case for create_persons_with_list_input

        Creates list of Persons with given input array
        """
        body = [Person()]
        response = self.client.open(
            '/api/v1//Database/createWithList',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_persons(self):
        """Test case for get_persons

        Returns Persons db
        """
        response = self.client.open(
            '/api/v1//Database',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
