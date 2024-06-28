# GetScimServiceProviderConfigOkResponse

Information about Postman's SCIM API configurations and supported operations.

**Properties**

| Name                   | Type                                       | Required | Description                                                                                                                                   |
| :--------------------- | :----------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------- |
| schemas                | List[str]                                  | ❌       | The [SCIM schema URI](https://www.iana.org/assignments/scim/scim.xhtml).                                                                      |
| documentation_uri      | str                                        | ❌       | A link to the URI's documentation.                                                                                                            |
| patch                  | Patch                                      | ❌       | Information about patch configuration.                                                                                                        |
| bulk                   | Bulk                                       | ❌       | Information about bulk configuration.                                                                                                         |
| filter                 | Filter                                     | ❌       | Information about the filter configuration.                                                                                                   |
| change_password        | ChangePassword                             | ❌       | Information about the change password configuration.                                                                                          |
| sort                   | GetScimServiceProviderConfigOkResponseSort | ❌       | Information about the sort configuration.                                                                                                     |
| authentication_schemes | List[AuthenticationSchemes]                | ❌       | A list of authentication schemes.                                                                                                             |
| etag                   | Etag                                       | ❌       | Information about the [entity tag](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag) (Etag) HTTP response header configuration. |
| meta                   | GetScimServiceProviderConfigOkResponseMeta | ❌       | The response's non-standard meta information.                                                                                                 |

# Patch

Information about patch configuration.

**Properties**

| Name      | Type | Required | Description                        |
| :-------- | :--- | :------- | :--------------------------------- |
| supported | bool | ❌       | If true, the feature is supported. |

# Bulk

Information about bulk configuration.

**Properties**

| Name             | Type  | Required | Description                                                         |
| :--------------- | :---- | :------- | :------------------------------------------------------------------ |
| max_operations   | float | ❌       | The total number of maximum operations allowed for bulk operations. |
| max_payload_size | float | ❌       | The maximum payload allowed for bulk operations.                    |
| supported        | bool  | ❌       | If true, the feature is supported.                                  |

# Filter

Information about the filter configuration.

**Properties**

| Name        | Type  | Required | Description                                                        |
| :---------- | :---- | :------- | :----------------------------------------------------------------- |
| max_results | float | ❌       | The total number of maximum results allowed for filter operations. |
| supported   | bool  | ❌       | If true, the feature is supported.                                 |

# ChangePassword

Information about the change password configuration.

**Properties**

| Name      | Type | Required | Description                        |
| :-------- | :--- | :------- | :--------------------------------- |
| supported | bool | ❌       | If true, the feature is supported. |

# GetScimServiceProviderConfigOkResponseSort

Information about the sort configuration.

**Properties**

| Name      | Type | Required | Description                        |
| :-------- | :--- | :------- | :--------------------------------- |
| supported | bool | ❌       | If true, the feature is supported. |

# AuthenticationSchemes

Information about the scheme.

**Properties**

| Name        | Type | Required | Description                                         |
| :---------- | :--- | :------- | :-------------------------------------------------- |
| description | str  | ❌       | The scheme's description.                           |
| name        | str  | ❌       | The scheme's friendly name.                         |
| spec_uri    | str  | ❌       | A link to the scheme's specification documentation. |
| type\_      | str  | ❌       | The scheme's type.                                  |

# Etag

Information about the [entity tag](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag) (Etag) HTTP response header configuration.

**Properties**

| Name      | Type | Required | Description                        |
| :-------- | :--- | :------- | :--------------------------------- |
| supported | bool | ❌       | If true, the feature is supported. |

# GetScimServiceProviderConfigOkResponseMeta

The response's non-standard meta information.

**Properties**

| Name          | Type | Required | Description |
| :------------ | :--- | :------- | :---------- |
| resource_type | str  | ❌       |             |
| location      | str  | ❌       |             |
<<<<<<< HEAD
=======

<!-- This file was generated by liblab | https://liblab.com/ -->
>>>>>>> 95da91c (initial commit)
