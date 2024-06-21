from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id"})
class CreateWorkspaceOkResponseWorkspace(BaseModel):
    """Information about the created workspace.

    :param id_: The workspace's ID., defaults to None
    :type id_: str, optional
    :param name: The workspace's name., defaults to None
    :type name: str, optional
    """

    def __init__(self, id_: str = None, name: str = None):
        if id_ is not None:
            self.id_ = id_
        if name is not None:
            self.name = name


@JsonMap({})
class CreateWorkspaceOkResponse(BaseModel):
    """CreateWorkspaceOkResponse

    :param workspace: Information about the created workspace., defaults to None
    :type workspace: CreateWorkspaceOkResponseWorkspace, optional
    """

    def __init__(self, workspace: CreateWorkspaceOkResponseWorkspace = None):
        if workspace is not None:
            self.workspace = self._define_object(
                workspace, CreateWorkspaceOkResponseWorkspace
            )
