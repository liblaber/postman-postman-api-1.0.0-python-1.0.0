from enum import Enum
from .utils.json_map import JsonMap
from .base import BaseModel


class Strategy(Enum):
    """An enumeration representing different categories.

    :cvar DELETESOURCE: "deleteSource"
    :vartype DELETESOURCE: str
    :cvar UPDATESOURCEWITHDESTINATION: "updateSourceWithDestination"
    :vartype UPDATESOURCEWITHDESTINATION: str
    """

    DELETESOURCE = "deleteSource"
    UPDATESOURCEWITHDESTINATION = "updateSourceWithDestination"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Strategy._member_map_.values()))


@JsonMap({})
class MergeCollectionForkRequest(BaseModel):
    """MergeCollectionForkRequest

    :param destination: The destination (parent) collection's unique ID.
    :type destination: str
    :param source: The source collection's unique ID.
    :type source: str
    :param strategy: The fork's merge strategy:<br/>- `deleteSource` — Merge the changes into the parent collection. After the merge process is complete, Postman deletes the fork. You must have Editor access to both the parent and forked collections.<br/>- `updateSourceWithDestination` — Merge the changes into the parent collection. Any differences in the parent collection are also made to the fork.<br/>, defaults to None
    :type strategy: Strategy, optional
    """

    def __init__(self, destination: str, source: str, strategy: Strategy = None):
        self.destination = destination
        self.source = source
        if strategy is not None:
            self.strategy = self._enum_matching(strategy, Strategy.list(), "strategy")
