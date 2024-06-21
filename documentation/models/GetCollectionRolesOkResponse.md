# GetCollectionRolesOkResponse

Information about the collection's roles.

**Properties**

| Name  | Type                                   | Required | Description                             |
| :---- | :------------------------------------- | :------- | :-------------------------------------- |
| group | List[Group]                            | ❌       | A list of the collection's group roles. |
| team  | List[GetCollectionRolesOkResponseTeam] | ❌       | A list of the collection's team roles.  |
| user  | List[GetCollectionRolesOkResponseUser] | ❌       | A list of the collection's user roles.  |

# Group

Information about the group role.

**Properties**

| Name | Type      | Required | Description                                                                                                                  |
| :--- | :-------- | :------- | :--------------------------------------------------------------------------------------------------------------------------- |
| role | GroupRole | ❌       | The role type:<br/>- `VIEWER` — Can view, fork, and export collections.<br/>- `EDITOR` — Can edit collections directly.<br/> |
| id\_ | float     | ❌       | The role's ID.                                                                                                               |

# GroupRole

The role type:

- `VIEWER` — Can view, fork, and export collections.
- `EDITOR` — Can edit collections directly.

**Properties**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| VIEWER | str  | ✅       | "VIEWER"    |
| EDITOR | str  | ✅       | "EDITOR"    |

# GetCollectionRolesOkResponseTeam

Information about the team role.

**Properties**

| Name | Type     | Required | Description                                                                                                                  |
| :--- | :------- | :------- | :--------------------------------------------------------------------------------------------------------------------------- |
| role | TeamRole | ❌       | The role type:<br/>- `VIEWER` — Can view, fork, and export collections.<br/>- `EDITOR` — Can edit collections directly.<br/> |
| id\_ | float    | ❌       | The role's ID.                                                                                                               |

# TeamRole

The role type:

- `VIEWER` — Can view, fork, and export collections.
- `EDITOR` — Can edit collections directly.

**Properties**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| VIEWER | str  | ✅       | "VIEWER"    |
| EDITOR | str  | ✅       | "EDITOR"    |

# GetCollectionRolesOkResponseUser

Information about the user role.

**Properties**

| Name | Type     | Required | Description                                                                                                                  |
| :--- | :------- | :------- | :--------------------------------------------------------------------------------------------------------------------------- |
| role | UserRole | ❌       | The role type:<br/>- `VIEWER` — Can view, fork, and export collections.<br/>- `EDITOR` — Can edit collections directly.<br/> |
| id\_ | float    | ❌       | The role's ID.                                                                                                               |

# UserRole

The role type:

- `VIEWER` — Can view, fork, and export collections.
- `EDITOR` — Can edit collections directly.

**Properties**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| VIEWER | str  | ✅       | "VIEWER"    |
| EDITOR | str  | ✅       | "EDITOR"    |
