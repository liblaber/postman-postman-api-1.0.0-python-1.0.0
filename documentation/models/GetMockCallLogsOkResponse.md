# GetMockCallLogsOkResponse

**Properties**

| Name      | Type                          | Required | Description                                   |
| :-------- | :---------------------------- | :------- | :-------------------------------------------- |
| call_logs | List[CallLogs]                | ❌       |                                               |
| meta      | GetMockCallLogsOkResponseMeta | ❌       | The response's non-standard meta information. |

# CallLogs

Information about the mock server's server responses.

**Properties**

| Name          | Type             | Required | Description                                                |
| :------------ | :--------------- | :------- | :--------------------------------------------------------- |
| id\_          | str              | ❌       | The server response's ID.                                  |
| response_name | str              | ❌       | The server response's name.                                |
| served_at     | str              | ❌       | The date and time at which the server response was served. |
| request       | CallLogsRequest  | ❌       | The server response's request information.                 |
| response      | CallLogsResponse | ❌       | The server response's response information.                |

# CallLogsRequest

The server response's request information.

**Properties**

| Name    | Type           | Required | Description                     |
| :------ | :------------- | :------- | :------------------------------ |
| method  | str            | ❌       | The request method.             |
| path    | str            | ❌       | The request's path.             |
| headers | RequestHeaders | ❌       | The request's headers.          |
| body    | RequestBody    | ❌       | The request's body information. |

# RequestHeaders

The request's headers.

**Properties**

| Name  | Type | Required | Description                 |
| :---- | :--- | :------- | :-------------------------- |
| key   | str  | ❌       | The request header's name.  |
| value | str  | ❌       | The request header's value. |

# RequestBody

The request's body information.

**Properties**

| Name | Type | Required | Description                           |
| :--- | :--- | :------- | :------------------------------------ |
| mode | str  | ❌       | The request body's media type (mode). |
| data | str  | ❌       | The request body's contents.          |

# CallLogsResponse

The server response's response information.

**Properties**

| Name        | Type            | Required | Description                      |
| :---------- | :-------------- | :------- | :------------------------------- |
| type\_      | str             | ❌       | The type of response.            |
| status_code | float           | ❌       | The response's status code.      |
| headers     | ResponseHeaders | ❌       | The response's headers.          |
| body        | ResponseBody    | ❌       | The response's body information. |

# ResponseHeaders

The response's headers.

**Properties**

| Name        | Type        | Required | Description                                    |
| :---------- | :---------- | :------- | :--------------------------------------------- |
| description | Description | ❌       | The response header's description information. |
| key         | str         | ❌       | The response header's name.                    |
| value       | str         | ❌       | The response header's value.                   |

# Description

The response header's description information.

**Properties**

| Name    | Type | Required | Description                                   |
| :------ | :--- | :------- | :-------------------------------------------- |
| content | str  | ❌       | The response header description's content.    |
| type\_  | str  | ❌       | The response header description's media type. |

# ResponseBody

The response's body information.

**Properties**

| Name | Type | Required | Description                   |
| :--- | :--- | :------- | :---------------------------- |
| data | str  | ❌       | The response body's contents. |

# GetMockCallLogsOkResponseMeta

The response's non-standard meta information.

**Properties**

| Name        | Type | Required | Description                                                              |
| :---------- | :--- | :------- | :----------------------------------------------------------------------- |
| next_cursor | str  | ❌       | The pagination cursor that points to the next record in the results set. |
