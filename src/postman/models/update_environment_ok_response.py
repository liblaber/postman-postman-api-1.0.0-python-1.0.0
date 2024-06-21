from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id"})
class UpdateEnvironmentOkResponseEnvironment(BaseModel):
    """UpdateEnvironmentOkResponseEnvironment

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
class UpdateEnvironmentOkResponse(BaseModel):
    """UpdateEnvironmentOkResponse

    :param environment: environment, defaults to None
    :type environment: UpdateEnvironmentOkResponseEnvironment, optional
    """

    def __init__(self, environment: UpdateEnvironmentOkResponseEnvironment = None):
        if environment is not None:
            self.environment = self._define_object(
                environment, UpdateEnvironmentOkResponseEnvironment
            )
