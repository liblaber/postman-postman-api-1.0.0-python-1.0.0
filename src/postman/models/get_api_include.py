from enum import Enum


class GetApiInclude(Enum):
    """An enumeration representing different categories.

    :cvar COLLECTIONS: "collections"
    :vartype COLLECTIONS: str
    :cvar VERSIONS: "versions"
    :vartype VERSIONS: str
    :cvar SCHEMAS: "schemas"
    :vartype SCHEMAS: str
    :cvar GITINFO: "gitInfo"
    :vartype GITINFO: str
    """

    COLLECTIONS = "collections"
    VERSIONS = "versions"
    SCHEMAS = "schemas"
    GITINFO = "gitInfo"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, GetApiInclude._member_map_.values()))
