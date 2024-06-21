from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id"})
class CreateMonitorOkResponseMonitor(BaseModel):
    """CreateMonitorOkResponseMonitor

    :param id_: The monitor's ID., defaults to None
    :type id_: str, optional
    :param name: The monitor's name., defaults to None
    :type name: str, optional
    :param uid: The monitor's unique ID., defaults to None
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
class CreateMonitorOkResponse(BaseModel):
    """CreateMonitorOkResponse

    :param monitor: monitor, defaults to None
    :type monitor: CreateMonitorOkResponseMonitor, optional
    """

    def __init__(self, monitor: CreateMonitorOkResponseMonitor = None):
        if monitor is not None:
            self.monitor = self._define_object(monitor, CreateMonitorOkResponseMonitor)
