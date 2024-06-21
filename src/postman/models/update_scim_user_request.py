from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"given_name": "givenName", "family_name": "familyName"})
class UpdateScimUserRequestName(BaseModel):
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


@JsonMap({})
class UpdateScimUserRequest(BaseModel):
    """UpdateScimUserRequest

    :param schemas: The [SCIM schema URI](https://www.iana.org/assignments/scim/scim.xhtml)., defaults to None
    :type schemas: List[str], optional
    :param name: Information about the user's name., defaults to None
    :type name: UpdateScimUserRequestName, optional
    """

    def __init__(
        self, schemas: List[str] = None, name: UpdateScimUserRequestName = None
    ):
        if schemas is not None:
            self.schemas = schemas
        if name is not None:
            self.name = self._define_object(name, UpdateScimUserRequestName)
