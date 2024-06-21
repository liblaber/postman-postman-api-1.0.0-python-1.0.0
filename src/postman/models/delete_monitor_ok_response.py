from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id"})
class DeleteMonitorOkResponseMonitor(BaseModel):
    """DeleteMonitorOkResponseMonitor

    :param id_: The monitor's ID., defaults to None
    :type id_: str, optional
    :param uid: The monitor's unique ID., defaults to None
    :type uid: str, optional
    """

    def __init__(self, id_: str = None, uid: str = None):
        if id_ is not None:
            self.id_ = id_
        if uid is not None:
            self.uid = uid


@JsonMap({})
class DeleteMonitorOkResponse(BaseModel):
    """DeleteMonitorOkResponse

    :param monitor: monitor, defaults to None
    :type monitor: DeleteMonitorOkResponseMonitor, optional
    """

    def __init__(self, monitor: DeleteMonitorOkResponseMonitor = None):
        if monitor is not None:
            self.monitor = self._define_object(monitor, DeleteMonitorOkResponseMonitor)
