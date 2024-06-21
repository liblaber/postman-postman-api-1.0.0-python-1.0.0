from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class CreateScimGroupCreatedResponseMembers(BaseModel):
    """An object containing the group's assigned SCIM members.

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


@JsonMap({"last_modified": "lastModified", "resource_type": "resourceType"})
class CreateScimGroupCreatedResponseMeta(BaseModel):
    """The response's non-standard meta information.

    :param created: The date and time at which the group was created., defaults to None
    :type created: str, optional
    :param last_modified: The date and time at which the group was last modified., defaults to None
    :type last_modified: str, optional
    :param resource_type: The SCIM resource type., defaults to None
    :type resource_type: str, optional
    """

    def __init__(
        self, created: str = None, last_modified: str = None, resource_type: str = None
    ):
        if created is not None:
            self.created = created
        if last_modified is not None:
            self.last_modified = last_modified
        if resource_type is not None:
            self.resource_type = resource_type


@JsonMap({"id_": "id", "display_name": "displayName", "external_id": "externalId"})
class CreateScimGroupCreatedResponse(BaseModel):
    """CreateScimGroupCreatedResponse

    :param schemas: The [SCIM schema URI](https://www.iana.org/assignments/scim/scim.xhtml)., defaults to None
    :type schemas: List[str], optional
    :param id_: The group's SCIM ID., defaults to None
    :type id_: str, optional
    :param display_name: The group's display name., defaults to None
    :type display_name: str, optional
    :param external_id: The group's external ID., defaults to None
    :type external_id: str, optional
    :param members: members, defaults to None
    :type members: List[CreateScimGroupCreatedResponseMembers], optional
    :param meta: The response's non-standard meta information., defaults to None
    :type meta: CreateScimGroupCreatedResponseMeta, optional
    """

    def __init__(
        self,
        schemas: List[str] = None,
        id_: str = None,
        display_name: str = None,
        external_id: str = None,
        members: List[CreateScimGroupCreatedResponseMembers] = None,
        meta: CreateScimGroupCreatedResponseMeta = None,
    ):
        if schemas is not None:
            self.schemas = schemas
        if id_ is not None:
            self.id_ = id_
        if display_name is not None:
            self.display_name = display_name
        if external_id is not None:
            self.external_id = external_id
        if members is not None:
            self.members = self._define_list(
                members, CreateScimGroupCreatedResponseMembers
            )
        if meta is not None:
            self.meta = self._define_object(meta, CreateScimGroupCreatedResponseMeta)
