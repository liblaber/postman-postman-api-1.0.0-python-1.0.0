from enum import Enum


class GetMockCallLogsSort(Enum):
    """An enumeration representing different categories.

    :cvar SERVEDAT: "servedAt"
    :vartype SERVEDAT: str
    """

    SERVEDAT = "servedAt"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, GetMockCallLogsSort._member_map_.values()))
