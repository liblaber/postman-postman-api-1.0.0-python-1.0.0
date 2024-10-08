# This file was generated by liblab | https://liblab.com/

from enum import Enum


class GetAllElementsAndFoldersSort(Enum):
    """An enumeration representing different categories.

    :cvar CREATEDAT: "createdAt"
    :vartype CREATEDAT: str
    :cvar UPDATEDAT: "updatedAt"
    :vartype UPDATEDAT: str
    """

    CREATEDAT = "createdAt"
    UPDATEDAT = "updatedAt"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, GetAllElementsAndFoldersSort._member_map_.values())
        )
