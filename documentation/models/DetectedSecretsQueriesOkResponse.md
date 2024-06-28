# DetectedSecretsQueriesOkResponse

**Properties**

| Name | Type                                       | Required | Description                                            |
| :--- | :----------------------------------------- | :------- | :----------------------------------------------------- |
| data | List[DetectedSecretsQueriesOkResponseData] | ❌       |                                                        |
| meta | DetectedSecretsQueriesOkResponseMeta       | ❌       | The response's meta information for paginated results. |

# DetectedSecretsQueriesOkResponseData

Information about the secret finding.

**Properties**

<<<<<<< HEAD
| Name                 | Type                    | Required | Description                                                                                                                                                                                                                                                                                                                                           |
| :------------------- | :---------------------- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| obfuscated_secret    | str                     | ❌       | The secret's obfuscated value.                                                                                                                                                                                                                                                                                                                        |
| occurrences          | float                   | ❌       | The number of times the secret was found in the workspace.                                                                                                                                                                                                                                                                                            |
| resolution           | DataResolution          | ❌       | The secret's current status:<br/>- `ACTIVE` — The secret is active.<br/>- `FALSE_POSITIVE` — The discovered secret is not an actual secret.<br/>- `REVOKED` — The secret is valid, but the user rotated their key to resolve the issue.<br/>- `ACCEPTED_RISK` — The Secret Scanner found the secret, but user accepts the risk of publishing it.<br/> |
| secret_hash          | str                     | ❌       | The SHA-256 hash of the detected secret.                                                                                                                                                                                                                                                                                                              |
| secret_id            | str                     | ❌       | The detected secret's ID.                                                                                                                                                                                                                                                                                                                             |
| secret_type          | str                     | ❌       | The type of the secret.                                                                                                                                                                                                                                                                                                                               |
| detected_at          | str                     | ❌       | The date and time at which the secret was first detected.                                                                                                                                                                                                                                                                                             |
| workspace_id         | str                     | ❌       | The ID of the workspace that contains the secret.                                                                                                                                                                                                                                                                                                     |
| workspace_visibility | DataWorkspaceVisibility | ❌       | The workspace's [visibility setting](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/managing-workspaces/#changing-workspace-visibility).                                                                                                                                                                                 |
=======
| Name                 | Type                    | Required | Description                                                                                                                                                                                                                                                                                                                                      |
| :------------------- | :---------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| obfuscated_secret    | str                     | ❌       | The secret's obfuscated value.                                                                                                                                                                                                                                                                                                                   |
| occurrences          | float                   | ❌       | The number of times the secret was found in the workspace.                                                                                                                                                                                                                                                                                       |
| resolution           | DataResolution          | ❌       | The secret's current status:<br>- `ACTIVE` — The secret is active.<br>- `FALSE_POSITIVE` — The discovered secret is not an actual secret.<br>- `REVOKED` — The secret is valid, but the user rotated their key to resolve the issue.<br>- `ACCEPTED_RISK` — The Secret Scanner found the secret, but user accepts the risk of publishing it.<br> |
| secret_hash          | str                     | ❌       | The SHA-256 hash of the detected secret.                                                                                                                                                                                                                                                                                                         |
| secret_id            | str                     | ❌       | The detected secret's ID.                                                                                                                                                                                                                                                                                                                        |
| secret_type          | str                     | ❌       | The type of the secret.                                                                                                                                                                                                                                                                                                                          |
| detected_at          | str                     | ❌       | The date and time at which the secret was first detected.                                                                                                                                                                                                                                                                                        |
| workspace_id         | str                     | ❌       | The ID of the workspace that contains the secret.                                                                                                                                                                                                                                                                                                |
| workspace_visibility | DataWorkspaceVisibility | ❌       | The workspace's [visibility setting](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/managing-workspaces/#changing-workspace-visibility).                                                                                                                                                                            |
>>>>>>> 95da91c (initial commit)

# DataResolution

The secret's current status:

- `ACTIVE` — The secret is active.
- `FALSE_POSITIVE` — The discovered secret is not an actual secret.
- `REVOKED` — The secret is valid, but the user rotated their key to resolve the issue.
- `ACCEPTED_RISK` — The Secret Scanner found the secret, but user accepts the risk of publishing it.

**Properties**

| Name           | Type | Required | Description      |
| :------------- | :--- | :------- | :--------------- |
| FALSE_POSITIVE | str  | ✅       | "FALSE_POSITIVE" |
| ACCEPTED_RISK  | str  | ✅       | "ACCEPTED_RISK"  |
| REVOKED        | str  | ✅       | "REVOKED"        |
| ACTIVE         | str  | ✅       | "ACTIVE"         |

# DataWorkspaceVisibility

The workspace's [visibility setting](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/managing-workspaces/#changing-workspace-visibility).

**Properties**

| Name     | Type | Required | Description |
| :------- | :--- | :------- | :---------- |
| PERSONAL | str  | ✅       | "personal"  |
| PRIVATE  | str  | ✅       | "private"   |
| TEAM     | str  | ✅       | "team"      |
| PUBLIC   | str  | ✅       | "public"    |

# DetectedSecretsQueriesOkResponseMeta

The response's meta information for paginated results.

**Properties**

| Name        | Type  | Required | Description                                                                                                                                                 |
| :---------- | :---- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| limit       | float | ❌       | The maximum number of records in the paginated response.                                                                                                    |
| next_cursor | str   | ❌       | The pagination cursor that points to the next record in the results set.                                                                                    |
| total       | float | ❌       | The number of records that match the defined criteria. This will only be present if the `include` query parameter is specified with the `meta.total` value. |
<<<<<<< HEAD
=======

<!-- This file was generated by liblab | https://liblab.com/ -->
>>>>>>> 95da91c (initial commit)
