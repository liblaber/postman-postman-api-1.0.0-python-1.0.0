# This file was generated by liblab | https://liblab.com/

from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class StatsAssertions1(BaseModel):
    """Information about the monitor's assertions.

    :param failed: The total number of test failures., defaults to None
    :type failed: float, optional
    :param total: The total number of tests performed., defaults to None
    :type total: float, optional
    """

    def __init__(self, failed: float = None, total: float = None):
        if failed is not None:
            self.failed = failed
        if total is not None:
            self.total = total


@JsonMap({})
class StatsRequests1(BaseModel):
    """Information about the monitor's requests.

    :param total: The total number of requests., defaults to None
    :type total: float, optional
    """

    def __init__(self, total: float = None):
        if total is not None:
            self.total = total


@JsonMap({})
class LastRunStats(BaseModel):
    """Information about the monitor's stats.

    :param assertions: Information about the monitor's assertions., defaults to None
    :type assertions: StatsAssertions1, optional
    :param requests: Information about the monitor's requests., defaults to None
    :type requests: StatsRequests1, optional
    """

    def __init__(
        self, assertions: StatsAssertions1 = None, requests: StatsRequests1 = None
    ):
        if assertions is not None:
            self.assertions = self._define_object(assertions, StatsAssertions1)
        if requests is not None:
            self.requests = self._define_object(requests, StatsRequests1)


@JsonMap({"finished_at": "finishedAt", "started_at": "startedAt"})
class LastRun(BaseModel):
    """Information about the monitor's previous run.

    :param finished_at: The date and time at which the monitor's previous run completed., defaults to None
    :type finished_at: str, optional
    :param started_at: The date and time at which the monitor's previous run started., defaults to None
    :type started_at: str, optional
    :param stats: Information about the monitor's stats., defaults to None
    :type stats: LastRunStats, optional
    :param status: The monitor's status after its last run., defaults to None
    :type status: str, optional
    """

    def __init__(
        self,
        finished_at: str = None,
        started_at: str = None,
        stats: LastRunStats = None,
        status: str = None,
    ):
        if finished_at is not None:
            self.finished_at = finished_at
        if started_at is not None:
            self.started_at = started_at
        if stats is not None:
            self.stats = self._define_object(stats, LastRunStats)
        if status is not None:
            self.status = status


@JsonMap({})
class OnError(BaseModel):
    """OnError

    :param email: The email address of the user to notify on monitor error., defaults to None
    :type email: str, optional
    """

    def __init__(self, email: str = None):
        if email is not None:
            self.email = email


@JsonMap({})
class OnFailure(BaseModel):
    """OnFailure

    :param email: The email address of the user to notify on monitor failure., defaults to None
    :type email: str, optional
    """

    def __init__(self, email: str = None):
        if email is not None:
            self.email = email


@JsonMap({"on_error": "onError", "on_failure": "onFailure"})
class Notifications(BaseModel):
    """Information about the monitor's notification settings.

    :param on_error: on_error, defaults to None
    :type on_error: List[OnError], optional
    :param on_failure: on_failure, defaults to None
    :type on_failure: List[OnFailure], optional
    """

    def __init__(
        self, on_error: List[OnError] = None, on_failure: List[OnFailure] = None
    ):
        if on_error is not None:
            self.on_error = self._define_list(on_error, OnError)
        if on_failure is not None:
            self.on_failure = self._define_list(on_failure, OnFailure)


@JsonMap(
    {
        "follow_redirects": "followRedirects",
        "request_delay": "requestDelay",
        "request_timeout": "requestTimeout",
        "strict_ssl": "strictSSL",
    }
)
class Options(BaseModel):
    """Information about the monitor's option settings.

    :param follow_redirects: If true, follow redirects enabled., defaults to None
    :type follow_redirects: bool, optional
    :param request_delay: The monitor's request delay value., defaults to None
    :type request_delay: float, optional
    :param request_timeout: The monitor's request timeout value., defaults to None
    :type request_timeout: float, optional
    :param strict_ssl: If true, strict SSL enabled., defaults to None
    :type strict_ssl: bool, optional
    """

    def __init__(
        self,
        follow_redirects: bool = None,
        request_delay: float = None,
        request_timeout: float = None,
        strict_ssl: bool = None,
    ):
        if follow_redirects is not None:
            self.follow_redirects = follow_redirects
        if request_delay is not None:
            self.request_delay = request_delay
        if request_timeout is not None:
            self.request_timeout = request_timeout
        if strict_ssl is not None:
            self.strict_ssl = strict_ssl


