from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"parent_folder_id": "parentFolderId"})
class UpdatePanWorkspaceWorkspace(BaseModel):
    """UpdatePanWorkspaceWorkspace

    :param parent_folder_id: The workspace's new parent folder ID., defaults to None
    :type parent_folder_id: int, optional
    """

    def __init__(self, parent_folder_id: int = None):
        if parent_folder_id is not None:
            self.parent_folder_id = parent_folder_id


@JsonMap({})
class UpdatePanWorkspace(BaseModel):
    """UpdatePanWorkspace

    :param workspace: workspace, defaults to None
    :type workspace: UpdatePanWorkspaceWorkspace, optional
    """

    def __init__(self, workspace: UpdatePanWorkspaceWorkspace = None):
        if workspace is not None:
            self.workspace = self._define_object(workspace, UpdatePanWorkspaceWorkspace)
