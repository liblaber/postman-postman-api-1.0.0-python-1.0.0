from enum import Enum


class AscDesc(Enum):
    """An enumeration representing different categories.

    :cvar ASC: "asc"
    :vartype ASC: str
    :cvar DESC: "desc"
    :vartype DESC: str
    """

    ASC = "asc"
    DESC = "desc"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, AscDesc._member_map_.values()))
