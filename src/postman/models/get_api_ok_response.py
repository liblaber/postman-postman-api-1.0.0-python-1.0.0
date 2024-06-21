from typing import Union
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .base import OneOfBaseModel


@JsonMap(
    {
        "id_": "id",
        "created_at": "createdAt",
        "created_by": "createdBy",
        "updated_at": "updatedAt",
        "updated_by": "updatedBy",
    }
)
class GetApiOkResponse1(BaseModel):
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


@JsonMap({"schema_folder": "schemaFolder", "collection_folder": "collectionFolder"})
class GitInfo(BaseModel):
    """Information about the API's Git repository integration.

    :param domain: The domain at which the Git repository is hosted., defaults to None
    :type domain: str, optional
    :param repository: The repository's name., defaults to None
    :type repository: str, optional
    :param organization: The organization that owns the repository., defaults to None
    :type organization: str, optional
    :param schema_folder: The API definition's repository folder location., defaults to None
    :type schema_folder: str, optional
    :param collection_folder: The API definition's collection repository folder location., defaults to None
    :type collection_folder: str, optional
    """

    def __init__(
        self,
        domain: str = None,
        repository: str = None,
        organization: str = None,
        schema_folder: str = None,
        collection_folder: str = None,
    ):
        if domain is not None:
            self.domain = domain
        if repository is not None:
            self.repository = repository
        if organization is not None:
            self.organization = organization
        if schema_folder is not None:
            self.schema_folder = schema_folder
        if collection_folder is not None:
            self.collection_folder = collection_folder


@JsonMap({"id_": "id"})
class GetApiOkResponse2Schemas(BaseModel):
    """Information about the schema.

    :param id_: The schema's ID., defaults to None
    :type id_: str, optional
    """

    def __init__(self, id_: str = None):
        if id_ is not None:
            self.id_ = id_


@JsonMap({"id_": "id"})
class GetApiOkResponse2Versions(BaseModel):
    """Information about the version.

    :param id_: The version's ID., defaults to None
    :type id_: str, optional
    :param name: The version's name., defaults to None
    :type name: str, optional
    """

    def __init__(self, id_: str = None, name: str = None):
        if id_ is not None:
            self.id_ = id_
        if name is not None:
            self.name = name


@JsonMap({"id_": "id"})
class GetApiOkResponse2Collections(BaseModel):
    """Information about the collection.

    :param id_: The collection's ID., defaults to None
    :type id_: str, optional
    """

    def __init__(self, id_: str = None):
        if id_ is not None:
            self.id_ = id_


@JsonMap(
    {
        "id_": "id",
        "created_at": "createdAt",
        "created_by": "createdBy",
        "updated_at": "updatedAt",
        "updated_by": "updatedBy",
        "git_info": "gitInfo",
    }
)
class GetApiOkResponse2(BaseModel):
    """GetApiOkResponse2

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
    :param git_info: Information about the API's Git repository integration., defaults to None
    :type git_info: GitInfo, optional
    :param schemas: The API's schemas., defaults to None
    :type schemas: List[GetApiOkResponse2Schemas], optional
    :param versions: The API's versions., defaults to None
    :type versions: List[GetApiOkResponse2Versions], optional
    :param collections: The API's collections., defaults to None
    :type collections: List[GetApiOkResponse2Collections], optional
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
        git_info: GitInfo = None,
        schemas: List[GetApiOkResponse2Schemas] = None,
        versions: List[GetApiOkResponse2Versions] = None,
        collections: List[GetApiOkResponse2Collections] = None,
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
        if git_info is not None:
            self.git_info = self._define_object(git_info, GitInfo)
        if schemas is not None:
            self.schemas = self._define_list(schemas, GetApiOkResponse2Schemas)
        if versions is not None:
            self.versions = self._define_list(versions, GetApiOkResponse2Versions)
        if collections is not None:
            self.collections = self._define_list(
                collections, GetApiOkResponse2Collections
            )


class GetApiOkResponseGuard(OneOfBaseModel):
    class_list = {
        "GetApiOkResponse1": GetApiOkResponse1,
        "GetApiOkResponse2": GetApiOkResponse2,
    }


GetApiOkResponse = Union[GetApiOkResponse1, GetApiOkResponse2]
