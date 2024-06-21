from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"fork_name": "forkName"})
class ForkEnvironmentRequest(BaseModel):
    """ForkEnvironmentRequest

    :param fork_name: The forked environment's label.
    :type fork_name: str
    """

    def __init__(self, fork_name: str):
        self.fork_name = fork_name
