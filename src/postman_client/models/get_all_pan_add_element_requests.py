# This file was generated by liblab | https://liblab.com/

from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


class RequestsStatus(Enum):
    """An enumeration representing different categories.

    :cvar PENDING: "pending"
    :vartype PENDING: str
    :cvar DENIED: "denied"
    :vartype DENIED: str
    """

    PENDING = "pending"
    DENIED = "denied"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, RequestsStatus._member_map_.values()))


class ElementType1(Enum):
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
        return list(map(lambda x: x.value, ElementType1._member_map_.values()))


@JsonMap({"id_": "id", "type_": "type"})
class RequestsElement(BaseModel):
    """Information about the requested element.

    :param id_: The element's ID., defaults to None
    :type id_: str, optional
    :param type_: The element type., defaults to None
    :type type_: ElementType1, optional
    :param name: The element's name., defaults to None
    :type name: str, optional
    :param summary: If applicable, the element's short summary., defaults to None
    :type summary: str, optional
    """

    def __init__(
        self,
        id_: str = None,
        type_: ElementType1 = None,
        name: str = None,
        summary: str = None,
    ):
        """Information about the requested element.

        :param id_: The element's ID., defaults to None
        :type id_: str, optional
        :param type_: The element type., defaults to None
        :type type_: ElementType1, optional
        :param name: The element's name., defaults to None
        :type name: str, optional
        :param summary: If applicable, the element's short summary., defaults to None
        :type summary: str, optional
        """
        if id_ is not None:
            self.id_ = id_
        if type_ is not None:
            self.type_ = self._enum_matching(type_, ElementType1.list(), "type_")
        if name is not None:
            self.name = name
        if summary is not None:
            self.summary = self._define_str("summary", summary, nullable=True)


@JsonMap({"created_at": "createdAt", "created_by": "createdBy"})
class RequestsResponse(BaseModel):
    """Information about the response to the request. This object only returns when the network manager denied a request with a message.

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
        """Information about the response to the request. This object only returns when the network manager denied a request with a message.

        :param created_at: The date and time at which the network manager denied the request., defaults to None
        :type created_at: str, optional
        :param created_by: The network manager's user ID., defaults to None
        :type created_by: int, optional
        :param message: The network manager's request response message., defaults to None
        :type message: str, optional
        """
        if created_at is not None:
            self.created_at = created_at
        if created_by is not None:
            self.created_by = created_by
        if message is not None:
            self.message = message


@JsonMap({"id_": "id", "created_at": "createdAt", "created_by": "createdBy"})
class GetAllPanAddElementRequestsRequests(BaseModel):
    """GetAllPanAddElementRequestsRequests

    :param id_: The request's ID., defaults to None
    :type id_: int, optional
    :param created_at: The date and time at which the request was created., defaults to None
    :type created_at: str, optional
    :param created_by: The ID of the user who created the request., defaults to None
    :type created_by: int, optional
    :param message: The user's optional message included in the request., defaults to None
    :type message: str, optional
    :param status: The request's status., defaults to None
    :type status: RequestsStatus, optional
    :param element: Information about the requested element., defaults to None
    :type element: RequestsElement, optional
    :param response: Information about the response to the request. This object only returns when the network manager denied a request with a message., defaults to None
    :type response: RequestsResponse, optional
    """

    def __init__(
        self,
        id_: int = None,
        created_at: str = None,
        created_by: int = None,
        message: str = None,
        status: RequestsStatus = None,
        element: RequestsElement = None,
        response: RequestsResponse = None,
    ):
        """GetAllPanAddElementRequestsRequests

        :param id_: The request's ID., defaults to None
        :type id_: int, optional
        :param created_at: The date and time at which the request was created., defaults to None
        :type created_at: str, optional
        :param created_by: The ID of the user who created the request., defaults to None
        :type created_by: int, optional
        :param message: The user's optional message included in the request., defaults to None
        :type message: str, optional
        :param status: The request's status., defaults to None
        :type status: RequestsStatus, optional
        :param element: Information about the requested element., defaults to None
        :type element: RequestsElement, optional
        :param response: Information about the response to the request. This object only returns when the network manager denied a request with a message., defaults to None
        :type response: RequestsResponse, optional
        """
        if id_ is not None:
            self.id_ = id_
        if created_at is not None:
            self.created_at = created_at
        if created_by is not None:
            self.created_by = created_by
        if message is not None:
            self.message = message
        if status is not None:
            self.status = self._enum_matching(status, RequestsStatus.list(), "status")
        if element is not None:
            self.element = self._define_object(element, RequestsElement)
        if response is not None:
            self.response = self._define_object(response, RequestsResponse)


@JsonMap({"total_count": "totalCount"})
class GetAllPanAddElementRequestsMeta(BaseModel):
    """The response's non-standard meta information.

    :param limit: The maximum number of items returned., defaults to None
    :type limit: int, optional
    :param offset: The zero-based offset of the first item returned., defaults to None
    :type offset: int, optional
    :param total_count: The total count of items found., defaults to None
    :type total_count: int, optional
    """

    def __init__(self, limit: int = None, offset: int = None, total_count: int = None):
        """The response's non-standard meta information.

        :param limit: The maximum number of items returned., defaults to None
        :type limit: int, optional
        :param offset: The zero-based offset of the first item returned., defaults to None
        :type offset: int, optional
        :param total_count: The total count of items found., defaults to None
        :type total_count: int, optional
        """
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if total_count is not None:
            self.total_count = total_count


@JsonMap({})
class GetAllPanAddElementRequests(BaseModel):
    """GetAllPanAddElementRequests

    :param requests: Information about the requests to add elements to the Private API Network., defaults to None
    :type requests: List[GetAllPanAddElementRequestsRequests], optional
    :param meta: The response's non-standard meta information., defaults to None
    :type meta: GetAllPanAddElementRequestsMeta, optional
    """

    def __init__(
        self,
        requests: List[GetAllPanAddElementRequestsRequests] = None,
        meta: GetAllPanAddElementRequestsMeta = None,
    ):
        """GetAllPanAddElementRequests

        :param requests: Information about the requests to add elements to the Private API Network., defaults to None
        :type requests: List[GetAllPanAddElementRequestsRequests], optional
        :param meta: The response's non-standard meta information., defaults to None
        :type meta: GetAllPanAddElementRequestsMeta, optional
        """
        if requests is not None:
            self.requests = self._define_list(
                requests, GetAllPanAddElementRequestsRequests
            )
        if meta is not None:
            self.meta = self._define_object(meta, GetAllPanAddElementRequestsMeta)
