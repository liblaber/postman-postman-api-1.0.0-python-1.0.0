# UpdateCollectionRolesRequest

**Properties**

| Name  | Type                                    | Required | Description |
| :---- | :-------------------------------------- | :------- | :---------- |
| roles | List[UpdateCollectionRolesRequestRoles] | ✅       |             |

# UpdateCollectionRolesRequestRoles

**Properties**

| Name  | Type              | Required | Description                            |
| :---- | :---------------- | :------- | :------------------------------------- |
| op    | RolesOp           | ✅       | The operation to perform on the path.  |
| path  | RolesPath1        | ✅       | The resource to perform the action on. |
| value | List[RolesValue1] | ✅       |                                        |

# RolesOp

The operation to perform on the path.

**Properties**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| UPDATE | str  | ✅       | "update"    |

# RolesPath_1

The resource to perform the action on.

**Properties**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| \_USER  | str  | ✅       | "/user"     |
| \_GROUP | str  | ✅       | "/group"    |
| \_TEAM  | str  | ✅       | "/team"     |

# RolesValue_1

Information about the updated role.

**Properties**

| Name | Type       | Required | Description                                                                                                             |
| :--- | :--------- | :------- | :---------------------------------------------------------------------------------------------------------------------- |
| id\_ | float      | ✅       | The user, group, or team's ID.                                                                                          |
| role | ValueRole1 | ✅       | The role type:<br/>- `VIEWER` — Can view, fork, and export collections.<br/>- `EDITOR` — Can edit collections directly. |

# ValueRole_1

The role type:

- `VIEWER` — Can view, fork, and export collections.
- `EDITOR` — Can edit collections directly.

**Properties**

| Name   | Type | Required | Description |
| :----- | :--- | :------- | :---------- |
| VIEWER | str  | ✅       | "VIEWER"    |
| EDITOR | str  | ✅       | "EDITOR"    |
