<<<<<<< HEAD
=======
# This file was generated by liblab | https://liblab.com/

>>>>>>> 95da91c (initial commit)
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id"})
class DeleteEnvironmentOkResponseEnvironment(BaseModel):
    """DeleteEnvironmentOkResponseEnvironment

    :param id_: The deleted environment's ID., defaults to None
    :type id_: str, optional
    :param uid: The deleted environment's unique ID., defaults to None
    :type uid: str, optional
    """

    def __init__(self, id_: str = None, uid: str = None):
        if id_ is not None:
            self.id_ = id_
        if uid is not None:
            self.uid = uid


@JsonMap({})
class DeleteEnvironmentOkResponse(BaseModel):
    """DeleteEnvironmentOkResponse

    :param environment: environment, defaults to None
    :type environment: DeleteEnvironmentOkResponseEnvironment, optional
    """

    def __init__(self, environment: DeleteEnvironmentOkResponseEnvironment = None):
        if environment is not None:
            self.environment = self._define_object(
                environment, DeleteEnvironmentOkResponseEnvironment
            )
