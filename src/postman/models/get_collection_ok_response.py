from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class GetCollectionOkResponse(BaseModel):
    """GetCollectionOkResponse

    :param collection: For a complete list of this endpoint's possible values, use the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json)., defaults to None
    :type collection: dict, optional
    """

    def __init__(self, collection: dict = None):
        if collection is not None:
            self.collection = collection
