from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class CollectionInfo2(BaseModel):
    """An object that contains the collection's updated name and description.

    :param name: The collection's updated name., defaults to None
    :type name: str, optional
    :param description: The collection's updated description., defaults to None
    :type description: str, optional
    """

    def __init__(self, name: str = None, description: str = None):
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description


@JsonMap({})
class PatchCollectionRequestCollection(BaseModel):
    """PatchCollectionRequestCollection

    :param info: An object that contains the collection's updated name and description., defaults to None
    :type info: CollectionInfo2, optional
    :param variables: The collection's updated variables. Refer to `"#/definitions/variable"` in the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json)., defaults to None
    :type variables: dict, optional
    :param auth: The collection's updated authentication. Refer to `"#/definitions/auth-attribute"` in the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json)., defaults to None
    :type auth: dict, optional
    :param events: The collection's updated events. Refer to `"#/definitions/event"` in the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json)., defaults to None
    :type events: dict, optional
    """

    def __init__(
        self,
        info: CollectionInfo2 = None,
        variables: dict = None,
        auth: dict = None,
        events: dict = None,
    ):
        if info is not None:
            self.info = self._define_object(info, CollectionInfo2)
        if variables is not None:
            self.variables = variables
        if auth is not None:
            self.auth = auth
        if events is not None:
            self.events = events


@JsonMap({})
class PatchCollectionRequest(BaseModel):
    """PatchCollectionRequest

    :param collection: collection, defaults to None
    :type collection: PatchCollectionRequestCollection, optional
    """

    def __init__(self, collection: PatchCollectionRequestCollection = None):
        if collection is not None:
            self.collection = self._define_object(
                collection, PatchCollectionRequestCollection
            )
