<<<<<<< HEAD
=======
# This file was generated by liblab | https://liblab.com/

>>>>>>> 95da91c (initial commit)
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class CollectionInfo1(BaseModel):
    """An object that contains basic information about the collection. For a complete list of values, refer to the `definitions.info` entry in the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json).

    :param name: The collection's name.
    :type name: str
    :param schema: A URL to the collection's schema.
    :type schema: str
    """

    def __init__(self, name: str, schema: str):
        self.name = name
        self.schema = schema


@JsonMap({})
class CollectionItem(BaseModel):
    """CollectionItem

    :param request: The collection's request information. For a complete list of values, refer to the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json). If you pass an empty object for this value, the system defaults to an untitled GET request.
    :type request: dict
    """

    def __init__(self, request: dict):
        self.request = request


@JsonMap({})
class CreateCollectionRequestCollection(BaseModel):
    """For a complete list of values, refer to the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json).

    :param info: An object that contains basic information about the collection. For a complete list of values, refer to the `definitions.info` entry in the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json).
    :type info: CollectionInfo1
    :param item: Information about the collection's HTTP requests and responses. For a complete list of values, refer to the `definitions.item` entry in the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json)., defaults to None
    :type item: List[CollectionItem], optional
    """

    def __init__(self, info: CollectionInfo1, item: List[CollectionItem] = None):
        self.info = self._define_object(info, CollectionInfo1)
        if item is not None:
            self.item = self._define_list(item, CollectionItem)


@JsonMap({})
class CreateCollectionRequest(BaseModel):
    """CreateCollectionRequest

    :param collection: For a complete list of values, refer to the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json)., defaults to None
    :type collection: CreateCollectionRequestCollection, optional
    """

    def __init__(self, collection: CreateCollectionRequestCollection = None):
        if collection is not None:
            self.collection = self._define_object(
                collection, CreateCollectionRequestCollection
            )
