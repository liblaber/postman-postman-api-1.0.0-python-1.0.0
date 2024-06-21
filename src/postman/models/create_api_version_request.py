from typing import Union
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .base import OneOfBaseModel


@JsonMap({"id_": "id"})
class CreateApiVersionRequest1Schemas(BaseModel):
    """Information about the schema.

    :param id_: The schema's ID., defaults to None
    :type id_: str, optional
    """

    def __init__(self, id_: str = None):
        if id_ is not None:
            self.id_ = id_


@JsonMap({"id_": "id"})
class CreateApiVersionRequest1Collections(BaseModel):
    """Information about the collection.

    :param id_: The collection's ID., defaults to None
    :type id_: str, optional
    """

    def __init__(self, id_: str = None):
        if id_ is not None:
            self.id_ = id_


@JsonMap({"release_notes": "releaseNotes"})
class CreateApiVersionRequest1(BaseModel):
    """Information about the API version.

    :param name: The version's name.
    :type name: str
    :param schemas: A list of the version's schemas.
    :type schemas: List[CreateApiVersionRequest1Schemas]
    :param collections: A list of the version's collections.
    :type collections: List[CreateApiVersionRequest1Collections]
    :param release_notes: Information about the API version release. For example, changelog notes., defaults to None
    :type release_notes: str, optional
    """

    def __init__(
        self,
        name: str,
        schemas: List[CreateApiVersionRequest1Schemas],
        collections: List[CreateApiVersionRequest1Collections],
        release_notes: str = None,
    ):
        self.name = name
        self.schemas = self._define_list(schemas, CreateApiVersionRequest1Schemas)
        self.collections = self._define_list(
            collections, CreateApiVersionRequest1Collections
        )
        if release_notes is not None:
            self.release_notes = release_notes


@JsonMap({"file_path": "filePath"})
class CreateApiVersionRequest2Schemas(BaseModel):
    """Information about the schema.

    :param file_path: The path to the schema root file in the Git repository., defaults to None
    :type file_path: str, optional
    """

    def __init__(self, file_path: str = None):
        if file_path is not None:
            self.file_path = file_path


@JsonMap({"file_path": "filePath"})
class CreateApiVersionRequest2Collections(BaseModel):
    """Information about the collection.

    :param file_path: Path to a collection in the Git repository., defaults to None
    :type file_path: str, optional
    """

    def __init__(self, file_path: str = None):
        if file_path is not None:
            self.file_path = file_path


@JsonMap({"release_notes": "releaseNotes"})
class CreateApiVersionRequest2(BaseModel):
    """Information about the API version.

    :param name: The version's name.
    :type name: str
    :param branch: The branch ID.
    :type branch: str
    :param schemas: A list of the version's schemas.
    :type schemas: List[CreateApiVersionRequest2Schemas]
    :param collections: A list of the version's collections.
    :type collections: List[CreateApiVersionRequest2Collections]
    :param release_notes: Information about the API version release. For example, changelog notes., defaults to None
    :type release_notes: str, optional
    """

    def __init__(
        self,
        name: str,
        branch: str,
        schemas: List[CreateApiVersionRequest2Schemas],
        collections: List[CreateApiVersionRequest2Collections],
        release_notes: str = None,
    ):
        self.name = name
        self.branch = branch
        self.schemas = self._define_list(schemas, CreateApiVersionRequest2Schemas)
        self.collections = self._define_list(
            collections, CreateApiVersionRequest2Collections
        )
        if release_notes is not None:
            self.release_notes = release_notes


@JsonMap({"directory_path": "directoryPath"})
class CreateApiVersionRequest3Schemas(BaseModel):
    """Information about the schema.

    :param directory_path: The path to the root directory where schemas are stored in the Git repository., defaults to None
    :type directory_path: str, optional
    """

    def __init__(self, directory_path: str = None):
        if directory_path is not None:
            self.directory_path = directory_path


@JsonMap({"file_path": "filePath"})
class CreateApiVersionRequest3Collections(BaseModel):
    """Information about the collection.

    :param file_path: The path to the collection in the Git repository., defaults to None
    :type file_path: str, optional
    """

    def __init__(self, file_path: str = None):
        if file_path is not None:
            self.file_path = file_path


@JsonMap({"release_notes": "releaseNotes"})
class CreateApiVersionRequest3(BaseModel):
    """Information about the API version.

    :param name: The version's name.
    :type name: str
    :param branch: The branch ID.
    :type branch: str
    :param schemas: A list of the version's schemas.
    :type schemas: List[CreateApiVersionRequest3Schemas]
    :param collections: A list of the version's collections.
    :type collections: List[CreateApiVersionRequest3Collections]
    :param release_notes: Information about the API version release. For example, changelog notes., defaults to None
    :type release_notes: str, optional
    """

    def __init__(
        self,
        name: str,
        branch: str,
        schemas: List[CreateApiVersionRequest3Schemas],
        collections: List[CreateApiVersionRequest3Collections],
        release_notes: str = None,
    ):
        self.name = name
        self.branch = branch
        self.schemas = self._define_list(schemas, CreateApiVersionRequest3Schemas)
        self.collections = self._define_list(
            collections, CreateApiVersionRequest3Collections
        )
        if release_notes is not None:
            self.release_notes = release_notes


class CreateApiVersionRequestGuard(OneOfBaseModel):
    class_list = {
        "CreateApiVersionRequest1": CreateApiVersionRequest1,
        "CreateApiVersionRequest2": CreateApiVersionRequest2,
        "CreateApiVersionRequest3": CreateApiVersionRequest3,
    }


CreateApiVersionRequest = Union[
    CreateApiVersionRequest1, CreateApiVersionRequest2, CreateApiVersionRequest3
]
