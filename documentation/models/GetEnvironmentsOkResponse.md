# GetEnvironmentsOkResponse

**Properties**

| Name         | Type                                        | Required | Description |
| :----------- | :------------------------------------------ | :------- | :---------- |
| environments | List[GetEnvironmentsOkResponseEnvironments] | ❌       |             |

# GetEnvironmentsOkResponseEnvironments

**Properties**

| Name       | Type | Required | Description                                                  |
| :--------- | :--- | :------- | :----------------------------------------------------------- |
| id\_       | str  | ❌       | The environment's ID.                                        |
| name       | str  | ❌       | The environment's name.                                      |
| created_at | str  | ❌       | The date and time at which the environment was created.      |
| updated_at | str  | ❌       | The date and time at which the environment was last updated. |
| owner      | str  | ❌       | The environment owner's ID.                                  |
| uid        | str  | ❌       | The environment's unique ID.                                 |
| is_public  | bool | ❌       | If true, the environment is public and visible to all users. |
