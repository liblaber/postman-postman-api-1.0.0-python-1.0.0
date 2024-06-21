# CreateEnvironmentRequest

**Properties**

| Name        | Type                                | Required | Description |
| :---------- | :---------------------------------- | :------- | :---------- |
| environment | CreateEnvironmentRequestEnvironment | ❌       |             |

# CreateEnvironmentRequestEnvironment

**Properties**

| Name   | Type                     | Required | Description                                    |
| :----- | :----------------------- | :------- | :--------------------------------------------- |
| name   | str                      | ✅       | The environment's name.                        |
| values | List[EnvironmentValues1] | ❌       | Information about the environment's variables. |

# EnvironmentValues_1

**Properties**

| Name    | Type        | Required | Description                       |
| :------ | :---------- | :------- | :-------------------------------- |
| enabled | bool        | ❌       | If true, the variable is enabled. |
| key     | str         | ❌       | The variable's name.              |
| value   | str         | ❌       | The variable's value.             |
| type\_  | ValuesType1 | ❌       | The variable type.                |

# ValuesType_1

The variable type.

**Properties**

| Name    | Type | Required | Description |
| :------ | :--- | :------- | :---------- |
| SECRET  | str  | ✅       | "secret"    |
| DEFAULT | str  | ✅       | "default"   |
| ANY     | str  | ✅       | "any"       |
