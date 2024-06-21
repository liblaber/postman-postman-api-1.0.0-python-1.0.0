from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id"})
class DeleteMockOkResponseMock(BaseModel):
    """Information about the mock server.

    :param id_: The mock server's ID., defaults to None
    :type id_: str, optional
    :param uid: The mock server's unique ID., defaults to None
    :type uid: str, optional
    """

    def __init__(self, id_: str = None, uid: str = None):
        if id_ is not None:
            self.id_ = id_
        if uid is not None:
            self.uid = uid


@JsonMap({})
class DeleteMockOkResponse(BaseModel):
    """DeleteMockOkResponse

    :param mock: Information about the mock server., defaults to None
    :type mock: DeleteMockOkResponseMock, optional
    """

    def __init__(self, mock: DeleteMockOkResponseMock = None):
        if mock is not None:
            self.mock = self._define_object(mock, DeleteMockOkResponseMock)
