# CreateCollectionRequestOkResponse

**Properties**

| Name     | Type  | Required | Description                                                                                                                                                                                                                             |
| :------- | :---- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| data     | dict  | ❌       | Information about the created request. For a complete list of properties, refer to the `definitions.request` property in the [collection.json schema file](https://schema.postman.com/collection/json/v1.0.0/draft-07/collection.json). |
| meta     | dict  | ❌       | A Postman-specific response that contains information about the internal performed operation.                                                                                                                                           |
| model_id | str   | ❌       | The request's ID.                                                                                                                                                                                                                       |
| revision | float | ❌       | An internal revision ID. Its value increments each time the resource changes. You can use this ID to track whether there were changes since the last time you fetched the resource.                                                     |
