# CreateApiVersionRequest

# CreateApiVersionRequest_1

Information about the API version.

**Properties**

| Name          | Type                                      | Required | Description                                                              |
| :------------ | :---------------------------------------- | :------- | :----------------------------------------------------------------------- |
| name          | str                                       | ✅       | The version's name.                                                      |
| schemas       | List[CreateApiVersionRequest1Schemas]     | ✅       | A list of the version's schemas.                                         |
| collections   | List[CreateApiVersionRequest1Collections] | ✅       | A list of the version's collections.                                     |
| release_notes | str                                       | ❌       | Information about the API version release. For example, changelog notes. |

# CreateApiVersionRequest_1Schemas

Information about the schema.

**Properties**

| Name | Type | Required | Description      |
| :--- | :--- | :------- | :--------------- |
| id\_ | str  | ❌       | The schema's ID. |

# CreateApiVersionRequest_1Collections

Information about the collection.

**Properties**

| Name | Type | Required | Description          |
| :--- | :--- | :------- | :------------------- |
| id\_ | str  | ❌       | The collection's ID. |

# CreateApiVersionRequest_2

Information about the API version.

**Properties**

| Name          | Type                                      | Required | Description                                                              |
| :------------ | :---------------------------------------- | :------- | :----------------------------------------------------------------------- |
| name          | str                                       | ✅       | The version's name.                                                      |
| branch        | str                                       | ✅       | The branch ID.                                                           |
| schemas       | List[CreateApiVersionRequest2Schemas]     | ✅       | A list of the version's schemas.                                         |
| collections   | List[CreateApiVersionRequest2Collections] | ✅       | A list of the version's collections.                                     |
| release_notes | str                                       | ❌       | Information about the API version release. For example, changelog notes. |

# CreateApiVersionRequest_2Schemas

Information about the schema.

**Properties**

| Name      | Type | Required | Description                                             |
| :-------- | :--- | :------- | :------------------------------------------------------ |
| file_path | str  | ❌       | The path to the schema root file in the Git repository. |

# CreateApiVersionRequest_2Collections

Information about the collection.

**Properties**

| Name      | Type | Required | Description                                 |
| :-------- | :--- | :------- | :------------------------------------------ |
| file_path | str  | ❌       | Path to a collection in the Git repository. |

# CreateApiVersionRequest_3

Information about the API version.

**Properties**

| Name          | Type                                      | Required | Description                                                              |
| :------------ | :---------------------------------------- | :------- | :----------------------------------------------------------------------- |
| name          | str                                       | ✅       | The version's name.                                                      |
| branch        | str                                       | ✅       | The branch ID.                                                           |
| schemas       | List[CreateApiVersionRequest3Schemas]     | ✅       | A list of the version's schemas.                                         |
| collections   | List[CreateApiVersionRequest3Collections] | ✅       | A list of the version's collections.                                     |
| release_notes | str                                       | ❌       | Information about the API version release. For example, changelog notes. |

# CreateApiVersionRequest_3Schemas

Information about the schema.

**Properties**

| Name           | Type | Required | Description                                                                    |
| :------------- | :--- | :------- | :----------------------------------------------------------------------------- |
| directory_path | str  | ❌       | The path to the root directory where schemas are stored in the Git repository. |

# CreateApiVersionRequest_3Collections

Information about the collection.

**Properties**

| Name      | Type | Required | Description                                       |
| :-------- | :--- | :------- | :------------------------------------------------ |
| file_path | str  | ❌       | The path to the collection in the Git repository. |
