from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"parent_folder_id": "parentFolderId"})
class PanCreateFolderFolder(BaseModel):
    """PanCreateFolderFolder

    :param name: The folder's name.
    :type name: str
    :param description: The folder's description., defaults to None
    :type description: str, optional
    :param parent_folder_id: The folder's parent folder ID. This value defaults to `0`. To create a folder at the root level, omit this property., defaults to None
    :type parent_folder_id: int, optional
    """

    def __init__(
        self, name: str, description: str = None, parent_folder_id: int = None
    ):
        self.name = name
        if description is not None:
            self.description = description
        if parent_folder_id is not None:
            self.parent_folder_id = parent_folder_id


@JsonMap({})
class PanCreateFolder(BaseModel):
    """PanCreateFolder

    :param folder: folder, defaults to None
    :type folder: PanCreateFolderFolder, optional
    """

    def __init__(self, folder: PanCreateFolderFolder = None):
        if folder is not None:
            self.folder = self._define_object(folder, PanCreateFolderFolder)
