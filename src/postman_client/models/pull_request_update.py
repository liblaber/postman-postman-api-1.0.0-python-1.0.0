# This file was generated by liblab | https://liblab.com/

from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class PullRequestUpdate(BaseModel):
    """PullRequestUpdate

    :param title: The pull request's updated title.
    :type title: str
    :param description: The updated pull request description., defaults to None
    :type description: str, optional
    :param reviewers: An updated list of the pull request's assigned reviewers. This replaces all existing users assigned to the pull request with those you pass in the request body.
    :type reviewers: List[str]
    """

    def __init__(self, title: str, reviewers: List[str], description: str = None):
        """PullRequestUpdate

        :param title: The pull request's updated title.
        :type title: str
        :param description: The updated pull request description., defaults to None
        :type description: str, optional
        :param reviewers: An updated list of the pull request's assigned reviewers. This replaces all existing users assigned to the pull request with those you pass in the request body.
        :type reviewers: List[str]
        """
        self.title = title
        if description is not None:
            self.description = description
        self.reviewers = reviewers
