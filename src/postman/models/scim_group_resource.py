from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class ScimGroupResourceMembers(BaseModel):
    """Information about the group's members.

    :param value: The resource value., defaults to None
    :type value: str, optional
    :param display: The resource's display name., defaults to None
    :type display: str, optional
    """

    def __init__(self, value: str = None, display: str = None):
        if value is not None:
            self.value = value
        if display is not None:
            self.display = display


@JsonMap({"resource_type": "resourceType", "last_modified": "lastModified"})
class ScimGroupResourceMeta(BaseModel):
    """The response's non-standard meta information.

    :param resource_type: The resource type., defaults to None
    :type resource_type: str, optional
    :param created: The date and time at which the group was created., defaults to None
    :type created: str, optional
    :param last_modified: The date and time at which the group was last modified., defaults to None
    :type last_modified: str, optional
    """

    def __init__(
        self, resource_type: str = None, created: str = None, last_modified: str = None
    ):
        if resource_type is not None:
            self.resource_type = resource_type
        if created is not None:
            self.created = created
        if last_modified is not None:
            self.last_modified = last_modified


@JsonMap({"id_": "id", "display_name": "displayName", "external_id": "externalId"})
class ScimGroupResource(BaseModel):
    """The SCIM group resource object.

    :param schemas: The [SCIM schema URI](https://www.iana.org/assignments/scim/scim.xhtml)., defaults to None
    :type schemas: List[str], optional
    :param id_: The group's SCIM ID., defaults to None
    :type id_: str, optional
    :param display_name: The group's display name., defaults to None
    :type display_name: str, optional
    :param members: A list of the group's members., defaults to None
    :type members: List[ScimGroupResourceMembers], optional
    :param external_id: The group's external ID., defaults to None
    :type external_id: str, optional
    :param meta: The response's non-standard meta information., defaults to None
    :type meta: ScimGroupResourceMeta, optional
    """

    def __init__(
        self,
        schemas: List[str] = None,
        id_: str = None,
        display_name: str = None,
        members: List[ScimGroupResourceMembers] = None,
        external_id: str = None,
        meta: ScimGroupResourceMeta = None,
    ):
        if schemas is not None:
            self.schemas = schemas
        if id_ is not None:
            self.id_ = id_
        if display_name is not None:
            self.display_name = display_name
        if members is not None:
            self.members = self._define_list(members, ScimGroupResourceMembers)
        if external_id is not None:
            self.external_id = external_id
        if meta is not None:
            self.meta = self._define_object(meta, ScimGroupResourceMeta)
