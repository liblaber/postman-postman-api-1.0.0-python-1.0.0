# DeleteCollectionResponseOkResponse

**Properties**

| Name     | Type                                   | Required | Description                                                                                                                                                                         |
| :------- | :------------------------------------- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| model_id | str                                    | ❌       | The response's ID.                                                                                                                                                                  |
| meta     | dict                                   | ❌       | A Postman-specific response that contains information about the internal performed operation.                                                                                       |
| data     | DeleteCollectionResponseOkResponseData | ❌       | The response's information.                                                                                                                                                         |
| revision | float                                  | ❌       | An internal revision ID. Its value increments each time the resource changes. You can use this ID to track whether there were changes since the last time you fetched the resource. |

# DeleteCollectionResponseOkResponseData

The response's information.

**Properties**

| Name  | Type | Required | Description                         |
| :---- | :--- | :------- | :---------------------------------- |
| id\_  | str  | ❌       | The response's ID.                  |
| owner | str  | ❌       | The user ID of the request's owner. |
