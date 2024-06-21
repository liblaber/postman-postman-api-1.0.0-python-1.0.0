# UpdateCollectionFolderOkResponse

**Properties**

| Name     | Type  | Required | Description                                                                                                                                                                                                                    |
| :------- | :---- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| data     | dict  | ❌       | The folder's updated information, including the updated properties. For a complete list of properties, refer to the [collection.json schema file](https://schema.postman.com/collection/json/v1.0.0/draft-07/collection.json). |
| meta     | dict  | ❌       | A Postman-specific response that contains information about the internal performed operation.                                                                                                                                  |
| model_id | str   | ❌       | The folder's ID.                                                                                                                                                                                                               |
| revision | float | ❌       | An internal revision ID. Its value increments each time the resource changes. You can use this ID to track whether there were changes since the last time you fetched the resource.                                            |
