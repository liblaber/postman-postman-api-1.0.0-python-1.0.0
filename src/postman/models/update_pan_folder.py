from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"parent_folder_id": "parentFolderId"})
class UpdatePanFolderFolder(BaseModel):
    """UpdatePanFolderFolder

    :param name: The folder's new name., defaults to None
    :type name: str, optional
    :param description: The folder's updated description., defaults to None
    :type description: str, optional
    :param parent_folder_id: The folder's new parent folder ID., defaults to None
    :type parent_folder_id: int, optional
    """

    def __init__(
        self, name: str = None, description: str = None, parent_folder_id: int = None
    ):
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if parent_folder_id is not None:
            self.parent_folder_id = parent_folder_id


@JsonMap({})
class UpdatePanFolder(BaseModel):
    """UpdatePanFolder

    :param folder: folder, defaults to None
    :type folder: UpdatePanFolderFolder, optional
    """

    def __init__(self, folder: UpdatePanFolderFolder = None):
        if folder is not None:
            self.folder = self._define_object(folder, UpdatePanFolderFolder)
