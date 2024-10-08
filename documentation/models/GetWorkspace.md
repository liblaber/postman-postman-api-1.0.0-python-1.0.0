# GetWorkspace

**Properties**

| Name      | Type                  | Required | Description                      |
| :-------- | :-------------------- | :------- | :------------------------------- |
| workspace | GetWorkspaceWorkspace | ❌       | Information about the workspace. |

# GetWorkspaceWorkspace

Information about the workspace.

**Properties**

| Name         | Type                        | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| :----------- | :-------------------------- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id\_         | str                         | ❌       | The workspace's ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| name         | str                         | ❌       | The workspace's name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| type\_       | WorkspaceType2              | ❌       | The type of workspace.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| description  | str                         | ❌       | The workspace's description.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| visibility   | WorkspaceVisibility         | ❌       | The workspace's visibility. [Visibility](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/managing-workspaces/#changing-workspace-visibility) determines who can access the workspace: - `personal` — Only you can access the workspace. - `team` — All team members can access the workspace. - `private` — Only invited team members can access the workspace ([**Professional** and **Enterprise** plans only](https://www.postman.com/pricing)). - `public` — Everyone can access the workspace. - `partner` — Only invited team members and [partners](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/partner-workspaces/) can access the workspace ([**Professional** and **Enterprise** plans only](https://www.postman.com/pricing)). |
| created_by   | str                         | ❌       | The user ID of the user who created the workspace.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| updated_by   | str                         | ❌       | The user ID of the user who last updated the workspace.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| created_at   | str                         | ❌       | The date and time at which the workspace was created.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| updated_at   | str                         | ❌       | The date and time at which the workspace was last updated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| collections  | List[WorkspaceCollections]  | ❌       | The workspace's collections.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| environments | List[WorkspaceEnvironments] | ❌       | The workspace's environments.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| mocks        | List[WorkspaceMocks]        | ❌       | The workspace's mock servers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| monitors     | List[WorkspaceMonitors]     | ❌       | The workspace's monitors.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| apis         | List[WorkspaceApis]         | ❌       | The workspace's APIs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

# WorkspaceType_2

The type of workspace.

**Properties**

| Name     | Type | Required | Description |
| :------- | :--- | :------- | :---------- |
| PERSONAL | str  | ✅       | "personal"  |
| TEAM     | str  | ✅       | "team"      |
| PRIVATE  | str  | ✅       | "private"   |
| PUBLIC   | str  | ✅       | "public"    |
| PARTNER  | str  | ✅       | "partner"   |

# WorkspaceVisibility

The workspace's visibility. [Visibility](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/managing-workspaces/#changing-workspace-visibility) determines who can access the workspace: - `personal` — Only you can access the workspace. - `team` — All team members can access the workspace. - `private` — Only invited team members can access the workspace ([**Professional** and **Enterprise** plans only](https://www.postman.com/pricing)). - `public` — Everyone can access the workspace. - `partner` — Only invited team members and [partners](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/partner-workspaces/) can access the workspace ([**Professional** and **Enterprise** plans only](https://www.postman.com/pricing)).

**Properties**

| Name     | Type | Required | Description |
| :------- | :--- | :------- | :---------- |
| PERSONAL | str  | ✅       | "personal"  |
| TEAM     | str  | ✅       | "team"      |
| PRIVATE  | str  | ✅       | "private"   |
| PUBLIC   | str  | ✅       | "public"    |
| PARTNER  | str  | ✅       | "partner"   |

# WorkspaceCollections

Information about the collection.

**Properties**

| Name | Type | Required | Description                 |
| :--- | :--- | :------- | :-------------------------- |
| id\_ | str  | ❌       | The collection's ID.        |
| name | str  | ❌       | The collection's name.      |
| uid  | str  | ❌       | The collection's unique ID. |

# WorkspaceEnvironments

Information about the environment.

**Properties**

| Name | Type | Required | Description                  |
| :--- | :--- | :------- | :--------------------------- |
| id\_ | str  | ❌       | The environment's ID.        |
| name | str  | ❌       | The environment's name.      |
| uid  | str  | ❌       | The environment's unique ID. |

# WorkspaceMocks

Information about the mock server.

**Properties**

| Name        | Type | Required | Description                                                                                                         |
| :---------- | :--- | :------- | :------------------------------------------------------------------------------------------------------------------ |
| id\_        | str  | ❌       | The mock server's ID.                                                                                               |
| name        | str  | ❌       | The mock server's name.                                                                                             |
| uid         | str  | ❌       | The mock server's unique ID.                                                                                        |
| deactivated | bool | ❌       | If true, the mock server is not active. Mock servers deactivate when a linked collection or environment is deleted. |

# WorkspaceMonitors

Information about the monitor.

**Properties**

| Name | Type | Required | Description              |
| :--- | :--- | :------- | :----------------------- |
| id\_ | str  | ❌       | The monitor's ID.        |
| name | str  | ❌       | The monitor's name.      |
| uid  | str  | ❌       | The monitor's unique ID. |

# WorkspaceApis

Information about the API.

**Properties**

| Name | Type | Required | Description          |
| :--- | :--- | :------- | :------------------- |
| id\_ | str  | ❌       | The API's ID.        |
| name | str  | ❌       | The API's name.      |
| uid  | str  | ❌       | The API's unique ID. |

<!-- This file was generated by liblab | https://liblab.com/ -->
