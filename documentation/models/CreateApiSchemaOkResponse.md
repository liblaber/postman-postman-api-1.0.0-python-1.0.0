# CreateApiSchemaOkResponse

Information about the created API schema.

**Properties**

| Name       | Type                                 | Required | Description                                             |
| :--------- | :----------------------------------- | :------- | :------------------------------------------------------ |
| id\_       | str                                  | ❌       | The schema's ID.                                        |
| type\_     | CreateApiSchemaOkResponseType        | ❌       | The schema's type.                                      |
| files      | List[CreateApiSchemaOkResponseFiles] | ❌       | The list of the schema's files.                         |
| created_at | str                                  | ❌       | The date and time at which the schema was created.      |
| created_by | str                                  | ❌       | The user ID of the user that created the schema.        |
| updated_at | str                                  | ❌       | The date and time at which the schema was last updated. |
| updated_by | str                                  | ❌       | The user ID of the user that updated the schema.        |

# CreateApiSchemaOkResponseType

The schema's type.

**Properties**

| Name        | Type | Required | Description   |
| :---------- | :--- | :------- | :------------ |
| PROTO_2     | str  | ✅       | "proto:2"     |
| PROTO_3     | str  | ✅       | "proto:3"     |
| GRAPHQL     | str  | ✅       | "graphql"     |
| OPENAPI_3_1 | str  | ✅       | "openapi:3_1" |
| OPENAPI_3   | str  | ✅       | "openapi:3"   |
| OPENAPI_2   | str  | ✅       | "openapi:2"   |
| OPENAPI_1   | str  | ✅       | "openapi:1"   |
| RAML_1      | str  | ✅       | "raml:1"      |
| RAML_0_8    | str  | ✅       | "raml:0_8"    |
| WSDL_2      | str  | ✅       | "wsdl:2"      |
| WSDL_1      | str  | ✅       | "wsdl:1"      |
| ASYNCAPI_2  | str  | ✅       | "asyncapi:2"  |

# CreateApiSchemaOkResponseFiles

Information about the schema file.

**Properties**

| Name       | Type | Required | Description                                           |
| :--------- | :--- | :------- | :---------------------------------------------------- |
| id\_       | str  | ❌       | The schema file's ID.                                 |
| name       | str  | ❌       | The schema file's name.                               |
| path       | str  | ❌       | The file system path to the schema file.              |
| created_at | str  | ❌       | The date and time at which the file was created.      |
| created_by | str  | ❌       | The user ID of the user that created the file.        |
| updated_at | str  | ❌       | The date and time at which the file was last updated. |
| updated_by | str  | ❌       | The user ID of the user that last updated the file.   |
