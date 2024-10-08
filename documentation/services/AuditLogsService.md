# AuditLogsService

A list of all methods in the `AuditLogsService` service. Click on the method name to view detailed information about that method.

| Methods                           | Description                                                                                                                                                                                              |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [get_audit_logs](#get_audit_logs) | Gets a list of your team's generated audit events. For a complete list of all audit events, read our [Utilizing audit logs](https://learning.postman.com/docs/administration/audit-logs/) documentation. |

## get_audit_logs

Gets a list of your team's generated audit events. For a complete list of all audit events, read our [Utilizing audit logs](https://learning.postman.com/docs/administration/audit-logs/) documentation.

- HTTP Method: `GET`
- Endpoint: `/audit/logs`

**Parameters**

| Name     | Type                                                  | Required | Description                                                                                                                                |
| :------- | :---------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| since    | str                                                   | ❌       | Return logs created after the given time, in `YYYY-MM-DD` format.                                                                          |
| until    | str                                                   | ❌       | Return logs created before the given time, in `YYYY-MM-DD` format.                                                                         |
| limit    | int                                                   | ❌       | The maximum number of audit events to return at once.                                                                                      |
| cursor   | str                                                   | ❌       | The pointer to the first record of the set of paginated results. To view the next response, use the `nextCursor` value for this parameter. |
| order_by | [AscDescDefaultDesc](../models/AscDescDefaultDesc.md) | ❌       | Return the records in ascending (`asc`) or descending (`desc`) order.                                                                      |

**Return Type**

`GetAuditLogs`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import AscDescDefaultDesc

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.audit_logs.get_audit_logs(
    since="2022-08-30",
    until="2022-09-15",
    limit=50,
    cursor="RnJpIEZlYiAyNCAyMDIzIDEzOjI0OjA5IEdNVCswMDAwIChDb29yZGluYXRlZCBVbml2ZXJzYWwgVGltZSk=",
    order_by="asc"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
