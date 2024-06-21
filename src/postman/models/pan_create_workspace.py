from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id", "parent_folder_id": "parentFolderId"})
class PanCreateWorkspaceWorkspace(BaseModel):
    """PanCreateWorkspaceWorkspace

    :param id_: The workspace's ID.
    :type id_: str
    :param parent_folder_id: The workspace's parent folder ID.
    :type parent_folder_id: int
    """

    def __init__(self, id_: str, parent_folder_id: int):
        self.id_ = id_
        self.parent_folder_id = parent_folder_id


@JsonMap({})
class PanCreateWorkspace(BaseModel):
    """PanCreateWorkspace

    :param workspace: workspace, defaults to None
    :type workspace: PanCreateWorkspaceWorkspace, optional
    """

    def __init__(self, workspace: PanCreateWorkspaceWorkspace = None):
        if workspace is not None:
            self.workspace = self._define_object(workspace, PanCreateWorkspaceWorkspace)
