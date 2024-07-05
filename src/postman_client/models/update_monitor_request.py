# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class MonitorSchedule3(BaseModel):
    """Information about the monitor's schedule.

    :param cron: The monitor's run frequency, based on the given cron pattern: \| Frequency \| Pattern \| \| --------- \| ------- \| \| Every 5 minutes \| `*\/5 * * * *` \| \| Every 30 minutes \| `*\/30 * * * *` \| \| Every hour \| `0 *\/1 * * *` \| \| Every 6 hours \| `0 *\/6 * * *` \| \| Every day at 5 pm \| `0 17 * * *` \| \| Every Monday at 12 pm \| `0 12 * * MON` \| \| Every weekday (Mon — Fri) at 6 am \| `0 6 * * MON-FRI` \| At this time you can only create monitors with limited schedules. , defaults to None
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
class UpdateMonitorMonitor1(BaseModel):
    """UpdateMonitorMonitor1

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
    :type monitor: UpdateMonitorMonitor1, optional
    """

    def __init__(self, monitor: UpdateMonitorMonitor1 = None):
        if monitor is not None:
            self.monitor = self._define_object(monitor, UpdateMonitorMonitor1)
