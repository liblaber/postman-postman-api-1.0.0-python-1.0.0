from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


class ValuesType2(Enum):
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
        return list(map(lambda x: x.value, ValuesType2._member_map_.values()))


@JsonMap({"type_": "type"})
class EnvironmentValues2(BaseModel):
    """EnvironmentValues2

    :param enabled: If true, the variable is enabled., defaults to None
    :type enabled: bool, optional
    :param key: The variable's name., defaults to None
    :type key: str, optional
    :param value: The variable's value., defaults to None
    :type value: str, optional
    :param type_: The variable type., defaults to None
    :type type_: ValuesType2, optional
    """

    def __init__(
        self,
        enabled: bool = None,
        key: str = None,
        value: str = None,
        type_: ValuesType2 = None,
    ):
        if enabled is not None:
            self.enabled = enabled
        if key is not None:
            self.key = key
        if value is not None:
            self.value = value
        if type_ is not None:
            self.type_ = self._enum_matching(type_, ValuesType2.list(), "type_")


@JsonMap(
    {
        "id_": "id",
        "created_at": "createdAt",
        "updated_at": "updatedAt",
        "is_public": "isPublic",
    }
)
class GetEnvironmentOkResponseEnvironment(BaseModel):
    """GetEnvironmentOkResponseEnvironment

    :param id_: The environment's ID., defaults to None
    :type id_: str, optional
    :param name: The environment's name., defaults to None
    :type name: str, optional
    :param owner: The ID of environment's owner., defaults to None
    :type owner: str, optional
    :param created_at: The date and time at which the environment was created., defaults to None
    :type created_at: str, optional
    :param updated_at: The date and time at which the environment was last updated., defaults to None
    :type updated_at: str, optional
    :param values: Information about the environment's variables., defaults to None
    :type values: List[EnvironmentValues2], optional
    :param is_public: If true, the environment is public and visible to all users., defaults to None
    :type is_public: bool, optional
    """

    def __init__(
        self,
        id_: str = None,
        name: str = None,
        owner: str = None,
        created_at: str = None,
        updated_at: str = None,
        values: List[EnvironmentValues2] = None,
        is_public: bool = None,
    ):
        if id_ is not None:
            self.id_ = id_
        if name is not None:
            self.name = name
        if owner is not None:
            self.owner = owner
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if values is not None:
            self.values = self._define_list(values, EnvironmentValues2)
        if is_public is not None:
            self.is_public = is_public


@JsonMap({})
class GetEnvironmentOkResponse(BaseModel):
    """GetEnvironmentOkResponse

    :param environment: environment, defaults to None
    :type environment: GetEnvironmentOkResponseEnvironment, optional
    """

    def __init__(self, environment: GetEnvironmentOkResponseEnvironment = None):
        if environment is not None:
            self.environment = self._define_object(
                environment, GetEnvironmentOkResponseEnvironment
            )
