# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class MonitorSchedule1(BaseModel):
    """Information about the monitor's schedule.

    :param cron: The monitor's run frequency, based on the given cron pattern: \| Frequency \| Pattern \| \| --------- \| ------- \| \| Every 5 minutes \| `*`/5 * * * *` \| \| Every 30 minutes \| `*`/30 * * * *` \| \| Every hour \| `0 *`/1 * * *` \| \| Every 6 hours \| `0 *`/6 * * *` \| \| Every day at 5 pm \| `0 17 * * *` \| \| Every Monday at 12 pm \| `0 12 * * MON` \| \| Every weekday (Mon — Fri) at 6 am \| `0 6 * * MON-FRI` \| At this time you can only create monitors with limited schedules. , defaults to None
    :type cron: str, optional
    :param timezone: The monitor's [timezone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)., defaults to None
    :type timezone: str, optional
    """

    def __init__(self, cron: str = None, timezone: str = None):
        """Information about the monitor's schedule.

        :param cron: The monitor's run frequency, based on the given cron pattern: \| Frequency \| Pattern \| \| --------- \| ------- \| \| Every 5 minutes \| `*`/5 * * * *` \| \| Every 30 minutes \| `*`/30 * * * *` \| \| Every hour \| `0 *`/1 * * *` \| \| Every 6 hours \| `0 *`/6 * * *` \| \| Every day at 5 pm \| `0 17 * * *` \| \| Every Monday at 12 pm \| `0 12 * * MON` \| \| Every weekday (Mon — Fri) at 6 am \| `0 6 * * MON-FRI` \| At this time you can only create monitors with limited schedules. , defaults to None
        :type cron: str, optional
        :param timezone: The monitor's [timezone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)., defaults to None
        :type timezone: str, optional
        """
        if cron is not None:
            self.cron = cron
        if timezone is not None:
            self.timezone = timezone


@JsonMap({})
class CreateMonitorMonitor1(BaseModel):
    """CreateMonitorMonitor1

    :param collection: The unique ID of the monitor's associated collection., defaults to None
    :type collection: str, optional
    :param environment: The unique ID of the monitor's associated environment., defaults to None
    :type environment: str, optional
    :param name: The monitor's name., defaults to None
    :type name: str, optional
    :param schedule: Information about the monitor's schedule., defaults to None
    :type schedule: MonitorSchedule1, optional
    """

    def __init__(
        self,
        collection: str = None,
        environment: str = None,
        name: str = None,
        schedule: MonitorSchedule1 = None,
    ):
        """CreateMonitorMonitor1

        :param collection: The unique ID of the monitor's associated collection., defaults to None
        :type collection: str, optional
        :param environment: The unique ID of the monitor's associated environment., defaults to None
        :type environment: str, optional
        :param name: The monitor's name., defaults to None
        :type name: str, optional
        :param schedule: Information about the monitor's schedule., defaults to None
        :type schedule: MonitorSchedule1, optional
        """
        if collection is not None:
            self.collection = collection
        if environment is not None:
            self.environment = environment
        if name is not None:
            self.name = name
        if schedule is not None:
            self.schedule = self._define_object(schedule, MonitorSchedule1)


@JsonMap({})
class CreateMonitorRequest(BaseModel):
    """CreateMonitorRequest

    :param monitor: monitor, defaults to None
    :type monitor: CreateMonitorMonitor1, optional
    """

    def __init__(self, monitor: CreateMonitorMonitor1 = None):
        """CreateMonitorRequest

        :param monitor: monitor, defaults to None
        :type monitor: CreateMonitorMonitor1, optional
        """
        if monitor is not None:
            self.monitor = self._define_object(monitor, CreateMonitorMonitor1)
