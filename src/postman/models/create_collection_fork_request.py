from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class CreateCollectionForkRequest(BaseModel):
    """CreateCollectionForkRequest

    :param label: The fork's label.
    :type label: str
    """

    def __init__(self, label: str):
        self.label = label
