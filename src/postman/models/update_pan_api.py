from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"parent_folder_id": "parentFolderId"})
class UpdatePanApiApi(BaseModel):
    """UpdatePanApiApi

    :param parent_folder_id: The API's new parent folder ID., defaults to None
    :type parent_folder_id: int, optional
    """

    def __init__(self, parent_folder_id: int = None):
        if parent_folder_id is not None:
            self.parent_folder_id = parent_folder_id


@JsonMap({})
class UpdatePanApi(BaseModel):
    """UpdatePanApi

    :param api: api, defaults to None
    :type api: UpdatePanApiApi, optional
    """

    def __init__(self, api: UpdatePanApiApi = None):
        if api is not None:
            self.api = self._define_object(api, UpdatePanApiApi)
