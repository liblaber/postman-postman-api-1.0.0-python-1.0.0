# ApiSecurityService

A list of all methods in the `ApiSecurityService` service. Click on the method name to view detailed information about that method.

| Methods                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                     |
| :-------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [schema_security_validation](#schema_security_validation) | Performs an analysis on the given definition and returns any issues based on your [predefined rulesets](https://learning.postman.com/docs/api-governance/configurable-rules/configurable-rules-overview/). This endpoint can help you understand the violations' impact and offers solutions to help you resolve any errors. You can include this endpoint to your CI/CD process to automate schema validation. |

For more information, see our [Rule violations in the API definition](https://learning.postman.com/docs/api-governance/api-definition/api-definition-warnings/) documentation.

**Note:**

- The maximum allowed size of the definition is 10 MB.
- You must [import and enable](https://learning.postman.com/docs/api-governance/configurable-rules/configuring-api-security-rules/) [Postman's OWASP security rules](https://postman.postman.co/api-governance/libraries/postman_owasp/view) in Postman for this endpoint to return any security rule violations.
  |

## schema_security_validation

Performs an analysis on the given definition and returns any issues based on your [predefined rulesets](https://learning.postman.com/docs/api-governance/configurable-rules/configurable-rules-overview/). This endpoint can help you understand the violations' impact and offers solutions to help you resolve any errors. You can include this endpoint to your CI/CD process to automate schema validation.

For more information, see our [Rule violations in the API definition](https://learning.postman.com/docs/api-governance/api-definition/api-definition-warnings/) documentation.

**Note:**

- The maximum allowed size of the definition is 10 MB.
- You must [import and enable](https://learning.postman.com/docs/api-governance/configurable-rules/configuring-api-security-rules/) [Postman's OWASP security rules](https://postman.postman.co/api-governance/libraries/postman_owasp/view) in Postman for this endpoint to return any security rule violations.

- HTTP Method: `POST`
- Endpoint: `/security/api-validation`

**Parameters**

| Name         | Type                                                                            | Required | Description       |
| :----------- | :------------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [SchemaSecurityValidationRequest](../models/SchemaSecurityValidationRequest.md) | ❌       | The request body. |

**Return Type**

`SchemaSecurityValidationOkResponse`

**Example Usage Code Snippet**

```python
from postman import Postman, Environment
from postman.models import SchemaSecurityValidationRequest

sdk = Postman(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = SchemaSecurityValidationRequest(
    schema={
        "language": "json",
        "schema": "{\"openapi\":\"3.0.0\",\"info\":{\"version\":\"1\",\"title\":\"temp\",\"license\":{\"name\":\"MIT\"}},\"servers\":[{\"url\":\"https://petstore.swagger.io/v1\"}],\"paths\":{\"/user\":{\"get\":{\"summary\":\"Details about a user\",\"operationId\":\"listUser\",\"tags\":[\"user\"],\"parameters\":[{\"name\":\"id\",\"in\":\"query\",\"description\":\"ID of the user\",\"required\":true,\"schema\":{\"type\":\"integer\",\"format\":\"int32\"}}],\"responses\":{\"200\":{\"description\":\"Details about a user\",\"headers\":{\"x-next\":{\"description\":\"A link to the next page of responses\",\"schema\":{\"type\":\"string\"}}},\"content\":{\"application/json\":{\"schema\":{$ref:\"#/components/schemas/User\"}}}},\"default\":{\"description\":\"unexpected error\",\"content\":{\"application/json\":{\"schema\":{$ref:\"#/components/schemas/Error\"}}}}}}}},\"components\":{\"schemas\":{\"User\":{\"type\":\"object\",\"required\":[\"id\",\"name\"],\"properties\":{\"id\":{\"type\":\"integer\",\"format\":\"int64\"},\"name\":{\"type\":\"string\"},\"tag\":{\"type\":\"string\"}}},\"Error\":{\"type\":\"object\",\"required\":[\"code\",\"message\"],\"properties\":{\"code\":{\"type\":\"integer\",\"format\":\"int32\"},\"message\":{\"type\":\"string\"}}}},\"securitySchemes\":{\"BasicAuth\":{\"type\":\"http\",\"scheme\":\"basic\"}}},\"security\":[{\"BasicAuth\":[]}]}",
        "type_": "openapi3"
    }
)

result = sdk.api_security.schema_security_validation(request_body=request_body)

print(result)
```
