from enum import Enum


class GetEnvironmentForksSort(Enum):
    """An enumeration representing different categories.

    :cvar CREATEDAT: "createdAt"
    :vartype CREATEDAT: str
    """

    CREATEDAT = "createdAt"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, GetEnvironmentForksSort._member_map_.values())
        )
