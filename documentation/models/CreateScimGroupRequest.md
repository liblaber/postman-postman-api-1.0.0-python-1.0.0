# CreateScimGroupRequest

**Properties**

| Name         | Type                                | Required | Description                                                              |
| :----------- | :---------------------------------- | :------- | :----------------------------------------------------------------------- |
| schemas      | List[str]                           | ❌       | The [SCIM schema URI](https://www.iana.org/assignments/scim/scim.xhtml). |
| display_name | str                                 | ❌       | The group's display name.                                                |
| members      | List[CreateScimGroupRequestMembers] | ❌       |                                                                          |

# CreateScimGroupRequestMembers

An object containing the SCIM users to assign to the group.

**Properties**

| Name    | Type | Required | Description              |
| :------ | :--- | :------- | :----------------------- |
| value   | str  | ❌       | The user's SCIM ID.      |
| display | str  | ❌       | The user's display name. |
