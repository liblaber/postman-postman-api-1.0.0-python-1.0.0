# CreateMockRequest

**Properties**

| Name | Type                  | Required | Description |
| :--- | :-------------------- | :------- | :---------- |
| mock | CreateMockRequestMock | ❌       |             |

# CreateMockRequestMock

**Properties**

| Name        | Type | Required | Description                                                                                                                     |
| :---------- | :--- | :------- | :------------------------------------------------------------------------------------------------------------------------------ |
| collection  | str  | ✅       | The unique ID of the mock's associated collection.                                                                              |
| environment | str  | ❌       | The unique ID of the mock's associated environment.                                                                             |
| name        | str  | ❌       | The mock server's name.                                                                                                         |
| private     | bool | ❌       | If true, the mock server is set private. By default, mock servers are public and can receive requests from anyone and anywhere. |
