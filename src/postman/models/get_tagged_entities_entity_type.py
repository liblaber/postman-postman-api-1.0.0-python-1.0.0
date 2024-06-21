from enum import Enum


class GetTaggedEntitiesEntityType(Enum):
    """An enumeration representing different categories.

    :cvar API: "api"
    :vartype API: str
    :cvar COLLECTION: "collection"
    :vartype COLLECTION: str
    :cvar WORKSPACE: "workspace"
    :vartype WORKSPACE: str
    """

    API = "api"
    COLLECTION = "collection"
    WORKSPACE = "workspace"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, GetTaggedEntitiesEntityType._member_map_.values())
        )
