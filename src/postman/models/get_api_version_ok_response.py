from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id", "type_": "type"})
class VersionSchemas(BaseModel):
    """VersionSchemas

    :param id_: The schema's ID., defaults to None
    :type id_: str, optional
    :param type_: The schema type., defaults to None
    :type type_: str, optional
    """

    def __init__(self, id_: str = None, type_: str = None):
        if id_ is not None:
            self.id_ = id_
        if type_ is not None:
            self.type_ = type_


@JsonMap({"id_": "id", "type_": "type"})
class VersionCollections(BaseModel):
    """VersionCollections

    :param id_: The collection's ID., defaults to None
    :type id_: str, optional
    :param type_: The collection's name., defaults to None
    :type type_: str, optional
    """

    def __init__(self, id_: str = None, type_: str = None):
        if id_ is not None:
            self.id_ = id_
        if type_ is not None:
            self.type_ = type_


@JsonMap(
    {
        "id_": "id",
        "created_at": "createdAt",
        "updated_at": "updatedAt",
        "release_notes": "releaseNotes",
    }
)
class Version(BaseModel):
    """Information about the API version.

    :param id_: The version's ID., defaults to None
    :type id_: str, optional
    :param name: The version's name., defaults to None
    :type name: str, optional
    :param created_at: The date and time at which the version was created., defaults to None
    :type created_at: str, optional
    :param updated_at: The date and time at which the version was last updated., defaults to None
    :type updated_at: str, optional
    :param release_notes: The version's release notes., defaults to None
    :type release_notes: str, optional
    :param schemas: schemas, defaults to None
    :type schemas: List[VersionSchemas], optional
    :param collections: collections, defaults to None
    :type collections: List[VersionCollections], optional
    """

    def __init__(
        self,
        id_: str = None,
        name: str = None,
        created_at: str = None,
        updated_at: str = None,
        release_notes: str = None,
        schemas: List[VersionSchemas] = None,
        collections: List[VersionCollections] = None,
    ):
        if id_ is not None:
            self.id_ = id_
        if name is not None:
            self.name = name
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if release_notes is not None:
            self.release_notes = release_notes
        if schemas is not None:
            self.schemas = self._define_list(schemas, VersionSchemas)
        if collections is not None:
            self.collections = self._define_list(collections, VersionCollections)


@JsonMap({})
class GetApiVersionOkResponse(BaseModel):
    """GetApiVersionOkResponse

    :param version: Information about the API version., defaults to None
    :type version: Version, optional
    """

    def __init__(self, version: Version = None):
        if version is not None:
            self.version = self._define_object(version, Version)
