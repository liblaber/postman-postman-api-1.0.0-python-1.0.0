# ImportService

A list of all methods in the `ImportService` service. Click on the method name to view detailed information about that method.

| Methods                                                   | Description                                                                                                                                                 |
| :-------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [import_open_api_definition](#import_open_api_definition) | Imports an OpenAPI definition into Postman as a new [Postman Collection](https://learning.postman.com/docs/getting-started/creating-the-first-collection/). |

## import_open_api_definition

Imports an OpenAPI definition into Postman as a new [Postman Collection](https://learning.postman.com/docs/getting-started/creating-the-first-collection/).

- HTTP Method: `POST`
- Endpoint: `/import/openapi`

**Parameters**

| Name         | Type                                                                          | Required | Description         |
| :----------- | :---------------------------------------------------------------------------- | :------- | :------------------ |
| request_body | [ImportOpenApiDefinitionRequest](../models/ImportOpenApiDefinitionRequest.md) | ❌       | The request body.   |
| workspace    | str                                                                           | ❌       | The workspace's ID. |

**Return Type**

`ImportOpenApiDefinitionOkResponse`

**Example Usage Code Snippet**

```python
from postman import Postman, Environment
from postman.models.import_open_api_definition_request import JsonSchema

sdk = Postman(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = JsonSchema(
    type_="json",
    input={},
    options={}
)

result = sdk.import_.import_open_api_definition(
    request_body=request_body,
    workspace="1f0df51a-8658-4ee8-a2a1-d2567dfa09a9"
)

print(result)
```
