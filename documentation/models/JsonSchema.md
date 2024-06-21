# JsonSchema

**Properties**

| Name    | Type           | Required | Description                                                                                                                                                                                                                                                                                                                              |
| :------ | :------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| type\_  | JsonSchemaType | ✅       | The OpenAPI definition type.                                                                                                                                                                                                                                                                                                             |
| input   | dict           | ✅       | An object that contains a valid JSON OpenAPI definition. For more information, read the [OpenAPI documentation](https://swagger.io/docs/specification/basic-structure/).                                                                                                                                                                 |
| options | dict           | ❌       | An object that contains advanced creation options and their values. You can find a complete list of properties and their values in Postman's [OpenAPI 3.0 to Postman Collection v2.1.0 Converter OPTIONS documentation](https://github.com/postmanlabs/openapi-to-postman/blob/develop/OPTIONS.md). These properties are case-sensitive. |

# JsonSchemaType

The OpenAPI definition type.

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| JSON | str  | ✅       | "json"      |
