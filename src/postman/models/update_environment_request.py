from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


class ValuesType3(Enum):
    """An enumeration representing different categories.

    :cvar SECRET: "secret"
    :vartype SECRET: str
    :cvar DEFAULT: "default"
    :vartype DEFAULT: str
    :cvar ANY: "any"
    :vartype ANY: str
    """

    SECRET = "secret"
    DEFAULT = "default"
    ANY = "any"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, ValuesType3._member_map_.values()))


@JsonMap({"type_": "type"})
class EnvironmentValues3(BaseModel):
    """EnvironmentValues3

    :param enabled: If true, the variable is enabled., defaults to None
    :type enabled: bool, optional
    :param key: The variable's name., defaults to None
    :type key: str, optional
    :param value: The variable's value., defaults to None
    :type value: str, optional
    :param type_: The variable type., defaults to None
    :type type_: ValuesType3, optional
    """

    def __init__(
        self,
        enabled: bool = None,
        key: str = None,
        value: str = None,
        type_: ValuesType3 = None,
    ):
        if enabled is not None:
            self.enabled = enabled
        if key is not None:
            self.key = key
        if value is not None:
            self.value = value
        if type_ is not None:
            self.type_ = self._enum_matching(type_, ValuesType3.list(), "type_")


@JsonMap({})
class UpdateEnvironmentRequestEnvironment(BaseModel):
    """UpdateEnvironmentRequestEnvironment

    :param name: The environment's name., defaults to None
    :type name: str, optional
    :param values: Information about the environment's variables., defaults to None
    :type values: List[EnvironmentValues3], optional
    """

    def __init__(self, name: str = None, values: List[EnvironmentValues3] = None):
        if name is not None:
            self.name = name
        if values is not None:
            self.values = self._define_list(values, EnvironmentValues3)


@JsonMap({})
class UpdateEnvironmentRequest(BaseModel):
    """UpdateEnvironmentRequest

    :param environment: environment, defaults to None
    :type environment: UpdateEnvironmentRequestEnvironment, optional
    """

    def __init__(self, environment: UpdateEnvironmentRequestEnvironment = None):
        if environment is not None:
            self.environment = self._define_object(
                environment, UpdateEnvironmentRequestEnvironment
            )
