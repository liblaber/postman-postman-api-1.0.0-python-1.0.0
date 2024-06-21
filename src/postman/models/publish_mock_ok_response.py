from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id"})
class PublishMockOkResponseMock(BaseModel):
    """PublishMockOkResponseMock

    :param id_: The mock server's ID., defaults to None
    :type id_: str, optional
    """

    def __init__(self, id_: str = None):
        if id_ is not None:
            self.id_ = id_


@JsonMap({})
class PublishMockOkResponse(BaseModel):
    """PublishMockOkResponse

    :param mock: mock, defaults to None
    :type mock: PublishMockOkResponseMock, optional
    """

    def __init__(self, mock: PublishMockOkResponseMock = None):
        if mock is not None:
            self.mock = self._define_object(mock, PublishMockOkResponseMock)
