# This file was generated by liblab | https://liblab.com/

from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


class DisplayName(Enum):
    """An enumeration representing different categories.

    :cvar ADMIN: "Admin"
    :vartype ADMIN: str
    :cvar VIEWER: "Viewer"
    :vartype VIEWER: str
    :cvar EDITOR: "Editor"
    :vartype EDITOR: str
    """

    ADMIN = "Admin"
    VIEWER = "Viewer"
    EDITOR = "Editor"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, DisplayName._member_map_.values()))


@JsonMap({"id_": "id", "display_name": "displayName"})
class UpdateWorkspaceRolesRoles2(BaseModel):
    """UpdateWorkspaceRolesRoles2

    :param id_: The role's ID., defaults to None
    :type id_: int, optional
    :param user: A list of user IDs assigned to the role., defaults to None
    :type user: List[float], optional
    :param usergroup: A list of user group IDs assigned to the role., defaults to None
    :type usergroup: List[float], optional
    :param display_name: The role's display name., defaults to None
    :type display_name: DisplayName, optional
    """

    def __init__(
        self,
        id_: int = None,
        user: List[float] = None,
        usergroup: List[float] = None,
        display_name: DisplayName = None,
    ):
        """UpdateWorkspaceRolesRoles2

        :param id_: The role's ID., defaults to None
        :type id_: int, optional
        :param user: A list of user IDs assigned to the role., defaults to None
        :type user: List[float], optional
        :param usergroup: A list of user group IDs assigned to the role., defaults to None
        :type usergroup: List[float], optional
        :param display_name: The role's display name., defaults to None
        :type display_name: DisplayName, optional
        """
        if id_ is not None:
            self.id_ = id_
        if user is not None:
            self.user = user
        if usergroup is not None:
            self.usergroup = usergroup
        if display_name is not None:
            self.display_name = self._enum_matching(
                display_name, DisplayName.list(), "display_name"
            )


@JsonMap({})
class UpdateWorkspaceRolesOkResponse(BaseModel):
    """UpdateWorkspaceRolesOkResponse

    :param roles: roles, defaults to None
    :type roles: List[UpdateWorkspaceRolesRoles2], optional
    """

    def __init__(self, roles: List[UpdateWorkspaceRolesRoles2] = None):
        """UpdateWorkspaceRolesOkResponse

        :param roles: roles, defaults to None
        :type roles: List[UpdateWorkspaceRolesRoles2], optional
        """
        if roles is not None:
            self.roles = self._define_list(roles, UpdateWorkspaceRolesRoles2)
