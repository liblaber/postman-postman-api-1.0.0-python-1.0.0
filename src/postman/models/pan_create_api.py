from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id", "parent_folder_id": "parentFolderId"})
class PanCreateApiApi(BaseModel):
    """PanCreateApiApi

    :param id_: The API's ID.
    :type id_: str
    :param parent_folder_id: The API's parent folder ID.
    :type parent_folder_id: int
    """

    def __init__(self, id_: str, parent_folder_id: int):
        self.id_ = id_
        self.parent_folder_id = parent_folder_id


@JsonMap({})
class PanCreateApi(BaseModel):
    """PanCreateApi

    :param api: api, defaults to None
    :type api: PanCreateApiApi, optional
    """

    def __init__(self, api: PanCreateApiApi = None):
        if api is not None:
            self.api = self._define_object(api, PanCreateApiApi)
