from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


class DataType(Enum):
    """An enumeration representing different categories.

    :cvar DEFAULT: "DEFAULT"
    :vartype DEFAULT: str
    :cvar TEAM_REGEX: "TEAM_REGEX"
    :vartype TEAM_REGEX: str
    """

    DEFAULT = "DEFAULT"
    TEAM_REGEX = "TEAM_REGEX"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, DataType._member_map_.values()))


@JsonMap({"id_": "id", "type_": "type"})
class GetSecretTypesOkResponseData(BaseModel):
    """Information about the secret type.

    :param name: The name of the secret type., defaults to None
    :type name: str, optional
    :param id_: The ID of the secret type., defaults to None
    :type id_: str, optional
    :param type_: The origin of the secret type:<br/>- `DEFAULT` — Supported by default in Postman.<br/>- `TEAM_REGEX` — A custom regex added by an Admin or Super Admin user in the **Configure Alerts** section of the [**Team Settings**](https://learning.postman.com/docs/administration/team-settings/) interface.<br/>, defaults to None
    :type type_: DataType, optional
    """

    def __init__(self, name: str = None, id_: str = None, type_: DataType = None):
        if name is not None:
            self.name = name
        if id_ is not None:
            self.id_ = id_
        if type_ is not None:
            self.type_ = self._enum_matching(type_, DataType.list(), "type_")


@JsonMap({})
class GetSecretTypesOkResponseMeta(BaseModel):
    """GetSecretTypesOkResponseMeta

    :param total: The total number of supported secrets., defaults to None
    :type total: int, optional
    """

    def __init__(self, total: int = None):
        if total is not None:
            self.total = total


@JsonMap({})
class GetSecretTypesOkResponse(BaseModel):
    """GetSecretTypesOkResponse

    :param data: data, defaults to None
    :type data: List[GetSecretTypesOkResponseData], optional
    :param meta: meta, defaults to None
    :type meta: GetSecretTypesOkResponseMeta, optional
    """

    def __init__(
        self,
        data: List[GetSecretTypesOkResponseData] = None,
        meta: GetSecretTypesOkResponseMeta = None,
    ):
        if data is not None:
            self.data = self._define_list(data, GetSecretTypesOkResponseData)
        if meta is not None:
            self.meta = self._define_object(meta, GetSecretTypesOkResponseMeta)
