from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"given_name": "givenName", "family_name": "familyName"})
class ScimUserResourceName(BaseModel):
    """Information about the Postman team member.

    :param given_name: The team member's first name., defaults to None
    :type given_name: str, optional
    :param family_name: The team member's last name., defaults to None
    :type family_name: str, optional
    """

    def __init__(self, given_name: str = None, family_name: str = None):
        if given_name is not None:
            self.given_name = given_name
        if family_name is not None:
            self.family_name = family_name


@JsonMap({"resource_type": "resourceType", "last_modified": "lastModified"})
class ScimUserResourceMeta(BaseModel):
    """The response's non-standard meta information.

    :param resource_type: The resource type., defaults to None
    :type resource_type: str, optional
    :param created: The date and time at which the team member was created., defaults to None
    :type created: str, optional
    :param last_modified: The date and time at which the team member was last modified., defaults to None
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
class ScimUserResource(BaseModel):
    """The SCIM user resource object.

    :param schemas: The [SCIM schema URI](https://www.iana.org/assignments/scim/scim.xhtml)., defaults to None
    :type schemas: List[str], optional
    :param id_: The team member's SCIM ID., defaults to None
    :type id_: str, optional
    :param user_name: The team member's SCIM username., defaults to None
    :type user_name: str, optional
    :param name: Information about the Postman team member., defaults to None
    :type name: ScimUserResourceName, optional
    :param external_id: The team member's external ID., defaults to None
    :type external_id: str, optional
    :param active: If true, the team member is active., defaults to None
    :type active: bool, optional
    :param meta: The response's non-standard meta information., defaults to None
    :type meta: ScimUserResourceMeta, optional
    """

    def __init__(
        self,
        schemas: List[str] = None,
        id_: str = None,
        user_name: str = None,
        name: ScimUserResourceName = None,
        external_id: str = None,
        active: bool = None,
        meta: ScimUserResourceMeta = None,
    ):
        if schemas is not None:
            self.schemas = schemas
        if id_ is not None:
            self.id_ = id_
        if user_name is not None:
            self.user_name = user_name
        if name is not None:
            self.name = self._define_object(name, ScimUserResourceName)
        if external_id is not None:
            self.external_id = external_id
        if active is not None:
            self.active = active
        if meta is not None:
            self.meta = self._define_object(meta, ScimUserResourceMeta)
