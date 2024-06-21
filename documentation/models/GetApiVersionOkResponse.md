# GetApiVersionOkResponse

**Properties**

| Name    | Type    | Required | Description                        |
| :------ | :------ | :------- | :--------------------------------- |
| version | Version | ❌       | Information about the API version. |

# Version

Information about the API version.

**Properties**

| Name          | Type                     | Required | Description                                              |
| :------------ | :----------------------- | :------- | :------------------------------------------------------- |
| id\_          | str                      | ❌       | The version's ID.                                        |
| name          | str                      | ❌       | The version's name.                                      |
| created_at    | str                      | ❌       | The date and time at which the version was created.      |
| updated_at    | str                      | ❌       | The date and time at which the version was last updated. |
| release_notes | str                      | ❌       | The version's release notes.                             |
| schemas       | List[VersionSchemas]     | ❌       |                                                          |
| collections   | List[VersionCollections] | ❌       |                                                          |

# VersionSchemas

**Properties**

| Name   | Type | Required | Description      |
| :----- | :--- | :------- | :--------------- |
| id\_   | str  | ❌       | The schema's ID. |
| type\_ | str  | ❌       | The schema type. |

# VersionCollections

**Properties**

| Name   | Type | Required | Description            |
| :----- | :--- | :------- | :--------------------- |
| id\_   | str  | ❌       | The collection's ID.   |
| type\_ | str  | ❌       | The collection's name. |
