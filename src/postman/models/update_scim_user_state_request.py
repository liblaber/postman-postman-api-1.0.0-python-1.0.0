from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


class OperationsOp2(Enum):
    """An enumeration representing different categories.

    :cvar REPLACE: "replace"
    :vartype REPLACE: str
    """

    REPLACE = "replace"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, OperationsOp2._member_map_.values()))


@JsonMap({})
class OperationsValue2(BaseModel):
    """The performed operation's value.

    :param active: Sets the user's `active` state:<br/>- `true` — Activates the user. This lets them authenticate in to your Postman team.<br/>- `false` — Removes the user from your Postman team and deactivates the account. This blocks the user from authenticating in to Postman.<br/>, defaults to None
    :type active: bool, optional
    """

    def __init__(self, active: bool = None):
        if active is not None:
            self.active = active


@JsonMap({})
class UpdateScimUserStateRequestOperations(BaseModel):
    """UpdateScimUserStateRequestOperations

    :param op: The operation to perform., defaults to None
    :type op: OperationsOp2, optional
    :param value: The performed operation's value., defaults to None
    :type value: OperationsValue2, optional
    """

    def __init__(self, op: OperationsOp2 = None, value: OperationsValue2 = None):
        if op is not None:
            self.op = self._enum_matching(op, OperationsOp2.list(), "op")
        if value is not None:
            self.value = self._define_object(value, OperationsValue2)


@JsonMap({"operations": "Operations"})
class UpdateScimUserStateRequest(BaseModel):
    """UpdateScimUserStateRequest

    :param schemas: The [SCIM schema URI](https://www.iana.org/assignments/scim/scim.xhtml)., defaults to None
    :type schemas: List[str], optional
    :param operations: Information about the user update operation., defaults to None
    :type operations: List[UpdateScimUserStateRequestOperations], optional
    """

    def __init__(
        self,
        schemas: List[str] = None,
        operations: List[UpdateScimUserStateRequestOperations] = None,
    ):
        if schemas is not None:
            self.schemas = schemas
        if operations is not None:
            self.operations = self._define_list(
                operations, UpdateScimUserStateRequestOperations
            )
