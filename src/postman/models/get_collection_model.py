from enum import Enum


class GetCollectionModel(Enum):
    """An enumeration representing different categories.

    :cvar MINIMAL: "minimal"
    :vartype MINIMAL: str
    """

    MINIMAL = "minimal"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, GetCollectionModel._member_map_.values()))
