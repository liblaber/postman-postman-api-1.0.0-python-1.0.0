# GetStatusOfAnAsyncTaskOkResponse

**Properties**

| Name       | Type                                   | Required | Description                                           |
| :--------- | :------------------------------------- | :------- | :---------------------------------------------------- |
| id\_       | str                                    | ❌       | The task's ID.                                        |
| meta       | GetStatusOfAnAsyncTaskOkResponseMeta   | ❌       | The response's non-standard meta information.         |
| status     | GetStatusOfAnAsyncTaskOkResponseStatus | ❌       | The task's current status.                            |
| details    | Details                                | ❌       |                                                       |
| created_at | str                                    | ❌       | The date and time at which the task was created.      |
| updated_at | str                                    | ❌       | The date and time at which the task was last updated. |

# GetStatusOfAnAsyncTaskOkResponseMeta

The response's non-standard meta information.

**Properties**

| Name   | Type      | Required | Description                                               |
| :----- | :-------- | :------- | :-------------------------------------------------------- |
| url    | str       | ❌       | The endpoint URL that created the task.                   |
| model  | MetaModel | ❌       | The model for which the task is performing the operation. |
| action | Action    | ❌       | The task's action.                                        |

# MetaModel

The model for which the task is performing the operation.

**Properties**

| Name        | Type | Required | Description   |
| :---------- | :--- | :------- | :------------ |
| COLLECTION  | str  | ✅       | "collection"  |
| API_VERSION | str  | ✅       | "api-version" |

# Action

The task's action.

**Properties**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| UPDATE | str  | ✅       | "update"    |
| CREATE | str  | ✅       | "create"    |

# GetStatusOfAnAsyncTaskOkResponseStatus

The task's current status.

**Properties**

| Name      | Type | Required | Description |
| :-------- | :--- | :------- | :---------- |
| PENDING   | str  | ✅       | "pending"   |
| FAILED    | str  | ✅       | "failed"    |
| COMPLETED | str  | ✅       | "completed" |

# Details

# Details_1

Information about the task's resources.

**Properties**

| Name      | Type            | Required | Description |
| :-------- | :-------------- | :------- | :---------- |
| resources | List[Resources] | ❌       |             |

# Resources

**Properties**

| Name | Type | Required | Description                       |
| :--- | :--- | :------- | :-------------------------------- |
| id\_ | str  | ❌       | The ID of the assigned resource.  |
| url  | str  | ❌       | The task's assigned resource URL. |

# Details_2

Information about the error that occurred during the task's processing.

**Properties**

| Name  | Type  | Required | Description |
| :---- | :---- | :------- | :---------- |
| error | Error | ❌       |             |

# Error

**Properties**

| Name    | Type | Required | Description               |
| :------ | :--- | :------- | :------------------------ |
| message | str  | ❌       | The task's error message. |
