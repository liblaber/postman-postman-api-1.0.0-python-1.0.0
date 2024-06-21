from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"next_cursor": "nextCursor"})
class GetApiVersionsOkResponseMeta(BaseModel):
    """The response's meta information for paginated results.

    :param limit: The maximum number of records in the paginated response., defaults to None
    :type limit: int, optional
    :param total: The number of records that match the defined criteria., defaults to None
    :type total: int, optional
    :param next_cursor: The pagination cursor that points to the next record in the results set., defaults to None
    :type next_cursor: str, optional
    """

    def __init__(self, limit: int = None, total: int = None, next_cursor: str = None):
        if limit is not None:
            self.limit = limit
        if total is not None:
            self.total = total
        if next_cursor is not None:
            self.next_cursor = next_cursor


@JsonMap(
    {
        "id_": "id",
        "created_at": "createdAt",
        "updated_at": "updatedAt",
        "release_notes": "releaseNotes",
    }
)
class GetApiVersionsOkResponseVersions(BaseModel):
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
    """

    def __init__(
        self,
        id_: str = None,
        name: str = None,
        created_at: str = None,
        updated_at: str = None,
        release_notes: str = None,
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


@JsonMap({})
class GetApiVersionsOkResponse(BaseModel):
    """Information about the API's versions.

    :param meta: The response's meta information for paginated results., defaults to None
    :type meta: GetApiVersionsOkResponseMeta, optional
    :param versions: versions, defaults to None
    :type versions: List[GetApiVersionsOkResponseVersions], optional
    """

    def __init__(
        self,
        meta: GetApiVersionsOkResponseMeta = None,
        versions: List[GetApiVersionsOkResponseVersions] = None,
    ):
        if meta is not None:
            self.meta = self._define_object(meta, GetApiVersionsOkResponseMeta)
        if versions is not None:
            self.versions = self._define_list(
                versions, GetApiVersionsOkResponseVersions
            )
