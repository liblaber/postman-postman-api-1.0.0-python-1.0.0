# WebhooksService

A list of all methods in the `WebhooksService` service. Click on the method name to view detailed information about that method.

| Methods                           | Description                                                                                                                                                  |
| :-------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_webhook](#create_webhook) | Creates a webhook that triggers a collection with a custom payload. You can get the webhook's URL from the `webhookUrl` property in the endpoint's response. |

## create_webhook

Creates a webhook that triggers a collection with a custom payload. You can get the webhook's URL from the `webhookUrl` property in the endpoint's response.

- HTTP Method: `POST`
- Endpoint: `/webhooks`

**Parameters**

| Name         | Type                                                      | Required | Description         |
| :----------- | :-------------------------------------------------------- | :------- | :------------------ |
| request_body | [CreateWebhookRequest](../models/CreateWebhookRequest.md) | ❌       | The request body.   |
| workspace    | str                                                       | ❌       | The workspace's ID. |

**Return Type**

`CreateWebhookOkResponse`

**Example Usage Code Snippet**

```python
from postman import Postman, Environment
from postman.models import CreateWebhookRequest

sdk = Postman(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = CreateWebhookRequest(
    webhook={
        "collection": "12345678-12ece9e1-2abf-4edc-8e34-de66e74114d2",
        "name": "Test Webhook"
    }
)

result = sdk.webhooks.create_webhook(
    request_body=request_body,
    workspace="1f0df51a-8658-4ee8-a2a1-d2567dfa09a9"
)

print(result)
```
