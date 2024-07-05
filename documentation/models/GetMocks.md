# GetMocks

**Properties**

| Name  | Type                | Required | Description |
| :---- | :------------------ | :------- | :---------- |
| mocks | List[GetMocksMocks] | ❌       |             |

# GetMocksMocks

Information about the mock servers.

**Properties**

| Name        | Type        | Required | Description                                                                                                                        |
| :---------- | :---------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| id\_        | str         | ❌       | The mock server's ID.                                                                                                              |
| owner       | str         | ❌       | The ID of mock server's owner.                                                                                                     |
| uid         | str         | ❌       | The mock server's unique ID.                                                                                                       |
| collection  | str         | ❌       | The unique ID of the mock's associated collection.                                                                                 |
| mock_url    | str         | ❌       | The mock server URL.                                                                                                               |
| config      | MocksConfig | ❌       | Information about the mock server's configuration.                                                                                 |
| created_at  | str         | ❌       | The date and time at which the mock server was created.                                                                            |
| environment | str         | ❌       | The mock server's associated environment ID.                                                                                       |
| is_public   | bool        | ❌       | If true, the mock server is public and visible to all users. This field does not indicate the mock server's access control status. |
| name        | str         | ❌       | The mock server's name.                                                                                                            |
| updated_at  | str         | ❌       | The date and time at which the mock server was last updated.                                                                       |

# MocksConfig

Information about the mock server's configuration.

**Properties**

| Name               | Type      | Required | Description                                                                                                                                        |
| :----------------- | :-------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------- |
| delay              | Delay     | ❌       | Information about the mock server's simulated network delay settings. This returns a null value if there are no configured network delay settings. |
| headers            | List[str] | ❌       | A list of the mock server's headers.                                                                                                               |
| match_body         | bool      | ❌       | If true, match the request body.                                                                                                                   |
| match_query_params | bool      | ❌       | If true, match query parameters.                                                                                                                   |
| match_wildcards    | bool      | ❌       | If true, use wildcard variable matching.                                                                                                           |
| server_response_id | str       | ❌       | The ID of mock server's default response for requests. All calls to the mock server will return the defined response.                              |

# Delay

Information about the mock server's simulated network delay settings. This returns a null value if there are no configured network delay settings.

**Properties**

| Name     | Type      | Required | Description                                                                                                                                       |
| :------- | :-------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------ |
| type\_   | DelayType | ❌       | The type of simulated delay value: - `fixed` — The delay value is a fixed value.                                                                  |
| preset   | Preset    | ❌       | The simulated fixed network delay value: - `1` — 2G (300 ms). - `2` — 3G (100 ms). The object does not return this value for custom delay values. |
| duration | int       | ❌       | The configured delay, in milliseconds.                                                                                                            |

# DelayType

The type of simulated delay value:

- `fixed` — The delay value is a fixed value.

**Properties**

| Name  | Type | Required | Description |
| :---- | :--- | :------- | :---------- |
| FIXED | str  | ✅       | "fixed"     |

# Preset

The simulated fixed network delay value:

- `1` — 2G (300 ms).
- `2` — 3G (100 ms).
  The object does not return this value for custom delay values.

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| \_1  | str  | ✅       | "1"         |
| \_2  | str  | ✅       | "2"         |

<!-- This file was generated by liblab | https://liblab.com/ -->
