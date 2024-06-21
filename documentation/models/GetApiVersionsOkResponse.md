# GetApiVersionsOkResponse

Information about the API's versions.

**Properties**

| Name     | Type                                   | Required | Description                                            |
| :------- | :------------------------------------- | :------- | :----------------------------------------------------- |
| meta     | GetApiVersionsOkResponseMeta           | ❌       | The response's meta information for paginated results. |
| versions | List[GetApiVersionsOkResponseVersions] | ❌       |                                                        |

# GetApiVersionsOkResponseMeta

The response's meta information for paginated results.

**Properties**

| Name        | Type | Required | Description                                                              |
| :---------- | :--- | :------- | :----------------------------------------------------------------------- |
| limit       | int  | ❌       | The maximum number of records in the paginated response.                 |
| total       | int  | ❌       | The number of records that match the defined criteria.                   |
| next_cursor | str  | ❌       | The pagination cursor that points to the next record in the results set. |

# GetApiVersionsOkResponseVersions

Information about the API version.

**Properties**

| Name          | Type | Required | Description                                              |
| :------------ | :--- | :------- | :------------------------------------------------------- |
| id\_          | str  | ❌       | The version's ID.                                        |
| name          | str  | ❌       | The version's name.                                      |
| created_at    | str  | ❌       | The date and time at which the version was created.      |
| updated_at    | str  | ❌       | The date and time at which the version was last updated. |
| release_notes | str  | ❌       | The version's release notes.                             |
