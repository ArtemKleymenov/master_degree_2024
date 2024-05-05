import connexion
import six
import os
import base64
from facial_service import DATABASE

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server.models.person import Person  # noqa: E501
from swagger_server import util


def __get_base64_img__(pers_id):
    binary_fc = open(f"{DATABASE}/{pers_id}.png", 'rb').read()  # fc aka file_content
    base64_utf8_str = base64.b64encode(binary_fc).decode('utf-8')
    dataurl = f'data:image/png;base64,{base64_utf8_str}'
    return dataurl


def add_person(body):  # noqa: E501
    """Add a new Person to the db

    Add a Person pet to the db # noqa: E501

    :param body: Create a new Person in the db
    :type body: dict | bytes

    :rtype: Person
    """
    if connexion.request.is_json:
        body = Person.from_dict(connexion.request.get_json())  # noqa: E501
        with open(f"{DATABASE}/{body.id}.png", "wb") as fh:
            fh.write(body.crop.decode('base64'))
    return body


def delete_person(person_id):  # noqa: E501
    """Deletes a Person

    delete a Person # noqa: E501

    :param person_id: Person id to delete
    :type person_id: str

    :rtype: ApiResponse
    """
    try: os.remove(f'{DATABASE}/{person_id}.png')
    except: pass
    return ApiResponse(200, int, 'OK!')


def get_person_by_id(person_id):  # noqa: E501
    """Find Person by ID

    Returns a single Person # noqa: E501

    :param person_id: ID of Person to return
    :type person_id: str

    :rtype: Person
    """
    dataurl = __get_base64_img__(person_id)
    pers = Person(person_id, dataurl)
    return pers


def update_person(body):  # noqa: E501
    """Update an existing Person

    Update an existing Person by Id # noqa: E501

    :param body: Update an existent Person in the db
    :type body: dict | bytes

    :rtype: Person
    """
    pers=None
    if connexion.request.is_json:
        body = Person.from_dict(connexion.request.get_json())  # noqa: E501
        with open(f"{DATABASE}/{body.id}.png", "wb") as fh:
            fh.write(body.crop.decode('base64'))
        pers=Person(body.id, body.crop)
    return pers


def update_person_with_form(person_id, crop=None):  # noqa: E501
    """Updates a Person in the db with form data

     # noqa: E501

    :param person_id: ID of Person that needs to be updated
    :type person_id: str
    :param crop: Image crop of Person that needs to be updated
    :type crop: str

    :rtype: ApiResponse
    """
    if crop:
        with open(f"{DATABASE}/{person_id}.png", "wb") as fh:
            fh.write(crop.decode('base64'))
    return ApiResponse(200, int, 'OK!')
