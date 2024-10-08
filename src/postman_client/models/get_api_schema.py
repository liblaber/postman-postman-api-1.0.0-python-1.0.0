# This file was generated by liblab | https://liblab.com/

from typing import Union
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.one_of_base_model import OneOfBaseModel


@JsonMap(
    {
        "id_": "id",
        "created_at": "createdAt",
        "created_by": "createdBy",
        "updated_at": "updatedAt",
        "updated_by": "updatedBy",
    }
)
class FilesData(BaseModel):
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


@JsonMap({"next_path": "nextPath"})
class FilesMeta(BaseModel):
    """FilesMeta

    :param next_path: The URL path to the next file., defaults to None
    :type next_path: str, optional
    """

    def __init__(self, next_path: str = None):
        """FilesMeta

        :param next_path: The URL path to the next file., defaults to None
        :type next_path: str, optional
        """
        if next_path is not None:
            self.next_path = next_path


@JsonMap({})
class GetApiSchema1Files(BaseModel):
    """Information about the schema's files. The response is paginated and limited to one page.

    :param data: A list of the schema files., defaults to None
    :type data: List[FilesData], optional
    :param meta: meta, defaults to None
    :type meta: FilesMeta, optional
    """

    def __init__(self, data: List[FilesData] = None, meta: FilesMeta = None):
        """Information about the schema's files. The response is paginated and limited to one page.

        :param data: A list of the schema files., defaults to None
        :type data: List[FilesData], optional
        :param meta: meta, defaults to None
        :type meta: FilesMeta, optional
        """
        if data is not None:
            self.data = self._define_list(data, FilesData)
        if meta is not None:
            self.meta = self._define_object(meta, FilesMeta)


@JsonMap(
    {
        "id_": "id",
        "type_": "type",
        "created_at": "createdAt",
        "created_by": "createdBy",
        "updated_at": "updatedAt",
        "updated_by": "updatedBy",
    }
)
class GetApiSchema1(BaseModel):
    """Information about the schema.

    :param id_: The schema's ID., defaults to None
    :type id_: str, optional
    :param type_: The schema's type., defaults to None
    :type type_: str, optional
    :param files: Information about the schema's files. The response is paginated and limited to one page., defaults to None
    :type files: GetApiSchema1Files, optional
    :param created_at: The date and time at which the schema was created., defaults to None
    :type created_at: str, optional
    :param created_by: The user ID of the user that created the schema., defaults to None
    :type created_by: str, optional
    :param updated_at: The date and time at which the schema was last updated., defaults to None
    :type updated_at: str, optional
    :param updated_by: The user ID of the user that last updated the schema., defaults to None
    :type updated_by: str, optional
    """

    def __init__(
        self,
        id_: str = None,
        type_: str = None,
        files: GetApiSchema1Files = None,
        created_at: str = None,
        created_by: str = None,
        updated_at: str = None,
        updated_by: str = None,
    ):
        """Information about the schema.

        :param id_: The schema's ID., defaults to None
        :type id_: str, optional
        :param type_: The schema's type., defaults to None
        :type type_: str, optional
        :param files: Information about the schema's files. The response is paginated and limited to one page., defaults to None
        :type files: GetApiSchema1Files, optional
        :param created_at: The date and time at which the schema was created., defaults to None
        :type created_at: str, optional
        :param created_by: The user ID of the user that created the schema., defaults to None
        :type created_by: str, optional
        :param updated_at: The date and time at which the schema was last updated., defaults to None
        :type updated_at: str, optional
        :param updated_by: The user ID of the user that last updated the schema., defaults to None
        :type updated_by: str, optional
        """
        if id_ is not None:
            self.id_ = id_
        if type_ is not None:
            self.type_ = type_
        if files is not None:
            self.files = self._define_object(files, GetApiSchema1Files)
        if created_at is not None:
            self.created_at = created_at
        if created_by is not None:
            self.created_by = created_by
        if updated_at is not None:
            self.updated_at = updated_at
        if updated_by is not None:
            self.updated_by = updated_by


@JsonMap(
    {
        "id_": "id",
        "type_": "type",
        "created_by": "createdBy",
        "updated_by": "updatedBy",
        "created_at": "createdAt",
        "updated_at": "updatedAt",
    }
)
class GetApiSchema2(BaseModel):
    """Information about the schema.

    :param id_: The schema's ID., defaults to None
    :type id_: str, optional
    :param type_: The schema's type., defaults to None
    :type type_: str, optional
    :param created_by: The user ID of the user that created the schema., defaults to None
    :type created_by: str, optional
    :param updated_by: The user ID of the user that last updated the schema., defaults to None
    :type updated_by: str, optional
    :param created_at: The date and time at which the schema was created., defaults to None
    :type created_at: str, optional
    :param updated_at: The date and time at which the schema was last updated., defaults to None
    :type updated_at: str, optional
    :param content: The schema file, in a bundled format., defaults to None
    :type content: str, optional
    """

    def __init__(
        self,
        id_: str = None,
        type_: str = None,
        created_by: str = None,
        updated_by: str = None,
        created_at: str = None,
        updated_at: str = None,
        content: str = None,
    ):
        """Information about the schema.

        :param id_: The schema's ID., defaults to None
        :type id_: str, optional
        :param type_: The schema's type., defaults to None
        :type type_: str, optional
        :param created_by: The user ID of the user that created the schema., defaults to None
        :type created_by: str, optional
        :param updated_by: The user ID of the user that last updated the schema., defaults to None
        :type updated_by: str, optional
        :param created_at: The date and time at which the schema was created., defaults to None
        :type created_at: str, optional
        :param updated_at: The date and time at which the schema was last updated., defaults to None
        :type updated_at: str, optional
        :param content: The schema file, in a bundled format., defaults to None
        :type content: str, optional
        """
        if id_ is not None:
            self.id_ = id_
        if type_ is not None:
            self.type_ = type_
        if created_by is not None:
            self.created_by = created_by
        if updated_by is not None:
            self.updated_by = updated_by
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if content is not None:
            self.content = content


class GetApiSchemaGuard(OneOfBaseModel):
    class_list = {"GetApiSchema1": GetApiSchema1, "GetApiSchema2": GetApiSchema2}


GetApiSchema = Union[GetApiSchema1, GetApiSchema2]
