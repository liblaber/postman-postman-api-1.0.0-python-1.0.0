from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"created_at": "createdAt", "created_by": "createdBy"})
class RequestResponse(BaseModel):
    """Information about the response to the element's request. This object only returns when the network manager denied a request with a message.

    :param created_at: The date and time at which the network manager denied the request., defaults to None
    :type created_at: str, optional
    :param created_by: The network manager's user ID., defaults to None
    :type created_by: int, optional
    :param message: The network manager's request response message., defaults to None
    :type message: str, optional
    """

    def __init__(
        self, created_at: str = None, created_by: int = None, message: str = None
    ):
        if created_at is not None:
            self.created_at = created_at
        if created_by is not None:
            self.created_by = created_by
        if message is not None:
            self.message = message


class ElementType2(Enum):
    """An enumeration representing different categories.

    :cvar API: "api"
    :vartype API: str
    :cvar WORKSPACE: "workspace"
    :vartype WORKSPACE: str
    :cvar COLLECTION: "collection"
    :vartype COLLECTION: str
    """

    API = "api"
    WORKSPACE = "workspace"
    COLLECTION = "collection"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, ElementType2._member_map_.values()))


@JsonMap(
    {"id_": "id", "created_at": "createdAt", "created_by": "createdBy", "type_": "type"}
)
class RequestElement(BaseModel):
    """Information about the requested element.

    :param id_: The element's ID., defaults to None
    :type id_: str, optional
    :param created_at: The date and time at which the element was approved and added to the Private API Network., defaults to None
    :type created_at: str, optional
    :param created_by: The user ID of the user who requested to add the element to the Private API Network., defaults to None
    :type created_by: int, optional
    :param type_: The element type., defaults to None
    :type type_: ElementType2, optional
    :param name: The element's name., defaults to None
    :type name: str, optional
    :param summary: If applicable, the element's short summary., defaults to None
    :type summary: str, optional
    """

    def __init__(
        self,
        id_: str = None,
        created_at: str = None,
        created_by: int = None,
        type_: ElementType2 = None,
        name: str = None,
        summary: str = None,
    ):
        if id_ is not None:
            self.id_ = id_
        if created_at is not None:
            self.created_at = created_at
        if created_by is not None:
            self.created_by = created_by
        if type_ is not None:
            self.type_ = self._enum_matching(type_, ElementType2.list(), "type_")
        if name is not None:
            self.name = name
        if summary is not None:
            self.summary = summary


class RequestStatus(Enum):
    """An enumeration representing different categories.

    :cvar APPROVED: "approved"
    :vartype APPROVED: str
    :cvar DENIED: "denied"
    :vartype DENIED: str
    """

    APPROVED = "approved"
    DENIED = "denied"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, RequestStatus._member_map_.values()))


@JsonMap({"id_": "id", "created_at": "createdAt", "created_by": "createdBy"})
class RespondPanElementAddRequestOkResponseRequest(BaseModel):
    """RespondPanElementAddRequestOkResponseRequest

    :param id_: The request's ID., defaults to None
    :type id_: int, optional
    :param created_at: The date and time at which the request was created., defaults to None
    :type created_at: str, optional
    :param created_by: The ID of the user who created the request., defaults to None
    :type created_by: int, optional
    :param message: The user's optional message included in the request., defaults to None
    :type message: str, optional
    :param response: Information about the response to the element's request. This object only returns when the network manager denied a request with a message., defaults to None
    :type response: RequestResponse, optional
    :param element: Information about the requested element., defaults to None
    :type element: RequestElement, optional
    :param status: The request's status., defaults to None
    :type status: RequestStatus, optional
    """

    def __init__(
        self,
        id_: int = None,
        created_at: str = None,
        created_by: int = None,
        message: str = None,
        response: RequestResponse = None,
        element: RequestElement = None,
        status: RequestStatus = None,
    ):
        if id_ is not None:
            self.id_ = id_
        if created_at is not None:
            self.created_at = created_at
        if created_by is not None:
            self.created_by = created_by
        if message is not None:
            self.message = message
        if response is not None:
            self.response = self._define_object(response, RequestResponse)
        if element is not None:
            self.element = self._define_object(element, RequestElement)
        if status is not None:
            self.status = self._enum_matching(status, RequestStatus.list(), "status")


@JsonMap({})
class RespondPanElementAddRequestOkResponse(BaseModel):
    """RespondPanElementAddRequestOkResponse

    :param request: Information about the Private API Network request., defaults to None
    :type request: List[RespondPanElementAddRequestOkResponseRequest], optional
    """

    def __init__(
        self, request: List[RespondPanElementAddRequestOkResponseRequest] = None
    ):
        if request is not None:
            self.request = self._define_list(
                request, RespondPanElementAddRequestOkResponseRequest
            )