@JsonMap({"next_run": "nextRun"})
class MonitorSchedule2(BaseModel):
    """Information about the monitor's schedule.

    :param cron: The monitor's cron frequency value., defaults to None
    :type cron: str, optional
    :param next_run: The date and time of monitor's next scheduled run., defaults to None
    :type next_run: str, optional
    :param timezone: The monitor's timezone., defaults to None
    :type timezone: str, optional
    """

    def __init__(self, cron: str = None, next_run: str = None, timezone: str = None):
        if cron is not None:
            self.cron = cron
        if next_run is not None:
            self.next_run = next_run
        if timezone is not None:
            self.timezone = timezone


@JsonMap(
    {
        "id_": "id",
        "collection_uid": "collectionUid",
        "environment_uid": "environmentUid",
        "last_run": "lastRun",
    }
)
class GetMonitorMonitor(BaseModel):
    """GetMonitorMonitor

    :param id_: The monitor's ID., defaults to None
    :type id_: str, optional
    :param name: The monitor's name., defaults to None
    :type name: str, optional
    :param uid: The monitor's unique ID., defaults to None
    :type uid: str, optional
    :param owner: The ID of monitor's owner., defaults to None
    :type owner: float, optional
    :param collection_uid: The unique ID of the monitor's associated collection., defaults to None
    :type collection_uid: str, optional
    :param environment_uid: The unique ID of the monitor's associated environment., defaults to None
    :type environment_uid: str, optional
    :param distribution: A list of the monitor's [geographic regions](https://learning.postman.com/docs/monitoring-your-api/setting-up-monitor/#adding-regions)., defaults to None
    :type distribution: List[str], optional
    :param last_run: Information about the monitor's previous run., defaults to None
    :type last_run: LastRun, optional
    :param notifications: Information about the monitor's notification settings., defaults to None
    :type notifications: Notifications, optional
    :param options: Information about the monitor's option settings., defaults to None
    :type options: Options, optional
    :param schedule: Information about the monitor's schedule., defaults to None
    :type schedule: MonitorSchedule2, optional
    """

    def __init__(
        self,
        id_: str = None,
        name: str = None,
        uid: str = None,
        owner: float = None,
        collection_uid: str = None,
        environment_uid: str = None,
        distribution: List[str] = None,
        last_run: LastRun = None,
        notifications: Notifications = None,
        options: Options = None,
        schedule: MonitorSchedule2 = None,
    ):
        if id_ is not None:
            self.id_ = id_
        if name is not None:
            self.name = name
        if uid is not None:
            self.uid = uid
        if owner is not None:
            self.owner = owner
        if collection_uid is not None:
            self.collection_uid = collection_uid
        if environment_uid is not None:
            self.environment_uid = environment_uid
        if distribution is not None:
            self.distribution = distribution
        if last_run is not None:
            self.last_run = self._define_object(last_run, LastRun)
        if notifications is not None:
            self.notifications = self._define_object(notifications, Notifications)
        if options is not None:
            self.options = self._define_object(options, Options)
        if schedule is not None:
            self.schedule = self._define_object(schedule, MonitorSchedule2)


@JsonMap({})
class GetMonitor(BaseModel):
    """GetMonitor

    :param monitor: monitor, defaults to None
    :type monitor: GetMonitorMonitor, optional
    """

    def __init__(self, monitor: GetMonitorMonitor = None):
        if monitor is not None:
            self.monitor = self._define_object(monitor, GetMonitorMonitor)
