from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"created_at": "createdAt", "from_": "from"})
class CollectionsFork(BaseModel):
    """If the collection is [forked](https://learning.postman.com/docs/collaborating-in-postman/version-control/#forking-postman-entities), the fork's information.

    :param label: The fork's label., defaults to None
    :type label: str, optional
    :param created_at: The fork's creation date and time., defaults to None
    :type created_at: str, optional
    :param from_: The unique ID of the fork's source collection., defaults to None
    :type from_: str, optional
    """

    def __init__(self, label: str = None, created_at: str = None, from_: str = None):
        if label is not None:
            self.label = label
        if created_at is not None:
            self.created_at = created_at
        if from_ is not None:
            self.from_ = from_


@JsonMap(
    {
        "id_": "id",
        "created_at": "createdAt",
        "updated_at": "updatedAt",
        "is_public": "isPublic",
    }
)
class GetCollectionsOkResponseCollections(BaseModel):
    """Information about the collection.

    :param id_: The collection's ID., defaults to None
    :type id_: str, optional
    :param name: The collection's name., defaults to None
    :type name: str, optional
    :param owner: The owner of the collection., defaults to None
    :type owner: str, optional
    :param created_at: The collection's creation date and time., defaults to None
    :type created_at: str, optional
    :param updated_at: The date and time at which the collection was last updated., defaults to None
    :type updated_at: str, optional
    :param uid: The collection's unique ID., defaults to None
    :type uid: str, optional
    :param fork: If the collection is [forked](https://learning.postman.com/docs/collaborating-in-postman/version-control/#forking-postman-entities), the fork's information., defaults to None
    :type fork: CollectionsFork, optional
    :param is_public: If true, the collection is public and visible to all users., defaults to None
    :type is_public: bool, optional
    """

    def __init__(
        self,
        id_: str = None,
        name: str = None,
        owner: str = None,
        created_at: str = None,
        updated_at: str = None,
        uid: str = None,
        fork: CollectionsFork = None,
        is_public: bool = None,
    ):
        if id_ is not None:
            self.id_ = id_
        if name is not None:
            self.name = name
        if owner is not None:
            self.owner = owner
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if uid is not None:
            self.uid = uid
        if fork is not None:
            self.fork = self._define_object(fork, CollectionsFork)
        if is_public is not None:
            self.is_public = is_public


@JsonMap({})
class GetCollectionsOkResponse(BaseModel):
    """GetCollectionsOkResponse

    :param collections: collections, defaults to None
    :type collections: List[GetCollectionsOkResponseCollections], optional
    """

    def __init__(self, collections: List[GetCollectionsOkResponseCollections] = None):
        if collections is not None:
            self.collections = self._define_list(
                collections, GetCollectionsOkResponseCollections
            )
