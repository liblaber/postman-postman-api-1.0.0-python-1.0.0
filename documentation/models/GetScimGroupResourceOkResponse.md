# GetScimGroupResourceOkResponse

**Properties**

| Name        | Type                                        | Required | Description                                                              |
| :---------- | :------------------------------------------ | :------- | :----------------------------------------------------------------------- |
| schemas     | List[str]                                   | ❌       | The [SCIM schema URI](https://www.iana.org/assignments/scim/scim.xhtml). |
| id\_        | str                                         | ❌       | The group's SCIM ID.                                                     |
| user_name   | str                                         | ❌       | The group's display name.                                                |
| members     | List[GetScimGroupResourceOkResponseMembers] | ❌       | Information about the group's members.                                   |
| external_id | str                                         | ❌       | The group's external ID.                                                 |
| meta        | GetScimGroupResourceOkResponseMeta          | ❌       | The response's non-standard meta information.                            |

# GetScimGroupResourceOkResponseMembers

**Properties**

| Name    | Type | Required | Description                |
| :------ | :--- | :------- | :------------------------- |
| value   | str  | ❌       | The member's SCIM ID.      |
| display | str  | ❌       | The member's display name. |

# GetScimGroupResourceOkResponseMeta

The response's non-standard meta information.

**Properties**

| Name          | Type | Required | Description                                             |
| :------------ | :--- | :------- | :------------------------------------------------------ |
| resource_type | str  | ❌       | The resource type.                                      |
| created       | str  | ❌       | The date and time at which the group was created.       |
| last_modified | str  | ❌       | The date and time at which the group was last modified. |
