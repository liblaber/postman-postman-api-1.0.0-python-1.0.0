from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class CreateScimGroupRequestMembers(BaseModel):
    """An object containing the SCIM users to assign to the group.

    :param value: The user's SCIM ID., defaults to None
    :type value: str, optional
    :param display: The user's display name., defaults to None
    :type display: str, optional
    """

    def __init__(self, value: str = None, display: str = None):
        if value is not None:
            self.value = value
        if display is not None:
            self.display = display


@JsonMap({"display_name": "displayName"})
class CreateScimGroupRequest(BaseModel):
    """CreateScimGroupRequest

    :param schemas: The [SCIM schema URI](https://www.iana.org/assignments/scim/scim.xhtml)., defaults to None
    :type schemas: List[str], optional
    :param display_name: The group's display name., defaults to None
    :type display_name: str, optional
    :param members: members, defaults to None
    :type members: List[CreateScimGroupRequestMembers], optional
    """

    def __init__(
        self,
        schemas: List[str] = None,
        display_name: str = None,
        members: List[CreateScimGroupRequestMembers] = None,
    ):
        if schemas is not None:
            self.schemas = schemas
        if display_name is not None:
            self.display_name = display_name
        if members is not None:
            self.members = self._define_list(members, CreateScimGroupRequestMembers)
