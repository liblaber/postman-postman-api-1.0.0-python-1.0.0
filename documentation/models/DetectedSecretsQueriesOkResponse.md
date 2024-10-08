# DetectedSecretsQueriesOkResponse

**Properties**

| Name | Type                             | Required | Description                                            |
| :--- | :------------------------------- | :------- | :----------------------------------------------------- |
| data | List[DetectedSecretsQueriesData] | ❌       |                                                        |
| meta | DetectedSecretsQueriesMeta       | ❌       | The response's meta information for paginated results. |

# DetectedSecretsQueriesData

Information about the secret finding.

**Properties**

| Name                 | Type                    | Required | Description                                                                                                                                                                                                                                                                                                                      |
| :------------------- | :---------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| obfuscated_secret    | str                     | ❌       | The secret's obfuscated value.                                                                                                                                                                                                                                                                                                   |
| occurrences          | float                   | ❌       | The number of times the secret was found in the workspace.                                                                                                                                                                                                                                                                       |
| resolution           | DataResolution          | ❌       | The secret's current status: - `ACTIVE` — The secret is active. - `FALSE_POSITIVE` — The discovered secret is not an actual secret. - `REVOKED` — The secret is valid, but the user rotated their key to resolve the issue. - `ACCEPTED_RISK` — The Secret Scanner found the secret, but user accepts the risk of publishing it. |
| secret_hash          | str                     | ❌       | The SHA-256 hash of the detected secret.                                                                                                                                                                                                                                                                                         |
| secret_id            | str                     | ❌       | The detected secret's ID.                                                                                                                                                                                                                                                                                                        |
| secret_type          | str                     | ❌       | The type of the secret.                                                                                                                                                                                                                                                                                                          |
| detected_at          | str                     | ❌       | The date and time at which the secret was first detected.                                                                                                                                                                                                                                                                        |
| workspace_id         | str                     | ❌       | The ID of the workspace that contains the secret.                                                                                                                                                                                                                                                                                |
| workspace_visibility | DataWorkspaceVisibility | ❌       | The workspace's [visibility setting](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/managing-workspaces/#changing-workspace-visibility).                                                                                                                                                            |

# DataResolution

The secret's current status: - `ACTIVE` — The secret is active. - `FALSE_POSITIVE` — The discovered secret is not an actual secret. - `REVOKED` — The secret is valid, but the user rotated their key to resolve the issue. - `ACCEPTED_RISK` — The Secret Scanner found the secret, but user accepts the risk of publishing it.

**Properties**

| Name          | Type | Required | Description      |
| :------------ | :--- | :------- | :--------------- |
| FALSEPOSITIVE | str  | ✅       | "FALSE_POSITIVE" |
| ACCEPTEDRISK  | str  | ✅       | "ACCEPTED_RISK"  |
| REVOKED       | str  | ✅       | "REVOKED"        |
| ACTIVE        | str  | ✅       | "ACTIVE"         |

# DataWorkspaceVisibility

The workspace's [visibility setting](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/managing-workspaces/#changing-workspace-visibility).

**Properties**

| Name     | Type | Required | Description |
| :------- | :--- | :------- | :---------- |
| PERSONAL | str  | ✅       | "personal"  |
| PRIVATE  | str  | ✅       | "private"   |
| TEAM     | str  | ✅       | "team"      |
| PUBLIC   | str  | ✅       | "public"    |

# DetectedSecretsQueriesMeta

The response's meta information for paginated results.

**Properties**

| Name        | Type  | Required | Description                                                                                                                                                 |
| :---------- | :---- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| limit       | float | ❌       | The maximum number of records in the paginated response.                                                                                                    |
| next_cursor | str   | ❌       | The pagination cursor that points to the next record in the results set.                                                                                    |
| total       | float | ❌       | The number of records that match the defined criteria. This will only be present if the `include` query parameter is specified with the `meta.total` value. |

<!-- This file was generated by liblab | https://liblab.com/ -->
