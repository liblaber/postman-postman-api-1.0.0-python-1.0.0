from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id"})
class PatchCollectionOkResponseCollection(BaseModel):
    """PatchCollectionOkResponseCollection

    :param id_: The collection's ID., defaults to None
    :type id_: str, optional
    :param name: The collection's updated name., defaults to None
    :type name: str, optional
    :param description: The collection's updated description., defaults to None
    :type description: str, optional
    """

    def __init__(self, id_: str = None, name: str = None, description: str = None):
        if id_ is not None:
            self.id_ = id_
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description


@JsonMap({})
class PatchCollectionOkResponse(BaseModel):
    """PatchCollectionOkResponse

    :param collection: collection, defaults to None
    :type collection: PatchCollectionOkResponseCollection, optional
    """

    def __init__(self, collection: PatchCollectionOkResponseCollection = None):
        if collection is not None:
            self.collection = self._define_object(
                collection, PatchCollectionOkResponseCollection
            )
