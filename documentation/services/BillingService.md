# BillingService

A list of all methods in the `BillingService` service. Click on the method name to view detailed information about that method.

| Methods                                       | Description                                                                            |
| :-------------------------------------------- | :------------------------------------------------------------------------------------- |
| [get_accounts](#get_accounts)                 | Gets Postman billing account details for the given team.                               |
| [get_account_invoices](#get_account_invoices) | Gets all invoices for a Postman billing account filtered by the status of the invoice. |

## get_accounts

Gets Postman billing account details for the given team.

- HTTP Method: `GET`
- Endpoint: `/accounts`

**Return Type**

`InvoicesAccountInfo`

**Example Usage Code Snippet**

```python
from postman import Postman, Environment

sdk = Postman(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.billing.get_accounts()

print(result)
```

## get_account_invoices

Gets all invoices for a Postman billing account filtered by the status of the invoice.

- HTTP Method: `GET`
- Endpoint: `/accounts/{accountId}/invoices`

**Parameters**

| Name       | Type                                                              | Required | Description           |
| :--------- | :---------------------------------------------------------------- | :------- | :-------------------- |
| account_id | str                                                               | ✅       | The account's ID.     |
| status     | [GetAccountInvoicesStatus](../models/GetAccountInvoicesStatus.md) | ✅       | The account's status. |

**Return Type**

`GetAccountInvoicesOkResponse`

**Example Usage Code Snippet**

```python
from postman import Postman, Environment
from postman.models import GetAccountInvoicesStatus

sdk = Postman(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.billing.get_account_invoices(
    account_id="123456",
    status="PAID"
)

print(result)
```
