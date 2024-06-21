# PullCollectionChangesOkResponse

**Properties**

| Name       | Type                                      | Required | Description                                    |
| :--------- | :---------------------------------------- | :------- | :--------------------------------------------- |
| collection | PullCollectionChangesOkResponseCollection | ❌       | Information about the updated collection fork. |

# PullCollectionChangesOkResponseCollection

Information about the updated collection fork.

**Properties**

| Name           | Type | Required | Description                                                   |
| :------------- | :--- | :------- | :------------------------------------------------------------ |
| destination_id | str  | ❌       | The ID of the forked collection the changes were pulled into. |
| source_id      | str  | ❌       | The ID of the source collection the changes were pulled from. |
