from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap(
    {
        "created_at": "createdAt",
        "created_by": "createdBy",
        "updated_at": "updatedAt",
        "updated_by": "updatedBy",
        "added_at": "addedAt",
        "added_by": "addedBy",
        "id_": "id",
        "type_": "type",
        "parent_folder_id": "parentFolderId",
    }
)
class Elements(BaseModel):
    """Elements

    :param created_at: The date and time at which the element was created., defaults to None
    :type created_at: str, optional
    :param created_by: The user who created the element., defaults to None
    :type created_by: int, optional
    :param updated_at: The date and time at which the element was last updated., defaults to None
    :type updated_at: str, optional
    :param updated_by: The user who updated the element., defaults to None
    :type updated_by: int, optional
    :param added_at: The date and time at which the element was published to Private API Network. This value is the same as the `updatedAt` value., defaults to None
    :type added_at: str, optional
    :param added_by: The user ID of the user who published the element., defaults to None
    :type added_by: int, optional
    :param description: The element's description., defaults to None
    :type description: str, optional
    :param id_: The element's ID., defaults to None
    :type id_: str, optional
    :param name: The element's name., defaults to None
    :type name: str, optional
    :param summary: The element's summary., defaults to None
    :type summary: str, optional
    :param type_: The element's type., defaults to None
    :type type_: str, optional
    :param parent_folder_id: The element's parent folder ID., defaults to None
    :type parent_folder_id: int, optional
    :param href: The element's HREF., defaults to None
    :type href: str, optional
    """

    def __init__(
        self,
        created_at: str = None,
        created_by: int = None,
        updated_at: str = None,
        updated_by: int = None,
        added_at: str = None,
        added_by: int = None,
        description: str = None,
        id_: str = None,
        name: str = None,
        summary: str = None,
        type_: str = None,
        parent_folder_id: int = None,
        href: str = None,
    ):
        if created_at is not None:
            self.created_at = created_at
        if created_by is not None:
            self.created_by = created_by
        if updated_at is not None:
            self.updated_at = updated_at
        if updated_by is not None:
            self.updated_by = updated_by
        if added_at is not None:
            self.added_at = added_at
        if added_by is not None:
            self.added_by = added_by
        if description is not None:
            self.description = description
        if id_ is not None:
            self.id_ = id_
        if name is not None:
            self.name = name
        if summary is not None:
            self.summary = summary
        if type_ is not None:
            self.type_ = type_
        if parent_folder_id is not None:
            self.parent_folder_id = parent_folder_id
        if href is not None:
            self.href = href


@JsonMap(
    {
        "id_": "id",
        "parent_folder_id": "parentFolderId",
        "updated_at": "updatedAt",
        "updated_by": "updatedBy",
        "created_at": "createdAt",
        "created_by": "createdBy",
        "type_": "type",
    }
)
class Folders(BaseModel):
    """Folders

    :param id_: The folder's ID., defaults to None
    :type id_: int, optional
    :param parent_folder_id: The folder's parent folder ID., defaults to None
    :type parent_folder_id: int, optional
    :param updated_at: The date and time at which the folder was updated., defaults to None
    :type updated_at: str, optional
    :param updated_by: The user ID of the user who updated the folder., defaults to None
    :type updated_by: int, optional
    :param created_at: The date and time at which the folder was created., defaults to None
    :type created_at: str, optional
    :param created_by: The user who created the folder., defaults to None
    :type created_by: int, optional
    :param name: The folder's name., defaults to None
    :type name: str, optional
    :param description: The folder's description., defaults to None
    :type description: str, optional
    :param type_: The element's type. This value is always `folder`., defaults to None
    :type type_: str, optional
    """

    def __init__(
        self,
        id_: int = None,
        parent_folder_id: int = None,
        updated_at: str = None,
        updated_by: int = None,
        created_at: str = None,
        created_by: int = None,
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
        if created_at is not None:
            self.created_at = created_at
        if created_by is not None:
            self.created_by = created_by
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if type_ is not None:
            self.type_ = type_


@JsonMap({"total_count": "totalCount"})
class GetAllElementsAndFoldersOkResponseMeta(BaseModel):
    """The response's non-standard meta information.

    :param limit: The maximum number of elements returned. If the value exceeds the maximum value of `1000`, then the system uses the `1000` value., defaults to None
    :type limit: int, optional
    :param offset: The zero-based offset of the first item returned., defaults to None
    :type offset: int, optional
    :param total_count: The total count of the `elements` and `folders` items., defaults to None
    :type total_count: int, optional
    """

    def __init__(self, limit: int = None, offset: int = None, total_count: int = None):
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if total_count is not None:
            self.total_count = total_count


@JsonMap({})
class GetAllElementsAndFoldersOkResponse(BaseModel):
    """GetAllElementsAndFoldersOkResponse

    :param elements: Information about a Private API Network's folder elements. Elements are APIs, collections, and workspaces., defaults to None
    :type elements: List[Elements], optional
    :param folders: Information about the Private API Network's folders., defaults to None
    :type folders: List[Folders], optional
    :param meta: The response's non-standard meta information., defaults to None
    :type meta: GetAllElementsAndFoldersOkResponseMeta, optional
    """

    def __init__(
        self,
        elements: List[Elements] = None,
        folders: List[Folders] = None,
        meta: GetAllElementsAndFoldersOkResponseMeta = None,
    ):
        if elements is not None:
            self.elements = self._define_list(elements, Elements)
        if folders is not None:
            self.folders = self._define_list(folders, Folders)
        if meta is not None:
            self.meta = self._define_object(
                meta, GetAllElementsAndFoldersOkResponseMeta
            )
