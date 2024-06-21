from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap(
    {
        "created_at": "createdAt",
        "created_by": "createdBy",
        "fork_id": "forkId",
        "fork_name": "forkName",
    }
)
class GetCollectionForksOkResponseData(BaseModel):
    """Information about the forked collection.

    :param created_at: The date and time at which the fork was created., defaults to None
    :type created_at: str, optional
    :param created_by: The user who created the collection fork., defaults to None
    :type created_by: str, optional
    :param fork_id: The forked collection's ID., defaults to None
    :type fork_id: str, optional
    :param fork_name: The forked collection's label., defaults to None
    :type fork_name: str, optional
    """

    def __init__(
        self,
        created_at: str = None,
        created_by: str = None,
        fork_id: str = None,
        fork_name: str = None,
    ):
        if created_at is not None:
            self.created_at = created_at
        if created_by is not None:
            self.created_by = created_by
        if fork_id is not None:
            self.fork_id = fork_id
        if fork_name is not None:
            self.fork_name = fork_name


@JsonMap({"next_cursor": "nextCursor"})
class GetCollectionForksOkResponseMeta(BaseModel):
    """The response's meta information for paginated results.

    :param next_cursor: The pagination cursor that points to the next record in the results set., defaults to None
    :type next_cursor: str, optional
    :param total: The total number of forked collections., defaults to None
    :type total: float, optional
    """

    def __init__(self, next_cursor: str = None, total: float = None):
        if next_cursor is not None:
            self.next_cursor = next_cursor
        if total is not None:
            self.total = total


@JsonMap({})
class GetCollectionForksOkResponse(BaseModel):
    """GetCollectionForksOkResponse

    :param data: A list of the collection's forks., defaults to None
    :type data: List[GetCollectionForksOkResponseData], optional
    :param meta: The response's meta information for paginated results., defaults to None
    :type meta: GetCollectionForksOkResponseMeta, optional
    """

    def __init__(
        self,
        data: List[GetCollectionForksOkResponseData] = None,
        meta: GetCollectionForksOkResponseMeta = None,
    ):
        if data is not None:
            self.data = self._define_list(data, GetCollectionForksOkResponseData)
        if meta is not None:
            self.meta = self._define_object(meta, GetCollectionForksOkResponseMeta)
