from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id"})
class CreateEnvironmentOkResponseEnvironment(BaseModel):
    """CreateEnvironmentOkResponseEnvironment

    :param id_: The environment's ID., defaults to None
    :type id_: str, optional
    :param name: The environment's name., defaults to None
    :type name: str, optional
    :param uid: The environment's unique ID., defaults to None
    :type uid: str, optional
    """

    def __init__(self, id_: str = None, name: str = None, uid: str = None):
        if id_ is not None:
            self.id_ = id_
        if name is not None:
            self.name = name
        if uid is not None:
            self.uid = uid


@JsonMap({})
class CreateEnvironmentOkResponse(BaseModel):
    """CreateEnvironmentOkResponse

    :param environment: environment, defaults to None
    :type environment: CreateEnvironmentOkResponseEnvironment, optional
    """

    def __init__(self, environment: CreateEnvironmentOkResponseEnvironment = None):
        if environment is not None:
            self.environment = self._define_object(
                environment, CreateEnvironmentOkResponseEnvironment
            )
