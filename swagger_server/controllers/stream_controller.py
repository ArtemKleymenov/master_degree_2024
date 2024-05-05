import connexion
import six
import base64
import cv2

from swagger_server.models.api_response import ApiResponse  # noqa: E501
from swagger_server import util
from facial_service import STREAM_URL, LAST_FRAME


def get_stream_frame():  # noqa: E501
    """Returns last frame in stream

    Returns last frame in stream # noqa: E501


    :rtype: str
    """
    retval, buffer = cv2.imencode('.png', LAST_FRAME)
    pic_str = base64.b64encode(buffer)
    pic_str = pic_str.decode()
    return pic_str


def get_stream_url():  # noqa: E501
    """Returns stream URL

    Returns stream URL # noqa: E501


    :rtype: str
    """
    return STREAM_URL


def update_stream_url(url=None):  # noqa: E501
    """Updates a camera source URL

     # noqa: E501

    :param url: URL of new source for video
    :type url: str

    :rtype: ApiResponse
    """
    STREAM_URL = url
    return ApiResponse(200, int, 'OK!')
