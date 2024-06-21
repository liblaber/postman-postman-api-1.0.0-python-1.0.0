from enum import Enum


class Accept(Enum):
    """An enumeration representing different categories.

    :cvar APPLICATION_VND_API_V10_JSON: "application/vnd.api.v10+json"
    :vartype APPLICATION_VND_API_V10_JSON: str
    """

    APPLICATION_VND_API_V10_JSON = "application/vnd.api.v10+json"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Accept._member_map_.values()))
