from enum import Enum
from .utils.json_map import JsonMap
from .base import BaseModel


class WorkspaceType3(Enum):
    """An enumeration representing different categories.

    :cvar PRIVATE: "private"
    :vartype PRIVATE: str
    :cvar PERSONAL: "personal"
    :vartype PERSONAL: str
    :cvar TEAM: "team"
    :vartype TEAM: str
    :cvar PUBLIC: "public"
    :vartype PUBLIC: str
    """

    PRIVATE = "private"
    PERSONAL = "personal"
    TEAM = "team"
    PUBLIC = "public"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, WorkspaceType3._member_map_.values()))


@JsonMap({"type_": "type"})
class UpdateWorkspaceRequestWorkspace(BaseModel):
    """UpdateWorkspaceRequestWorkspace

    :param name: The workspace's new name., defaults to None
    :type name: str, optional
    :param type_: The new workspace visibility [type](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/managing-workspaces/#changing-workspace-visibility). This property does not support the following workspace visibility changes:<br/>- `private` to `public`, `public` to `private`, and `private` to `personal` for Free and Basic [plans](https://www.postman.com/pricing/).<br/>- `public` to `personal` for team users.<br/>, defaults to None
    :type type_: WorkspaceType3, optional
    :param description: The new workspace description., defaults to None
    :type description: str, optional
    """

    def __init__(
        self, name: str = None, type_: WorkspaceType3 = None, description: str = None
    ):
        if name is not None:
            self.name = name
        if type_ is not None:
            self.type_ = self._enum_matching(type_, WorkspaceType3.list(), "type_")
        if description is not None:
            self.description = description


@JsonMap({})
class UpdateWorkspaceRequest(BaseModel):
    """UpdateWorkspaceRequest

    :param workspace: workspace, defaults to None
    :type workspace: UpdateWorkspaceRequestWorkspace, optional
    """

    def __init__(self, workspace: UpdateWorkspaceRequestWorkspace = None):
        if workspace is not None:
            self.workspace = self._define_object(
                workspace, UpdateWorkspaceRequestWorkspace
            )
