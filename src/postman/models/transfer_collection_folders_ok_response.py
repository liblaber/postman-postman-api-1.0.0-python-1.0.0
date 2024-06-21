from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class TransferCollectionFoldersOkResponse(BaseModel):
    """TransferCollectionFoldersOkResponse

    :param ids: A list of the transferred collection request, response, or folder UIDs., defaults to None
    :type ids: List[str], optional
    """

    def __init__(self, ids: List[str] = None):
        if ids is not None:
            self.ids = ids
