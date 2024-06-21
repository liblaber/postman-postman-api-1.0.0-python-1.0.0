# GetAllPanAddElementRequestsOkResponse

**Properties**

| Name     | Type                                                | Required | Description                                                                |
| :------- | :-------------------------------------------------- | :------- | :------------------------------------------------------------------------- |
| requests | List[GetAllPanAddElementRequestsOkResponseRequests] | ❌       | Information about the requests to add elements to the Private API Network. |
| meta     | GetAllPanAddElementRequestsOkResponseMeta           | ❌       | The response's non-standard meta information.                              |

# GetAllPanAddElementRequestsOkResponseRequests

**Properties**

| Name       | Type             | Required | Description                                                                                                                       |
| :--------- | :--------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------- |
| id\_       | int              | ❌       | The request's ID.                                                                                                                 |
| created_at | str              | ❌       | The date and time at which the request was created.                                                                               |
| created_by | int              | ❌       | The ID of the user who created the request.                                                                                       |
| message    | str              | ❌       | The user's optional message included in the request.                                                                              |
| status     | RequestsStatus   | ❌       | The request's status.                                                                                                             |
| element    | RequestsElement  | ❌       | Information about the requested element.                                                                                          |
| response   | RequestsResponse | ❌       | Information about the response to the request. This object only returns when the network manager denied a request with a message. |

# RequestsStatus

The request's status.

**Properties**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| PENDING | str  | ✅       | "pending"   |
| DENIED  | str  | ✅       | "denied"    |

# RequestsElement

Information about the requested element.

**Properties**

| Name    | Type         | Required | Description                                 |
| :------ | :----------- | :------- | :------------------------------------------ |
| id\_    | str          | ❌       | The element's ID.                           |
| type\_  | ElementType1 | ❌       | The element type.                           |
| name    | str          | ❌       | The element's name.                         |
| summary | str          | ❌       | If applicable, the element's short summary. |

# ElementType_1

The element type.

**Properties**

| Name       | Type | Required | Description  |
| :--------- | :--- | :------- | :----------- |
| API        | str  | ✅       | "api"        |
| WORKSPACE  | str  | ✅       | "workspace"  |
| COLLECTION | str  | ✅       | "collection" |

# RequestsResponse

Information about the response to the request. This object only returns when the network manager denied a request with a message.

**Properties**

| Name       | Type | Required | Description                                                        |
| :--------- | :--- | :------- | :----------------------------------------------------------------- |
| created_at | str  | ❌       | The date and time at which the network manager denied the request. |
| created_by | int  | ❌       | The network manager's user ID.                                     |
| message    | str  | ❌       | The network manager's request response message.                    |

# GetAllPanAddElementRequestsOkResponseMeta

The response's non-standard meta information.

**Properties**

| Name        | Type | Required | Description                                       |
| :---------- | :--- | :------- | :------------------------------------------------ |
| limit       | int  | ❌       | The maximum number of items returned.             |
| offset      | int  | ❌       | The zero-based offset of the first item returned. |
| total_count | int  | ❌       | The total count of items found.                   |
