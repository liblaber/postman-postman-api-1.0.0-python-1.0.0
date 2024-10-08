# EnvironmentsService

A list of all methods in the `EnvironmentsService` service. Click on the method name to view detailed information about that method.

| Methods                                           | Description                                                                                                                                                                                                                |
| :------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [get_environments](#get_environments)             | Gets information about all of your [environments](https://learning.postman.com/docs/sending-requests/managing-environments/).                                                                                              |
| [create_environment](#create_environment)         | Creates an environment.                                                                                                                                                                                                    |
| [get_environment](#get_environment)               | Gets information about an environment.                                                                                                                                                                                     |
| [update_environment](#update_environment)         | Updates an environment.                                                                                                                                                                                                    |
| [delete_environment](#delete_environment)         | Deletes an environment.                                                                                                                                                                                                    |
| [get_environment_forks](#get_environment_forks)   | Gets all of an environment's forked environments.                                                                                                                                                                          |
| [fork_environment](#fork_environment)             | Creates a [fork](https://learning.postman.com/docs/collaborating-in-postman/using-version-control/forking-elements/) of an existing environment.                                                                           |
| [merge_environment_fork](#merge_environment_fork) | [Merges](https://learning.postman.com/docs/collaborating-in-postman/using-version-control/forking-elements/#merge-changes-from-a-fork) a forked environment back into its parent environment.                              |
| [pull_environment](#pull_environment)             | [Pulls](https://learning.postman.com/docs/collaborating-in-postman/using-version-control/forking-elements/#pull-updates-from-a-parent-element) the changes from a parent (source) environment into the forked environment. |

## get_environments

Gets information about all of your [environments](https://learning.postman.com/docs/sending-requests/managing-environments/).

- HTTP Method: `GET`
- Endpoint: `/environments`

**Parameters**

| Name      | Type | Required | Description         |
| :-------- | :--- | :------- | :------------------ |
| workspace | str  | ❌       | The workspace's ID. |

**Return Type**

`GetEnvironments`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.environments.get_environments(workspace="1f0df51a-8658-4ee8-a2a1-d2567dfa09a9")

print(result)
```

## create_environment

Creates an environment.

- HTTP Method: `POST`
- Endpoint: `/environments`

**Parameters**

| Name         | Type                                                              | Required | Description         |
| :----------- | :---------------------------------------------------------------- | :------- | :------------------ |
| request_body | [CreateEnvironmentRequest](../models/CreateEnvironmentRequest.md) | ❌       | The request body.   |
| workspace    | str                                                               | ❌       | The workspace's ID. |

**Return Type**

`CreateEnvironmentOkResponse`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import CreateEnvironmentRequest

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = CreateEnvironmentRequest(
    environment={
        "name": "Test Environment",
        "values": [
            {
                "enabled": True,
                "key": "apiKey",
                "value": "PMAK-XXX",
                "type_": "secret"
            }
        ]
    }
)

result = sdk.environments.create_environment(
    request_body=request_body,
    workspace="1f0df51a-8658-4ee8-a2a1-d2567dfa09a9"
)

print(result)
```

## get_environment

Gets information about an environment.

- HTTP Method: `GET`
- Endpoint: `/environments/{environmentId}`

**Parameters**

| Name           | Type | Required | Description           |
| :------------- | :--- | :------- | :-------------------- |
| environment_id | str  | ✅       | The environment's ID. |

**Return Type**

`GetEnvironment`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.environments.get_environment(environment_id="5daabc50-8451-43f6-922d-96b403b4f28e")

print(result)
```

## update_environment

Updates an environment.

- HTTP Method: `PUT`
- Endpoint: `/environments/{environmentId}`

**Parameters**

| Name           | Type                                                              | Required | Description           |
| :------------- | :---------------------------------------------------------------- | :------- | :-------------------- |
| request_body   | [UpdateEnvironmentRequest](../models/UpdateEnvironmentRequest.md) | ❌       | The request body.     |
| environment_id | str                                                               | ✅       | The environment's ID. |

**Return Type**

`UpdateEnvironmentOkResponse`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import UpdateEnvironmentRequest

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = UpdateEnvironmentRequest(
    environment={
        "name": "Test Environment",
        "values": [
            {
                "enabled": True,
                "key": "apiKey",
                "value": "PMAK-XXX",
                "type_": "secret"
            }
        ]
    }
)

result = sdk.environments.update_environment(
    request_body=request_body,
    environment_id="5daabc50-8451-43f6-922d-96b403b4f28e"
)

print(result)
```

## delete_environment

Deletes an environment.

- HTTP Method: `DELETE`
- Endpoint: `/environments/{environmentId}`

**Parameters**

| Name           | Type | Required | Description           |
| :------------- | :--- | :------- | :-------------------- |
| environment_id | str  | ✅       | The environment's ID. |

**Return Type**

`DeleteEnvironment`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.environments.delete_environment(environment_id="5daabc50-8451-43f6-922d-96b403b4f28e")

print(result)
```

## get_environment_forks

Gets all of an environment's forked environments.

- HTTP Method: `GET`
- Endpoint: `/environments/{environmentId}/forks`

**Parameters**

| Name           | Type                                                            | Required | Description                                                                                                                                |
| :------------- | :-------------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| environment_id | str                                                             | ✅       | The environment's unique ID.                                                                                                               |
| cursor         | str                                                             | ❌       | The pointer to the first record of the set of paginated results. To view the next response, use the `nextCursor` value for this parameter. |
| direction      | [AscDesc](../models/AscDesc.md)                                 | ❌       | Sort results in ascending (`asc`) or descending (`desc`) order.                                                                            |
| limit          | int                                                             | ❌       | The maximum number of rows to return in the response.                                                                                      |
| sort           | [GetEnvironmentForksSort](../models/GetEnvironmentForksSort.md) | ❌       | Sort the results by the date and time of creation.                                                                                         |

**Return Type**

`GetEnvironmentForks`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import AscDesc, GetEnvironmentForksSort

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.environments.get_environment_forks(
    environment_id="12345678-12ece9e1-2abf-4edc-8e34-de66e74114d2",
    cursor="RnJpIEZlYiAyNCAyMDIzIDEzOjI0OjA5IEdNVCswMDAwIChDb29yZGluYXRlZCBVbml2ZXJzYWwgVGltZSk=",
    direction="asc",
    limit=10,
    sort="createdAt"
)

print(result)
```

## fork_environment

Creates a [fork](https://learning.postman.com/docs/collaborating-in-postman/using-version-control/forking-elements/) of an existing environment.

- HTTP Method: `POST`
- Endpoint: `/environments/{environmentId}/forks`

**Parameters**

| Name           | Type                                                          | Required | Description                  |
| :------------- | :------------------------------------------------------------ | :------- | :--------------------------- |
| request_body   | [ForkEnvironmentRequest](../models/ForkEnvironmentRequest.md) | ❌       | The request body.            |
| environment_id | str                                                           | ✅       | The environment's unique ID. |
| workspace_id   | str                                                           | ✅       | The workspace's ID.          |

**Return Type**

`ForkEnvironmentOkResponse`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import ForkEnvironmentRequest

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = ForkEnvironmentRequest(
    fork_name="My fork"
)

result = sdk.environments.fork_environment(
    request_body=request_body,
    environment_id="12345678-12ece9e1-2abf-4edc-8e34-de66e74114d2",
    workspace_id="1f0df51a-8658-4ee8-a2a1-d2567dfa09a9"
)

print(result)
```

## merge_environment_fork

[Merges](https://learning.postman.com/docs/collaborating-in-postman/using-version-control/forking-elements/#merge-changes-from-a-fork) a forked environment back into its parent environment.

- HTTP Method: `POST`
- Endpoint: `/environments/{environmentId}/merges`

**Parameters**

| Name           | Type                                                                    | Required | Description                  |
| :------------- | :---------------------------------------------------------------------- | :------- | :--------------------------- |
| request_body   | [MergeEnvironmentForkRequest](../models/MergeEnvironmentForkRequest.md) | ❌       | The request body.            |
| environment_id | str                                                                     | ✅       | The environment's unique ID. |

**Return Type**

`MergeEnvironmentForkOkResponse`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import MergeEnvironmentForkRequest

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = MergeEnvironmentForkRequest(
    source="12345678-d9c7dc8f-904e-4bba-99b5-4d490aae1957",
    delete_source=True
)

result = sdk.environments.merge_environment_fork(
    request_body=request_body,
    environment_id="12345678-12ece9e1-2abf-4edc-8e34-de66e74114d2"
)

print(result)
```

## pull_environment

[Pulls](https://learning.postman.com/docs/collaborating-in-postman/using-version-control/forking-elements/#pull-updates-from-a-parent-element) the changes from a parent (source) environment into the forked environment.

- HTTP Method: `POST`
- Endpoint: `/environments/{environmentId}/pulls`

**Parameters**

| Name           | Type                                                          | Required | Description                  |
| :------------- | :------------------------------------------------------------ | :------- | :--------------------------- |
| request_body   | [PullEnvironmentRequest](../models/PullEnvironmentRequest.md) | ❌       | The request body.            |
| environment_id | str                                                           | ✅       | The environment's unique ID. |

**Return Type**

`PullEnvironmentOkResponse`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import PullEnvironmentRequest

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = PullEnvironmentRequest(
    source="12345678-d9c7dc8f-904e-4bba-99b5-4d490aae1957"
)

result = sdk.environments.pull_environment(
    request_body=request_body,
    environment_id="12345678-12ece9e1-2abf-4edc-8e34-de66e74114d2"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
