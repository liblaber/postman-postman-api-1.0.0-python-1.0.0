from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id", "parent_folder_id": "parentFolderId"})
class PanCreateCollectionCollection(BaseModel):
    """PanCreateCollectionCollection

    :param id_: The collection's ID.
    :type id_: str
    :param parent_folder_id: The collection's parent folder ID.
    :type parent_folder_id: int
    :param environments: A list of environment UIDs (`userId`-`environmentId``) to add to the collection., defaults to None
    :type environments: List[str], optional
    """

    def __init__(self, id_: str, parent_folder_id: int, environments: List[str] = None):
        self.id_ = id_
        self.parent_folder_id = parent_folder_id
        if environments is not None:
            self.environments = environments


@JsonMap({})
class PanCreateCollection(BaseModel):
    """PanCreateCollection

    :param collection: collection, defaults to None
    :type collection: PanCreateCollectionCollection, optional
    """

    def __init__(self, collection: PanCreateCollectionCollection = None):
        if collection is not None:
            self.collection = self._define_object(
                collection, PanCreateCollectionCollection
            )
