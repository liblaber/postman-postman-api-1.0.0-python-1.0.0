# This file was generated by liblab | https://liblab.com/

from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap(
    {
        "id_": "id",
        "created_by": "createdBy",
        "created_at": "createdAt",
        "updated_at": "updatedAt",
    }
)
class CommentResponseData(BaseModel):
    """Information about the comment.

    :param id_: The comment's ID., defaults to None
    :type id_: int, optional
    :param created_by: The user ID of the user who created the comment., defaults to None
    :type created_by: int, optional
    :param created_at: The date and time at which the comment was created., defaults to None
    :type created_at: str, optional
    :param updated_at: The date and time when the comment was last updated., defaults to None
    :type updated_at: str, optional
    :param body: The contents of the comment., defaults to None
    :type body: str, optional
    """

    def __init__(
        self,
        id_: int = None,
        created_by: int = None,
        created_at: str = None,
        updated_at: str = None,
        body: str = None,
    ):
        if id_ is not None:
            self.id_ = id_
        if created_by is not None:
            self.created_by = created_by
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if body is not None:
            self.body = body


@JsonMap({})
class CommentResponse(BaseModel):
    """CommentResponse

    :param data: data, defaults to None
    :type data: List[CommentResponseData], optional
    """

    def __init__(self, data: List[CommentResponseData] = None):
        if data is not None:
            self.data = self._define_list(data, CommentResponseData)
