# GetDetectedSecretsLocationsOkResponse

**Properties**

| Name | Type                                            | Required | Description |
| :--- | :---------------------------------------------- | :------- | :---------- |
| data | List[GetDetectedSecretsLocationsOkResponseData] | ❌       |             |
| meta | GetDetectedSecretsLocationsOkResponseMeta       | ❌       |             |

# GetDetectedSecretsLocationsOkResponseData

Information about the secret finding locations.

**Properties**

| Name                | Type             | Required | Description                                                                                                                                                                                            |
| :------------------ | :--------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| is_resource_deleted | bool             | ❌       | If true, the resource in which the secret was found was deleted.                                                                                                                                       |
| leaked_by           | int              | ❌       | The ID of the user who exposed the secret.                                                                                                                                                             |
| location            | str              | ❌       | The location where the secret was found.                                                                                                                                                               |
| occurrences         | int              | ❌       | The number of times the secret occurs in the location.                                                                                                                                                 |
| parent_resource_id  | str              | ❌       | The parent resource's unique ID. If the resource is a request, folder, or example, this value is a collection ID. If the resource is a collection, globals, or environment, this is the resource's ID. |
| resource_id         | str              | ❌       | The unique ID of the resource where the secret was detected.                                                                                                                                           |
| resource_type       | DataResourceType | ❌       | The type of resource in which the secret was detected.                                                                                                                                                 |
| detected_at         | str              | ❌       | The date and time at which the secret was detected.                                                                                                                                                    |
| url                 | str              | ❌       | The URL to the resource that contains the secret.                                                                                                                                                      |

# DataResourceType

The type of resource in which the secret was detected.

**Properties**

| Name        | Type | Required | Description   |
| :---------- | :--- | :------- | :------------ |
| COLLECTION  | str  | ✅       | "collection"  |
| FOLDER      | str  | ✅       | "folder"      |
| REQUEST     | str  | ✅       | "request"     |
| EXAMPLE     | str  | ✅       | "example"     |
| ENVIRONMENT | str  | ✅       | "environment" |
| GLOBALS     | str  | ✅       | "globals"     |
| API         | str  | ✅       | "api"         |

# GetDetectedSecretsLocationsOkResponseMeta

**Properties**

| Name              | Type               | Required | Description                                                                 |
| :---------------- | :----------------- | :------- | :-------------------------------------------------------------------------- |
| activity_feed     | List[ActivityFeed] | ❌       | The history of the secret's resolution status changes.                      |
| cursor            | str                | ❌       | The pointer to the first record of the set of paginated results.            |
| limit             | int                | ❌       | The maximum number of rows to return in the response.                       |
| next_cursor       | str                | ❌       | The Base64-encoded value that points to the next record in the results set. |
| obfuscated_secret | str                | ❌       | The secret's obfuscated value.                                              |
| secret_hash       | str                | ❌       | The secret's SHA-256 hash.                                                  |
| secret_type       | str                | ❌       | The type of thesecret.                                                      |
| total             | int                | ❌       | The total number of discovered secret locations.                            |

# ActivityFeed

**Properties**

<<<<<<< HEAD
| Name        | Type               | Required | Description                                                                                                                                                                                                                                                                                                                                                      |
| :---------- | :----------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| resolved_at | str                | ❌       | The date and time at which the resolution status was last updated.                                                                                                                                                                                                                                                                                               |
| resolved_by | int                | ❌       | The ID of the user that updated the secret's resolution status.                                                                                                                                                                                                                                                                                                  |
| status      | ActivityFeedStatus | ❌       | The secret's current resolution status:<br/>- `ACTIVE` — The secret is active.<br/>- `FALSE_POSITIVE` — The discovered secret is not an actual secret.<br/>- `REVOKED` — The secret is valid, but the user rotated their key to resolve the issue.<br/>- `ACCEPTED_RISK` — The Secret Scanner found the secret, but user accepts the risk of publishing it.<br/> |
=======
| Name        | Type               | Required | Description                                                                                                                                                                                                                                                                                                                                                 |
| :---------- | :----------------- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| resolved_at | str                | ❌       | The date and time at which the resolution status was last updated.                                                                                                                                                                                                                                                                                          |
| resolved_by | int                | ❌       | The ID of the user that updated the secret's resolution status.                                                                                                                                                                                                                                                                                             |
| status      | ActivityFeedStatus | ❌       | The secret's current resolution status:<br>- `ACTIVE` — The secret is active.<br>- `FALSE_POSITIVE` — The discovered secret is not an actual secret.<br>- `REVOKED` — The secret is valid, but the user rotated their key to resolve the issue.<br>- `ACCEPTED_RISK` — The Secret Scanner found the secret, but user accepts the risk of publishing it.<br> |
>>>>>>> 95da91c (initial commit)

# ActivityFeedStatus

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
<<<<<<< HEAD
=======

<!-- This file was generated by liblab | https://liblab.com/ -->
>>>>>>> 95da91c (initial commit)
