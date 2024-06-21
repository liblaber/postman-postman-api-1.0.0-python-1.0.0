from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"next_cursor": "nextCursor"})
class GetApiSchemaFilesOkResponseMeta(BaseModel):
    """The schema's non-standard meta information.

    :param next_cursor: The pointer to the next record in the set of paginated results., defaults to None
    :type next_cursor: str, optional
    """

    def __init__(self, next_cursor: str = None):
        if next_cursor is not None:
            self.next_cursor = next_cursor


@JsonMap(
    {
        "id_": "id",
        "created_at": "createdAt",
        "created_by": "createdBy",
        "updated_at": "updatedAt",
        "updated_by": "updatedBy",
    }
)
class GetApiSchemaFilesOkResponseFiles(BaseModel):
    """Information about the schema file.

    :param id_: The schema file's ID., defaults to None
    :type id_: str, optional
    :param name: The schema file's name., defaults to None
    :type name: str, optional
    :param path: The file system path to the schema file., defaults to None
    :type path: str, optional
    :param created_at: The date and time at which the file was created., defaults to None
    :type created_at: str, optional
    :param created_by: The user Id of the user that created the file., defaults to None
    :type created_by: int, optional
    :param updated_at: The date and time at which the file was last updated., defaults to None
    :type updated_at: str, optional
    :param updated_by: The user ID of the user that last updated the file., defaults to None
    :type updated_by: int, optional
    """

    def __init__(
        self,
        id_: str = None,
        name: str = None,
        path: str = None,
        created_at: str = None,
        created_by: int = None,
        updated_at: str = None,
        updated_by: int = None,
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


@JsonMap({})
class GetApiSchemaFilesOkResponse(BaseModel):
    """Information about the schema files and its meta information.

    :param meta: The schema's non-standard meta information., defaults to None
    :type meta: GetApiSchemaFilesOkResponseMeta, optional
    :param files: The schema's files., defaults to None
    :type files: List[GetApiSchemaFilesOkResponseFiles], optional
    """

    def __init__(
        self,
        meta: GetApiSchemaFilesOkResponseMeta = None,
        files: List[GetApiSchemaFilesOkResponseFiles] = None,
    ):
        if meta is not None:
            self.meta = self._define_object(meta, GetApiSchemaFilesOkResponseMeta)
        if files is not None:
            self.files = self._define_list(files, GetApiSchemaFilesOkResponseFiles)
