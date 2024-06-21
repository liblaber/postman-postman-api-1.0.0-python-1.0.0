# UpdateDetectedSecretResolutionsOkResponse

**Properties**

| Name         | Type                                                | Required | Description                                                                                                                                                                                                                                                                                                                                                      |
| :----------- | :-------------------------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| history      | List[History]                                       | ❌       | The history of the secret's resolution status changes.                                                                                                                                                                                                                                                                                                           |
| resolution   | UpdateDetectedSecretResolutionsOkResponseResolution | ❌       | The secret's current resolution status:<br/>- `ACTIVE` — The secret is active.<br/>- `FALSE_POSITIVE` — The discovered secret is not an actual secret.<br/>- `REVOKED` — The secret is valid, but the user rotated their key to resolve the issue.<br/>- `ACCEPTED_RISK` — The Secret Scanner found the secret, but user accepts the risk of publishing it.<br/> |
| secret_hash  | str                                                 | ❌       | The SHA-256 hash of the detected secret.                                                                                                                                                                                                                                                                                                                         |
| workspace_id | str                                                 | ❌       | The ID of the workspace that contains the secret.                                                                                                                                                                                                                                                                                                                |

# History

**Properties**

| Name       | Type              | Required | Description                                                                                                                                                                                                                                                                                                                                                      |
| :--------- | :---------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| actor      | float             | ❌       | The ID of the user that updated the secret's resolution status.                                                                                                                                                                                                                                                                                                  |
| created_at | str               | ❌       | The date and time at which the resolution status was updated.                                                                                                                                                                                                                                                                                                    |
| resolution | HistoryResolution | ❌       | The secret's updated resolution status:<br/>- `ACTIVE` — The secret is active.<br/>- `FALSE_POSITIVE` — The discovered secret is not an actual secret.<br/>- `REVOKED` — The secret is valid, but the user rotated their key to resolve the issue.<br/>- `ACCEPTED_RISK` — The Secret Scanner found the secret, but user accepts the risk of publishing it.<br/> |

# HistoryResolution

The secret's updated resolution status:

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

# UpdateDetectedSecretResolutionsOkResponseResolution

The secret's current resolution status:

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
