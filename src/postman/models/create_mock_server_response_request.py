from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class ServerResponseHeaders1(BaseModel):
    """ServerResponseHeaders1

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


class ServerResponseLanguage1(Enum):
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
            map(lambda x: x.value, ServerResponseLanguage1._member_map_.values())
        )


@JsonMap({"status_code": "statusCode"})
class CreateMockServerResponseRequestServerResponse(BaseModel):
    """CreateMockServerResponseRequestServerResponse

    :param name: The server response's name.
    :type name: str
    :param status_code: The server response's 5xx HTTP response code. This property only accepts 5xx values.
    :type status_code: int
    :param headers: The server response's request headers, such as Content-Type, Accept, encoding, and other information., defaults to None
    :type headers: List[ServerResponseHeaders1], optional
    :param language: The server response's body language type., defaults to None
    :type language: ServerResponseLanguage1, optional
    :param body: The server response's body that returns when calling the mock server., defaults to None
    :type body: str, optional
    """

    def __init__(
        self,
        name: str,
        status_code: int,
        headers: List[ServerResponseHeaders1] = None,
        language: ServerResponseLanguage1 = None,
        body: str = None,
    ):
        self.name = name
        self.status_code = status_code
        if headers is not None:
            self.headers = self._define_list(headers, ServerResponseHeaders1)
        if language is not None:
            self.language = self._enum_matching(
                language, ServerResponseLanguage1.list(), "language"
            )
        if body is not None:
            self.body = body


@JsonMap({"server_response": "serverResponse"})
class CreateMockServerResponseRequest(BaseModel):
    """CreateMockServerResponseRequest

    :param server_response: server_response, defaults to None
    :type server_response: CreateMockServerResponseRequestServerResponse, optional
    """

    def __init__(
        self, server_response: CreateMockServerResponseRequestServerResponse = None
    ):
        if server_response is not None:
            self.server_response = self._define_object(
                server_response, CreateMockServerResponseRequestServerResponse
            )
