# RespondPanElementAddRequestOkResponse

**Properties**

| Name    | Type                                      | Required | Description                                        |
| :------ | :---------------------------------------- | :------- | :------------------------------------------------- |
| request | List[RespondPanElementAddRequestRequest2] | ❌       | Information about the Private API Network request. |

# RespondPanElementAddRequestRequest_2

**Properties**

| Name       | Type            | Required | Description                                                                                                                                 |
| :--------- | :-------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------ |
| id\_       | int             | ❌       | The request's ID.                                                                                                                           |
| created_at | str             | ❌       | The date and time at which the request was created.                                                                                         |
| created_by | int             | ❌       | The ID of the user who created the request.                                                                                                 |
| message    | str             | ❌       | The user's optional message included in the request.                                                                                        |
| response   | RequestResponse | ❌       | Information about the response to the element's request. This object only returns when the network manager denied a request with a message. |
| element    | RequestElement  | ❌       | Information about the requested element.                                                                                                    |
| status     | RequestStatus   | ❌       | The request's status.                                                                                                                       |

# RequestResponse

Information about the response to the element's request. This object only returns when the network manager denied a request with a message.

**Properties**

| Name       | Type | Required | Description                                                        |
| :--------- | :--- | :------- | :----------------------------------------------------------------- |
| created_at | str  | ❌       | The date and time at which the network manager denied the request. |
| created_by | int  | ❌       | The network manager's user ID.                                     |
| message    | str  | ❌       | The network manager's request response message.                    |

# RequestElement

Information about the requested element.

**Properties**

| Name       | Type         | Required | Description                                                                               |
| :--------- | :----------- | :------- | :---------------------------------------------------------------------------------------- |
| id\_       | str          | ❌       | The element's ID.                                                                         |
| created_at | str          | ❌       | The date and time at which the element was approved and added to the Private API Network. |
| created_by | int          | ❌       | The user ID of the user who requested to add the element to the Private API Network.      |
| type\_     | ElementType2 | ❌       | The element type.                                                                         |
| name       | str          | ❌       | The element's name.                                                                       |
| summary    | str          | ❌       | If applicable, the element's short summary.                                               |

# ElementType_2

The element type.

**Properties**

| Name       | Type | Required | Description  |
| :--------- | :--- | :------- | :----------- |
| API        | str  | ✅       | "api"        |
| WORKSPACE  | str  | ✅       | "workspace"  |
| COLLECTION | str  | ✅       | "collection" |

# RequestStatus

The request's status.

**Properties**

| Name     | Type | Required | Description |
| :------- | :--- | :------- | :---------- |
| APPROVED | str  | ✅       | "approved"  |
| DENIED   | str  | ✅       | "denied"    |

<!-- This file was generated by liblab | https://liblab.com/ -->
