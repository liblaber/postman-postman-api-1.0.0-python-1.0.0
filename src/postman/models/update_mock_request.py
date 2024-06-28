<<<<<<< HEAD
=======
# This file was generated by liblab | https://liblab.com/

>>>>>>> 95da91c (initial commit)
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"server_response_id": "serverResponseId"})
class MockConfig2(BaseModel):
    """The mock server's configuration settings.

<<<<<<< HEAD
    :param server_response_id: The server response ID. This sets the given server response as the default response for each request.<br/><br/>To deactivate a server response, pass a null value.<br/>, defaults to None
=======
    :param server_response_id: The server response ID. This sets the given server response as the default response for each request.<br><br>To deactivate a server response, pass a null value.<br>, defaults to None
>>>>>>> 95da91c (initial commit)
    :type server_response_id: str, optional
    """

    def __init__(self, server_response_id: str = None):
        if server_response_id is not None:
            self.server_response_id = server_response_id


@JsonMap({"version_tag": "versionTag"})
class UpdateMockRequestMock(BaseModel):
    """UpdateMockRequestMock

    :param name: The mock server's name., defaults to None
    :type name: str, optional
    :param environment: The associated environment's unique ID., defaults to None
    :type environment: str, optional
    :param description: The mock server's description., defaults to None
    :type description: str, optional
    :param private: If true, the mock server is set private. By default, mock servers are public and can receive requests from anyone and anywhere., defaults to None
    :type private: bool, optional
    :param version_tag: The API's version tag ID., defaults to None
    :type version_tag: str, optional
    :param config: The mock server's configuration settings., defaults to None
    :type config: MockConfig2, optional
    """

    def __init__(
        self,
        name: str = None,
        environment: str = None,
        description: str = None,
        private: bool = None,
        version_tag: str = None,
        config: MockConfig2 = None,
    ):
        if name is not None:
            self.name = name
        if environment is not None:
            self.environment = environment
        if description is not None:
            self.description = description
        if private is not None:
            self.private = private
        if version_tag is not None:
            self.version_tag = version_tag
        if config is not None:
            self.config = self._define_object(config, MockConfig2)


@JsonMap({})
class UpdateMockRequest(BaseModel):
    """UpdateMockRequest

    :param mock: mock, defaults to None
    :type mock: UpdateMockRequestMock, optional
    """

    def __init__(self, mock: UpdateMockRequestMock = None):
        if mock is not None:
            self.mock = self._define_object(mock, UpdateMockRequestMock)
