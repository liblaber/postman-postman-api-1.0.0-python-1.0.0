from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"is_source_ahead": "isSourceAhead"})
class CollectionUid(BaseModel):
    """Information about the forked collection. The object's name is the forked collection's UID (`userId`-`collectionId`).

    :param is_source_ahead: If true, there is a difference between the forked collection and its source collection., defaults to None
    :type is_source_ahead: bool, optional
    """

    def __init__(self, is_source_ahead: bool = None):
        if is_source_ahead is not None:
            self.is_source_ahead = is_source_ahead


@JsonMap({"collection_uid": "collectionUid"})
class GetSourceCollectionStatusOkResponseCollection(BaseModel):
    """GetSourceCollectionStatusOkResponseCollection

    :param collection_uid: Information about the forked collection. The object's name is the forked collection's UID (`userId`-`collectionId`)., defaults to None
    :type collection_uid: CollectionUid, optional
    """

    def __init__(self, collection_uid: CollectionUid = None):
        if collection_uid is not None:
            self.collection_uid = self._define_object(collection_uid, CollectionUid)


@JsonMap({})
class GetSourceCollectionStatusOkResponse(BaseModel):
    """GetSourceCollectionStatusOkResponse

    :param collection: collection, defaults to None
    :type collection: GetSourceCollectionStatusOkResponseCollection, optional
    """

    def __init__(
        self, collection: GetSourceCollectionStatusOkResponseCollection = None
    ):
        if collection is not None:
            self.collection = self._define_object(
                collection, GetSourceCollectionStatusOkResponseCollection
            )
