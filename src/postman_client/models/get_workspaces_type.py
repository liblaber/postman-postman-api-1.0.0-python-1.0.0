# This file was generated by liblab | https://liblab.com/

from enum import Enum


class GetWorkspacesType(Enum):
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
        return list(map(lambda x: x.value, GetWorkspacesType._member_map_.values()))
