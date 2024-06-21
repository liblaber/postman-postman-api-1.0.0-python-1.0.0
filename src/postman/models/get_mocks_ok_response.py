from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


class DelayType(Enum):
    """An enumeration representing different categories.

    :cvar FIXED: "fixed"
    :vartype FIXED: str
    """

    FIXED = "fixed"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, DelayType._member_map_.values()))


class Preset(Enum):
    """An enumeration representing different categories.

    :cvar _1: "1"
    :vartype _1: str
    :cvar _2: "2"
    :vartype _2: str
    """

    _1 = "1"
    _2 = "2"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Preset._member_map_.values()))


@JsonMap({"type_": "type"})
class Delay(BaseModel):
    """Information about the mock server's simulated network delay settings. This returns a null value if there are no configured network delay settings.

    :param type_: The type of simulated delay value:<br/>- `fixed` — The delay value is a fixed value.<br/>, defaults to None
    :type type_: DelayType, optional
    :param preset: The simulated fixed network delay value:<br/>- `1` — 2G (300 ms).<br/>- `2` — 3G (100 ms).<br/>The object does not return this value for custom delay values.<br/>, defaults to None
    :type preset: Preset, optional
    :param duration: The configured delay, in milliseconds., defaults to None
    :type duration: int, optional
    """

    def __init__(
        self, type_: DelayType = None, preset: Preset = None, duration: int = None
    ):
        if type_ is not None:
            self.type_ = self._enum_matching(type_, DelayType.list(), "type_")
        if preset is not None:
            self.preset = self._enum_matching(preset, Preset.list(), "preset")
        if duration is not None:
            self.duration = duration


@JsonMap(
    {
        "match_body": "matchBody",
        "match_query_params": "matchQueryParams",
        "match_wildcards": "matchWildcards",
        "server_response_id": "serverResponseId",
    }
)
class MocksConfig(BaseModel):
    """Information about the mock server's configuration.

    :param delay: Information about the mock server's simulated network delay settings. This returns a null value if there are no configured network delay settings., defaults to None
    :type delay: Delay, optional
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
        delay: Delay = None,
        headers: List[str] = None,
        match_body: bool = None,
        match_query_params: bool = None,
        match_wildcards: bool = None,
        server_response_id: str = None,
    ):
        if delay is not None:
            self.delay = self._define_object(delay, Delay)
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
        "is_public": "isPublic",
        "updated_at": "updatedAt",
    }
)
class GetMocksOkResponseMocks(BaseModel):
    """Information about the mock servers.

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
    :type config: MocksConfig, optional
    :param created_at: The date and time at which the mock server was created., defaults to None
    :type created_at: str, optional
    :param environment: The mock server's associated environment ID., defaults to None
    :type environment: str, optional
    :param is_public: If true, the mock server is public and visible to all users. This field does not indicate the mock server's access control status., defaults to None
    :type is_public: bool, optional
    :param name: The mock server's name., defaults to None
    :type name: str, optional
    :param updated_at: The date and time at which the mock server was last updated., defaults to None
    :type updated_at: str, optional
    """

    def __init__(
        self,
        id_: str = None,
        owner: str = None,
        uid: str = None,
        collection: str = None,
        mock_url: str = None,
        config: MocksConfig = None,
        created_at: str = None,
        environment: str = None,
        is_public: bool = None,
        name: str = None,
        updated_at: str = None,
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
            self.config = self._define_object(config, MocksConfig)
        if created_at is not None:
            self.created_at = created_at
        if environment is not None:
            self.environment = environment
        if is_public is not None:
            self.is_public = is_public
        if name is not None:
            self.name = name
        if updated_at is not None:
            self.updated_at = updated_at


@JsonMap({})
class GetMocksOkResponse(BaseModel):
    """GetMocksOkResponse

    :param mocks: mocks, defaults to None
    :type mocks: List[GetMocksOkResponseMocks], optional
    """

    def __init__(self, mocks: List[GetMocksOkResponseMocks] = None):
        if mocks is not None:
            self.mocks = self._define_list(mocks, GetMocksOkResponseMocks)
