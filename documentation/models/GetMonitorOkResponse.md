# GetMonitorOkResponse

**Properties**

| Name    | Type                        | Required | Description |
| :------ | :-------------------------- | :------- | :---------- |
| monitor | GetMonitorOkResponseMonitor | ❌       |             |

# GetMonitorOkResponseMonitor

**Properties**

| Name            | Type             | Required | Description                                                                                                                             |
| :-------------- | :--------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------- |
| id\_            | str              | ❌       | The monitor's ID.                                                                                                                       |
| name            | str              | ❌       | The monitor's name.                                                                                                                     |
| uid             | str              | ❌       | The monitor's unique ID.                                                                                                                |
| owner           | float            | ❌       | The ID of monitor's owner.                                                                                                              |
| collection_uid  | str              | ❌       | The unique ID of the monitor's associated collection.                                                                                   |
| environment_uid | str              | ❌       | The unique ID of the monitor's associated environment.                                                                                  |
| distribution    | List[str]        | ❌       | A list of the monitor's [geographic regions](https://learning.postman.com/docs/monitoring-your-api/setting-up-monitor/#adding-regions). |
| last_run        | LastRun          | ❌       | Information about the monitor's previous run.                                                                                           |
| notifications   | Notifications    | ❌       | Information about the monitor's notification settings.                                                                                  |
| options         | Options          | ❌       | Information about the monitor's option settings.                                                                                        |
| schedule        | MonitorSchedule2 | ❌       | Information about the monitor's schedule.                                                                                               |

# LastRun

Information about the monitor's previous run.

**Properties**

| Name        | Type         | Required | Description                                                      |
| :---------- | :----------- | :------- | :--------------------------------------------------------------- |
| finished_at | str          | ❌       | The date and time at which the monitor's previous run completed. |
| started_at  | str          | ❌       | The date and time at which the monitor's previous run started.   |
| stats       | LastRunStats | ❌       | Information about the monitor's stats.                           |
| status      | str          | ❌       | The monitor's status after its last run.                         |

# LastRunStats

Information about the monitor's stats.

**Properties**

| Name       | Type             | Required | Description                                 |
| :--------- | :--------------- | :------- | :------------------------------------------ |
| assertions | StatsAssertions1 | ❌       | Information about the monitor's assertions. |
| requests   | StatsRequests1   | ❌       | Information about the monitor's requests.   |

# StatsAssertions_1

Information about the monitor's assertions.

**Properties**

| Name   | Type  | Required | Description                          |
| :----- | :---- | :------- | :----------------------------------- |
| failed | float | ❌       | The total number of test failures.   |
| total  | float | ❌       | The total number of tests performed. |

# StatsRequests_1

Information about the monitor's requests.

**Properties**

| Name  | Type  | Required | Description                   |
| :---- | :---- | :------- | :---------------------------- |
| total | float | ❌       | The total number of requests. |

# Notifications

Information about the monitor's notification settings.

**Properties**

| Name       | Type            | Required | Description |
| :--------- | :-------------- | :------- | :---------- |
| on_error   | List[OnError]   | ❌       |             |
| on_failure | List[OnFailure] | ❌       |             |

# OnError

**Properties**

| Name  | Type | Required | Description                                               |
| :---- | :--- | :------- | :-------------------------------------------------------- |
| email | str  | ❌       | The email address of the user to notify on monitor error. |

# OnFailure

**Properties**

| Name  | Type | Required | Description                                                 |
| :---- | :--- | :------- | :---------------------------------------------------------- |
| email | str  | ❌       | The email address of the user to notify on monitor failure. |

# Options

Information about the monitor's option settings.

**Properties**

| Name             | Type  | Required | Description                          |
| :--------------- | :---- | :------- | :----------------------------------- |
| follow_redirects | bool  | ❌       | If true, follow redirects enabled.   |
| request_delay    | float | ❌       | The monitor's request delay value.   |
| request_timeout  | float | ❌       | The monitor's request timeout value. |
| strict_ssl       | bool  | ❌       | If true, strict SSL enabled.         |

# MonitorSchedule_2

Information about the monitor's schedule.

**Properties**

| Name     | Type | Required | Description                                        |
| :------- | :--- | :------- | :------------------------------------------------- |
| cron     | str  | ❌       | The monitor's cron frequency value.                |
| next_run | str  | ❌       | The date and time of monitor's next scheduled run. |
| timezone | str  | ❌       | The monitor's timezone.                            |
