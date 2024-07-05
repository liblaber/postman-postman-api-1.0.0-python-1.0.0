# MocksService

A list of all methods in the `MocksService` service. Click on the method name to view detailed information about that method.

| Methods                 | Description                                                                                                   |
| :---------------------- | :------------------------------------------------------------------------------------------------------------ |
| [get_mocks](#get_mocks) | Gets all mock servers. By default, this endpoint returns only mock servers you created across all workspaces. |

**Note:**

If you pass both the `teamId` and `workspace` query parameters, this endpoint only accepts the `workspace` query.
|
|[create_mock](#create_mock)| Creates a mock server in a collection.

**Note:**

- If you do not include the `workspaceId` query parameter, the system creates the mock server in your [Personal
  workspace](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/creating-workspaces/).
- You cannot create mocks for collections added to an API definition.
  |
  |[get_mock](#get_mock)| Gets information about a mock server. |
  |[update_mock](#update_mock)| Updates a mock server. |
  |[delete_mock](#delete_mock)| Deletes a mock server. |
  |[get_mock_call_logs](#get_mock_call_logs)| Gets a mock server's call logs. You can get a maximum of 6.5MB of call logs or a total of 100 call logs, whichever limit is met first in one API call.

Call logs contain exchanged request and response data made to mock servers. The logs provide visibility into how the mock servers are being used. You can log data to debug, test, analyze, and more, depending upon the use case.
|
|[publish_mock](#publish_mock)| Publishes a mock server. Publishing a mock server sets its **Access Control** configuration setting to public. |
|[unpublish_mock](#unpublish_mock)| Unpublishes a mock server. Unpublishing a mock server sets its **Access Control** configuration setting to private. |
|[get_mock_server_responses](#get_mock_server_responses)| Gets all of a mock server's server responses. |
|[create_mock_server_response](#create_mock_server_response)| Creates a server response. Server responses let you simulate 5xx server-level responses, such as 500 or 503.

Server-level responses are agnostic to application-level logic. Server responses let you simulate this behavior on a mock server. You do not need to define each error for all exposed paths on the mock server.

If you set a server response as active, then all the calls to the mock server return with that active server response.

**Note:**

You can create multiple server responses for a mock server, but only one mock server can be set as active.
|
|[get_mock_server_response](#get_mock_server_response)| Gets information about a server response. |
|[update_mock_server_response](#update_mock_server_response)| Updates a server response. |
|[delete_mock_server_response](#delete_mock_server_response)| Deletes a mock server's server response. |

## get_mocks

Gets all mock servers. By default, this endpoint returns only mock servers you created across all workspaces.

**Note:**

If you pass both the `teamId` and `workspace` query parameters, this endpoint only accepts the `workspace` query.

- HTTP Method: `GET`
- Endpoint: `/mocks`

**Parameters**

| Name      | Type | Required | Description                                           |
| :-------- | :--- | :------- | :---------------------------------------------------- |
| team_id   | str  | ❌       | Return only results that belong to the given team ID. |
| workspace | str  | ❌       | Return only results found in the given workspace.     |

**Return Type**

`GetMocks`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.mocks.get_mocks(
    team_id="1b96f65f-8d23-4e1d-b5e2-055992c3b8cbd2567dfa09a9",
    workspace="1f0df51a-8658-4ee8-a2a1-d2567dfa09a9"
)

print(result)
```

## create_mock

Creates a mock server in a collection.

**Note:**

- If you do not include the `workspaceId` query parameter, the system creates the mock server in your [Personal
  workspace](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/creating-workspaces/).
- You cannot create mocks for collections added to an API definition.

- HTTP Method: `POST`
- Endpoint: `/mocks`

**Parameters**

| Name         | Type                                  | Required | Description         |
| :----------- | :------------------------------------ | :------- | :------------------ |
| request_body | [CreateMock](../models/CreateMock.md) | ✅       | The request body.   |
| workspace_id | str                                   | ❌       | The workspace's ID. |

**Return Type**

`MockCreateUpdate`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import CreateMock

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = CreateMock(
    mock={
        "collection": "12345678-12ece9e1-2abf-4edc-8e34-de66e74114d2",
        "environment": "12345678-5daabc50-8451-43f6-922d-96b403b4f28e",
        "name": "Test Mock",
        "private": True
    }
)

result = sdk.mocks.create_mock(
    request_body=request_body,
    workspace_id="1f0df51a-8658-4ee8-a2a1-d2567dfa09a9"
)

print(result)
```

## get_mock

Gets information about a mock server.

- HTTP Method: `GET`
- Endpoint: `/mocks/{mockId}`

**Parameters**

| Name    | Type | Required | Description    |
| :------ | :--- | :------- | :------------- |
| mock_id | str  | ✅       | The mock's ID. |

**Return Type**

`GetMock`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.mocks.get_mock(mock_id="e3d951bf-873f-49ac-a658-b2dcb91d3289")

print(result)
```

## update_mock

Updates a mock server.

- HTTP Method: `PUT`
- Endpoint: `/mocks/{mockId}`

**Parameters**

| Name         | Type                                  | Required | Description       |
| :----------- | :------------------------------------ | :------- | :---------------- |
| request_body | [UpdateMock](../models/UpdateMock.md) | ❌       | The request body. |
| mock_id      | str                                   | ✅       | The mock's ID.    |

**Return Type**

`MockCreateUpdate`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import UpdateMock

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = UpdateMock(
    mock={
        "name": "Test Mock",
        "environment": "12345678-5daabc50-8451-43f6-922d-96b403b4f28e",
        "description": "This is a test mock server.",
        "private": True,
        "version_tag": "abf07d3d-f8ec-47d4-8015-9fe83078b4ec",
        "config": {
            "server_response_id": "9a291bbe-dc0a-44ba-a3c8-6dbd06a61460"
        }
    }
)

result = sdk.mocks.update_mock(
    request_body=request_body,
    mock_id="e3d951bf-873f-49ac-a658-b2dcb91d3289"
)

print(result)
```

## delete_mock

Deletes a mock server.

- HTTP Method: `DELETE`
- Endpoint: `/mocks/{mockId}`

**Parameters**

| Name    | Type | Required | Description    |
| :------ | :--- | :------- | :------------- |
| mock_id | str  | ✅       | The mock's ID. |

**Return Type**

`DeleteMock`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.mocks.delete_mock(mock_id="e3d951bf-873f-49ac-a658-b2dcb91d3289")

print(result)
```

## get_mock_call_logs

Gets a mock server's call logs. You can get a maximum of 6.5MB of call logs or a total of 100 call logs, whichever limit is met first in one API call.

Call logs contain exchanged request and response data made to mock servers. The logs provide visibility into how the mock servers are being used. You can log data to debug, test, analyze, and more, depending upon the use case.

- HTTP Method: `GET`
- Endpoint: `/mocks/{mockId}/call-logs`

**Parameters**

| Name                 | Type                                                    | Required | Description                                                                                                                                                                                                                    |
| :------------------- | :------------------------------------------------------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| mock_id              | str                                                     | ✅       | The mock's ID.                                                                                                                                                                                                                 |
| limit                | float                                                   | ❌       | The maximum number of rows to return in the response.                                                                                                                                                                          |
| cursor               | str                                                     | ❌       | The pointer to the first record of the set of paginated results. To view the next response, use the `nextCursor` value for this parameter.                                                                                     |
| until                | str                                                     | ❌       | Return only results created until this given time, in [ISO 8601](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) format. This value cannot be earlier than the `since` value.                                       |
| since                | str                                                     | ❌       | Return only results created since the given time, in [ISO 8601](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) format. This value cannot be later than the `until` value.                                          |
| response_status_code | float                                                   | ❌       | Return only call logs that match the given HTTP response status code.                                                                                                                                                          |
| response_type        | str                                                     | ❌       | Return only call logs that match the given response type. Matching is not case-sensitive.                                                                                                                                      |
| request_method       | str                                                     | ❌       | Return only call logs that match the given HTTP method. Matching is not case-sensitive.                                                                                                                                        |
| request_path         | str                                                     | ❌       | Return only call logs that match the given request path. Matching is not case-sensitive.                                                                                                                                       |
| sort                 | [GetMockCallLogsSort](../models/GetMockCallLogsSort.md) | ❌       | Sort the results by the given value. If you use this query parameter, you must also use the `direction` parameter.                                                                                                             |
| direction            | [AscDesc](../models/AscDesc.md)                         | ❌       | Sort in ascending (`asc`) or descending (`desc`) order. Matching is not case-sensitive. If you use this query parameter, you must also use the `sort` parameter.                                                               |
| include              | str                                                     | ❌       | Include call log records with header and body data. This query parameter accepts the `request.headers`, `request.body`, `response.headers`, and `response.body` values. For multiple include types, comma-separate each value. |

**Return Type**

`GetMockCallLogs`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import GetMockCallLogsSort, AscDesc

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.mocks.get_mock_call_logs(
    mock_id="e3d951bf-873f-49ac-a658-b2dcb91d3289",
    limit=3,
    cursor="RnJpIEZlYiAyNCAyMDIzIDEzOjI0OjA5IEdNVCswMDAwIChDb29yZGluYXRlZCBVbml2ZXJzYWwgVGltZSk=",
    until="2022-06-15T00:00:00.000Z",
    since="2022-06-01T00:00:00.000Z",
    response_status_code=500,
    response_type="success",
    request_method="post",
    request_path="/animals?type=Dog",
    sort="servedAt",
    direction="asc",
    include="request.headers,request.body,response.headers,response.body"
)

print(result)
```

## publish_mock

Publishes a mock server. Publishing a mock server sets its **Access Control** configuration setting to public.

- HTTP Method: `POST`
- Endpoint: `/mocks/{mockId}/publish`

**Parameters**

| Name    | Type | Required | Description    |
| :------ | :--- | :------- | :------------- |
| mock_id | str  | ✅       | The mock's ID. |

**Return Type**

`PublishMock`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.mocks.publish_mock(mock_id="e3d951bf-873f-49ac-a658-b2dcb91d3289")

print(result)
```

## unpublish_mock

Unpublishes a mock server. Unpublishing a mock server sets its **Access Control** configuration setting to private.

- HTTP Method: `DELETE`
- Endpoint: `/mocks/{mockId}/unpublish`

**Parameters**

| Name    | Type | Required | Description    |
| :------ | :--- | :------- | :------------- |
| mock_id | str  | ✅       | The mock's ID. |

**Return Type**

`UnpublishMock`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.mocks.unpublish_mock(mock_id="e3d951bf-873f-49ac-a658-b2dcb91d3289")

print(result)
```

## get_mock_server_responses

Gets all of a mock server's server responses.

- HTTP Method: `GET`
- Endpoint: `/mocks/{mockId}/server-responses`

**Parameters**

| Name    | Type | Required | Description    |
| :------ | :--- | :------- | :------------- |
| mock_id | str  | ✅       | The mock's ID. |

**Return Type**

`List[GetMockServerResponses]`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.mocks.get_mock_server_responses(mock_id="e3d951bf-873f-49ac-a658-b2dcb91d3289")

print(result)
```

## create_mock_server_response

Creates a server response. Server responses let you simulate 5xx server-level responses, such as 500 or 503.

Server-level responses are agnostic to application-level logic. Server responses let you simulate this behavior on a mock server. You do not need to define each error for all exposed paths on the mock server.

If you set a server response as active, then all the calls to the mock server return with that active server response.

**Note:**

You can create multiple server responses for a mock server, but only one mock server can be set as active.

- HTTP Method: `POST`
- Endpoint: `/mocks/{mockId}/server-responses`

**Parameters**

| Name         | Type                                                              | Required | Description       |
| :----------- | :---------------------------------------------------------------- | :------- | :---------------- |
| request_body | [CreateMockServerResponse](../models/CreateMockServerResponse.md) | ✅       | The request body. |
| mock_id      | str                                                               | ✅       | The mock's ID.    |

**Return Type**

`dict`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import CreateMockServerResponse

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = CreateMockServerResponse(
    server_response={
        "name": "Internal Server Error",
        "status_code": 500,
        "headers": [
            {
                "key": "Content-Type",
                "value": "application/json"
            }
        ],
        "language": "text",
        "body": "{\n    \"message\": \"Something went wrong; try again later.\"\n}"
    }
)

result = sdk.mocks.create_mock_server_response(
    request_body=request_body,
    mock_id="e3d951bf-873f-49ac-a658-b2dcb91d3289"
)

print(result)
```

## get_mock_server_response

Gets information about a server response.

- HTTP Method: `GET`
- Endpoint: `/mocks/{mockId}/server-responses/{serverResponseId}`

**Parameters**

| Name               | Type | Required | Description               |
| :----------------- | :--- | :------- | :------------------------ |
| mock_id            | str  | ✅       | The mock's ID.            |
| server_response_id | str  | ✅       | The server response's ID. |

**Return Type**

`dict`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.mocks.get_mock_server_response(
    mock_id="e3d951bf-873f-49ac-a658-b2dcb91d3289",
    server_response_id="965cdd16-fe22-4d96-a161-3d05490ac421"
)

print(result)
```

## update_mock_server_response

Updates a server response.

- HTTP Method: `PUT`
- Endpoint: `/mocks/{mockId}/server-responses/{serverResponseId}`

**Parameters**

| Name               | Type                                                              | Required | Description               |
| :----------------- | :---------------------------------------------------------------- | :------- | :------------------------ |
| request_body       | [UpdateMockServerResponse](../models/UpdateMockServerResponse.md) | ✅       | The request body.         |
| mock_id            | str                                                               | ✅       | The mock's ID.            |
| server_response_id | str                                                               | ✅       | The server response's ID. |

**Return Type**

`dict`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import UpdateMockServerResponse

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = UpdateMockServerResponse(
    server_response={
        "name": "Internal Server Error",
        "status_code": 500,
        "headers": [
            {
                "key": "Content-Type",
                "value": "application/json"
            }
        ],
        "language": "text",
        "body": "{\n    \"message\": \"Something went wrong; try again later.\"\n}"
    }
)

result = sdk.mocks.update_mock_server_response(
    request_body=request_body,
    mock_id="e3d951bf-873f-49ac-a658-b2dcb91d3289",
    server_response_id="965cdd16-fe22-4d96-a161-3d05490ac421"
)

print(result)
```

## delete_mock_server_response

Deletes a mock server's server response.

- HTTP Method: `DELETE`
- Endpoint: `/mocks/{mockId}/server-responses/{serverResponseId}`

**Parameters**

| Name               | Type | Required | Description               |
| :----------------- | :--- | :------- | :------------------------ |
| mock_id            | str  | ✅       | The mock's ID.            |
| server_response_id | str  | ✅       | The server response's ID. |

**Return Type**

`DeleteMockServerResponse`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.mocks.delete_mock_server_response(
    mock_id="e3d951bf-873f-49ac-a658-b2dcb91d3289",
    server_response_id="965cdd16-fe22-4d96-a161-3d05490ac421"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
