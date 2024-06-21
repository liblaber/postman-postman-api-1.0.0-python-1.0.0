from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap(
    {
        "id_": "id",
        "mock_url": "mockUrl",
        "created_at": "createdAt",
        "updated_at": "updatedAt",
    }
)
class CreateMockOkResponseMock(BaseModel):
    """Information about the mock server.

    :param id_: The mock server's ID., defaults to None
    :type id_: str, optional
    :param owner: The ID of mock server's owner., defaults to None
    :type owner: str, optional
    :param uid: The mock server's unique ID., defaults to None
    :type uid: str, optional
    :param collection: The unique ID of the mock's associated collection., defaults to None
    :type collection: str, optional
    :param mock_url: The mock server URL., defaults to None
    :type mock_url: str, optional
    :param config: Information about the mock server's configuration., defaults to None
    :type config: dict, optional
    :param created_at: The date and time at which the mock server was created., defaults to None
    :type created_at: str, optional
    :param updated_at: The date and time at which the mock server was last updated., defaults to None
    :type updated_at: str, optional
    :param environment: The unique ID of the mock's associated environment., defaults to None
    :type environment: str, optional
    """

    def __init__(
        self,
        id_: str = None,
        owner: str = None,
        uid: str = None,
        collection: str = None,
        mock_url: str = None,
        config: dict = None,
        created_at: str = None,
        updated_at: str = None,
        environment: str = None,
    ):
        if id_ is not None:
            self.id_ = id_
        if owner is not None:
            self.owner = owner
        if uid is not None:
            self.uid = uid
        if collection is not None:
            self.collection = collection
        if mock_url is not None:
            self.mock_url = mock_url
        if config is not None:
            self.config = config
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if environment is not None:
            self.environment = environment


@JsonMap({})
class CreateMockOkResponse(BaseModel):
    """CreateMockOkResponse

    :param mock: Information about the mock server., defaults to None
    :type mock: CreateMockOkResponseMock, optional
    """

    def __init__(self, mock: CreateMockOkResponseMock = None):
        if mock is not None:
            self.mock = self._define_object(mock, CreateMockOkResponseMock)
