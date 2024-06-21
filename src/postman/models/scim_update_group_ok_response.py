from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"resource_type": "resourceType", "last_modified": "lastModified"})
class ScimUpdateGroupOkResponseMeta(BaseModel):
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
class ScimUpdateGroupOkResponse(BaseModel):
    """ScimUpdateGroupOkResponse

    :param schemas: The [SCIM schema URI](https://www.iana.org/assignments/scim/scim.xhtml)., defaults to None
    :type schemas: List[str], optional
    :param id_: The group's ID., defaults to None
    :type id_: str, optional
    :param display_name: The group's name., defaults to None
    :type display_name: str, optional
    :param external_id: The group's external ID., defaults to None
    :type external_id: str, optional
    :param meta: The response's non-standard meta information., defaults to None
    :type meta: ScimUpdateGroupOkResponseMeta, optional
    """

    def __init__(
        self,
        schemas: List[str] = None,
        id_: str = None,
        display_name: str = None,
        external_id: str = None,
        meta: ScimUpdateGroupOkResponseMeta = None,
    ):
        if schemas is not None:
            self.schemas = schemas
        if id_ is not None:
            self.id_ = id_
        if display_name is not None:
            self.display_name = display_name
        if external_id is not None:
            self.external_id = external_id
        if meta is not None:
            self.meta = self._define_object(meta, ScimUpdateGroupOkResponseMeta)
