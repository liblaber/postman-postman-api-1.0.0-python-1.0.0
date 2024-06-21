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
class CreateUpdateApiSchemaFileOkResponse(BaseModel):
    """Information about the schema file.

    :param id_: The schema file's ID., defaults to None
    :type id_: str, optional
    :param name: The schema file's name., defaults to None
    :type name: str, optional
    :param path: The file system path to the schema file., defaults to None
    :type path: str, optional
    :param created_at: The date and time at which the file was created., defaults to None
    :type created_at: str, optional
    :param created_by: The user ID of the user that created the file., defaults to None
    :type created_by: str, optional
    :param updated_at: The date and time at which the file was last updated., defaults to None
    :type updated_at: str, optional
    :param updated_by: The user ID of the user that last updated the file., defaults to None
    :type updated_by: str, optional
    """

    def __init__(
        self,
        id_: str = None,
        name: str = None,
        path: str = None,
        created_at: str = None,
        created_by: str = None,
        updated_at: str = None,
        updated_by: str = None,
    ):
        if id_ is not None:
            self.id_ = id_
        if name is not None:
            self.name = name
        if path is not None:
            self.path = path
        if created_at is not None:
            self.created_at = created_at
        if created_by is not None:
            self.created_by = created_by
        if updated_at is not None:
            self.updated_at = updated_at
        if updated_by is not None:
            self.updated_by = updated_by
