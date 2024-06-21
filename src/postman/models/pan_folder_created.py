from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap(
    {
        "id_": "id",
        "parent_folder_id": "parentFolderId",
        "updated_at": "updatedAt",
        "updated_by": "updatedBy",
        "created_by": "createdBy",
        "created_at": "createdAt",
        "type_": "type",
    }
)
class PanFolderCreated(BaseModel):
    """Information about the Private API Network folder.

    :param id_: The folder's ID., defaults to None
    :type id_: int, optional
    :param parent_folder_id: The parent folder ID., defaults to None
    :type parent_folder_id: int, optional
    :param updated_at: The date and time at which the folder was updated., defaults to None
    :type updated_at: str, optional
    :param updated_by: The user who updated the folder., defaults to None
    :type updated_by: int, optional
    :param created_by: The user who created the folder., defaults to None
    :type created_by: int, optional
    :param created_at: The date and time at which the element was created., defaults to None
    :type created_at: str, optional
    :param name: The folder's name., defaults to None
    :type name: str, optional
    :param description: The folder's description., defaults to None
    :type description: str, optional
    :param type_: The folder's type. This is always the `folder` value., defaults to None
    :type type_: str, optional
    """

    def __init__(
        self,
        id_: int = None,
        parent_folder_id: int = None,
        updated_at: str = None,
        updated_by: int = None,
        created_by: int = None,
        created_at: str = None,
        name: str = None,
        description: str = None,
        type_: str = None,
    ):
        if id_ is not None:
            self.id_ = id_
        if parent_folder_id is not None:
            self.parent_folder_id = parent_folder_id
        if updated_at is not None:
            self.updated_at = updated_at
        if updated_by is not None:
            self.updated_by = updated_by
        if created_by is not None:
            self.created_by = created_by
        if created_at is not None:
            self.created_at = created_at
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if type_ is not None:
            self.type_ = type_
