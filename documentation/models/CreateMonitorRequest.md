# CreateMonitorRequest

**Properties**

| Name    | Type                        | Required | Description |
| :------ | :-------------------------- | :------- | :---------- |
| monitor | CreateMonitorRequestMonitor | ❌       |             |

# CreateMonitorRequestMonitor

**Properties**

| Name        | Type             | Required | Description                                            |
| :---------- | :--------------- | :------- | :----------------------------------------------------- |
| collection  | str              | ❌       | The unique ID of the monitor's associated collection.  |
| environment | str              | ❌       | The unique ID of the monitor's associated environment. |
| name        | str              | ❌       | The monitor's name.                                    |
| schedule    | MonitorSchedule1 | ❌       | Information about the monitor's schedule.              |

# MonitorSchedule_1

Information about the monitor's schedule.

**Properties**

| Name     | Type | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| :------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| cron     | str  | ❌       | The monitor's run frequency, based on the given cron pattern:<br/><br/>\| Frequency \| Pattern \|<br/>\| --------- \| ------- \|<br/>\| Every 5 minutes \| `*/5 * * * *` \|<br/>\| Every 30 minutes \| `*/30 * * * *` \|<br/>\| Every hour \| `0 */1 * * *` \|<br/>\| Every 6 hours \| `0 */6 * * *` \|<br/>\| Every day at 5 pm \| `0 17 * * *` \|<br/>\| Every Monday at 12 pm \| `0 12 * * MON` \|<br/>\| Every weekday (Mon — Fri) at 6 am \| `0 6 * * MON-FRI` \|<br/><br/>At this time you can only create monitors with limited schedules.<br/> |
| timezone | str  | ❌       | The monitor's [timezone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
