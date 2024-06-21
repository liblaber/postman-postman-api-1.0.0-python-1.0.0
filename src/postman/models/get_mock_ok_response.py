from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap(
    {
        "match_body": "matchBody",
        "match_query_params": "matchQueryParams",
        "match_wildcards": "matchWildcards",
        "server_response_id": "serverResponseId",
    }
)
class MockConfig1(BaseModel):
    """Information about the mock server's configuration.

    :param headers: A list of the mock server's headers., defaults to None
    :type headers: List[str], optional
    :param match_body: If true, match the request body., defaults to None
    :type match_body: bool, optional
    :param match_query_params: If true, match query parameters., defaults to None
    :type match_query_params: bool, optional
    :param match_wildcards: If true, use wildcard variable matching., defaults to None
    :type match_wildcards: bool, optional
    :param server_response_id: The ID of mock server's default response for requests. All calls to the mock server will return the defined response., defaults to None
    :type server_response_id: str, optional
    """

    def __init__(
        self,
        headers: List[str] = None,
        match_body: bool = None,
        match_query_params: bool = None,
        match_wildcards: bool = None,
        server_response_id: str = None,
    ):
        if headers is not None:
            self.headers = headers
        if match_body is not None:
            self.match_body = match_body
        if match_query_params is not None:
            self.match_query_params = match_query_params
        if match_wildcards is not None:
            self.match_wildcards = match_wildcards
        if server_response_id is not None:
            self.server_response_id = server_response_id


@JsonMap(
    {
        "id_": "id",
        "mock_url": "mockUrl",
        "created_at": "createdAt",
        "updated_at": "updatedAt",
        "is_public": "isPublic",
    }
)
class GetMockOkResponseMock(BaseModel):
    """GetMockOkResponseMock

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
    :param name: The mock server's name., defaults to None
    :type name: str, optional
    :param config: Information about the mock server's configuration., defaults to None
    :type config: MockConfig1, optional
    :param created_at: The date and time at which the mock server was created., defaults to None
    :type created_at: str, optional
    :param updated_at: The date and time at which the mock server was last updated., defaults to None
    :type updated_at: str, optional
    :param is_public: If true, the mock server is public and visible to all users. This field does not indicate the mock server's access control status., defaults to None
    :type is_public: bool, optional
    :param deactivated: If true, the mock server is not active. Mock servers deactivate when a linked collection or environment is deleted., defaults to None
    :type deactivated: bool, optional
    :param environment: The mock server's associated environment ID., defaults to None
    :type environment: str, optional
    """

    def __init__(
        self,
        id_: str = None,
        owner: str = None,
        uid: str = None,
        collection: str = None,
        mock_url: str = None,
        name: str = None,
        config: MockConfig1 = None,
        created_at: str = None,
        updated_at: str = None,
        is_public: bool = None,
        deactivated: bool = None,
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
        if name is not None:
            self.name = name
        if config is not None:
            self.config = self._define_object(config, MockConfig1)
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if is_public is not None:
            self.is_public = is_public
        if deactivated is not None:
            self.deactivated = deactivated
        if environment is not None:
            self.environment = environment


@JsonMap({})
class GetMockOkResponse(BaseModel):
    """GetMockOkResponse

    :param mock: mock, defaults to None
    :type mock: GetMockOkResponseMock, optional
    """

    def __init__(self, mock: GetMockOkResponseMock = None):
        if mock is not None:
            self.mock = self._define_object(mock, GetMockOkResponseMock)
