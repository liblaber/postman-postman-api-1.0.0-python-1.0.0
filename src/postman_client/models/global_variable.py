# This file was generated by liblab | https://liblab.com/

from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


class GlobalVariableType(Enum):
    """An enumeration representing different categories.

    :cvar DEFAULT: "default"
    :vartype DEFAULT: str
    :cvar SECRET: "secret"
    :vartype SECRET: str
    """

    DEFAULT = "default"
    SECRET = "secret"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, GlobalVariableType._member_map_.values()))


@JsonMap({"type_": "type"})
class GlobalVariable(BaseModel):
    """Information about the global variable.

    :param key: The variable's name., defaults to None
    :type key: str, optional
    :param type_: The [type](https://learning.postman.com/docs/sending-requests/variables/#variable-types) of variable., defaults to None
    :type type_: GlobalVariableType, optional
    :param value: The variable's value., defaults to None
    :type value: str, optional
    :param enabled: If true, the variable is enabled., defaults to None
    :type enabled: bool, optional
    """

    def __init__(
        self,
        key: str = None,
        type_: GlobalVariableType = None,
        value: str = None,
        enabled: bool = None,
    ):
        """Information about the global variable.

        :param key: The variable's name., defaults to None
        :type key: str, optional
        :param type_: The [type](https://learning.postman.com/docs/sending-requests/variables/#variable-types) of variable., defaults to None
        :type type_: GlobalVariableType, optional
        :param value: The variable's value., defaults to None
        :type value: str, optional
        :param enabled: If true, the variable is enabled., defaults to None
        :type enabled: bool, optional
        """
        if key is not None:
            self.key = key
        if type_ is not None:
            self.type_ = self._enum_matching(type_, GlobalVariableType.list(), "type_")
        if value is not None:
            self.value = value
        if enabled is not None:
            self.enabled = enabled
