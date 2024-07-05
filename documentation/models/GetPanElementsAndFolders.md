# GetPanElementsAndFolders

**Properties**

| Name     | Type                         | Required | Description                                                                                                |
| :------- | :--------------------------- | :------- | :--------------------------------------------------------------------------------------------------------- |
| elements | List[Elements]               | ❌       | Information about a Private API Network's folder elements. Elements are APIs, collections, and workspaces. |
| folders  | List[Folders]                | ❌       | Information about the Private API Network's folders.                                                       |
| meta     | GetPanElementsAndFoldersMeta | ❌       | The response's non-standard meta information.                                                              |

# Elements

**Properties**

| Name             | Type | Required | Description                                                                                                                   |
| :--------------- | :--- | :------- | :---------------------------------------------------------------------------------------------------------------------------- |
| created_at       | str  | ❌       | The date and time at which the element was created.                                                                           |
| created_by       | int  | ❌       | The user who created the element.                                                                                             |
| updated_at       | str  | ❌       | The date and time at which the element was last updated.                                                                      |
| updated_by       | int  | ❌       | The user who updated the element.                                                                                             |
| added_at         | str  | ❌       | The date and time at which the element was published to Private API Network. This value is the same as the `updatedAt` value. |
| added_by         | int  | ❌       | The user ID of the user who published the element.                                                                            |
| description      | str  | ❌       | The element's description.                                                                                                    |
| id\_             | str  | ❌       | The element's ID.                                                                                                             |
| name             | str  | ❌       | The element's name.                                                                                                           |
| summary          | str  | ❌       | The element's summary.                                                                                                        |
| type\_           | str  | ❌       | The element's type.                                                                                                           |
| parent_folder_id | int  | ❌       | The element's parent folder ID.                                                                                               |
| href             | str  | ❌       | The element's HREF.                                                                                                           |

# Folders

**Properties**

| Name             | Type | Required | Description                                        |
| :--------------- | :--- | :------- | :------------------------------------------------- |
| id\_             | int  | ❌       | The folder's ID.                                   |
| parent_folder_id | int  | ❌       | The folder's parent folder ID.                     |
| updated_at       | str  | ❌       | The date and time at which the folder was updated. |
| updated_by       | int  | ❌       | The user ID of the user who updated the folder.    |
| created_at       | str  | ❌       | The date and time at which the folder was created. |
| created_by       | int  | ❌       | The user who created the folder.                   |
| name             | str  | ❌       | The folder's name.                                 |
| description      | str  | ❌       | The folder's description.                          |
| type\_           | str  | ❌       | The element's type. This value is always `folder`. |

# GetPanElementsAndFoldersMeta

The response's non-standard meta information.

**Properties**

| Name        | Type | Required | Description                                                                                                                       |
| :---------- | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------------------- |
| limit       | int  | ❌       | The maximum number of elements returned. If the value exceeds the maximum value of `1000`, then the system uses the `1000` value. |
| offset      | int  | ❌       | The zero-based offset of the first item returned.                                                                                 |
| total_count | int  | ❌       | The total count of the `elements` and `folders` items.                                                                            |

<!-- This file was generated by liblab | https://liblab.com/ -->
