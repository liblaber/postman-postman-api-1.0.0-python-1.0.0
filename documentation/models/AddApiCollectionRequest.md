# AddApiCollectionRequest

# AddApiCollection_1

**Properties**

| Name           | Type                           | Required | Description                   |
| :------------- | :----------------------------- | :------- | :---------------------------- |
| data           | AddApiCollection1Data          | ❌       |                               |
| operation_type | AddApiCollection1OperationType | ❌       | The `COPY_COLLECTION` method. |

# AddApiCollection_1Data

**Properties**

| Name          | Type | Required | Description                           |
| :------------ | :--- | :------- | :------------------------------------ |
| collection_id | str  | ❌       | The collection ID to copy to the API. |

# AddApiCollection_1OperationType

The `COPY_COLLECTION` method.

**Properties**

| Name           | Type | Required | Description       |
| :------------- | :--- | :------- | :---------------- |
| COPYCOLLECTION | str  | ✅       | "COPY_COLLECTION" |

# AddApiCollection_2

**Properties**

| Name           | Type                           | Required | Description                                                                                                                                                                                                                                                                                                                   |
| :------------- | :----------------------------- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name           | str                            | ❌       | The collection's name.                                                                                                                                                                                                                                                                                                        |
| operation_type | AddApiCollection2OperationType | ❌       | The `GENERATE_FROM_SCHEMA` method.                                                                                                                                                                                                                                                                                            |
| options        | dict                           | ❌       | The advanced creation options for collections and their values. For a complete list of properties and their values, see Postman's [OpenAPI 3.0 to Postman Collection v2.1.0 Converter OPTIONS documentation](https://github.com/postmanlabs/openapi-to-postman/blob/develop/OPTIONS.md). These properties are case-sensitive. |

# AddApiCollection_2OperationType

The `GENERATE_FROM_SCHEMA` method.

**Properties**

| Name               | Type | Required | Description            |
| :----------------- | :--- | :------- | :--------------------- |
| GENERATEFROMSCHEMA | str  | ✅       | "GENERATE_FROM_SCHEMA" |

# AddApiCollection_3

**Properties**

| Name           | Type                           | Required | Description                                                                                                                                                                                                                |
| :------------- | :----------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| data           | AddApiCollection3Data          | ❌       | Information about the collection's contents, such as requests and responses. For a complete list of values, refer to the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json). |
| operation_type | AddApiCollection3OperationType | ❌       | The `CREATE_NEW` method.                                                                                                                                                                                                   |

# AddApiCollection_3Data

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

| Name                                                       | Type | Required | Description                                                            |
| :--------------------------------------------------------- | :--- | :------- | :--------------------------------------------------------------------- |
| HTTPSSCHEMAGETPOSTMANCOMJSONCOLLECTIONV2_1_0COLLECTIONJSON | str  | ✅       | "https://schema.getpostman.com/json/collection/v2.1.0/collection.json" |

# AddApiCollection_3OperationType

The `CREATE_NEW` method.

**Properties**

| Name      | Type | Required | Description  |
| :-------- | :--- | :------- | :----------- |
| CREATENEW | str  | ✅       | "CREATE_NEW" |

<!-- This file was generated by liblab | https://liblab.com/ -->
