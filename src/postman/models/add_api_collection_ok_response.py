from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id"})
class AddApiCollectionOkResponse(BaseModel):
    """AddApiCollectionOkResponse

    :param id_: The collection's ID., defaults to None
    :type id_: str, optional
    """

    def __init__(self, id_: str = None):
        if id_ is not None:
            self.id_ = id_
