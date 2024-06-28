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

<<<<<<< HEAD
| Name | Type      | Required | Description                                                                                                                  |
| :--- | :-------- | :------- | :--------------------------------------------------------------------------------------------------------------------------- |
| role | GroupRole | ❌       | The role type:<br/>- `VIEWER` — Can view, fork, and export collections.<br/>- `EDITOR` — Can edit collections directly.<br/> |
| id\_ | float     | ❌       | The role's ID.                                                                                                               |
=======
| Name | Type      | Required | Description                                                                                                               |
| :--- | :-------- | :------- | :------------------------------------------------------------------------------------------------------------------------ |
| role | GroupRole | ❌       | The role type:<br>- `VIEWER` — Can view, fork, and export collections.<br>- `EDITOR` — Can edit collections directly.<br> |
| id\_ | float     | ❌       | The role's ID.                                                                                                            |
>>>>>>> 95da91c (initial commit)

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

<<<<<<< HEAD
| Name | Type     | Required | Description                                                                                                                  |
| :--- | :------- | :------- | :--------------------------------------------------------------------------------------------------------------------------- |
| role | TeamRole | ❌       | The role type:<br/>- `VIEWER` — Can view, fork, and export collections.<br/>- `EDITOR` — Can edit collections directly.<br/> |
| id\_ | float    | ❌       | The role's ID.                                                                                                               |
=======
| Name | Type     | Required | Description                                                                                                               |
| :--- | :------- | :------- | :------------------------------------------------------------------------------------------------------------------------ |
| role | TeamRole | ❌       | The role type:<br>- `VIEWER` — Can view, fork, and export collections.<br>- `EDITOR` — Can edit collections directly.<br> |
| id\_ | float    | ❌       | The role's ID.                                                                                                            |
>>>>>>> 95da91c (initial commit)

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

<<<<<<< HEAD
| Name | Type     | Required | Description                                                                                                                  |
| :--- | :------- | :------- | :--------------------------------------------------------------------------------------------------------------------------- |
| role | UserRole | ❌       | The role type:<br/>- `VIEWER` — Can view, fork, and export collections.<br/>- `EDITOR` — Can edit collections directly.<br/> |
| id\_ | float    | ❌       | The role's ID.                                                                                                               |
=======
| Name | Type     | Required | Description                                                                                                               |
| :--- | :------- | :------- | :------------------------------------------------------------------------------------------------------------------------ |
| role | UserRole | ❌       | The role type:<br>- `VIEWER` — Can view, fork, and export collections.<br>- `EDITOR` — Can edit collections directly.<br> |
| id\_ | float    | ❌       | The role's ID.                                                                                                            |
>>>>>>> 95da91c (initial commit)

# UserRole

The role type:

- `VIEWER` — Can view, fork, and export collections.
- `EDITOR` — Can edit collections directly.

**Properties**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| VIEWER | str  | ✅       | "VIEWER"    |
| EDITOR | str  | ✅       | "EDITOR"    |
<<<<<<< HEAD
=======

<!-- This file was generated by liblab | https://liblab.com/ -->
>>>>>>> 95da91c (initial commit)
