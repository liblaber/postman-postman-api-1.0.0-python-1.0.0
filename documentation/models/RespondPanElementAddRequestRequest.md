# RespondPanElementAddRequestRequest

**Properties**

| Name     | Type                                       | Required | Description                         |
| :------- | :----------------------------------------- | :------- | :---------------------------------- |
| response | RespondPanElementAddRequestRequestResponse | ❌       | The response to the user's request. |
| status   | RespondPanElementAddRequestRequestStatus   | ✅       | The request's status.               |

# RespondPanElementAddRequestRequestResponse

The response to the user's request.

**Properties**

| Name    | Type | Required | Description                                               |
| :------ | :--- | :------- | :-------------------------------------------------------- |
| message | str  | ❌       | A message that details why the user's request was denied. |

# RespondPanElementAddRequestRequestStatus

The request's status.

**Properties**

| Name     | Type | Required | Description |
| :------- | :--- | :------- | :---------- |
| DENIED   | str  | ✅       | "denied"    |
| APPROVED | str  | ✅       | "approved"  |
