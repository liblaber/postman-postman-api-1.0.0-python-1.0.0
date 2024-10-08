# DeleteCollectionFolder

**Properties**

| Name     | Type                       | Required | Description                                                                                                                                                                         |
| :------- | :------------------------- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| data     | DeleteCollectionFolderData | ❌       | The folder's information.                                                                                                                                                           |
| meta     | dict                       | ❌       | A Postman-specific response that contains information about the internal performed operation.                                                                                       |
| model_id | str                        | ❌       | The folder's ID.                                                                                                                                                                    |
| revision | float                      | ❌       | An internal revision ID. Its value increments each time the resource changes. You can use this ID to track whether there were changes since the last time you fetched the resource. |

# DeleteCollectionFolderData

The folder's information.

**Properties**

| Name  | Type | Required | Description                        |
| :---- | :--- | :------- | :--------------------------------- |
| id\_  | str  | ❌       | The folder's ID.                   |
| owner | str  | ❌       | The user ID of the folder's owner. |

<!-- This file was generated by liblab | https://liblab.com/ -->
