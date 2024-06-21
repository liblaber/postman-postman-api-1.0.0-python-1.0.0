# PatchCollectionRequest

**Properties**

| Name       | Type                             | Required | Description |
| :--------- | :------------------------------- | :------- | :---------- |
| collection | PatchCollectionRequestCollection | ❌       |             |

# PatchCollectionRequestCollection

**Properties**

| Name      | Type            | Required | Description                                                                                                                                                                                 |
| :-------- | :-------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| info      | CollectionInfo2 | ❌       | An object that contains the collection's updated name and description.                                                                                                                      |
| variables | dict            | ❌       | The collection's updated variables. Refer to `"#/definitions/variable"` in the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json).            |
| auth      | dict            | ❌       | The collection's updated authentication. Refer to `"#/definitions/auth-attribute"` in the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json). |
| events    | dict            | ❌       | The collection's updated events. Refer to `"#/definitions/event"` in the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json).                  |

# CollectionInfo_2

An object that contains the collection's updated name and description.

**Properties**

| Name        | Type | Required | Description                           |
| :---------- | :--- | :------- | :------------------------------------ |
| name        | str  | ❌       | The collection's updated name.        |
| description | str  | ❌       | The collection's updated description. |
