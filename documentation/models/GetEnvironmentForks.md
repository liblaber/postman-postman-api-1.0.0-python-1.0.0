# GetEnvironmentForks

**Properties**

| Name | Type                          | Required | Description                                            |
| :--- | :---------------------------- | :------- | :----------------------------------------------------- |
| data | List[GetEnvironmentForksData] | ❌       | A list of the environment's forks.                     |
| meta | GetEnvironmentForksMeta       | ❌       | The response's meta information for paginated results. |

# GetEnvironmentForksData

Information about the forked environment.

**Properties**

| Name       | Type | Required | Description                                           |
| :--------- | :--- | :------- | :---------------------------------------------------- |
| fork_id    | str  | ❌       | The forked environment's unique ID.                   |
| fork_name  | str  | ❌       | The forked environment's label.                       |
| created_at | str  | ❌       | The date and time at which the fork was created.      |
| created_by | str  | ❌       | The user who created the environment fork.            |
| updated_at | str  | ❌       | The date and time at which the fork was last updated. |

# GetEnvironmentForksMeta

The response's meta information for paginated results.

**Properties**

| Name        | Type  | Required | Description                                                              |
| :---------- | :---- | :------- | :----------------------------------------------------------------------- |
| total       | float | ❌       | The total number of forked environments.                                 |
| next_cursor | str   | ❌       | The pagination cursor that points to the next record in the results set. |

<!-- This file was generated by liblab | https://liblab.com/ -->
