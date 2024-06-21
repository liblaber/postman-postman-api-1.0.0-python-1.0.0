# UpdateMockServerResponseRequest

**Properties**

| Name            | Type                                          | Required | Description |
| :-------------- | :-------------------------------------------- | :------- | :---------- |
| server_response | UpdateMockServerResponseRequestServerResponse | ❌       |             |

# UpdateMockServerResponseRequestServerResponse

**Properties**

| Name        | Type                         | Required | Description                                                                                           |
| :---------- | :--------------------------- | :------- | :---------------------------------------------------------------------------------------------------- |
| name        | str                          | ❌       | The server response's name.                                                                           |
| status_code | int                          | ❌       | The server response's 5xx HTTP response code. This property only accepts 5xx values.                  |
| headers     | List[ServerResponseHeaders2] | ❌       | The server response's request headers, such as Content-Type, Accept, encoding, and other information. |
| language    | ServerResponseLanguage2      | ❌       | The server response's body language type.                                                             |
| body        | str                          | ❌       | The server response's body that returns when calling the mock server.                                 |

# ServerResponseHeaders_2

Information about they key-value pair.

**Properties**

| Name  | Type | Required | Description                     |
| :---- | :--- | :------- | :------------------------------ |
| key   | str  | ❌       | The request header's key value. |
| value | str  | ❌       | The request header's value.     |

# ServerResponseLanguage_2

The server response's body language type.

**Properties**

| Name       | Type | Required | Description  |
| :--------- | :--- | :------- | :----------- |
| TEXT       | str  | ✅       | "text"       |
| JAVASCRIPT | str  | ✅       | "javascript" |
| JSON       | str  | ✅       | "json"       |
| HTML       | str  | ✅       | "html"       |
| XML        | str  | ✅       | "xml"        |
