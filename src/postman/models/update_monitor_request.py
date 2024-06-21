from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class MonitorSchedule3(BaseModel):
    """Information about the monitor's schedule.

    :param cron: The monitor's run frequency, based on the given cron pattern:<br/><br/>\| Frequency \| Pattern \|<br/>\| --------- \| ------- \|<br/>\| Every 5 minutes \| `*/5 * * * *` \|<br/>\| Every 30 minutes \| `*/30 * * * *` \|<br/>\| Every hour \| `0 */1 * * *` \|<br/>\| Every 6 hours \| `0 */6 * * *` \|<br/>\| Every day at 5 pm \| `0 17 * * *` \|<br/>\| Every Monday at 12 pm \| `0 12 * * MON` \|<br/>\| Every weekday (Mon — Fri) at 6 am \| `0 6 * * MON-FRI` \|<br/><br/>At this time you can only create monitors with limited schedules.<br/>, defaults to None
    :type cron: str, optional
    :param timezone: The monitor's [timezone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)., defaults to None
    :type timezone: str, optional
    """

    def __init__(self, cron: str = None, timezone: str = None):
        if cron is not None:
            self.cron = cron
        if timezone is not None:
            self.timezone = timezone


@JsonMap({})
class UpdateMonitorRequestMonitor(BaseModel):
    """UpdateMonitorRequestMonitor

    :param name: The monitor's name., defaults to None
    :type name: str, optional
    :param schedule: Information about the monitor's schedule., defaults to None
    :type schedule: MonitorSchedule3, optional
    """

    def __init__(self, name: str = None, schedule: MonitorSchedule3 = None):
        if name is not None:
            self.name = name
        if schedule is not None:
            self.schedule = self._define_object(schedule, MonitorSchedule3)


@JsonMap({})
class UpdateMonitorRequest(BaseModel):
    """UpdateMonitorRequest

    :param monitor: monitor, defaults to None
    :type monitor: UpdateMonitorRequestMonitor, optional
    """

    def __init__(self, monitor: UpdateMonitorRequestMonitor = None):
        if monitor is not None:
            self.monitor = self._define_object(monitor, UpdateMonitorRequestMonitor)
