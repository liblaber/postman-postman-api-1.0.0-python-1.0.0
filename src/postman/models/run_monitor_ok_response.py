from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap(
    {
        "job_id": "jobId",
        "collection_uid": "collectionUid",
        "environment_uid": "environmentUid",
        "monitor_id": "monitorId",
        "started_at": "startedAt",
        "finished_at": "finishedAt",
    }
)
class RunInfo(BaseModel):
    """Information about the monitor.

    :param job_id: The monitor's run job ID., defaults to None
    :type job_id: str, optional
    :param collection_uid: The unique ID of the monitor's associated collection., defaults to None
    :type collection_uid: str, optional
    :param environment_uid: The unique ID of the monitor's associated environment., defaults to None
    :type environment_uid: str, optional
    :param monitor_id: The monitor's ID., defaults to None
    :type monitor_id: str, optional
    :param name: The monitor's name., defaults to None
    :type name: str, optional
    :param status: The monitor run's status., defaults to None
    :type status: str, optional
    :param started_at: The date and time at which the monitor run began., defaults to None
    :type started_at: str, optional
    :param finished_at: The date and time at which the monitor's run completed., defaults to None
    :type finished_at: str, optional
    """

    def __init__(
        self,
        job_id: str = None,
        collection_uid: str = None,
        environment_uid: str = None,
        monitor_id: str = None,
        name: str = None,
        status: str = None,
        started_at: str = None,
        finished_at: str = None,
    ):
        if job_id is not None:
            self.job_id = job_id
        if collection_uid is not None:
            self.collection_uid = collection_uid
        if environment_uid is not None:
            self.environment_uid = environment_uid
        if monitor_id is not None:
            self.monitor_id = monitor_id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if started_at is not None:
            self.started_at = started_at
        if finished_at is not None:
            self.finished_at = finished_at


@JsonMap({})
class StatsAssertions2(BaseModel):
    """The monitor run's assertions stats.

    :param total: The total number of tests performed., defaults to None
    :type total: float, optional
    :param failed: The total number of test failures., defaults to None
    :type failed: float, optional
    """

    def __init__(self, total: float = None, failed: float = None):
        if total is not None:
            self.total = total
        if failed is not None:
            self.failed = failed


@JsonMap({})
class StatsRequests2(BaseModel):
    """The monitor run's request stats.

    :param total: The total number of requests., defaults to None
    :type total: float, optional
    :param failed: The number of request failures., defaults to None
    :type failed: float, optional
    """

    def __init__(self, total: float = None, failed: float = None):
        if total is not None:
            self.total = total
        if failed is not None:
            self.failed = failed


@JsonMap({})
class RunStats(BaseModel):
    """Information about the monitor run's stats.

    :param assertions: The monitor run's assertions stats., defaults to None
    :type assertions: StatsAssertions2, optional
    :param requests: The monitor run's request stats., defaults to None
    :type requests: StatsRequests2, optional
    """

    def __init__(
        self, assertions: StatsAssertions2 = None, requests: StatsRequests2 = None
    ):
        if assertions is not None:
            self.assertions = self._define_object(assertions, StatsAssertions2)
        if requests is not None:
            self.requests = self._define_object(requests, StatsRequests2)


@JsonMap({})
class ExecutionsItem(BaseModel):
    """Information about the executed item.

    :param name: The executed item's name., defaults to None
    :type name: str, optional
    """

    def __init__(self, name: str = None):
        if name is not None:
            self.name = name


@JsonMap({})
class ExecutionsRequest(BaseModel):
    """Information about the monitor run's requests.

    :param method: The request method., defaults to None
    :type method: str, optional
    :param url: The request's URL., defaults to None
    :type url: str, optional
    :param body: Information about the request body, such as Content-Length., defaults to None
    :type body: dict, optional
    :param headers: Information about the request headers, such as Content-Type, Accept, encoding, and other information., defaults to None
    :type headers: dict, optional
    :param timestamp: The date and time of the request., defaults to None
    :type timestamp: str, optional
    """

    def __init__(
        self,
        method: str = None,
        url: str = None,
        body: dict = None,
        headers: dict = None,
        timestamp: str = None,
    ):
        if method is not None:
            self.method = method
        if url is not None:
            self.url = url
        if body is not None:
            self.body = body
        if headers is not None:
            self.headers = headers
        if timestamp is not None:
            self.timestamp = timestamp


@JsonMap({"response_size": "responseSize", "response_time": "responseTime"})
class ExecutionsResponse(BaseModel):
    """Information about the monitor run's response.

    :param body: Information about the request body, such as Content-Length., defaults to None
    :type body: dict, optional
    :param code: The response's HTTP status code., defaults to None
    :type code: float, optional
    :param headers: Information about the response headers, such as Content-Type, Accept, encoding, and other information., defaults to None
    :type headers: dict, optional
    :param response_size: The response size, in bytes., defaults to None
    :type response_size: float, optional
    :param response_time: The response time, in milliseconds., defaults to None
    :type response_time: float, optional
    """

    def __init__(
        self,
        body: dict = None,
        code: float = None,
        headers: dict = None,
        response_size: float = None,
        response_time: float = None,
    ):
        if body is not None:
            self.body = body
        if code is not None:
            self.code = code
        if headers is not None:
            self.headers = headers
        if response_size is not None:
            self.response_size = response_size
        if response_time is not None:
            self.response_time = response_time


@JsonMap({"id_": "id"})
class Executions(BaseModel):
    """Executions

    :param id_: The execution ID., defaults to None
    :type id_: float, optional
    :param item: Information about the executed item., defaults to None
    :type item: ExecutionsItem, optional
    :param request: Information about the monitor run's requests., defaults to None
    :type request: ExecutionsRequest, optional
    :param response: Information about the monitor run's response., defaults to None
    :type response: ExecutionsResponse, optional
    """

    def __init__(
        self,
        id_: float = None,
        item: ExecutionsItem = None,
        request: ExecutionsRequest = None,
        response: ExecutionsResponse = None,
    ):
        if id_ is not None:
            self.id_ = id_
        if item is not None:
            self.item = self._define_object(item, ExecutionsItem)
        if request is not None:
            self.request = self._define_object(request, ExecutionsRequest)
        if response is not None:
            self.response = self._define_object(response, ExecutionsResponse)


@JsonMap({})
class Run(BaseModel):
    """Information about the monitor run.

    :param info: Information about the monitor., defaults to None
    :type info: RunInfo, optional
    :param stats: Information about the monitor run's stats., defaults to None
    :type stats: RunStats, optional
    :param executions: Information about the monitor run's executions., defaults to None
    :type executions: List[Executions], optional
    :param failures: If the monitor run failed, information about the run's failures., defaults to None
    :type failures: List[dict], optional
    """

    def __init__(
        self,
        info: RunInfo = None,
        stats: RunStats = None,
        executions: List[Executions] = None,
        failures: List[dict] = None,
    ):
        if info is not None:
            self.info = self._define_object(info, RunInfo)
        if stats is not None:
            self.stats = self._define_object(stats, RunStats)
        if executions is not None:
            self.executions = self._define_list(executions, Executions)
        if failures is not None:
            self.failures = failures


@JsonMap({})
class RunMonitorOkResponse(BaseModel):
    """RunMonitorOkResponse

    :param run: Information about the monitor run., defaults to None
    :type run: Run, optional
    """

    def __init__(self, run: Run = None):
        if run is not None:
            self.run = self._define_object(run, Run)
