from enum import Enum


class GetWorkspacesInclude(Enum):
    """An enumeration representing different categories.

    :cvar MOCKS_DEACTIVATED: "mocks:deactivated"
    :vartype MOCKS_DEACTIVATED: str
    """

    MOCKS_DEACTIVATED = "mocks:deactivated"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, GetWorkspacesInclude._member_map_.values()))
