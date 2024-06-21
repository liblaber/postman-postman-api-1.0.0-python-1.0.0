from enum import Enum


class GetAllElementsAndFoldersType(Enum):
    """An enumeration representing different categories.

    :cvar API: "api"
    :vartype API: str
    :cvar FOLDER: "folder"
    :vartype FOLDER: str
    :cvar COLLECTION: "collection"
    :vartype COLLECTION: str
    :cvar WORKSPACE: "workspace"
    :vartype WORKSPACE: str
    """

    API = "api"
    FOLDER = "folder"
    COLLECTION = "collection"
    WORKSPACE = "workspace"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, GetAllElementsAndFoldersType._member_map_.values())
        )
