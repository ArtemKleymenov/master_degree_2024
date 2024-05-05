import connexion
import six
import glob

from swagger_server.models.person import Person  # noqa: E501
from swagger_server import util
from swagger_server.controllers.person_controller import __get_base64_img__, add_person
from facial_service import DATABASE


def create_persons_with_list_input(body=None):  # noqa: E501
    """Creates list of Persons with given input array

    Creates list of Persons with given input array # noqa: E501

    :param body: 
    :type body: list | bytes

    :rtype: Person
    """
    if connexion.request.is_json:
        body = [Person.from_dict(d) for d in connexion.request.get_json()]  # noqa: E501
        for b in body:
            add_person(b)
    return body[0]


def get_persons():  # noqa: E501
    """Returns Persons db

    Returns a map of Persons IDs to images # noqa: E501


    :rtype: List[Person]
    """
    lst=[]
    faces = glob.glob(f'{DATABASE}/*.png')
    for f in faces:
        person_id = f[:-4]
        dataurl = __get_base64_img__(person_id)
        pers = Person(person_id, dataurl)
        lst.append(pers)
    return lst
