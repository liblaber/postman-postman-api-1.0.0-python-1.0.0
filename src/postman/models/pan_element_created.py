from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap(
    {
        "added_at": "addedAt",
        "added_by": "addedBy",
        "created_by": "createdBy",
        "created_at": "createdAt",
        "updated_by": "updatedBy",
        "updated_at": "updatedAt",
        "type_": "type",
        "id_": "id",
        "parent_folder_id": "parentFolderId",
    }
)
class PanElementCreated(BaseModel):
    """Information about the Private API Network element.

    :param added_at: The date and time at which the element was added., defaults to None
    :type added_at: str, optional
    :param added_by: The user who added the element., defaults to None
    :type added_by: int, optional
    :param created_by: The user who created the element., defaults to None
    :type created_by: int, optional
    :param created_at: The date and time at which the element was created., defaults to None
    :type created_at: str, optional
    :param updated_by: The user who last updated the element., defaults to None
    :type updated_by: int, optional
    :param updated_at: The date and time at which the element was last updated., defaults to None
    :type updated_at: str, optional
    :param type_: The element's type., defaults to None
    :type type_: str, optional
    :param id_: The element's ID or UID., defaults to None
    :type id_: str, optional
    :param name: The element's name., defaults to None
    :type name: str, optional
    :param summary: The element's summary., defaults to None
    :type summary: str, optional
    :param description: The element's description., defaults to None
    :type description: str, optional
    :param href: The element's Postman URL., defaults to None
    :type href: str, optional
    :param parent_folder_id: The parent folder's ID., defaults to None
    :type parent_folder_id: int, optional
    :param environments: A list of the element's environments., defaults to None
    :type environments: List[str], optional
    """

    def __init__(
        self,
        added_at: str = None,
        added_by: int = None,
        created_by: int = None,
        created_at: str = None,
        updated_by: int = None,
        updated_at: str = None,
        type_: str = None,
        id_: str = None,
        name: str = None,
        summary: str = None,
        description: str = None,
        href: str = None,
        parent_folder_id: int = None,
        environments: List[str] = None,
    ):
        if added_at is not None:
            self.added_at = added_at
        if added_by is not None:
            self.added_by = added_by
        if created_by is not None:
            self.created_by = created_by
        if created_at is not None:
            self.created_at = created_at
        if updated_by is not None:
            self.updated_by = updated_by
        if updated_at is not None:
            self.updated_at = updated_at
        if type_ is not None:
            self.type_ = type_
        if id_ is not None:
            self.id_ = id_
        if name is not None:
            self.name = name
        if summary is not None:
            self.summary = summary
        if description is not None:
            self.description = description
        if href is not None:
            self.href = href
        if parent_folder_id is not None:
            self.parent_folder_id = parent_folder_id
        if environments is not None:
            self.environments = environments
