# GetApiOkResponse

# GetApiOkResponse_1

The API's base data schema.

**Properties**

| Name        | Type | Required | Description                                      |
| :---------- | :--- | :------- | :----------------------------------------------- |
| id\_        | str  | ❌       | The API's ID.                                    |
| name        | str  | ❌       | The API's name.                                  |
| summary     | str  | ❌       | The API's short summary.                         |
| created_at  | str  | ❌       | The date and time at which the API was created.  |
| created_by  | int  | ❌       | The Postman ID of the user that created the API. |
| updated_at  | str  | ❌       | The date and time at which the API was updated.  |
| updated_by  | int  | ❌       | The Postman ID of the user that updated the API. |
| description | str  | ❌       | The API's description.                           |

# GetApiOkResponse_2

**Properties**

| Name        | Type                               | Required | Description                                             |
| :---------- | :--------------------------------- | :------- | :------------------------------------------------------ |
| id\_        | str                                | ❌       | The API's ID.                                           |
| name        | str                                | ❌       | The API's name.                                         |
| summary     | str                                | ❌       | The API's short summary.                                |
| created_at  | str                                | ❌       | The date and time at which the API was created.         |
| created_by  | int                                | ❌       | The Postman ID of the user that created the API.        |
| updated_at  | str                                | ❌       | The date and time at which the API was updated.         |
| updated_by  | int                                | ❌       | The Postman ID of the user that updated the API.        |
| description | str                                | ❌       | The API's description.                                  |
| git_info    | GitInfo                            | ❌       | Information about the API's Git repository integration. |
| schemas     | List[GetApiOkResponse2Schemas]     | ❌       | The API's schemas.                                      |
| versions    | List[GetApiOkResponse2Versions]    | ❌       | The API's versions.                                     |
| collections | List[GetApiOkResponse2Collections] | ❌       | The API's collections.                                  |

# GitInfo

Information about the API's Git repository integration.

**Properties**

| Name              | Type | Required | Description                                                 |
| :---------------- | :--- | :------- | :---------------------------------------------------------- |
| domain            | str  | ❌       | The domain at which the Git repository is hosted.           |
| repository        | str  | ❌       | The repository's name.                                      |
| organization      | str  | ❌       | The organization that owns the repository.                  |
| schema_folder     | str  | ❌       | The API definition's repository folder location.            |
| collection_folder | str  | ❌       | The API definition's collection repository folder location. |

# GetApiOkResponse_2Schemas

Information about the schema.

**Properties**

| Name | Type | Required | Description      |
| :--- | :--- | :------- | :--------------- |
| id\_ | str  | ❌       | The schema's ID. |

# GetApiOkResponse_2Versions

Information about the version.

**Properties**

| Name | Type | Required | Description         |
| :--- | :--- | :------- | :------------------ |
| id\_ | str  | ❌       | The version's ID.   |
| name | str  | ❌       | The version's name. |

# GetApiOkResponse_2Collections

Information about the collection.

**Properties**

| Name | Type | Required | Description          |
| :--- | :--- | :------- | :------------------- |
| id\_ | str  | ❌       | The collection's ID. |
