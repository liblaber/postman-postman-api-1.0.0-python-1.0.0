# WorkspacesService

A list of all methods in the `WorkspacesService` service. Click on the method name to view detailed information about that method.

| Methods                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| :---------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [get_workspaces](#get_workspaces)                                       | Gets all [workspaces](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/creating-workspaces/). The response includes your workspaces and any workspaces that you have access to. **Note:** This endpoint's response contains the visibility field. Visibility determines who can access the workspace: - `personal` — Only you can access the workspace. - `team` — All team members can access the workspace. - `private` — Only invited team members can access the workspace ([**Professional** and **Enterprise** plans only](https://www.postman.com/pricing)). - `public` — Everyone can access the workspace. - `partner` — Only invited team members and [partners](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/partner-workspaces/) can access the workspace ([**Professional** and **Enterprise** plans only](https://www.postman.com/pricing)).                                                                                                                                  |
| [create_workspace](#create_workspace)                                   | Creates a new [workspace](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/creating-workspaces/). **Note:** This endpoint returns a 403 `Forbidden` response if the user does not have permission to create workspaces. [Admins and Super Admins](https://learning.postman.com/docs/collaborating-in-postman/roles-and-permissions/#team-roles) can configure workspace permissions to restrict users and/or user groups from creating workspaces or require approvals for the creation of team workspaces. ### Important We deprecated linking collections or environments between workspaces. We do not recommend that you do this. If you have a linked collection or environment, note the following: - The endpoint does not create a clone of a collection or environment. - Any changes you make to a linked collection or environment changes them in all workspaces. - If you delete a collection or environment linked between workspaces, the system deletes it in all the workspaces.                          |
| [get_workspace_roles](#get_workspace_roles)                             | Gets information about all roles in a workspace, based on the team's [plan](https://www.postman.com/pricing/).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [get_workspace](#get_workspace)                                         | Gets information about a workspace. **Note:** This endpoint's response contains the `visibility` field. [Visibility](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/managing-workspaces/#changing-workspace-visibility) determines who can access the workspace: - `personal` — Only you can access the workspace. - `team` — All team members can access the workspace. - `private` — Only invited team members can access the workspace ([**Professional** and **Enterprise** plans only](https://www.postman.com/pricing)). - `public` — Everyone can access the workspace. - `partner` — Only invited team members and [partners](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/partner-workspaces/) can access the workspace ([**Professional** and **Enterprise** plans only](https://www.postman.com/pricing)). ### Important We have deprecated the `name` and `uid` responses in the following array of objects: - `collections` - `environments` - `mocks` - `monitors` - `apis` |
| [update_workspace](#update_workspace)                                   | Updates a workspace. ### Important We deprecated linking collections or environments between workspaces. We do not recommend that you do this. If you have a linked collection or environment, note the following: - The endpoint does not create a clone of a collection or environment. - Any changes you make to a linked collection or environment changes them in all workspaces. - If you delete a collection or environment linked between workspaces, the system deletes it in all the workspaces.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [delete_workspace](#delete_workspace)                                   | Deletes an existing workspace. ### Important If you delete a workspace that has a linked collection or environment with another workspace, this will delete the collection and environment in all workspaces.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [get_workspace_global_variables](#get_workspace_global_variables)       | Gets a workspace's global [variables](https://learning.postman.com/docs/sending-requests/variables/#variable-scopes).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [update_workspace_global_variables](#update_workspace_global_variables) | Updates and replaces a workspace's global [variables](https://learning.postman.com/docs/sending-requests/variables/#variable-scopes). This endpoint replaces all existing global variables with the variables you pass in the request body.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [update_workspace_roles](#update_workspace_roles)                       | Updates the roles of [users](https://learning.postman.com/docs/collaborating-in-postman/roles-and-permissions/#team-roles) or [user groups](https://learning.postman.com/docs/collaborating-in-postman/user-groups/) in a workspace. To get a list of roles, use the `GET /workspace-roles` endpoint. **Note:** - This endpoint does not support the external [Partner or Guest roles](https://learning.postman.com/docs/collaborating-in-postman/roles-and-permissions/#team-roles). - This endpoint is restricted to 50 operations per call. - The request body must contain one unique action per user or user group. For example, you cannot add and remove multiple roles for a user in the same request body.                                                                                                                                                                                                                                                                                                                                   |

## get_workspaces

Gets all [workspaces](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/creating-workspaces/). The response includes your workspaces and any workspaces that you have access to. **Note:** This endpoint's response contains the visibility field. Visibility determines who can access the workspace: - `personal` — Only you can access the workspace. - `team` — All team members can access the workspace. - `private` — Only invited team members can access the workspace ([**Professional** and **Enterprise** plans only](https://www.postman.com/pricing)). - `public` — Everyone can access the workspace. - `partner` — Only invited team members and [partners](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/partner-workspaces/) can access the workspace ([**Professional** and **Enterprise** plans only](https://www.postman.com/pricing)).

- HTTP Method: `GET`
- Endpoint: `/workspaces`

**Parameters**

| Name       | Type                                                      | Required | Description                                                                                                                                                                                    |
| :--------- | :-------------------------------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| type\_     | [GetWorkspacesType](../models/GetWorkspacesType.md)       | ❌       | The type of workspace to filter the response by.                                                                                                                                               |
| created_by | int                                                       | ❌       | Return only workspaces created by a specific user ID. For multiple users, pass this value as a comma-separated list of user IDs. The response only returns workspaces that you have access to. |
| include    | [GetWorkspacesInclude](../models/GetWorkspacesInclude.md) | ❌       | Include the following information in the endpoint's response: - `mocks:deactivated` — Include all deactivated mock servers in the response.                                                    |

**Return Type**

`GetWorkspaces`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import GetWorkspacesType, GetWorkspacesInclude

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.workspaces.get_workspaces(
    type_="personal",
    created_by=12345678,
    include="mocks:deactivated"
)

print(result)
```

## create_workspace

Creates a new [workspace](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/creating-workspaces/). **Note:** This endpoint returns a 403 `Forbidden` response if the user does not have permission to create workspaces. [Admins and Super Admins](https://learning.postman.com/docs/collaborating-in-postman/roles-and-permissions/#team-roles) can configure workspace permissions to restrict users and/or user groups from creating workspaces or require approvals for the creation of team workspaces. ### Important We deprecated linking collections or environments between workspaces. We do not recommend that you do this. If you have a linked collection or environment, note the following: - The endpoint does not create a clone of a collection or environment. - Any changes you make to a linked collection or environment changes them in all workspaces. - If you delete a collection or environment linked between workspaces, the system deletes it in all the workspaces.

- HTTP Method: `POST`
- Endpoint: `/workspaces`

**Parameters**

| Name         | Type                                                          | Required | Description       |
| :----------- | :------------------------------------------------------------ | :------- | :---------------- |
| request_body | [CreateWorkspaceRequest](../models/CreateWorkspaceRequest.md) | ❌       | The request body. |

**Return Type**

`CreateWorkspaceOkResponse`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import CreateWorkspaceRequest

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = CreateWorkspaceRequest(
    workspace={
        "name": "Team Workspace",
        "type_": "personal",
        "description": "This is a team workspace."
    }
)

result = sdk.workspaces.create_workspace(request_body=request_body)

print(result)
```

## get_workspace_roles

Gets information about all roles in a workspace, based on the team's [plan](https://www.postman.com/pricing/).

- HTTP Method: `GET`
- Endpoint: `/workspaces-roles`

**Return Type**

`GetWorkspaceRoles`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.workspaces.get_workspace_roles()

print(result)
```

## get_workspace

Gets information about a workspace. **Note:** This endpoint's response contains the `visibility` field. [Visibility](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/managing-workspaces/#changing-workspace-visibility) determines who can access the workspace: - `personal` — Only you can access the workspace. - `team` — All team members can access the workspace. - `private` — Only invited team members can access the workspace ([**Professional** and **Enterprise** plans only](https://www.postman.com/pricing)). - `public` — Everyone can access the workspace. - `partner` — Only invited team members and [partners](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/partner-workspaces/) can access the workspace ([**Professional** and **Enterprise** plans only](https://www.postman.com/pricing)). ### Important We have deprecated the `name` and `uid` responses in the following array of objects: - `collections` - `environments` - `mocks` - `monitors` - `apis`

- HTTP Method: `GET`
- Endpoint: `/workspaces/{workspaceId}`

**Parameters**

| Name         | Type | Required | Description         |
| :----------- | :--- | :------- | :------------------ |
| workspace_id | str  | ✅       | The workspace's ID. |

**Return Type**

`GetWorkspace`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.workspaces.get_workspace(workspace_id="1f0df51a-8658-4ee8-a2a1-d2567dfa09a9")

print(result)
```

## update_workspace

Updates a workspace. ### Important We deprecated linking collections or environments between workspaces. We do not recommend that you do this. If you have a linked collection or environment, note the following: - The endpoint does not create a clone of a collection or environment. - Any changes you make to a linked collection or environment changes them in all workspaces. - If you delete a collection or environment linked between workspaces, the system deletes it in all the workspaces.

- HTTP Method: `PUT`
- Endpoint: `/workspaces/{workspaceId}`

**Parameters**

| Name         | Type                                                          | Required | Description         |
| :----------- | :------------------------------------------------------------ | :------- | :------------------ |
| request_body | [UpdateWorkspaceRequest](../models/UpdateWorkspaceRequest.md) | ❌       | The request body.   |
| workspace_id | str                                                           | ✅       | The workspace's ID. |

**Return Type**

`UpdateWorkspaceOkResponse`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import UpdateWorkspaceRequest

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = UpdateWorkspaceRequest(
    workspace={
        "name": "Test Workspace",
        "type_": "private",
        "description": "This is a test team workspace."
    }
)

result = sdk.workspaces.update_workspace(
    request_body=request_body,
    workspace_id="1f0df51a-8658-4ee8-a2a1-d2567dfa09a9"
)

print(result)
```

## delete_workspace

Deletes an existing workspace. ### Important If you delete a workspace that has a linked collection or environment with another workspace, this will delete the collection and environment in all workspaces.

- HTTP Method: `DELETE`
- Endpoint: `/workspaces/{workspaceId}`

**Parameters**

| Name         | Type | Required | Description         |
| :----------- | :--- | :------- | :------------------ |
| workspace_id | str  | ✅       | The workspace's ID. |

**Return Type**

`DeleteWorkspace`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.workspaces.delete_workspace(workspace_id="1f0df51a-8658-4ee8-a2a1-d2567dfa09a9")

print(result)
```

## get_workspace_global_variables

Gets a workspace's global [variables](https://learning.postman.com/docs/sending-requests/variables/#variable-scopes).

- HTTP Method: `GET`
- Endpoint: `/workspaces/{workspaceId}/global-variables`

**Parameters**

| Name         | Type | Required | Description         |
| :----------- | :--- | :------- | :------------------ |
| workspace_id | str  | ✅       | The workspace's ID. |

**Return Type**

`GetWorkspaceGlobalVariables`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.workspaces.get_workspace_global_variables(workspace_id="1f0df51a-8658-4ee8-a2a1-d2567dfa09a9")

print(result)
```

## update_workspace_global_variables

Updates and replaces a workspace's global [variables](https://learning.postman.com/docs/sending-requests/variables/#variable-scopes). This endpoint replaces all existing global variables with the variables you pass in the request body.

- HTTP Method: `PUT`
- Endpoint: `/workspaces/{workspaceId}/global-variables`

**Parameters**

| Name         | Type                                                                                        | Required | Description         |
| :----------- | :------------------------------------------------------------------------------------------ | :------- | :------------------ |
| request_body | [UpdateWorkspaceGlobalVariablesRequest](../models/UpdateWorkspaceGlobalVariablesRequest.md) | ❌       | The request body.   |
| workspace_id | str                                                                                         | ✅       | The workspace's ID. |

**Return Type**

`UpdateWorkspaceGlobalVariablesOkResponse`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import UpdateWorkspaceGlobalVariablesRequest

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = UpdateWorkspaceGlobalVariablesRequest(
    values=[
        {
            "key": "variableName",
            "type_": "default",
            "value": "variableValue",
            "enabled": True
        }
    ]
)

result = sdk.workspaces.update_workspace_global_variables(
    request_body=request_body,
    workspace_id="1f0df51a-8658-4ee8-a2a1-d2567dfa09a9"
)

print(result)
```

## update_workspace_roles

Updates the roles of [users](https://learning.postman.com/docs/collaborating-in-postman/roles-and-permissions/#team-roles) or [user groups](https://learning.postman.com/docs/collaborating-in-postman/user-groups/) in a workspace. To get a list of roles, use the `GET /workspace-roles` endpoint. **Note:** - This endpoint does not support the external [Partner or Guest roles](https://learning.postman.com/docs/collaborating-in-postman/roles-and-permissions/#team-roles). - This endpoint is restricted to 50 operations per call. - The request body must contain one unique action per user or user group. For example, you cannot add and remove multiple roles for a user in the same request body.

- HTTP Method: `PATCH`
- Endpoint: `/workspaces/{workspaceId}/roles`

**Parameters**

| Name         | Type                                                                    | Required | Description         |
| :----------- | :---------------------------------------------------------------------- | :------- | :------------------ |
| request_body | [UpdateWorkspaceRolesRequest](../models/UpdateWorkspaceRolesRequest.md) | ❌       | The request body.   |
| workspace_id | str                                                                     | ✅       | The workspace's ID. |

**Return Type**

`UpdateWorkspaceRolesOkResponse`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import UpdateWorkspaceRolesRequest

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

request_body = UpdateWorkspaceRolesRequest(
    roles=[
        {
            "op": "add",
            "path": "/user",
            "value": [
                {
                    "id_": "12345678",
                    "role": 1
                }
            ]
        }
    ]
)

result = sdk.workspaces.update_workspace_roles(
    request_body=request_body,
    workspace_id="1f0df51a-8658-4ee8-a2a1-d2567dfa09a9"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
