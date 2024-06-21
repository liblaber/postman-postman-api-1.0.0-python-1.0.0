# GetApiSchemaFilesOkResponse

Information about the schema files and its meta information.

**Properties**

| Name  | Type                                   | Required | Description                                 |
| :---- | :------------------------------------- | :------- | :------------------------------------------ |
| meta  | GetApiSchemaFilesOkResponseMeta        | ❌       | The schema's non-standard meta information. |
| files | List[GetApiSchemaFilesOkResponseFiles] | ❌       | The schema's files.                         |

# GetApiSchemaFilesOkResponseMeta

The schema's non-standard meta information.

**Properties**

| Name        | Type | Required | Description                                                     |
| :---------- | :--- | :------- | :-------------------------------------------------------------- |
| next_cursor | str  | ❌       | The pointer to the next record in the set of paginated results. |

# GetApiSchemaFilesOkResponseFiles

Information about the schema file.

**Properties**

| Name       | Type | Required | Description                                           |
| :--------- | :--- | :------- | :---------------------------------------------------- |
| id\_       | str  | ❌       | The schema file's ID.                                 |
| name       | str  | ❌       | The schema file's name.                               |
| path       | str  | ❌       | The file system path to the schema file.              |
| created_at | str  | ❌       | The date and time at which the file was created.      |
| created_by | int  | ❌       | The user Id of the user that created the file.        |
| updated_at | str  | ❌       | The date and time at which the file was last updated. |
| updated_by | int  | ❌       | The user ID of the user that last updated the file.   |
