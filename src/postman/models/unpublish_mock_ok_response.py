from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id"})
class UnpublishMockOkResponseMock(BaseModel):
    """UnpublishMockOkResponseMock

    :param id_: The mock server's ID., defaults to None
    :type id_: str, optional
    """

    def __init__(self, id_: str = None):
        if id_ is not None:
            self.id_ = id_


@JsonMap({})
class UnpublishMockOkResponse(BaseModel):
    """UnpublishMockOkResponse

    :param mock: mock, defaults to None
    :type mock: UnpublishMockOkResponseMock, optional
    """

    def __init__(self, mock: UnpublishMockOkResponseMock = None):
        if mock is not None:
            self.mock = self._define_object(mock, UnpublishMockOkResponseMock)
