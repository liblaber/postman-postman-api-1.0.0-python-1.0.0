# PanCreateCollection

**Properties**

| Name       | Type                          | Required | Description |
| :--------- | :---------------------------- | :------- | :---------- |
| collection | PanCreateCollectionCollection | ❌       |             |

# PanCreateCollectionCollection

**Properties**

| Name             | Type      | Required | Description                                                                      |
| :--------------- | :-------- | :------- | :------------------------------------------------------------------------------- |
| id\_             | str       | ✅       | The collection's ID.                                                             |
| parent_folder_id | int       | ✅       | The collection's parent folder ID.                                               |
| environments     | List[str] | ❌       | A list of environment UIDs (`userId`-`environmentId``) to add to the collection. |
