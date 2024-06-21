from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class PutCollectionRequestCollection(BaseModel):
    """For a complete list of values, refer to the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json).

    :param info: An object that contains basic information about the collection. For a complete list of values, refer to the `definitions.info` entry in the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json).
    :type info: dict
    :param item: Information about the collection's contents, such as folders, requests, and responses. For a complete list of values, refer to the `#/definitions/item-group` entry in the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json).<br/><br/>The maximum collection size cannot exceed 20 MB.<br/>
    :type item: List[dict]
    """

    def __init__(self, info: dict, item: List[dict]):
        self.info = info
        self.item = item


@JsonMap({})
class PutCollectionRequest(BaseModel):
    """PutCollectionRequest

    :param collection: For a complete list of values, refer to the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json)., defaults to None
    :type collection: PutCollectionRequestCollection, optional
    """

    def __init__(self, collection: PutCollectionRequestCollection = None):
        if collection is not None:
            self.collection = self._define_object(
                collection, PutCollectionRequestCollection
            )
