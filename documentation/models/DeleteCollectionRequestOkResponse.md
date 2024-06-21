# DeleteCollectionRequestOkResponse

**Properties**

| Name     | Type                                  | Required | Description                                                                                                                                                                         |
| :------- | :------------------------------------ | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| model_id | str                                   | ❌       | The request's ID.                                                                                                                                                                   |
| meta     | dict                                  | ❌       | A Postman-specific response that contains information about the internal performed operation.                                                                                       |
| data     | DeleteCollectionRequestOkResponseData | ❌       | The request's information.                                                                                                                                                          |
| revision | float                                 | ❌       | An internal revision ID. Its value increments each time the resource changes. You can use this ID to track whether there were changes since the last time you fetched the resource. |

# DeleteCollectionRequestOkResponseData

The request's information.

**Properties**

| Name  | Type | Required | Description                         |
| :---- | :--- | :------- | :---------------------------------- |
| id\_  | str  | ❌       | The request's ID.                   |
| owner | str  | ❌       | The user ID of the request's owner. |
