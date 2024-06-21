from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"given_name": "givenName", "family_name": "familyName"})
class CreateScimUserRequestName(BaseModel):
    """Information about the user's name.

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


@JsonMap({"user_name": "userName", "external_id": "externalId"})
class CreateScimUserRequest(BaseModel):
    """CreateScimUserRequest

    :param schemas: The [SCIM schema URI](https://www.iana.org/assignments/scim/scim.xhtml)., defaults to None
    :type schemas: List[str], optional
    :param user_name: The user's username., defaults to None
    :type user_name: str, optional
    :param active: If true, activates the user. This lets them authenticate in to your Postman team., defaults to None
    :type active: bool, optional
    :param external_id: The user's external ID., defaults to None
    :type external_id: str, optional
    :param groups: A list of groups to assign the user to., defaults to None
    :type groups: List[str], optional
    :param locale: The user's [IETF language tag](https://datatracker.ietf.org/doc/html/rfc5646)., defaults to None
    :type locale: str, optional
    :param name: Information about the user's name., defaults to None
    :type name: CreateScimUserRequestName, optional
    """

    def __init__(
        self,
        schemas: List[str] = None,
        user_name: str = None,
        active: bool = None,
        external_id: str = None,
        groups: List[str] = None,
        locale: str = None,
        name: CreateScimUserRequestName = None,
    ):
        if schemas is not None:
            self.schemas = schemas
        if user_name is not None:
            self.user_name = user_name
        if active is not None:
            self.active = active
        if external_id is not None:
            self.external_id = external_id
        if groups is not None:
            self.groups = groups
        if locale is not None:
            self.locale = locale
        if name is not None:
            self.name = self._define_object(name, CreateScimUserRequestName)
