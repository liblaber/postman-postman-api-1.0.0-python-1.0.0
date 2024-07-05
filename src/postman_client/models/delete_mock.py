# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id"})
class DeleteMockMock(BaseModel):
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
class DeleteMock(BaseModel):
    """DeleteMock

    :param mock: Information about the mock server., defaults to None
    :type mock: DeleteMockMock, optional
    """

    def __init__(self, mock: DeleteMockMock = None):
        if mock is not None:
            self.mock = self._define_object(mock, DeleteMockMock)
