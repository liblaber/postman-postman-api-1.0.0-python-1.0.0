<<<<<<< HEAD
=======
# This file was generated by liblab | https://liblab.com/

>>>>>>> 95da91c (initial commit)
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"created_at": "createdAt", "from_": "from"})
class CollectionFork(BaseModel):
    """Information about the collection's fork.

    :param label: The fork's label., defaults to None
    :type label: str, optional
    :param created_at: The fork's creation date and time., defaults to None
    :type created_at: str, optional
    :param from_: The unique ID of fork's source collection., defaults to None
    :type from_: str, optional
    """

    def __init__(self, label: str = None, created_at: str = None, from_: str = None):
        if label is not None:
            self.label = label
        if created_at is not None:
            self.created_at = created_at
        if from_ is not None:
            self.from_ = from_


@JsonMap({"id_": "id"})
class CreateCollectionForkOkResponseCollection(BaseModel):
    """Information about the forked collection.

    :param id_: The forked collection's ID., defaults to None
    :type id_: str, optional
    :param name: The collection's name., defaults to None
    :type name: str, optional
    :param fork: Information about the collection's fork., defaults to None
    :type fork: CollectionFork, optional
    :param uid: The forked collection's unique ID., defaults to None
    :type uid: str, optional
    """

    def __init__(
        self,
        id_: str = None,
        name: str = None,
        fork: CollectionFork = None,
        uid: str = None,
    ):
        if id_ is not None:
            self.id_ = id_
        if name is not None:
            self.name = name
        if fork is not None:
            self.fork = self._define_object(fork, CollectionFork)
        if uid is not None:
            self.uid = uid


@JsonMap({})
class CreateCollectionForkOkResponse(BaseModel):
    """CreateCollectionForkOkResponse

    :param collection: Information about the forked collection., defaults to None
    :type collection: CreateCollectionForkOkResponseCollection, optional
    """

    def __init__(self, collection: CreateCollectionForkOkResponseCollection = None):
        if collection is not None:
            self.collection = self._define_object(
                collection, CreateCollectionForkOkResponseCollection
            )
