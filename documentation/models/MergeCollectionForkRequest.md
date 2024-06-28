# MergeCollectionForkRequest

**Properties**

<<<<<<< HEAD
| Name        | Type     | Required | Description                                                                                                                                                                                                                                                                                                                                                                                        |
| :---------- | :------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| destination | str      | ✅       | The destination (parent) collection's unique ID.                                                                                                                                                                                                                                                                                                                                                   |
| source      | str      | ✅       | The source collection's unique ID.                                                                                                                                                                                                                                                                                                                                                                 |
| strategy    | Strategy | ❌       | The fork's merge strategy:<br/>- `deleteSource` — Merge the changes into the parent collection. After the merge process is complete, Postman deletes the fork. You must have Editor access to both the parent and forked collections.<br/>- `updateSourceWithDestination` — Merge the changes into the parent collection. Any differences in the parent collection are also made to the fork.<br/> |
=======
| Name        | Type     | Required | Description                                                                                                                                                                                                                                                                                                                                                                                     |
| :---------- | :------- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| destination | str      | ✅       | The destination (parent) collection's unique ID.                                                                                                                                                                                                                                                                                                                                                |
| source      | str      | ✅       | The source collection's unique ID.                                                                                                                                                                                                                                                                                                                                                              |
| strategy    | Strategy | ❌       | The fork's merge strategy:<br>- `deleteSource` — Merge the changes into the parent collection. After the merge process is complete, Postman deletes the fork. You must have Editor access to both the parent and forked collections.<br>- `updateSourceWithDestination` — Merge the changes into the parent collection. Any differences in the parent collection are also made to the fork.<br> |
>>>>>>> 95da91c (initial commit)

# Strategy

The fork's merge strategy:

- `deleteSource` — Merge the changes into the parent collection. After the merge process is complete, Postman deletes the fork. You must have Editor access to both the parent and forked collections.
- `updateSourceWithDestination` — Merge the changes into the parent collection. Any differences in the parent collection are also made to the fork.

**Properties**

| Name                        | Type | Required | Description                   |
| :-------------------------- | :--- | :------- | :---------------------------- |
| DELETESOURCE                | str  | ✅       | "deleteSource"                |
| UPDATESOURCEWITHDESTINATION | str  | ✅       | "updateSourceWithDestination" |
<<<<<<< HEAD
=======

<!-- This file was generated by liblab | https://liblab.com/ -->
>>>>>>> 95da91c (initial commit)
