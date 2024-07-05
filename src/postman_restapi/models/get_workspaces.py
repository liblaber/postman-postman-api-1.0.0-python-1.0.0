# This file was generated by liblab | https://liblab.com/

from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


class WorkspacesType(Enum):
    """An enumeration representing different categories.

    :cvar PERSONAL: "personal"
    :vartype PERSONAL: str
    :cvar TEAM: "team"
    :vartype TEAM: str
    :cvar PRIVATE: "private"
    :vartype PRIVATE: str
    :cvar PUBLIC: "public"
    :vartype PUBLIC: str
    :cvar PARTNER: "partner"
    :vartype PARTNER: str
    """

    PERSONAL = "personal"
    TEAM = "team"
    PRIVATE = "private"
    PUBLIC = "public"
    PARTNER = "partner"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, WorkspacesType._member_map_.values()))


class WorkspacesVisibility(Enum):
    """An enumeration representing different categories.

    :cvar PERSONAL: "personal"
    :vartype PERSONAL: str
    :cvar TEAM: "team"
    :vartype TEAM: str
    :cvar PRIVATE: "private"
    :vartype PRIVATE: str
    :cvar PUBLIC: "public"
    :vartype PUBLIC: str
    :cvar PARTNER: "partner"
    :vartype PARTNER: str
    """

    PERSONAL = "personal"
    TEAM = "team"
    PRIVATE = "private"
    PUBLIC = "public"
    PARTNER = "partner"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, WorkspacesVisibility._member_map_.values()))


@JsonMap({"id_": "id", "created_by": "createdBy", "type_": "type"})
class Workspaces(BaseModel):
    """Information about the workspace.

    :param id_: The workspace's ID., defaults to None
    :type id_: str, optional
    :param name: The workspace's name., defaults to None
    :type name: str, optional
    :param created_by: The user who created the workspace. The response only returns workspaces that you have access to., defaults to None
    :type created_by: int, optional
    :param type_: The type of workspace., defaults to None
    :type type_: WorkspacesType, optional
    :param visibility: The workspace's visibility. [Visibility](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/managing-workspaces/#changing-workspace-visibility) determines who can access the workspace:<br>- `personal` — Only you can access the workspace.<br>- `team` — All team members can access the workspace.<br>- `private` — Only invited team members can access the workspace ([**Professional** and **Enterprise** plans only](https://www.postman.com/pricing)).<br>- `public` — Everyone can access the workspace.<br>- `partner` — Only invited team members and [partners](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/partner-workspaces/) can access the workspace ([**Professional** and **Enterprise** plans only](https://www.postman.com/pricing)).<br>, defaults to None
    :type visibility: WorkspacesVisibility, optional
    """

    def __init__(
        self,
        id_: str = None,
        name: str = None,
        created_by: int = None,
        type_: WorkspacesType = None,
        visibility: WorkspacesVisibility = None,
    ):
        if id_ is not None:
            self.id_ = id_
        if name is not None:
            self.name = name
        if created_by is not None:
            self.created_by = created_by
        if type_ is not None:
            self.type_ = self._enum_matching(type_, WorkspacesType.list(), "type_")
        if visibility is not None:
            self.visibility = self._enum_matching(
                visibility, WorkspacesVisibility.list(), "visibility"
            )


@JsonMap({})
class GetWorkspaces(BaseModel):
    """GetWorkspaces

    :param workspaces: workspaces, defaults to None
    :type workspaces: List[Workspaces], optional
    """

    def __init__(self, workspaces: List[Workspaces] = None):
        if workspaces is not None:
            self.workspaces = self._define_list(workspaces, Workspaces)
