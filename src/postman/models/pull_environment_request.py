from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class PullEnvironmentRequest(BaseModel):
    """PullEnvironmentRequest

    :param source: The source environment's unique ID to pull data from., defaults to None
    :type source: str, optional
    """

    def __init__(self, source: str = None):
        if source is not None:
            self.source = source
