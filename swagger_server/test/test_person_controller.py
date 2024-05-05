# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.person import Person  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPersonController(BaseTestCase):
    """PersonController integration test stubs"""

    def test_add_person(self):
        """Test case for add_person

        Add a new Person to the db
        """
        body = Person()
        response = self.client.open(
            '/api/v1//Person',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_person(self):
        """Test case for delete_person

        Deletes a Person
        """
        response = self.client.open(
            '/api/v1//Person/{PersonId}'.format(person_id='person_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_person_by_id(self):
        """Test case for get_person_by_id

        Find Person by ID
        """
        response = self.client.open(
            '/api/v1//Person/{PersonId}'.format(person_id='person_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_person(self):
        """Test case for update_person

        Update an existing Person
        """
        body = Person()
        response = self.client.open(
            '/api/v1//Person',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_person_with_form(self):
        """Test case for update_person_with_form

        Updates a Person in the db with form data
        """
        query_string = [('crop', 'crop_example')]
        response = self.client.open(
            '/api/v1//Person/{PersonId}'.format(person_id='person_id_example'),
            method='POST',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
