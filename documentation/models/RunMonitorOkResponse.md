# RunMonitorOkResponse

**Properties**

| Name | Type | Required | Description                        |
| :--- | :--- | :------- | :--------------------------------- |
| run  | Run  | ❌       | Information about the monitor run. |

# Run

Information about the monitor run.

**Properties**

| Name       | Type             | Required | Description                                                      |
| :--------- | :--------------- | :------- | :--------------------------------------------------------------- |
| info       | RunInfo          | ❌       | Information about the monitor.                                   |
| stats      | RunStats         | ❌       | Information about the monitor run's stats.                       |
| executions | List[Executions] | ❌       | Information about the monitor run's executions.                  |
| failures   | List[dict]       | ❌       | If the monitor run failed, information about the run's failures. |

# RunInfo

Information about the monitor.

**Properties**

| Name            | Type | Required | Description                                             |
| :-------------- | :--- | :------- | :------------------------------------------------------ |
| job_id          | str  | ❌       | The monitor's run job ID.                               |
| collection_uid  | str  | ❌       | The unique ID of the monitor's associated collection.   |
| environment_uid | str  | ❌       | The unique ID of the monitor's associated environment.  |
| monitor_id      | str  | ❌       | The monitor's ID.                                       |
| name            | str  | ❌       | The monitor's name.                                     |
| status          | str  | ❌       | The monitor run's status.                               |
| started_at      | str  | ❌       | The date and time at which the monitor run began.       |
| finished_at     | str  | ❌       | The date and time at which the monitor's run completed. |

# RunStats

Information about the monitor run's stats.

**Properties**

| Name       | Type             | Required | Description                         |
| :--------- | :--------------- | :------- | :---------------------------------- |
| assertions | StatsAssertions2 | ❌       | The monitor run's assertions stats. |
| requests   | StatsRequests2   | ❌       | The monitor run's request stats.    |

# StatsAssertions_2

The monitor run's assertions stats.

**Properties**

| Name   | Type  | Required | Description                          |
| :----- | :---- | :------- | :----------------------------------- |
| total  | float | ❌       | The total number of tests performed. |
| failed | float | ❌       | The total number of test failures.   |

# StatsRequests_2

The monitor run's request stats.

**Properties**

| Name   | Type  | Required | Description                     |
| :----- | :---- | :------- | :------------------------------ |
| total  | float | ❌       | The total number of requests.   |
| failed | float | ❌       | The number of request failures. |

# Executions

**Properties**

| Name     | Type               | Required | Description                                   |
| :------- | :----------------- | :------- | :-------------------------------------------- |
| id\_     | float              | ❌       | The execution ID.                             |
| item     | ExecutionsItem     | ❌       | Information about the executed item.          |
| request  | ExecutionsRequest  | ❌       | Information about the monitor run's requests. |
| response | ExecutionsResponse | ❌       | Information about the monitor run's response. |

# ExecutionsItem

Information about the executed item.

**Properties**

| Name | Type | Required | Description               |
| :--- | :--- | :------- | :------------------------ |
| name | str  | ❌       | The executed item's name. |

# ExecutionsRequest

Information about the monitor run's requests.

**Properties**

| Name      | Type | Required | Description                                                                                           |
| :-------- | :--- | :------- | :---------------------------------------------------------------------------------------------------- |
| method    | str  | ❌       | The request method.                                                                                   |
| url       | str  | ❌       | The request's URL.                                                                                    |
| body      | dict | ❌       | Information about the request body, such as Content-Length.                                           |
| headers   | dict | ❌       | Information about the request headers, such as Content-Type, Accept, encoding, and other information. |
| timestamp | str  | ❌       | The date and time of the request.                                                                     |

# ExecutionsResponse

Information about the monitor run's response.

**Properties**

| Name          | Type  | Required | Description                                                                                            |
| :------------ | :---- | :------- | :----------------------------------------------------------------------------------------------------- |
| body          | dict  | ❌       | Information about the request body, such as Content-Length.                                            |
| code          | float | ❌       | The response's HTTP status code.                                                                       |
| headers       | dict  | ❌       | Information about the response headers, such as Content-Type, Accept, encoding, and other information. |
| response_size | float | ❌       | The response size, in bytes.                                                                           |
| response_time | float | ❌       | The response time, in milliseconds.                                                                    |
<<<<<<< HEAD
=======

<!-- This file was generated by liblab | https://liblab.com/ -->
>>>>>>> 95da91c (initial commit)
