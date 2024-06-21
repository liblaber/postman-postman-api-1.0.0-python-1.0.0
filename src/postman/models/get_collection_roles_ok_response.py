from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


class GroupRole(Enum):
    """An enumeration representing different categories.

    :cvar VIEWER: "VIEWER"
    :vartype VIEWER: str
    :cvar EDITOR: "EDITOR"
    :vartype EDITOR: str
    """

    VIEWER = "VIEWER"
    EDITOR = "EDITOR"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, GroupRole._member_map_.values()))


@JsonMap({"id_": "id"})
class Group(BaseModel):
    """Information about the group role.

    :param role: The role type:<br/>- `VIEWER` — Can view, fork, and export collections.<br/>- `EDITOR` — Can edit collections directly.<br/>, defaults to None
    :type role: GroupRole, optional
    :param id_: The role's ID., defaults to None
    :type id_: float, optional
    """

    def __init__(self, role: GroupRole = None, id_: float = None):
        if role is not None:
            self.role = self._enum_matching(role, GroupRole.list(), "role")
        if id_ is not None:
            self.id_ = id_


class TeamRole(Enum):
    """An enumeration representing different categories.

    :cvar VIEWER: "VIEWER"
    :vartype VIEWER: str
    :cvar EDITOR: "EDITOR"
    :vartype EDITOR: str
    """

    VIEWER = "VIEWER"
    EDITOR = "EDITOR"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, TeamRole._member_map_.values()))


@JsonMap({"id_": "id"})
class GetCollectionRolesOkResponseTeam(BaseModel):
    """Information about the team role.

    :param role: The role type:<br/>- `VIEWER` — Can view, fork, and export collections.<br/>- `EDITOR` — Can edit collections directly.<br/>, defaults to None
    :type role: TeamRole, optional
    :param id_: The role's ID., defaults to None
    :type id_: float, optional
    """

    def __init__(self, role: TeamRole = None, id_: float = None):
        if role is not None:
            self.role = self._enum_matching(role, TeamRole.list(), "role")
        if id_ is not None:
            self.id_ = id_


class UserRole(Enum):
    """An enumeration representing different categories.

    :cvar VIEWER: "VIEWER"
    :vartype VIEWER: str
    :cvar EDITOR: "EDITOR"
    :vartype EDITOR: str
    """

    VIEWER = "VIEWER"
    EDITOR = "EDITOR"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, UserRole._member_map_.values()))


@JsonMap({"id_": "id"})
class GetCollectionRolesOkResponseUser(BaseModel):
    """Information about the user role.

    :param role: The role type:<br/>- `VIEWER` — Can view, fork, and export collections.<br/>- `EDITOR` — Can edit collections directly.<br/>, defaults to None
    :type role: UserRole, optional
    :param id_: The role's ID., defaults to None
    :type id_: float, optional
    """

    def __init__(self, role: UserRole = None, id_: float = None):
        if role is not None:
            self.role = self._enum_matching(role, UserRole.list(), "role")
        if id_ is not None:
            self.id_ = id_


@JsonMap({})
class GetCollectionRolesOkResponse(BaseModel):
    """Information about the collection's roles.

    :param group: A list of the collection's group roles., defaults to None
    :type group: List[Group], optional
    :param team: A list of the collection's team roles., defaults to None
    :type team: List[GetCollectionRolesOkResponseTeam], optional
    :param user: A list of the collection's user roles., defaults to None
    :type user: List[GetCollectionRolesOkResponseUser], optional
    """

    def __init__(
        self,
        group: List[Group] = None,
        team: List[GetCollectionRolesOkResponseTeam] = None,
        user: List[GetCollectionRolesOkResponseUser] = None,
    ):
        if group is not None:
            self.group = self._define_list(group, Group)
        if team is not None:
            self.team = self._define_list(team, GetCollectionRolesOkResponseTeam)
        if user is not None:
            self.user = self._define_list(user, GetCollectionRolesOkResponseUser)
