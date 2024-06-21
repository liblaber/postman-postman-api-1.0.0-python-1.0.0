# CreateWebhookRequest

**Properties**

| Name    | Type                        | Required | Description |
| :------ | :-------------------------- | :------- | :---------- |
| webhook | CreateWebhookRequestWebhook | ❌       |             |

# CreateWebhookRequestWebhook

**Properties**

| Name       | Type | Required | Description                                                                                              |
| :--------- | :--- | :------- | :------------------------------------------------------------------------------------------------------- |
| collection | str  | ❌       | The unique ID of the collection to trigger when calling this webhook.                                    |
| name       | str  | ❌       | The webhook's name. On success, the system creates a new monitor with this name in the **Monitors** tab. |
