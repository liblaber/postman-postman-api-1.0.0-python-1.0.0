# UpdateWorkspaceRequest

**Properties**

| Name      | Type                            | Required | Description |
| :-------- | :------------------------------ | :------- | :---------- |
| workspace | UpdateWorkspaceRequestWorkspace | ❌       |             |

# UpdateWorkspaceRequestWorkspace

**Properties**

<<<<<<< HEAD
| Name        | Type           | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| :---------- | :------------- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name        | str            | ❌       | The workspace's new name.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| type\_      | WorkspaceType3 | ❌       | The new workspace visibility [type](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/managing-workspaces/#changing-workspace-visibility). This property does not support the following workspace visibility changes:<br/>- `private` to `public`, `public` to `private`, and `private` to `personal` for Free and Basic [plans](https://www.postman.com/pricing/).<br/>- `public` to `personal` for team users.<br/> |
| description | str            | ❌       | The new workspace description.                                                                                                                                                                                                                                                                                                                                                                                                                  |
=======
| Name        | Type           | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| :---------- | :------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name        | str            | ❌       | The workspace's new name.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| type\_      | WorkspaceType3 | ❌       | The new workspace visibility [type](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/managing-workspaces/#changing-workspace-visibility). This property does not support the following workspace visibility changes:<br>- `private` to `public`, `public` to `private`, and `private` to `personal` for Free and Basic [plans](https://www.postman.com/pricing/).<br>- `public` to `personal` for team users.<br> |
| description | str            | ❌       | The new workspace description.                                                                                                                                                                                                                                                                                                                                                                                                               |
>>>>>>> 95da91c (initial commit)

# WorkspaceType_3

The new workspace visibility [type](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/managing-workspaces/#changing-workspace-visibility). This property does not support the following workspace visibility changes:

- `private` to `public`, `public` to `private`, and `private` to `personal` for Free and Basic [plans](https://www.postman.com/pricing/).
- `public` to `personal` for team users.

**Properties**

| Name     | Type | Required | Description |
| :------- | :--- | :------- | :---------- |
| PRIVATE  | str  | ✅       | "private"   |
| PERSONAL | str  | ✅       | "personal"  |
| TEAM     | str  | ✅       | "team"      |
| PUBLIC   | str  | ✅       | "public"    |
<<<<<<< HEAD
=======

<!-- This file was generated by liblab | https://liblab.com/ -->
>>>>>>> 95da91c (initial commit)
