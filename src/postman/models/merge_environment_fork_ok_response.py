from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class MergeEnvironmentForkOkResponseEnvironment(BaseModel):
    """Information about the merged environment.

    :param uid: The merged environment's ID., defaults to None
    :type uid: str, optional
    """

    def __init__(self, uid: str = None):
        if uid is not None:
            self.uid = uid


@JsonMap({})
class MergeEnvironmentForkOkResponse(BaseModel):
    """MergeEnvironmentForkOkResponse

    :param environment: Information about the merged environment., defaults to None
    :type environment: MergeEnvironmentForkOkResponseEnvironment, optional
    """

    def __init__(self, environment: MergeEnvironmentForkOkResponseEnvironment = None):
        if environment is not None:
            self.environment = self._define_object(
                environment, MergeEnvironmentForkOkResponseEnvironment
            )
