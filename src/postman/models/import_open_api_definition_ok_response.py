from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id"})
class ImportOpenApiDefinitionOkResponseCollections(BaseModel):
    """ImportOpenApiDefinitionOkResponseCollections

    :param id_: The collection's ID., defaults to None
    :type id_: str, optional
    :param name: The collection's name., defaults to None
    :type name: str, optional
    :param uid: The collection's unique ID., defaults to None
    :type uid: str, optional
    """

    def __init__(self, id_: str = None, name: str = None, uid: str = None):
        if id_ is not None:
            self.id_ = id_
        if name is not None:
            self.name = name
        if uid is not None:
            self.uid = uid


@JsonMap({})
class ImportOpenApiDefinitionOkResponse(BaseModel):
    """ImportOpenApiDefinitionOkResponse

    :param collections: collections, defaults to None
    :type collections: List[ImportOpenApiDefinitionOkResponseCollections], optional
    """

    def __init__(
        self, collections: List[ImportOpenApiDefinitionOkResponseCollections] = None
    ):
        if collections is not None:
            self.collections = self._define_list(
                collections, ImportOpenApiDefinitionOkResponseCollections
            )
