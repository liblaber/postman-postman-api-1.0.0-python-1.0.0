from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap(
    {
        "fork_id": "forkId",
        "fork_name": "forkName",
        "created_at": "createdAt",
        "created_by": "createdBy",
        "updated_at": "updatedAt",
    }
)
class GetEnvironmentForksOkResponseData(BaseModel):
    """Information about the forked environment.

    :param fork_id: The forked environment's unique ID., defaults to None
    :type fork_id: str, optional
    :param fork_name: The forked environment's label., defaults to None
    :type fork_name: str, optional
    :param created_at: The date and time at which the fork was created., defaults to None
    :type created_at: str, optional
    :param created_by: The user who created the environment fork., defaults to None
    :type created_by: str, optional
    :param updated_at: The date and time at which the fork was last updated., defaults to None
    :type updated_at: str, optional
    """

    def __init__(
        self,
        fork_id: str = None,
        fork_name: str = None,
        created_at: str = None,
        created_by: str = None,
        updated_at: str = None,
    ):
        if fork_id is not None:
            self.fork_id = fork_id
        if fork_name is not None:
            self.fork_name = fork_name
        if created_at is not None:
            self.created_at = created_at
        if created_by is not None:
            self.created_by = created_by
        if updated_at is not None:
            self.updated_at = updated_at


@JsonMap({"next_cursor": "nextCursor"})
class GetEnvironmentForksOkResponseMeta(BaseModel):
    """The response's meta information for paginated results.

    :param total: The total number of forked environments., defaults to None
    :type total: float, optional
    :param next_cursor: The pagination cursor that points to the next record in the results set., defaults to None
    :type next_cursor: str, optional
    """

    def __init__(self, total: float = None, next_cursor: str = None):
        if total is not None:
            self.total = total
        if next_cursor is not None:
            self.next_cursor = next_cursor


@JsonMap({})
class GetEnvironmentForksOkResponse(BaseModel):
    """GetEnvironmentForksOkResponse

    :param data: A list of the environment's forks., defaults to None
    :type data: List[GetEnvironmentForksOkResponseData], optional
    :param meta: The response's meta information for paginated results., defaults to None
    :type meta: GetEnvironmentForksOkResponseMeta, optional
    """

    def __init__(
        self,
        data: List[GetEnvironmentForksOkResponseData] = None,
        meta: GetEnvironmentForksOkResponseMeta = None,
    ):
        if data is not None:
            self.data = self._define_list(data, GetEnvironmentForksOkResponseData)
        if meta is not None:
            self.meta = self._define_object(meta, GetEnvironmentForksOkResponseMeta)
