from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id"})
class MergeCollectionForkOkResponseCollection(BaseModel):
    """MergeCollectionForkOkResponseCollection

    :param id_: The source collection's ID., defaults to None
    :type id_: str, optional
    :param uid: The source collection's unique ID., defaults to None
    :type uid: str, optional
    """

    def __init__(self, id_: str = None, uid: str = None):
        if id_ is not None:
            self.id_ = id_
        if uid is not None:
            self.uid = uid


@JsonMap({})
class MergeCollectionForkOkResponse(BaseModel):
    """MergeCollectionForkOkResponse

    :param collection: collection, defaults to None
    :type collection: MergeCollectionForkOkResponseCollection, optional
    """

    def __init__(self, collection: MergeCollectionForkOkResponseCollection = None):
        if collection is not None:
            self.collection = self._define_object(
                collection, MergeCollectionForkOkResponseCollection
            )
