# This file was generated by liblab | https://liblab.com/

from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class PutCollectionCollection1(BaseModel):
    """For a complete list of values, refer to the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json).

    :param info: An object that contains basic information about the collection. For a complete list of values, refer to the `definitions.info` entry in the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json).
    :type info: dict
    :param item: Information about the collection's contents, such as folders, requests, and responses. For a complete list of values, refer to the `#/definitions/item-group` entry in the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json). The maximum collection size cannot exceed 20 MB.
    :type item: List[dict]
    """

    def __init__(self, info: dict, item: List[dict]):
        """For a complete list of values, refer to the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json).

        :param info: An object that contains basic information about the collection. For a complete list of values, refer to the `definitions.info` entry in the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json).
        :type info: dict
        :param item: Information about the collection's contents, such as folders, requests, and responses. For a complete list of values, refer to the `#/definitions/item-group` entry in the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json). The maximum collection size cannot exceed 20 MB.
        :type item: List[dict]
        """
        self.info = info
        self.item = item


@JsonMap({})
class PutCollectionRequest(BaseModel):
    """PutCollectionRequest

    :param collection: For a complete list of values, refer to the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json)., defaults to None
    :type collection: PutCollectionCollection1, optional
    """

    def __init__(self, collection: PutCollectionCollection1 = None):
        """PutCollectionRequest

        :param collection: For a complete list of values, refer to the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json)., defaults to None
        :type collection: PutCollectionCollection1, optional
        """
        if collection is not None:
            self.collection = self._define_object(collection, PutCollectionCollection1)
