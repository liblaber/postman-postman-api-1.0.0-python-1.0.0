# This file was generated by liblab | https://liblab.com/

from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


class ValuesType1(Enum):
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
        return list(map(lambda x: x.value, ValuesType1._member_map_.values()))


@JsonMap({"type_": "type"})
class EnvironmentValues1(BaseModel):
    """EnvironmentValues1

    :param enabled: If true, the variable is enabled., defaults to None
    :type enabled: bool, optional
    :param key: The variable's name., defaults to None
    :type key: str, optional
    :param value: The variable's value., defaults to None
    :type value: str, optional
    :param type_: The variable type., defaults to None
    :type type_: ValuesType1, optional
    """

    def __init__(
        self,
        enabled: bool = None,
        key: str = None,
        value: str = None,
        type_: ValuesType1 = None,
    ):
        """EnvironmentValues1

        :param enabled: If true, the variable is enabled., defaults to None
        :type enabled: bool, optional
        :param key: The variable's name., defaults to None
        :type key: str, optional
        :param value: The variable's value., defaults to None
        :type value: str, optional
        :param type_: The variable type., defaults to None
        :type type_: ValuesType1, optional
        """
        if enabled is not None:
            self.enabled = enabled
        if key is not None:
            self.key = key
        if value is not None:
            self.value = value
        if type_ is not None:
            self.type_ = self._enum_matching(type_, ValuesType1.list(), "type_")


@JsonMap({})
class CreateEnvironmentEnvironment1(BaseModel):
    """CreateEnvironmentEnvironment1

    :param name: The environment's name.
    :type name: str
    :param values: Information about the environment's variables., defaults to None
    :type values: List[EnvironmentValues1], optional
    """

    def __init__(self, name: str, values: List[EnvironmentValues1] = None):
        """CreateEnvironmentEnvironment1

        :param name: The environment's name.
        :type name: str
        :param values: Information about the environment's variables., defaults to None
        :type values: List[EnvironmentValues1], optional
        """
        self.name = name
        if values is not None:
            self.values = self._define_list(values, EnvironmentValues1)


@JsonMap({})
class CreateEnvironmentRequest(BaseModel):
    """CreateEnvironmentRequest

    :param environment: environment, defaults to None
    :type environment: CreateEnvironmentEnvironment1, optional
    """

    def __init__(self, environment: CreateEnvironmentEnvironment1 = None):
        """CreateEnvironmentRequest

        :param environment: environment, defaults to None
        :type environment: CreateEnvironmentEnvironment1, optional
        """
        if environment is not None:
            self.environment = self._define_object(
                environment, CreateEnvironmentEnvironment1
            )
