from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id", "fork_name": "forkName"})
class Source(BaseModel):
    """Information about the pull request's source (parent) element.

    :param id_: The pull request's source ID., defaults to None
    :type id_: str, optional
    :param name: The source element's name., defaults to None
    :type name: str, optional
    :param fork_name: The name of the fork created from the source element., defaults to None
    :type fork_name: str, optional
    :param exists: If true, whether the element is present and not deleted., defaults to None
    :type exists: bool, optional
    """

    def __init__(
        self,
        id_: str = None,
        name: str = None,
        fork_name: str = None,
        exists: bool = None,
    ):
        if id_ is not None:
            self.id_ = id_
        if name is not None:
            self.name = name
        if fork_name is not None:
            self.fork_name = fork_name
        if exists is not None:
            self.exists = exists


@JsonMap({"id_": "id"})
class Destination(BaseModel):
    """Information about the pull request destination element.

    :param id_: The destination element's ID., defaults to None
    :type id_: str, optional
    :param name: The destination element's name., defaults to None
    :type name: str, optional
    :param exists: If true, whether the element is present and not deleted., defaults to None
    :type exists: bool, optional
    """

    def __init__(self, id_: str = None, name: str = None, exists: bool = None):
        if id_ is not None:
            self.id_ = id_
        if name is not None:
            self.name = name
        if exists is not None:
            self.exists = exists


class MergeStatus(Enum):
    """An enumeration representing different categories.

    :cvar INACTIVE: "inactive"
    :vartype INACTIVE: str
    :cvar INPROGRESS: "inprogress"
    :vartype INPROGRESS: str
    :cvar FAILED: "failed"
    :vartype FAILED: str
    """

    INACTIVE = "inactive"
    INPROGRESS = "inprogress"
    FAILED = "failed"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, MergeStatus._member_map_.values()))


@JsonMap({})
class Merge(BaseModel):
    """Information about the current progress of the pull request's merge.

    :param status: The pull request's current merge status:<br/>- `inactive` — There is no merge in progress.<br/>- `inprogress` — The pull request is currently merging.<br/>- `failed` — The pull request's merge failed.<br/>, defaults to None
    :type status: MergeStatus, optional
    """

    def __init__(self, status: MergeStatus = None):
        if status is not None:
            self.status = self._enum_matching(status, MergeStatus.list(), "status")


@JsonMap({"id_": "id"})
class Reviewers(BaseModel):
    """Reviewers

    :param id_: The reviewer's user ID., defaults to None
    :type id_: str, optional
    :param status: The reviewer's review status response. One of:<br/>- `approved`<br/>- `declined`<br/>, defaults to None
    :type status: str, optional
    """

    def __init__(self, id_: str = None, status: str = None):
        if id_ is not None:
            self.id_ = id_
        if status is not None:
            self.status = status


@JsonMap(
    {
        "created_at": "createdAt",
        "updated_at": "updatedAt",
        "id_": "id",
        "created_by": "createdBy",
        "updated_by": "updatedBy",
        "fortk_type": "fortkType",
    }
)
class PullRequestGet(BaseModel):
    """PullRequestGet

    :param created_at: The date and time at which the pull request was created., defaults to None
    :type created_at: str, optional
    :param updated_at: The date and time at which the pull request was updated., defaults to None
    :type updated_at: str, optional
    :param id_: The pull request's ID., defaults to None
    :type id_: str, optional
    :param title: The pull request's title., defaults to None
    :type title: str, optional
    :param description: The pull request's description., defaults to None
    :type description: str, optional
    :param created_by: The ID of the user who created the pull request., defaults to None
    :type created_by: str, optional
    :param updated_by: The ID of the user who last updated the pull request., defaults to None
    :type updated_by: str, optional
    :param comment: If the pull request is a `decline` status, an optoinal comment about why the pull request was declined., defaults to None
    :type comment: str, optional
    :param fortk_type: The type of element the pull request was forked from., defaults to None
    :type fortk_type: str, optional
    :param source: Information about the pull request's source (parent) element., defaults to None
    :type source: Source, optional
    :param destination: Information about the pull request destination element., defaults to None
    :type destination: Destination, optional
    :param status: The pull request's current review status:<br/>- `open` — The pull request is still open.<br/>- `approved` — The pull request was approved by its reviewers.<br/>- `declined` — The pull request was not approved by its reviewers.<br/>, defaults to None
    :type status: str, optional
    :param merge: Information about the current progress of the pull request's merge., defaults to None
    :type merge: Merge, optional
    :param reviewers: Information about the reviewers assigned to the pull request., defaults to None
    :type reviewers: List[Reviewers], optional
    """

    def __init__(
        self,
        created_at: str = None,
        updated_at: str = None,
        id_: str = None,
        title: str = None,
        description: str = None,
        created_by: str = None,
        updated_by: str = None,
        comment: str = None,
        fortk_type: str = None,
        source: Source = None,
        destination: Destination = None,
        status: str = None,
        merge: Merge = None,
        reviewers: List[Reviewers] = None,
    ):
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if id_ is not None:
            self.id_ = id_
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if created_by is not None:
            self.created_by = created_by
        if updated_by is not None:
            self.updated_by = updated_by
        if comment is not None:
            self.comment = comment
        if fortk_type is not None:
            self.fortk_type = fortk_type
        if source is not None:
            self.source = self._define_object(source, Source)
        if destination is not None:
            self.destination = self._define_object(destination, Destination)
        if status is not None:
            self.status = status
        if merge is not None:
            self.merge = self._define_object(merge, Merge)
        if reviewers is not None:
            self.reviewers = self._define_list(reviewers, Reviewers)
