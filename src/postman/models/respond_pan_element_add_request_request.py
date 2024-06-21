from enum import Enum
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class RespondPanElementAddRequestRequestResponse(BaseModel):
    """The response to the user's request.

    :param message: A message that details why the user's request was denied., defaults to None
    :type message: str, optional
    """

    def __init__(self, message: str = None):
        if message is not None:
            self.message = message


class RespondPanElementAddRequestRequestStatus(Enum):
    """An enumeration representing different categories.

    :cvar DENIED: "denied"
    :vartype DENIED: str
    :cvar APPROVED: "approved"
    :vartype APPROVED: str
    """

    DENIED = "denied"
    APPROVED = "approved"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                RespondPanElementAddRequestRequestStatus._member_map_.values(),
            )
        )


@JsonMap({})
class RespondPanElementAddRequestRequest(BaseModel):
    """RespondPanElementAddRequestRequest

    :param response: The response to the user's request., defaults to None
    :type response: RespondPanElementAddRequestRequestResponse, optional
    :param status: The request's status.
    :type status: RespondPanElementAddRequestRequestStatus
    """

    def __init__(
        self,
        status: RespondPanElementAddRequestRequestStatus,
        response: RespondPanElementAddRequestRequestResponse = None,
    ):
        if response is not None:
            self.response = self._define_object(
                response, RespondPanElementAddRequestRequestResponse
            )
        self.status = self._enum_matching(
            status, RespondPanElementAddRequestRequestStatus.list(), "status"
        )
