# CreateScimUserCreatedResponse

**Properties**

| Name        | Type                              | Required | Description                                                              |
| :---------- | :-------------------------------- | :------- | :----------------------------------------------------------------------- |
| schemas     | List[str]                         | ❌       | The [SCIM schema URI](https://www.iana.org/assignments/scim/scim.xhtml). |
| id\_        | str                               | ❌       | The user's SCIM ID.                                                      |
| user_name   | str                               | ❌       | The user's username.                                                     |
| name        | CreateScimUserCreatedResponseName | ❌       |                                                                          |
| external_id | str                               | ❌       | The user's external ID.                                                  |
| active      | bool                              | ❌       | If true, the user is active.                                             |
| meta        | CreateScimUserCreatedResponseMeta | ❌       | The response's non-standard meta information.                            |

# CreateScimUserCreatedResponseName

**Properties**

| Name        | Type | Required | Description            |
| :---------- | :--- | :------- | :--------------------- |
| given_name  | str  | ❌       | The user's first name. |
| family_name | str  | ❌       | The user's last name.  |

# CreateScimUserCreatedResponseMeta

The response's non-standard meta information.

**Properties**

| Name          | Type             | Required | Description                                            |
| :------------ | :--------------- | :------- | :----------------------------------------------------- |
| created       | str              | ❌       | The date and time at which the user was created.       |
| last_modified | str              | ❌       | The date and time at which the user was last modified. |
| resource_type | MetaResourceType | ❌       | The SCIM resource type.                                |

# MetaResourceType

The SCIM resource type.

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| USER | str  | ✅       | "User"      |
