from enum import Enum
from .utils.json_map import JsonMap
from .base import BaseModel


class WorkspaceType1(Enum):
    """An enumeration representing different categories.

    :cvar PERSONAL: "personal"
    :vartype PERSONAL: str
    :cvar PRIVATE: "private"
    :vartype PRIVATE: str
    :cvar PUBLIC: "public"
    :vartype PUBLIC: str
    :cvar TEAM: "team"
    :vartype TEAM: str
    :cvar PARTNER: "partner"
    :vartype PARTNER: str
    """

    PERSONAL = "personal"
    PRIVATE = "private"
    PUBLIC = "public"
    TEAM = "team"
    PARTNER = "partner"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, WorkspaceType1._member_map_.values()))


@JsonMap({"type_": "type"})
class CreateWorkspaceRequestWorkspace(BaseModel):
    """Information about the workspace.

    :param name: The workspace's name.
    :type name: str
    :param type_: The type of workspace:<br/>- `personal`<br/>- `private` — Private workspaces are available on Postman [**Professional** and **Enterprise** plans](https://www.postman.com/pricing).<br/>- `public`<br/>- `team`<br/>- `partner` — [Partner Workspaces](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/partner-workspaces/) are available on Postman [**Professional** and **Enterprise** plans](https://www.postman.com/pricing)).<br/>
    :type type_: WorkspaceType1
    :param description: The workspace's description., defaults to None
    :type description: str, optional
    """

    def __init__(self, name: str, type_: WorkspaceType1, description: str = None):
        self.name = name
        self.type_ = self._enum_matching(type_, WorkspaceType1.list(), "type_")
        if description is not None:
            self.description = description


@JsonMap({})
class CreateWorkspaceRequest(BaseModel):
    """CreateWorkspaceRequest

    :param workspace: Information about the workspace., defaults to None
    :type workspace: CreateWorkspaceRequestWorkspace, optional
    """

    def __init__(self, workspace: CreateWorkspaceRequestWorkspace = None):
        if workspace is not None:
            self.workspace = self._define_object(
                workspace, CreateWorkspaceRequestWorkspace
            )
