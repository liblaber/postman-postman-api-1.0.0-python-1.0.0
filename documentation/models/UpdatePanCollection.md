# UpdatePanCollection

**Properties**

| Name       | Type                          | Required | Description |
| :--------- | :---------------------------- | :------- | :---------- |
| collection | UpdatePanCollectionCollection | ❌       |             |

# UpdatePanCollectionCollection

**Properties**

| Name             | Type                   | Required | Description                            |
| :--------------- | :--------------------- | :------- | :------------------------------------- |
| parent_folder_id | int                    | ❌       | The collection's new parent folder ID. |
| environments     | CollectionEnvironments | ❌       | The collection's updated environments. |

# CollectionEnvironments

The collection's updated environments.

**Properties**

| Name   | Type      | Required | Description |
| :----- | :-------- | :------- | :---------- |
| add    | List[str] | ❌       |             |
| remove | List[str] | ❌       |             |

<!-- This file was generated by liblab | https://liblab.com/ -->
