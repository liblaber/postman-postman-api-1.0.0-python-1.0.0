# MonitorsService

A list of all methods in the `MonitorsService` service. Click on the method name to view detailed information about that method.

| Methods                           | Description        |
| :-------------------------------- | :----------------- |
| [get_monitors](#get_monitors)     | Gets all monitors. |
| [create_monitor](#create_monitor) | Creates a monitor. |

**Note:**

You cannot create monitors for collections added to an API definition.
|
|[get_monitor](#get_monitor)| Gets information about a monitor. |
|[update_monitor](#update_monitor)| Updates a monitor. |
|[delete_monitor](#delete_monitor)| Deletes a monitor. |
|[run_monitor](#run_monitor)| Runs a monitor and returns its run results. |

## get_monitors

Gets all monitors.

- HTTP Method: `GET`
- Endpoint: `/monitors`

**Parameters**

| Name      | Type | Required | Description                                       |
| :-------- | :--- | :------- | :------------------------------------------------ |
| workspace | str  | ❌       | Return only results found in the given workspace. |

**Return Type**

`GetMonitors`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.monitors.get_monitors(workspace="1f0df51a-8658-4ee8-a2a1-d2567dfa09a9")

print(result)
```

## create_monitor

Creates a monitor.

**Note:**

You cannot create monitors for collections added to an API definition.

- HTTP Method: `POST`
- Endpoint: `/monitors`

**Parameters**

| Name         | Type                                                      | Required | Description         |
| :----------- | :-------------------------------------------------------- | :------- | :------------------ |
| request_body | [CreateMonitorRequest](../models/CreateMonitorRequest.md) | ❌       | The request body.   |
| workspace    | str                                                       | ❌       | The workspace's ID. |

**Return Type**

`CreateMonitorOkResponse`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import CreateMonitorRequest

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = CreateMonitorRequest(
    monitor={
        "collection": "12345678-12ece9e1-2abf-4edc-8e34-de66e74114d2",
        "environment": "12345678-5daabc50-8451-43f6-922d-96b403b4f28e",
        "name": "Test Monitor",
        "schedule": {
            "cron": "0 0 * * *",
            "timezone": "America/Chicago"
        }
    }
)

result = sdk.monitors.create_monitor(
    request_body=request_body,
    workspace="1f0df51a-8658-4ee8-a2a1-d2567dfa09a9"
)

print(result)
```

## get_monitor

Gets information about a monitor.

- HTTP Method: `GET`
- Endpoint: `/monitors/{monitorId}`

**Parameters**

| Name       | Type | Required | Description       |
| :--------- | :--- | :------- | :---------------- |
| monitor_id | str  | ✅       | The monitor's ID. |

**Return Type**

`GetMonitor`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.monitors.get_monitor(monitor_id="1e6b6cc1-c760-48e0-968f-4bfaeeae9af1")

print(result)
```

## update_monitor

Updates a monitor.

- HTTP Method: `PUT`
- Endpoint: `/monitors/{monitorId}`

**Parameters**

| Name         | Type                                                      | Required | Description       |
| :----------- | :-------------------------------------------------------- | :------- | :---------------- |
| request_body | [UpdateMonitorRequest](../models/UpdateMonitorRequest.md) | ❌       | The request body. |
| monitor_id   | str                                                       | ✅       | The monitor's ID. |

**Return Type**

`UpdateMonitorOkResponse`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import UpdateMonitorRequest

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = UpdateMonitorRequest(
    monitor={
        "name": "Test Monitor",
        "schedule": {
            "cron": "*/5 * * * *",
            "timezone": "America/Chicago"
        }
    }
)

result = sdk.monitors.update_monitor(
    request_body=request_body,
    monitor_id="1e6b6cc1-c760-48e0-968f-4bfaeeae9af1"
)

print(result)
```

## delete_monitor

Deletes a monitor.

- HTTP Method: `DELETE`
- Endpoint: `/monitors/{monitorId}`

**Parameters**

| Name       | Type | Required | Description       |
| :--------- | :--- | :------- | :---------------- |
| monitor_id | str  | ✅       | The monitor's ID. |

**Return Type**

`DeleteMonitor`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.monitors.delete_monitor(monitor_id="1e6b6cc1-c760-48e0-968f-4bfaeeae9af1")

print(result)
```

## run_monitor

Runs a monitor and returns its run results.

- HTTP Method: `POST`
- Endpoint: `/monitors/{monitorId}/run`

**Parameters**

| Name       | Type | Required | Description       |
| :--------- | :--- | :------- | :---------------- |
| monitor_id | str  | ✅       | The monitor's ID. |

**Return Type**

`RunMonitor`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.monitors.run_monitor(monitor_id="1e6b6cc1-c760-48e0-968f-4bfaeeae9af1")

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
