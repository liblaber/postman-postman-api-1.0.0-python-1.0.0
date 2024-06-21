from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


class RolesPath2(Enum):
    """An enumeration representing different categories.

    :cvar _USER: "/user"
    :vartype _USER: str
    :cvar _USERGROUP: "/usergroup"
    :vartype _USERGROUP: str
    """

    _USER = "/user"
    _USERGROUP = "/usergroup"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, RolesPath2._member_map_.values()))


class ValueRole2(Enum):
    """An enumeration representing different categories.

    :cvar _1: 1
    :vartype _1: str
    :cvar _2: 2
    :vartype _2: str
    :cvar _3: 3
    :vartype _3: str
    """

    _1 = 1
    _2 = 2
    _3 = 3

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, ValueRole2._member_map_.values()))


@JsonMap({"id_": "id"})
class RolesValue2(BaseModel):
    """Information about the updated user or user group role.

    :param id_: The user or user group ID.
    :type id_: str
    :param role: The workspace role's ID:<br/>- `1` — Viewer. Can view, fork, and export workspace resources.<br/>- `2` — Editor. Can create and edit workspace resources.<br/>- `3` — Admin. Can manage workspace details and members.<br/>
    :type role: ValueRole2
    """

    def __init__(self, id_: str, role: ValueRole2):
        self.id_ = id_
        self.role = self._enum_matching(role, ValueRole2.list(), "role")


@JsonMap({})
class UpdateWorkspaceRolesRequestRoles(BaseModel):
    """UpdateWorkspaceRolesRequestRoles

    :param op: The operation to perform on the path.
    :type op: str
    :param path: The resource to perform the action on.
    :type path: RolesPath2
    :param value: value
    :type value: List[RolesValue2]
    """

    def __init__(self, op: str, path: RolesPath2, value: List[RolesValue2]):
        self.op = op
        self.path = self._enum_matching(path, RolesPath2.list(), "path")
        self.value = self._define_list(value, RolesValue2)


@JsonMap({})
class UpdateWorkspaceRolesRequest(BaseModel):
    """UpdateWorkspaceRolesRequest

    :param roles: roles, defaults to None
    :type roles: List[UpdateWorkspaceRolesRequestRoles], optional
    """

    def __init__(self, roles: List[UpdateWorkspaceRolesRequestRoles] = None):
        if roles is not None:
            self.roles = self._define_list(roles, UpdateWorkspaceRolesRequestRoles)
