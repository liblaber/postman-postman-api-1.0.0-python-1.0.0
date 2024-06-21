# GetSecretTypesOkResponse

**Properties**

| Name | Type                               | Required | Description |
| :--- | :--------------------------------- | :------- | :---------- |
| data | List[GetSecretTypesOkResponseData] | ❌       |             |
| meta | GetSecretTypesOkResponseMeta       | ❌       |             |

# GetSecretTypesOkResponseData

Information about the secret type.

**Properties**

| Name   | Type     | Required | Description                                                                                                                                                                                                                                                                                                 |
| :----- | :------- | :------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name   | str      | ❌       | The name of the secret type.                                                                                                                                                                                                                                                                                |
| id\_   | str      | ❌       | The ID of the secret type.                                                                                                                                                                                                                                                                                  |
| type\_ | DataType | ❌       | The origin of the secret type:<br/>- `DEFAULT` — Supported by default in Postman.<br/>- `TEAM_REGEX` — A custom regex added by an Admin or Super Admin user in the **Configure Alerts** section of the [**Team Settings**](https://learning.postman.com/docs/administration/team-settings/) interface.<br/> |

# DataType

The origin of the secret type:

- `DEFAULT` — Supported by default in Postman.
- `TEAM_REGEX` — A custom regex added by an Admin or Super Admin user in the **Configure Alerts** section of the [**Team Settings**](https://learning.postman.com/docs/administration/team-settings/) interface.

**Properties**

| Name       | Type | Required | Description  |
| :--------- | :--- | :------- | :----------- |
| DEFAULT    | str  | ✅       | "DEFAULT"    |
| TEAM_REGEX | str  | ✅       | "TEAM_REGEX" |

# GetSecretTypesOkResponseMeta

**Properties**

| Name  | Type | Required | Description                            |
| :---- | :--- | :------- | :------------------------------------- |
| total | int  | ❌       | The total number of supported secrets. |
