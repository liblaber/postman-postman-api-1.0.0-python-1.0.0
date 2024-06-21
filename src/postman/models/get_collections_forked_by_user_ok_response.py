from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap(
    {
        "fork_name": "forkName",
        "fork_id": "forkId",
        "source_id": "sourceId",
        "created_at": "createdAt",
    }
)
class GetCollectionsForkedByUserOkResponseData(BaseModel):
    """Information about the forked collection.

    :param fork_name: The forked collection's label., defaults to None
    :type fork_name: str, optional
    :param fork_id: The forked collection's ID., defaults to None
    :type fork_id: str, optional
    :param source_id: The ID of the forked collection's source collection., defaults to None
    :type source_id: str, optional
    :param created_at: The date and time at which the fork was created., defaults to None
    :type created_at: str, optional
    """

    def __init__(
        self,
        fork_name: str = None,
        fork_id: str = None,
        source_id: str = None,
        created_at: str = None,
    ):
        if fork_name is not None:
            self.fork_name = fork_name
        if fork_id is not None:
            self.fork_id = fork_id
        if source_id is not None:
            self.source_id = source_id
        if created_at is not None:
            self.created_at = created_at


@JsonMap({"next_cursor": "nextCursor", "inaccessible_fork": "inaccessibleFork"})
class GetCollectionsForkedByUserOkResponseMeta(BaseModel):
    """The response's meta information for paginated results.

    :param total: The total number of forked collections., defaults to None
    :type total: float, optional
    :param next_cursor: The pagination cursor that points to the next record in the results set., defaults to None
    :type next_cursor: str, optional
    :param inaccessible_fork: The total number of forked collections that the user cannot access., defaults to None
    :type inaccessible_fork: float, optional
    """

    def __init__(
        self,
        total: float = None,
        next_cursor: str = None,
        inaccessible_fork: float = None,
    ):
        if total is not None:
            self.total = total
        if next_cursor is not None:
            self.next_cursor = next_cursor
        if inaccessible_fork is not None:
            self.inaccessible_fork = inaccessible_fork


@JsonMap({})
class GetCollectionsForkedByUserOkResponse(BaseModel):
    """GetCollectionsForkedByUserOkResponse

    :param data: A list of the user's forked collections., defaults to None
    :type data: List[GetCollectionsForkedByUserOkResponseData], optional
    :param meta: The response's meta information for paginated results., defaults to None
    :type meta: GetCollectionsForkedByUserOkResponseMeta, optional
    """

    def __init__(
        self,
        data: List[GetCollectionsForkedByUserOkResponseData] = None,
        meta: GetCollectionsForkedByUserOkResponseMeta = None,
    ):
        if data is not None:
            self.data = self._define_list(
                data, GetCollectionsForkedByUserOkResponseData
            )
        if meta is not None:
            self.meta = self._define_object(
                meta, GetCollectionsForkedByUserOkResponseMeta
            )
