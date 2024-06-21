from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


class OperationsOp1(Enum):
    """An enumeration representing different categories.

    :cvar REPLACE: "replace"
    :vartype REPLACE: str
    :cvar REMOVE: "remove"
    :vartype REMOVE: str
    :cvar ADD: "add"
    :vartype ADD: str
    """

    REPLACE = "replace"
    REMOVE = "remove"
    ADD = "add"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, OperationsOp1._member_map_.values()))


@JsonMap({"id_": "id", "display_name": "displayName"})
class OperationsValue1(BaseModel):
    """The performed operation's value.

    :param id_: The group's ID., defaults to None
    :type id_: str, optional
    :param display_name: The group's name., defaults to None
    :type display_name: str, optional
    """

    def __init__(self, id_: str = None, display_name: str = None):
        if id_ is not None:
            self.id_ = id_
        if display_name is not None:
            self.display_name = display_name


@JsonMap({})
class ScimUpdateGroupRequestOperations(BaseModel):
    """ScimUpdateGroupRequestOperations

    :param op: The operation to perform., defaults to None
    :type op: OperationsOp1, optional
    :param path: The operation's path. Include this value when you update a group's members., defaults to None
    :type path: str, optional
    :param value: The performed operation's value., defaults to None
    :type value: OperationsValue1, optional
    """

    def __init__(
        self, op: OperationsOp1 = None, path: str = None, value: OperationsValue1 = None
    ):
        if op is not None:
            self.op = self._enum_matching(op, OperationsOp1.list(), "op")
        if path is not None:
            self.path = path
        if value is not None:
            self.value = self._define_object(value, OperationsValue1)


@JsonMap({"operations": "Operations"})
class ScimUpdateGroupRequest(BaseModel):
    """ScimUpdateGroupRequest

    :param schemas: The [SCIM schema URI](https://www.iana.org/assignments/scim/scim.xhtml)., defaults to None
    :type schemas: List[str], optional
    :param operations: Information about the group update operation., defaults to None
    :type operations: List[ScimUpdateGroupRequestOperations], optional
    """

    def __init__(
        self,
        schemas: List[str] = None,
        operations: List[ScimUpdateGroupRequestOperations] = None,
    ):
        if schemas is not None:
            self.schemas = schemas
        if operations is not None:
            self.operations = self._define_list(
                operations, ScimUpdateGroupRequestOperations
            )
