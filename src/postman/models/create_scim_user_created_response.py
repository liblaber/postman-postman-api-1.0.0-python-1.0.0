from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"given_name": "givenName", "family_name": "familyName"})
class CreateScimUserCreatedResponseName(BaseModel):
    """CreateScimUserCreatedResponseName

    :param given_name: The user's first name., defaults to None
    :type given_name: str, optional
    :param family_name: The user's last name., defaults to None
    :type family_name: str, optional
    """

    def __init__(self, given_name: str = None, family_name: str = None):
        if given_name is not None:
            self.given_name = given_name
        if family_name is not None:
            self.family_name = family_name


class MetaResourceType(Enum):
    """An enumeration representing different categories.

    :cvar USER: "User"
    :vartype USER: str
    """

    USER = "User"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, MetaResourceType._member_map_.values()))


@JsonMap({"last_modified": "lastModified", "resource_type": "resourceType"})
class CreateScimUserCreatedResponseMeta(BaseModel):
    """The response's non-standard meta information.

    :param created: The date and time at which the user was created., defaults to None
    :type created: str, optional
    :param last_modified: The date and time at which the user was last modified., defaults to None
    :type last_modified: str, optional
    :param resource_type: The SCIM resource type., defaults to None
    :type resource_type: MetaResourceType, optional
    """

    def __init__(
        self,
        created: str = None,
        last_modified: str = None,
        resource_type: MetaResourceType = None,
    ):
        if created is not None:
            self.created = created
        if last_modified is not None:
            self.last_modified = last_modified
        if resource_type is not None:
            self.resource_type = self._enum_matching(
                resource_type, MetaResourceType.list(), "resource_type"
            )


@JsonMap({"id_": "id", "user_name": "userName", "external_id": "externalId"})
class CreateScimUserCreatedResponse(BaseModel):
    """CreateScimUserCreatedResponse

    :param schemas: The [SCIM schema URI](https://www.iana.org/assignments/scim/scim.xhtml)., defaults to None
    :type schemas: List[str], optional
    :param id_: The user's SCIM ID., defaults to None
    :type id_: str, optional
    :param user_name: The user's username., defaults to None
    :type user_name: str, optional
    :param name: name, defaults to None
    :type name: CreateScimUserCreatedResponseName, optional
    :param external_id: The user's external ID., defaults to None
    :type external_id: str, optional
    :param active: If true, the user is active., defaults to None
    :type active: bool, optional
    :param meta: The response's non-standard meta information., defaults to None
    :type meta: CreateScimUserCreatedResponseMeta, optional
    """

    def __init__(
        self,
        schemas: List[str] = None,
        id_: str = None,
        user_name: str = None,
        name: CreateScimUserCreatedResponseName = None,
        external_id: str = None,
        active: bool = None,
        meta: CreateScimUserCreatedResponseMeta = None,
    ):
        if schemas is not None:
            self.schemas = schemas
        if id_ is not None:
            self.id_ = id_
        if user_name is not None:
            self.user_name = user_name
        if name is not None:
            self.name = self._define_object(name, CreateScimUserCreatedResponseName)
        if external_id is not None:
            self.external_id = external_id
        if active is not None:
            self.active = active
        if meta is not None:
            self.meta = self._define_object(meta, CreateScimUserCreatedResponseMeta)
