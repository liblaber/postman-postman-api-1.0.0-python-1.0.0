# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"fork_name": "forkName"})
class ForkEnvironmentEnvironment(BaseModel):
    """Information about the forked environment.

    :param uid: The forked environment's ID., defaults to None
    :type uid: str, optional
    :param name: The name of the forked environment., defaults to None
    :type name: str, optional
    :param fork_name: The forked environment's label., defaults to None
    :type fork_name: str, optional
    """

    def __init__(self, uid: str = None, name: str = None, fork_name: str = None):
        if uid is not None:
            self.uid = uid
        if name is not None:
            self.name = name
        if fork_name is not None:
            self.fork_name = fork_name


@JsonMap({})
class ForkEnvironmentOkResponse(BaseModel):
    """ForkEnvironmentOkResponse

    :param environment: Information about the forked environment., defaults to None
    :type environment: ForkEnvironmentEnvironment, optional
    """

    def __init__(self, environment: ForkEnvironmentEnvironment = None):
        if environment is not None:
            self.environment = self._define_object(
                environment, ForkEnvironmentEnvironment
            )
