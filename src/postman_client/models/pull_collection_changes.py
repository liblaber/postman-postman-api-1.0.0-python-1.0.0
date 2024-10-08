# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({"destination_id": "destinationId", "source_id": "sourceId"})
class PullCollectionChangesCollection(BaseModel):
    """Information about the updated collection fork.

    :param destination_id: The ID of the forked collection the changes were pulled into., defaults to None
    :type destination_id: str, optional
    :param source_id: The ID of the source collection the changes were pulled from., defaults to None
    :type source_id: str, optional
    """

    def __init__(self, destination_id: str = None, source_id: str = None):
        """Information about the updated collection fork.

        :param destination_id: The ID of the forked collection the changes were pulled into., defaults to None
        :type destination_id: str, optional
        :param source_id: The ID of the source collection the changes were pulled from., defaults to None
        :type source_id: str, optional
        """
        if destination_id is not None:
            self.destination_id = destination_id
        if source_id is not None:
            self.source_id = source_id


@JsonMap({})
class PullCollectionChanges(BaseModel):
    """PullCollectionChanges

    :param collection: Information about the updated collection fork., defaults to None
    :type collection: PullCollectionChangesCollection, optional
    """

    def __init__(self, collection: PullCollectionChangesCollection = None):
        """PullCollectionChanges

        :param collection: Information about the updated collection fork., defaults to None
        :type collection: PullCollectionChangesCollection, optional
        """
        if collection is not None:
            self.collection = self._define_object(
                collection, PullCollectionChangesCollection
            )
