from typing import List
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
class GetApisOkResponseApis(BaseModel):
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


@JsonMap({"next_cursor": "nextCursor"})
class GetApisOkResponseMeta(BaseModel):
    """The response's meta information for paginated results.

    :param limit: The maximum number of records in the paginated response., defaults to None
    :type limit: float, optional
    :param total: The number of records that match the defined criteria., defaults to None
    :type total: float, optional
    :param next_cursor: The pagination cursor that points to the next record in the results set., defaults to None
    :type next_cursor: str, optional
    """

    def __init__(
        self, limit: float = None, total: float = None, next_cursor: str = None
    ):
        if limit is not None:
            self.limit = limit
        if total is not None:
            self.total = total
        if next_cursor is not None:
            self.next_cursor = next_cursor


@JsonMap({})
class GetApisOkResponse(BaseModel):
    """Information about the API schema.

    :param apis: apis, defaults to None
    :type apis: List[GetApisOkResponseApis], optional
    :param meta: The response's meta information for paginated results., defaults to None
    :type meta: GetApisOkResponseMeta, optional
    """

    def __init__(
        self,
        apis: List[GetApisOkResponseApis] = None,
        meta: GetApisOkResponseMeta = None,
    ):
        if apis is not None:
            self.apis = self._define_list(apis, GetApisOkResponseApis)
        if meta is not None:
            self.meta = self._define_object(meta, GetApisOkResponseMeta)
