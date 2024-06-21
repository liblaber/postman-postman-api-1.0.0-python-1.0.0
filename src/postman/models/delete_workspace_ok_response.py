from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id"})
class DeleteWorkspaceOkResponseWorkspace(BaseModel):
    """Information about the deleted workspace.

    :param id_: The workspace's ID., defaults to None
    :type id_: str, optional
    """

    def __init__(self, id_: str = None):
        if id_ is not None:
            self.id_ = id_


@JsonMap({})
class DeleteWorkspaceOkResponse(BaseModel):
    """DeleteWorkspaceOkResponse

    :param workspace: Information about the deleted workspace., defaults to None
    :type workspace: DeleteWorkspaceOkResponseWorkspace, optional
    """

    def __init__(self, workspace: DeleteWorkspaceOkResponseWorkspace = None):
        if workspace is not None:
            self.workspace = self._define_object(
                workspace, DeleteWorkspaceOkResponseWorkspace
            )
