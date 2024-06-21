from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id"})
class DeleteCollectionOkResponseCollection(BaseModel):
    """Information about the deleted collection.

    :param id_: The deleted collection's ID., defaults to None
    :type id_: str, optional
    :param uid: The deleted collection's unique ID., defaults to None
    :type uid: str, optional
    """

    def __init__(self, id_: str = None, uid: str = None):
        if id_ is not None:
            self.id_ = id_
        if uid is not None:
            self.uid = uid


@JsonMap({})
class DeleteCollectionOkResponse(BaseModel):
    """DeleteCollectionOkResponse

    :param collection: Information about the deleted collection., defaults to None
    :type collection: DeleteCollectionOkResponseCollection, optional
    """

    def __init__(self, collection: DeleteCollectionOkResponseCollection = None):
        if collection is not None:
            self.collection = self._define_object(
                collection, DeleteCollectionOkResponseCollection
            )
