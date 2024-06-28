<<<<<<< HEAD
=======
# This file was generated by liblab | https://liblab.com/

>>>>>>> 95da91c (initial commit)
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class ServerResponseHeaders2(BaseModel):
    """Information about they key-value pair.

    :param key: The request header's key value., defaults to None
    :type key: str, optional
    :param value: The request header's value., defaults to None
    :type value: str, optional
    """

    def __init__(self, key: str = None, value: str = None):
        if key is not None:
            self.key = key
        if value is not None:
            self.value = value


class ServerResponseLanguage2(Enum):
    """An enumeration representing different categories.

    :cvar TEXT: "text"
    :vartype TEXT: str
    :cvar JAVASCRIPT: "javascript"
    :vartype JAVASCRIPT: str
    :cvar JSON: "json"
    :vartype JSON: str
    :cvar HTML: "html"
    :vartype HTML: str
    :cvar XML: "xml"
    :vartype XML: str
    """

    TEXT = "text"
    JAVASCRIPT = "javascript"
    JSON = "json"
    HTML = "html"
    XML = "xml"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, ServerResponseLanguage2._member_map_.values())
        )


@JsonMap({"status_code": "statusCode"})
class UpdateMockServerResponseRequestServerResponse(BaseModel):
    """UpdateMockServerResponseRequestServerResponse

    :param name: The server response's name., defaults to None
    :type name: str, optional
    :param status_code: The server response's 5xx HTTP response code. This property only accepts 5xx values., defaults to None
    :type status_code: int, optional
    :param headers: The server response's request headers, such as Content-Type, Accept, encoding, and other information., defaults to None
    :type headers: List[ServerResponseHeaders2], optional
    :param language: The server response's body language type., defaults to None
    :type language: ServerResponseLanguage2, optional
    :param body: The server response's body that returns when calling the mock server., defaults to None
    :type body: str, optional
    """

    def __init__(
        self,
        name: str = None,
        status_code: int = None,
        headers: List[ServerResponseHeaders2] = None,
        language: ServerResponseLanguage2 = None,
        body: str = None,
    ):
        if name is not None:
            self.name = name
        if status_code is not None:
            self.status_code = status_code
        if headers is not None:
            self.headers = self._define_list(headers, ServerResponseHeaders2)
        if language is not None:
            self.language = self._enum_matching(
                language, ServerResponseLanguage2.list(), "language"
            )
        if body is not None:
            self.body = body


@JsonMap({"server_response": "serverResponse"})
class UpdateMockServerResponseRequest(BaseModel):
    """UpdateMockServerResponseRequest

    :param server_response: server_response, defaults to None
    :type server_response: UpdateMockServerResponseRequestServerResponse, optional
    """

    def __init__(
        self, server_response: UpdateMockServerResponseRequestServerResponse = None
    ):
        if server_response is not None:
            self.server_response = self._define_object(
                server_response, UpdateMockServerResponseRequestServerResponse
            )
