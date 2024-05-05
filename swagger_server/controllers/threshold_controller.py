import connexion
import six

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server import util
from facial_service import THRESHOLD


def get_threshold():  # noqa: E501
    """Returns Threshold value

    Returns Threshold value # noqa: E501


    :rtype: str
    """
    return THRESHOLD


def update_threhold(thresh=None):  # noqa: E501
    """Updates a service threshold

     # noqa: E501

    :param thresh: New threshold value
    :type thresh: float

    :rtype: ApiResponse
    """
    THRESHOLD=thresh
    return ApiResponse(200, int, 'OK!')
