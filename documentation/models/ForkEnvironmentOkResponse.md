# ForkEnvironmentOkResponse

**Properties**

| Name        | Type                                 | Required | Description                               |
| :---------- | :----------------------------------- | :------- | :---------------------------------------- |
| environment | ForkEnvironmentOkResponseEnvironment | ❌       | Information about the forked environment. |

# ForkEnvironmentOkResponseEnvironment

Information about the forked environment.

**Properties**

| Name      | Type | Required | Description                         |
| :-------- | :--- | :------- | :---------------------------------- |
| uid       | str  | ❌       | The forked environment's ID.        |
| name      | str  | ❌       | The name of the forked environment. |
| fork_name | str  | ❌       | The forked environment's label.     |
