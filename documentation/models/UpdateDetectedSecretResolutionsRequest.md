# UpdateDetectedSecretResolutionsRequest

**Properties**

| Name         | Type                                             | Required | Description                                                                                                                                                                                                                                                                                                               |
| :----------- | :----------------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| resolution   | UpdateDetectedSecretResolutionsRequestResolution | ✅       | The secret's updated resolution status:<br/>- `FALSE_POSITIVE` — The discovered secret is not an actual secret.<br/>- `REVOKED` — The secret is valid, but the user rotated their key to resolve the issue.<br/>- `ACCEPTED_RISK` — The Secret Scanner found the secret, but user accepts the risk of publishing it.<br/> |
| workspace_id | str                                              | ✅       | The ID of the workspace that contains the secret.                                                                                                                                                                                                                                                                         |

# UpdateDetectedSecretResolutionsRequestResolution

The secret's updated resolution status:

- `FALSE_POSITIVE` — The discovered secret is not an actual secret.
- `REVOKED` — The secret is valid, but the user rotated their key to resolve the issue.
- `ACCEPTED_RISK` — The Secret Scanner found the secret, but user accepts the risk of publishing it.

**Properties**

| Name           | Type | Required | Description      |
| :------------- | :--- | :------- | :--------------- |
| FALSE_POSITIVE | str  | ✅       | "FALSE_POSITIVE" |
| REVOKED        | str  | ✅       | "REVOKED"        |
| ACCEPTED_RISK  | str  | ✅       | "ACCEPTED_RISK"  |
