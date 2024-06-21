# AddApiCollectionRequest

# AddApiCollectionRequest_1

**Properties**

| Name           | Type                                  | Required | Description                   |
| :------------- | :------------------------------------ | :------- | :---------------------------- |
| data           | AddApiCollectionRequest1Data          | ❌       |                               |
| operation_type | AddApiCollectionRequest1OperationType | ❌       | The `COPY_COLLECTION` method. |

# AddApiCollectionRequest_1Data

**Properties**

| Name          | Type | Required | Description                           |
| :------------ | :--- | :------- | :------------------------------------ |
| collection_id | str  | ❌       | The collection ID to copy to the API. |

# AddApiCollectionRequest_1OperationType

The `COPY_COLLECTION` method.

**Properties**

| Name            | Type | Required | Description       |
| :-------------- | :--- | :------- | :---------------- |
| COPY_COLLECTION | str  | ✅       | "COPY_COLLECTION" |

# AddApiCollectionRequest_2

**Properties**

| Name           | Type                                  | Required | Description                                                                                                                                                                                                                                                                                                                   |
| :------------- | :------------------------------------ | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name           | str                                   | ❌       | The collection's name.                                                                                                                                                                                                                                                                                                        |
| operation_type | AddApiCollectionRequest2OperationType | ❌       | The `GENERATE_FROM_SCHEMA` method.                                                                                                                                                                                                                                                                                            |
| options        | dict                                  | ❌       | The advanced creation options for collections and their values. For a complete list of properties and their values, see Postman's [OpenAPI 3.0 to Postman Collection v2.1.0 Converter OPTIONS documentation](https://github.com/postmanlabs/openapi-to-postman/blob/develop/OPTIONS.md). These properties are case-sensitive. |

# AddApiCollectionRequest_2OperationType

The `GENERATE_FROM_SCHEMA` method.

**Properties**

| Name                 | Type | Required | Description            |
| :------------------- | :--- | :------- | :--------------------- |
| GENERATE_FROM_SCHEMA | str  | ✅       | "GENERATE_FROM_SCHEMA" |

# AddApiCollectionRequest_3

**Properties**

| Name           | Type                                  | Required | Description                                                                                                                                                                                                                |
| :------------- | :------------------------------------ | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| data           | AddApiCollectionRequest3Data          | ❌       | Information about the collection's contents, such as requests and responses. For a complete list of values, refer to the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json). |
| operation_type | AddApiCollectionRequest3OperationType | ❌       | The `CREATE_NEW` method.                                                                                                                                                                                                   |

# AddApiCollectionRequest_3Data

Information about the collection's contents, such as requests and responses. For a complete list of values, refer to the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json).

**Properties**

| Name | Type      | Required | Description                                                                                                                                                                                                   |
| :--- | :-------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| info | DataInfo  | ❌       | Information about the collection.                                                                                                                                                                             |
| item | List[any] | ❌       | Information about the requests and responses in the collection. For a complete list of values, refer to the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json). |

# DataInfo

Information about the collection.

**Properties**

| Name   | Type       | Required | Description                     |
| :----- | :--------- | :------- | :------------------------------ |
| name   | str        | ❌       | The collection's name.          |
| schema | InfoSchema | ❌       | The collection's schema format. |

# InfoSchema

The collection's schema format.

**Properties**

| Name                                                               | Type | Required | Description                                                            |
| :----------------------------------------------------------------- | :--- | :------- | :--------------------------------------------------------------------- |
| HTTPS_SCHEMA_GETPOSTMAN_COM_JSON_COLLECTION_V2_1_0_COLLECTION_JSON | str  | ✅       | "https://schema.getpostman.com/json/collection/v2.1.0/collection.json" |

# AddApiCollectionRequest_3OperationType

The `CREATE_NEW` method.

**Properties**

| Name       | Type | Required | Description  |
| :--------- | :--- | :------- | :----------- |
| CREATE_NEW | str  | ✅       | "CREATE_NEW" |
