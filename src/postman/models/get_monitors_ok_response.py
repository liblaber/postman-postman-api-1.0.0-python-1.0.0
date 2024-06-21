from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id"})
class GetMonitorsOkResponseMonitors(BaseModel):
    """GetMonitorsOkResponseMonitors

    :param id_: The monitor's ID., defaults to None
    :type id_: str, optional
    :param name: The monitor's name., defaults to None
    :type name: str, optional
    :param owner: The ID of the monitor's owner., defaults to None
    :type owner: str, optional
    :param uid: The monitor's unique ID., defaults to None
    :type uid: str, optional
    """

    def __init__(
        self, id_: str = None, name: str = None, owner: str = None, uid: str = None
    ):
        if id_ is not None:
            self.id_ = id_
        if name is not None:
            self.name = name
        if owner is not None:
            self.owner = owner
        if uid is not None:
            self.uid = uid


@JsonMap({})
class GetMonitorsOkResponse(BaseModel):
    """GetMonitorsOkResponse

    :param monitors: monitors, defaults to None
    :type monitors: List[GetMonitorsOkResponseMonitors], optional
    """

    def __init__(self, monitors: List[GetMonitorsOkResponseMonitors] = None):
        if monitors is not None:
            self.monitors = self._define_list(monitors, GetMonitorsOkResponseMonitors)
