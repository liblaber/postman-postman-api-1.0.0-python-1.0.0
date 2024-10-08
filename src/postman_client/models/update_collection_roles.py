# This file was generated by liblab | https://liblab.com/

from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


class RolesOp(Enum):
    """An enumeration representing different categories.

    :cvar UPDATE: "update"
    :vartype UPDATE: str
    """

    UPDATE = "update"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, RolesOp._member_map_.values()))


class RolesPath1(Enum):
    """An enumeration representing different categories.

    :cvar _USER: "/user"
    :vartype _USER: str
    :cvar _GROUP: "/group"
    :vartype _GROUP: str
    :cvar _TEAM: "/team"
    :vartype _TEAM: str
    """

    _USER = "/user"
    _GROUP = "/group"
    _TEAM = "/team"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, RolesPath1._member_map_.values()))


class ValueRole1(Enum):
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
        return list(map(lambda x: x.value, ValueRole1._member_map_.values()))


@JsonMap({"id_": "id"})
class RolesValue1(BaseModel):
    """Information about the updated role.

    :param id_: The user, group, or team's ID.
    :type id_: float
    :param role: The role type: - `VIEWER` — Can view, fork, and export collections. - `EDITOR` — Can edit collections directly.
    :type role: ValueRole1
    """

    def __init__(self, id_: float, role: ValueRole1):
        """Information about the updated role.

        :param id_: The user, group, or team's ID.
        :type id_: float
        :param role: The role type: - `VIEWER` — Can view, fork, and export collections. - `EDITOR` — Can edit collections directly.
        :type role: ValueRole1
        """
        self.id_ = id_
        self.role = self._enum_matching(role, ValueRole1.list(), "role")


@JsonMap({})
class UpdateCollectionRolesRoles(BaseModel):
    """UpdateCollectionRolesRoles

    :param op: The operation to perform on the path.
    :type op: RolesOp
    :param path: The resource to perform the action on.
    :type path: RolesPath1
    :param value: value
    :type value: List[RolesValue1]
    """

    def __init__(self, op: RolesOp, path: RolesPath1, value: List[RolesValue1]):
        """UpdateCollectionRolesRoles

        :param op: The operation to perform on the path.
        :type op: RolesOp
        :param path: The resource to perform the action on.
        :type path: RolesPath1
        :param value: value
        :type value: List[RolesValue1]
        """
        self.op = self._enum_matching(op, RolesOp.list(), "op")
        self.path = self._enum_matching(path, RolesPath1.list(), "path")
        self.value = self._define_list(value, RolesValue1)


@JsonMap({})
class UpdateCollectionRoles(BaseModel):
    """UpdateCollectionRoles

    :param roles: roles
    :type roles: List[UpdateCollectionRolesRoles]
    """

    def __init__(self, roles: List[UpdateCollectionRolesRoles]):
        """UpdateCollectionRoles

        :param roles: roles
        :type roles: List[UpdateCollectionRolesRoles]
        """
        self.roles = self._define_list(roles, UpdateCollectionRolesRoles)
