# JsonStringified

**Properties**

| Name    | Type                | Required | Description                                                                                                                                                                                                                                                                                                                              |
| :------ | :------------------ | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| type\_  | JsonStringifiedType | ❌       | The OpenAPI definition type.                                                                                                                                                                                                                                                                                                             |
| input   | str                 | ❌       | The stringified OpenAPI definition.                                                                                                                                                                                                                                                                                                      |
| options | dict                | ❌       | An object that contains advanced creation options and their values. You can find a complete list of properties and their values in Postman's [OpenAPI 3.0 to Postman Collection v2.1.0 Converter OPTIONS documentation](https://github.com/postmanlabs/openapi-to-postman/blob/develop/OPTIONS.md). These properties are case-sensitive. |

# JsonStringifiedType

The OpenAPI definition type.

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| JSON | str  | ✅       | "json"      |
