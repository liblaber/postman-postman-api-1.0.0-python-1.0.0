from enum import Enum


class Format(Enum):
    """An enumeration representing different categories.

    :cvar JSON: "json"
    :vartype JSON: str
    :cvar YAML: "yaml"
    :vartype YAML: str
    """

    JSON = "json"
    YAML = "yaml"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Format._member_map_.values()))
