from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class GetScimGroupResourceOkResponseMembers(BaseModel):
    """GetScimGroupResourceOkResponseMembers

    :param value: The member's SCIM ID., defaults to None
    :type value: str, optional
    :param display: The member's display name., defaults to None
    :type display: str, optional
    """

    def __init__(self, value: str = None, display: str = None):
        if value is not None:
            self.value = value
        if display is not None:
            self.display = display


@JsonMap({"resource_type": "resourceType", "last_modified": "lastModified"})
class GetScimGroupResourceOkResponseMeta(BaseModel):
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


@JsonMap({"id_": "id", "user_name": "userName", "external_id": "externalId"})
class GetScimGroupResourceOkResponse(BaseModel):
    """GetScimGroupResourceOkResponse

    :param schemas: The [SCIM schema URI](https://www.iana.org/assignments/scim/scim.xhtml)., defaults to None
    :type schemas: List[str], optional
    :param id_: The group's SCIM ID., defaults to None
    :type id_: str, optional
    :param user_name: The group's display name., defaults to None
    :type user_name: str, optional
    :param members: Information about the group's members., defaults to None
    :type members: List[GetScimGroupResourceOkResponseMembers], optional
    :param external_id: The group's external ID., defaults to None
    :type external_id: str, optional
    :param meta: The response's non-standard meta information., defaults to None
    :type meta: GetScimGroupResourceOkResponseMeta, optional
    """

    def __init__(
        self,
        schemas: List[str] = None,
        id_: str = None,
        user_name: str = None,
        members: List[GetScimGroupResourceOkResponseMembers] = None,
        external_id: str = None,
        meta: GetScimGroupResourceOkResponseMeta = None,
    ):
        if schemas is not None:
            self.schemas = schemas
        if id_ is not None:
            self.id_ = id_
        if user_name is not None:
            self.user_name = user_name
        if members is not None:
            self.members = self._define_list(
                members, GetScimGroupResourceOkResponseMembers
            )
        if external_id is not None:
            self.external_id = external_id
        if meta is not None:
            self.meta = self._define_object(meta, GetScimGroupResourceOkResponseMeta)
