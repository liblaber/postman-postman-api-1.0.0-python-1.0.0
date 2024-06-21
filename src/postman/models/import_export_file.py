from enum import Enum
from .utils.json_map import JsonMap
from .base import BaseModel


class ImportExportFileType(Enum):
    """An enumeration representing different categories.

    :cvar FILE: "file"
    :vartype FILE: str
    """

    FILE = "file"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, ImportExportFileType._member_map_.values()))


@JsonMap({"type_": "type"})
class ImportExportFile(BaseModel):
    """ImportExportFile

    :param type_: The `file` type value.
    :type type_: ImportExportFileType
    :param input: A file containing a valid user's export .zip file.
    :type input: str
    """

    def __init__(self, type_: ImportExportFileType, input: str):
        self.type_ = self._enum_matching(type_, ImportExportFileType.list(), "type_")
        self.input = input
