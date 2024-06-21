from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class CreateMockRequestMock(BaseModel):
    """CreateMockRequestMock

    :param collection: The unique ID of the mock's associated collection.
    :type collection: str
    :param environment: The unique ID of the mock's associated environment., defaults to None
    :type environment: str, optional
    :param name: The mock server's name., defaults to None
    :type name: str, optional
    :param private: If true, the mock server is set private. By default, mock servers are public and can receive requests from anyone and anywhere., defaults to None
    :type private: bool, optional
    """

    def __init__(
        self,
        collection: str,
        environment: str = None,
        name: str = None,
        private: bool = None,
    ):
        self.collection = collection
        if environment is not None:
            self.environment = environment
        if name is not None:
            self.name = name
        if private is not None:
            self.private = private


@JsonMap({})
class CreateMockRequest(BaseModel):
    """CreateMockRequest

    :param mock: mock, defaults to None
    :type mock: CreateMockRequestMock, optional
    """

    def __init__(self, mock: CreateMockRequestMock = None):
        if mock is not None:
            self.mock = self._define_object(mock, CreateMockRequestMock)
