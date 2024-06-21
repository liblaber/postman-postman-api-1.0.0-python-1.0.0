from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"add": "$add", "remove": "$remove"})
class CollectionEnvironments(BaseModel):
    """The collection's updated environments.

    :param add: add, defaults to None
    :type add: List[str], optional
    :param remove: remove, defaults to None
    :type remove: List[str], optional
    """

    def __init__(self, add: List[str] = None, remove: List[str] = None):
        if add is not None:
            self.add = add
        if remove is not None:
            self.remove = remove


@JsonMap({"parent_folder_id": "parentFolderId"})
class UpdatePanCollectionCollection(BaseModel):
    """UpdatePanCollectionCollection

    :param parent_folder_id: The collection's new parent folder ID., defaults to None
    :type parent_folder_id: int, optional
    :param environments: The collection's updated environments., defaults to None
    :type environments: CollectionEnvironments, optional
    """

    def __init__(
        self, parent_folder_id: int = None, environments: CollectionEnvironments = None
    ):
        if parent_folder_id is not None:
            self.parent_folder_id = parent_folder_id
        if environments is not None:
            self.environments = self._define_object(
                environments, CollectionEnvironments
            )


@JsonMap({})
class UpdatePanCollection(BaseModel):
    """UpdatePanCollection

    :param collection: collection, defaults to None
    :type collection: UpdatePanCollectionCollection, optional
    """

    def __init__(self, collection: UpdatePanCollectionCollection = None):
        if collection is not None:
            self.collection = self._define_object(
                collection, UpdatePanCollectionCollection
            )
