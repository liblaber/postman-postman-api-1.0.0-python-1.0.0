# GlobalVariable

Information about the global variable.

**Properties**

| Name    | Type               | Required | Description                                                                                           |
| :------ | :----------------- | :------- | :---------------------------------------------------------------------------------------------------- |
| key     | str                | ❌       | The variable's name.                                                                                  |
| type\_  | GlobalVariableType | ❌       | The [type](https://learning.postman.com/docs/sending-requests/variables/#variable-types) of variable. |
| value   | str                | ❌       | The variable's value.                                                                                 |
| enabled | bool               | ❌       | If true, the variable is enabled.                                                                     |

# GlobalVariableType

The [type](https://learning.postman.com/docs/sending-requests/variables/#variable-types) of variable.

**Properties**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| DEFAULT | str  | ✅       | "default"   |
| SECRET  | str  | ✅       | "secret"    |
