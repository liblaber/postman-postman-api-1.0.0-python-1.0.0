from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap(
    {
        "id_": "id",
        "created_at": "createdAt",
        "created_by": "createdBy",
        "updated_at": "updatedAt",
        "updated_by": "updatedBy",
    }
)
class CreateApiOkResponse(BaseModel):
    """The API's base data schema.

    :param id_: The API's ID., defaults to None
    :type id_: str, optional
    :param name: The API's name., defaults to None
    :type name: str, optional
    :param summary: The API's short summary., defaults to None
    :type summary: str, optional
    :param created_at: The date and time at which the API was created., defaults to None
    :type created_at: str, optional
    :param created_by: The Postman ID of the user that created the API., defaults to None
    :type created_by: int, optional
    :param updated_at: The date and time at which the API was updated., defaults to None
    :type updated_at: str, optional
    :param updated_by: The Postman ID of the user that updated the API., defaults to None
    :type updated_by: int, optional
    :param description: The API's description., defaults to None
    :type description: str, optional
    """

    def __init__(
        self,
        id_: str = None,
        name: str = None,
        summary: str = None,
        created_at: str = None,
        created_by: int = None,
        updated_at: str = None,
        updated_by: int = None,
        description: str = None,
    ):
        if id_ is not None:
            self.id_ = id_
        if name is not None:
            self.name = name
        if summary is not None:
            self.summary = summary
        if created_at is not None:
            self.created_at = created_at
        if created_by is not None:
            self.created_by = created_by
        if updated_at is not None:
            self.updated_at = updated_at
        if updated_by is not None:
            self.updated_by = updated_by
        if description is not None:
            self.description = description
