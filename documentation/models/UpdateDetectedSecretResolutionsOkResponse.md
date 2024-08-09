# UpdateDetectedSecretResolutionsOkResponse

**Properties**

| Name         | Type                               | Required | Description                                                                                                                                                                                                                                                                                                                                 |
| :----------- | :--------------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| history      | List[History]                      | ❌       | The history of the secret's resolution status changes.                                                                                                                                                                                                                                                                                      |
| resolution   | UpdateSecretResolutionsResolution2 | ❌       | The secret's current resolution status: - `ACTIVE` — The secret is active. - `FALSE_POSITIVE` — The discovered secret is not an actual secret. - `REVOKED` — The secret is valid, but the user rotated their key to resolve the issue. - `ACCEPTED_RISK` — The Secret Scanner found the secret, but user accepts the risk of publishing it. |
| secret_hash  | str                                | ❌       | The SHA-256 hash of the detected secret.                                                                                                                                                                                                                                                                                                    |
| workspace_id | str                                | ❌       | The ID of the workspace that contains the secret.                                                                                                                                                                                                                                                                                           |

# History

**Properties**

| Name       | Type              | Required | Description                                                                                                                                                                                                                                                                                                                                 |
| :--------- | :---------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| actor      | float             | ❌       | The ID of the user that updated the secret's resolution status.                                                                                                                                                                                                                                                                             |
| created_at | str               | ❌       | The date and time at which the resolution status was updated.                                                                                                                                                                                                                                                                               |
| resolution | HistoryResolution | ❌       | The secret's updated resolution status: - `ACTIVE` — The secret is active. - `FALSE_POSITIVE` — The discovered secret is not an actual secret. - `REVOKED` — The secret is valid, but the user rotated their key to resolve the issue. - `ACCEPTED_RISK` — The Secret Scanner found the secret, but user accepts the risk of publishing it. |

# HistoryResolution

The secret's updated resolution status: - `ACTIVE` — The secret is active. - `FALSE_POSITIVE` — The discovered secret is not an actual secret. - `REVOKED` — The secret is valid, but the user rotated their key to resolve the issue. - `ACCEPTED_RISK` — The Secret Scanner found the secret, but user accepts the risk of publishing it.

**Properties**

| Name          | Type | Required | Description      |
| :------------ | :--- | :------- | :--------------- |
| FALSEPOSITIVE | str  | ✅       | "FALSE_POSITIVE" |
| ACCEPTEDRISK  | str  | ✅       | "ACCEPTED_RISK"  |
| REVOKED       | str  | ✅       | "REVOKED"        |
| ACTIVE        | str  | ✅       | "ACTIVE"         |

# UpdateSecretResolutionsResolution_2

The secret's current resolution status: - `ACTIVE` — The secret is active. - `FALSE_POSITIVE` — The discovered secret is not an actual secret. - `REVOKED` — The secret is valid, but the user rotated their key to resolve the issue. - `ACCEPTED_RISK` — The Secret Scanner found the secret, but user accepts the risk of publishing it.

**Properties**

| Name          | Type | Required | Description      |
| :------------ | :--- | :------- | :--------------- |
| FALSEPOSITIVE | str  | ✅       | "FALSE_POSITIVE" |
| ACCEPTEDRISK  | str  | ✅       | "ACCEPTED_RISK"  |
| REVOKED       | str  | ✅       | "REVOKED"        |
| ACTIVE        | str  | ✅       | "ACTIVE"         |

<!-- This file was generated by liblab | https://liblab.com/ -->
