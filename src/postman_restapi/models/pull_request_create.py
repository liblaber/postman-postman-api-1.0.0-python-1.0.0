# This file was generated by liblab | https://liblab.com/

from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"destination_id": "destinationId"})
class PullRequestCreate(BaseModel):
    """Information about the pull request.

    :param title: The title of the pull request.
    :type title: str
    :param description: The pull request's description.
    :type description: str
    :param reviewers: A list of reviewers to assign to the pull request.
    :type reviewers: List[str]
    :param destination_id: The collection ID to merge the pull request into.
    :type destination_id: str
    """

    def __init__(
        self, title: str, description: str, reviewers: List[str], destination_id: str
    ):
        self.title = title
        self.description = description
        self.reviewers = reviewers
        self.destination_id = destination_id
