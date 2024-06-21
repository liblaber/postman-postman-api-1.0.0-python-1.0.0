from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class DeleteMockServerResponseOkResponseHeaders(BaseModel):
    """DeleteMockServerResponseOkResponseHeaders

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


class DeleteMockServerResponseOkResponseLanguage(Enum):
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
            map(
                lambda x: x.value,
                DeleteMockServerResponseOkResponseLanguage._member_map_.values(),
            )
        )


@JsonMap(
    {
        "id_": "id",
        "status_code": "statusCode",
        "created_by": "createdBy",
        "updated_by": "updatedBy",
        "created_at": "createdAt",
    }
)
class DeleteMockServerResponseOkResponse(BaseModel):
    """Information about the deleted server response.

    :param id_: The server response's ID., defaults to None
    :type id_: str, optional
    :param name: The server response's name., defaults to None
    :type name: str, optional
    :param status_code: The server response's 5xx HTTP response code., defaults to None
    :type status_code: float, optional
    :param headers: The server response's request headers, such as Content-Type, Accept, encoding, and other information., defaults to None
    :type headers: List[DeleteMockServerResponseOkResponseHeaders], optional
    :param language: The server response's body language type., defaults to None
    :type language: DeleteMockServerResponseOkResponseLanguage, optional
    :param body: The server response's body that returns when calling the mock server., defaults to None
    :type body: str, optional
    :param created_by: The user ID of the user who created the server response., defaults to None
    :type created_by: str, optional
    :param updated_by: The user ID of the user who last updated the server response., defaults to None
    :type updated_by: str, optional
    :param created_at: The date and time at which the server response was created., defaults to None
    :type created_at: str, optional
    """

    def __init__(
        self,
        id_: str = None,
        name: str = None,
        status_code: float = None,
        headers: List[DeleteMockServerResponseOkResponseHeaders] = None,
        language: DeleteMockServerResponseOkResponseLanguage = None,
        body: str = None,
        created_by: str = None,
        updated_by: str = None,
        created_at: str = None,
    ):
        if id_ is not None:
            self.id_ = id_
        if name is not None:
            self.name = name
        if status_code is not None:
            self.status_code = status_code
        if headers is not None:
            self.headers = self._define_list(
                headers, DeleteMockServerResponseOkResponseHeaders
            )
        if language is not None:
            self.language = self._enum_matching(
                language, DeleteMockServerResponseOkResponseLanguage.list(), "language"
            )
        if body is not None:
            self.body = body
        if created_by is not None:
            self.created_by = created_by
        if updated_by is not None:
            self.updated_by = updated_by
        if created_at is not None:
            self.created_at = created_at
