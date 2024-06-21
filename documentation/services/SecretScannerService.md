# SecretScannerService

A list of all methods in the `SecretScannerService` service. Click on the method name to view detailed information about that method.

| Methods                                                                   | Description                                                                                                                                                                                                                                                          |
| :------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [detected_secrets_queries](#detected_secrets_queries)                     | Returns all secrets detected by Postman's [Secret Scanner](https://learning.postman.com/docs/administration/secret-scanner/), grouped by workspace. If you pass an empty request body, this endpoint returns all results.                                            |
| [update_detected_secret_resolutions](#update_detected_secret_resolutions) | Updates the resolution status of a secret detected in a workspace.                                                                                                                                                                                                   |
| [get_detected_secrets_locations](#get_detected_secrets_locations)         | Gets the locations of secrets detected by Postman's [Secret Scanner](https://learning.postman.com/docs/administration/secret-scanner/).                                                                                                                              |
| [get_secret_types](#get_secret_types)                                     | Gets the metadata of the secret types supported by Postman's [Secret Scanner](https://learning.postman.com/docs/administration/secret-scanner/). You can use a secret type's ID in the response to query data with the POST `/detected-secrets/{secretId}` endpoint. |

## detected_secrets_queries

Returns all secrets detected by Postman's [Secret Scanner](https://learning.postman.com/docs/administration/secret-scanner/), grouped by workspace. If you pass an empty request body, this endpoint returns all results.

- HTTP Method: `POST`
- Endpoint: `/detected-secrets-queries`

**Parameters**

| Name         | Type                                                                        | Required | Description                                                                                                                                |
| :----------- | :-------------------------------------------------------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | [DetectedSecretsQueriesRequest](../models/DetectedSecretsQueriesRequest.md) | ❌       | The request body.                                                                                                                          |
| limit        | int                                                                         | ❌       | The maximum number of rows to return in the response.                                                                                      |
| cursor       | str                                                                         | ❌       | The pointer to the first record of the set of paginated results. To view the next response, use the `nextCursor` value for this parameter. |
| include      | str                                                                         | ❌       | The additional fields to be included as a part of the request.                                                                             |

**Return Type**

`DetectedSecretsQueriesOkResponse`

**Example Usage Code Snippet**

```python
from postman import Postman, Environment
from postman.models import DetectedSecretsQueriesRequest

sdk = Postman(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = DetectedSecretsQueriesRequest(
    resolved=True,
    secret_types=[
        "1a7ec5d1-dcba-4ec7-8220-3c1ee490416b"
    ],
    statuses=[
        "FALSE_POSITIVE"
    ],
    workspace_ids=[
        "0fe6c2f2-022d-48f7-8e7e-3244369445b0"
    ],
    workspace_visiblities=[
        "team"
    ]
)

result = sdk.secret_scanner.detected_secrets_queries(
    request_body=request_body,
    limit=10,
    cursor="RnJpIEZlYiAyNCAyMDIzIDEzOjI0OjA5IEdNVCswMDAwIChDb29yZGluYXRlZCBVbml2ZXJzYWwgVGltZSk=",
    include="meta.total"
)

print(result)
```

## update_detected_secret_resolutions

Updates the resolution status of a secret detected in a workspace.

- HTTP Method: `PUT`
- Endpoint: `/detected-secrets/{secretId}`

**Parameters**

| Name         | Type                                                                                          | Required | Description       |
| :----------- | :-------------------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [UpdateDetectedSecretResolutionsRequest](../models/UpdateDetectedSecretResolutionsRequest.md) | ❌       | The request body. |
| secret_id    | str                                                                                           | ✅       | The secret's ID.  |

**Return Type**

`UpdateDetectedSecretResolutionsOkResponse`

**Example Usage Code Snippet**

```python
from postman import Postman, Environment
from postman.models import UpdateDetectedSecretResolutionsRequest

sdk = Postman(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = UpdateDetectedSecretResolutionsRequest(
    resolution="FALSE_POSITIVE",
    workspace_id="e361eeb4-00dd-4225-9774-6146a2555999"
)

result = sdk.secret_scanner.update_detected_secret_resolutions(
    request_body=request_body,
    secret_id="ODk0MTU2"
)

print(result)
```

## get_detected_secrets_locations

Gets the locations of secrets detected by Postman's [Secret Scanner](https://learning.postman.com/docs/administration/secret-scanner/).

- HTTP Method: `GET`
- Endpoint: `/detected-secrets/{secretId}/locations`

**Parameters**

| Name         | Type | Required | Description                                                                                                                                |
| :----------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| secret_id    | str  | ✅       | The secret's ID.                                                                                                                           |
| workspace_id | str  | ✅       | The workspace's ID.                                                                                                                        |
| limit        | int  | ❌       | The maximum number of rows to return in the response.                                                                                      |
| cursor       | str  | ❌       | The pointer to the first record of the set of paginated results. To view the next response, use the `nextCursor` value for this parameter. |

**Return Type**

`GetDetectedSecretsLocationsOkResponse`

**Example Usage Code Snippet**

```python
from postman import Postman, Environment

sdk = Postman(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.secret_scanner.get_detected_secrets_locations(
    secret_id="ODk0MTU2",
    workspace_id="1f0df51a-8658-4ee8-a2a1-d2567dfa09a9",
    limit=10,
    cursor="RnJpIEZlYiAyNCAyMDIzIDEzOjI0OjA5IEdNVCswMDAwIChDb29yZGluYXRlZCBVbml2ZXJzYWwgVGltZSk="
)

print(result)
```

## get_secret_types

Gets the metadata of the secret types supported by Postman's [Secret Scanner](https://learning.postman.com/docs/administration/secret-scanner/). You can use a secret type's ID in the response to query data with the POST `/detected-secrets/{secretId}` endpoint.

- HTTP Method: `GET`
- Endpoint: `/secret-types`

**Return Type**

`GetSecretTypesOkResponse`

**Example Usage Code Snippet**

```python
from postman import Postman, Environment

sdk = Postman(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.secret_scanner.get_secret_types()

print(result)
```
