# ApiService

A list of all methods in the `ApiService` service. Click on the method name to view detailed information about that method.

| Methods                   | Description                                     |
| :------------------------ | :---------------------------------------------- |
| [get_apis](#get_apis)     | Gets information about all APIs in a workspace. |
| [create_api](#create_api) | Creates an API.                                 |
| [get_api](#get_api)       | Gets information about an API.                  |

**Note:**

- Git-connected APIs will only return the `versions` and `gitInfo` query responses. This is because schema and collection information is stored in the connected Git repository. The `gitInfo` object only lists the repository and folder locations of the files.
- API viewers can only use the `versions` option in the `include` query parameter.
  |
  |[update_api](#update_api)| Updates an API. |
  |[delete_api](#delete_api)| Deletes an API. |
  |[add_api_collection](#add_api_collection)| Adds a collection to an API. To do this, use the following `operationType` values:

- `COPY_COLLECTION` — Copies a collection from the workspace and adds it to an API.
- `CREATE_NEW` — Creates a new collection by providing the new collection's content.
- `GENERATE_FROM_SCHEMA` — Generates the collection from an API schema. - `options` — An object that contains advanced creation options and their values. You can find a complete list of properties and their values in Postman's [OpenAPI 3.0 to Postman Collection v2.1.0 Converter OPTIONS documentation](https://github.com/postmanlabs/openapi-to-postman/blob/develop/OPTIONS.md). These properties are case-sensitive.
  |
  |[get_api_collection](#get_api_collection)| Gets a collection attached to an API. You can use the `versionId` query parameter to get a collection published in a version.

**Note:**

The `versionId` query parameter is a required parameter for API viewers.
|
|[sync_collection_with_schema](#sync_collection_with_schema)| Syncs a collection attached to an API with the API schema.

This is an asynchronous endpoint that returns an HTTP `202 Accepted` response. The response contains a polling link to the `/apis/{apiId}/tasks/{taskId}` endpoint in the `Location` header.

**Note:**

This endpoint only supports the OpenAPI 3 schema type.
|
|[get_api_comments](#get_api_comments)| Gets all comments left by users in an API. |
|[create_api_comment](#create_api_comment)| Creates a comment on an API.

**Note:**

This endpoint accepts a max of 10,000 characters.
|
|[update_api_comment](#update_api_comment)| Updates a comment on an API.

**Note:**

This endpoint accepts a max of 10,000 characters.
|
|[delete_api_comment](#delete_api_comment)| Deletes a comment from an API. On success, this returns an HTTP `204 No Content` response.

**Note:**

Deleting the first comment of a thread deletes all the comments in the thread.
|
|[create_api_schema](#create_api_schema)| Creates a schema for an API. |
|[get_api_schema](#get_api_schema)| Gets information about API schema. You can use the `versionId` query parameter to get a schema published in an API version.

You can use this API to do the following:

- Get a schema's metadata.
- Get all the files in a schema. This only returns the first file in the schema. The endpoint response contains a link to the next set of response results.
- Get a schema's contents in multi-file or bundled format.

**Note:**

The `versionId` query parameter is a required parameter for API viewers.
|
|[get_api_schema_files](#get_api_schema_files)| Gets the files in an API schema. You can use the `versionId` query parameter to get schema files published in an API version.

**Note:**

The `versionId` query parameter is a required parameter for API viewers.
|
|[get_api_schema_file_contents](#get_api_schema_file_contents)| Gets an API schema file contents at the defined path. You can use the `versionId` query parameter to get schema file contents published in an API version.

**Note:**

The `versionId` query parameter is a required parameter for API viewers.
|
|[create_update_api_schema_file](#create_update_api_schema_file)| Creates or updates an API schema file.

**Note:**

- If the provided file path exists, the file will be updated with the new contents.
- If the provided file path does not exist, then a new schema file will be created.
- If the file path contains a `/` (forward slash) character, then a folder is created. For example, if the file path is the `dir/schema.json` value, then a `dir` folder is created with the `schema.json` file inside.
  |
  |[delete_api_schema_file](#delete_api_schema_file)| Deletes a file in an API schema. |
  |[get_status_of_an_async_task](#get_status_of_an_async_task)| Gets the status of an asynchronous task. |
  |[get_api_versions](#get_api_versions)| Gets all the published versions of an API. |
  |[create_api_version](#create_api_version)| Creates a new API version asynchronously and immediately returns an HTTP `202 Accepted` response. The response contains a polling link to the task status API in the `Location` header.

This endpoint is equivalent to publishing a version in Postman app, which is the snapshot of API collections and schema at a given point in time.
|
|[get_api_version](#get_api_version)| Gets information about an API version.

**Note:**

- For API editors, this endpoint returns an HTTP `302 Found` status code when the version status is pending. It also returns the `/apis/{apiId}/tasks/{taskId}` task status response header.
- For API viewers, this endpoint returns an HTTP `404 Not Found` when the version status is pending.
  |
  |[update_api_version](#update_api_version)| Updates an API version.

**Note:**

This endpoint returns an HTTP `404 Not Found` response when an API version is pending publication.
|
|[delete_api_version](#delete_api_version)| Deletes an API version.

**Note:**

This endpoint returns an HTTP `404 Not Found` response when an API version is pending publication.
|

## get_apis

Gets information about all APIs in a workspace.

- HTTP Method: `GET`
- Endpoint: `/apis`

**Parameters**

| Name         | Type                          | Required | Description                                                                                                                                |
| :----------- | :---------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| workspace_id | str                           | ✅       | The workspace's ID.                                                                                                                        |
| accept       | [Accept](../models/Accept.md) | ✅       | The `application/vnd.api.v10+json` request header required to use the endpoint.                                                            |
| created_by   | int                           | ❌       | Return only results created by the given user ID.                                                                                          |
| cursor       | str                           | ❌       | The pointer to the first record of the set of paginated results. To view the next response, use the `nextCursor` value for this parameter. |
| description  | str                           | ❌       | Return only APIs whose description includes the given value. Matching is not case-sensitive.                                               |
| limit        | int                           | ❌       | The maximum number of rows to return in the response.                                                                                      |

**Return Type**

`GetApis`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import Accept

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.api.get_apis(
    workspace_id="1f0df51a-8658-4ee8-a2a1-d2567dfa09a9",
    accept="application/vnd.api.v10+json",
    created_by=12345678,
    cursor="RnJpIEZlYiAyNCAyMDIzIDEzOjI0OjA5IEdNVCswMDAwIChDb29yZGluYXRlZCBVbml2ZXJzYWwgVGltZSk=",
    description="This is an API for testing purposes",
    limit=10
)

print(result)
```

## create_api

Creates an API.

- HTTP Method: `POST`
- Endpoint: `/apis`

**Parameters**

| Name         | Type                                              | Required | Description                                                                     |
| :----------- | :------------------------------------------------ | :------- | :------------------------------------------------------------------------------ |
| request_body | [CreateApiRequest](../models/CreateApiRequest.md) | ❌       | The request body.                                                               |
| workspace_id | str                                               | ✅       | The workspace's ID.                                                             |
| accept       | [Accept](../models/Accept.md)                     | ✅       | The `application/vnd.api.v10+json` request header required to use the endpoint. |

**Return Type**

`CreateApiOkResponse`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import CreateApiRequest, Accept

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = CreateApiRequest(
    name="Test API",
    summary="Testing API",
    description="This is a test API."
)

result = sdk.api.create_api(
    request_body=request_body,
    workspace_id="1f0df51a-8658-4ee8-a2a1-d2567dfa09a9",
    accept="application/vnd.api.v10+json"
)

print(result)
```

## get_api

Gets information about an API.

**Note:**

- Git-connected APIs will only return the `versions` and `gitInfo` query responses. This is because schema and collection information is stored in the connected Git repository. The `gitInfo` object only lists the repository and folder locations of the files.
- API viewers can only use the `versions` option in the `include` query parameter.

- HTTP Method: `GET`
- Endpoint: `/apis/{apiId}`

**Parameters**

| Name    | Type                                              | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| :------ | :------------------------------------------------ | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| api_id  | str                                               | ✅       | The API's ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| accept  | [Accept](../models/Accept.md)                     | ✅       | The `application/vnd.api.v10+json` request header required to use the endpoint.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| include | [List[GetApiInclude]](../models/GetApiInclude.md) | ❌       | An array that contains additional resources to include in the response. Use this parameter to query for element links to the API, such as collections and schemas: - `collections` — Query for linked Postman collections. - `versions` — Query for linked versions. - `schemas` — Query for linked schemas. - `gitInfo` — Query for information about the API's git-linked repository. This query only returns the linked repository and folder locations of the files. It does not return `collections` or `schemas` information. **Note:** API viewers can only use the `versions` option. |

**Return Type**

`GetApi`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import Accept

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)
include=[
    "collections"
]

result = sdk.api.get_api(
    api_id="90ca9f5a-c4c4-11ed-afa1-0242ac120002",
    accept="application/vnd.api.v10+json",
    include=include
)

print(result)
```

## update_api

Updates an API.

- HTTP Method: `PUT`
- Endpoint: `/apis/{apiId}`

**Parameters**

| Name         | Type                                              | Required | Description                                                                     |
| :----------- | :------------------------------------------------ | :------- | :------------------------------------------------------------------------------ |
| request_body | [UpdateApiRequest](../models/UpdateApiRequest.md) | ❌       | The request body.                                                               |
| api_id       | str                                               | ✅       | The API's ID.                                                                   |
| accept       | [Accept](../models/Accept.md)                     | ✅       | The `application/vnd.api.v10+json` request header required to use the endpoint. |

**Return Type**

`UpdateApiOkResponse`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import UpdateApiRequest, Accept

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = UpdateApiRequest(
    name="Test API",
    summary="Testing API",
    description="This is a test API."
)

result = sdk.api.update_api(
    request_body=request_body,
    api_id="90ca9f5a-c4c4-11ed-afa1-0242ac120002",
    accept="application/vnd.api.v10+json"
)

print(result)
```

## delete_api

Deletes an API.

- HTTP Method: `DELETE`
- Endpoint: `/apis/{apiId}`

**Parameters**

| Name   | Type                          | Required | Description                                                                     |
| :----- | :---------------------------- | :------- | :------------------------------------------------------------------------------ |
| api_id | str                           | ✅       | The API's ID.                                                                   |
| accept | [Accept](../models/Accept.md) | ✅       | The `application/vnd.api.v10+json` request header required to use the endpoint. |

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import Accept

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.api.delete_api(
    api_id="90ca9f5a-c4c4-11ed-afa1-0242ac120002",
    accept="application/vnd.api.v10+json"
)

print(result)
```

## add_api_collection

Adds a collection to an API. To do this, use the following `operationType` values:

- `COPY_COLLECTION` — Copies a collection from the workspace and adds it to an API.
- `CREATE_NEW` — Creates a new collection by providing the new collection's content.
- `GENERATE_FROM_SCHEMA` — Generates the collection from an API schema.

  - `options` — An object that contains advanced creation options and their values. You can find a complete list of properties and their values in Postman's [OpenAPI 3.0 to Postman Collection v2.1.0 Converter OPTIONS documentation](https://github.com/postmanlabs/openapi-to-postman/blob/develop/OPTIONS.md). These properties are case-sensitive.

- HTTP Method: `POST`
- Endpoint: `/apis/{apiId}/collections`

**Parameters**

| Name         | Type                                                            | Required | Description                                                                     |
| :----------- | :-------------------------------------------------------------- | :------- | :------------------------------------------------------------------------------ |
| request_body | [AddApiCollectionRequest](../models/AddApiCollectionRequest.md) | ❌       | The request body.                                                               |
| api_id       | str                                                             | ✅       | The API's ID.                                                                   |
| accept       | [Accept](../models/Accept.md)                                   | ✅       | The `application/vnd.api.v10+json` request header required to use the endpoint. |

**Return Type**

`AddApiCollectionOkResponse`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import Accept
from postman_client.models.add_api_collection_request import AddApiCollection1

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = AddApiCollection1(
    data={
        "collection_id": "12345678-61867bcc-c4c1-11ed-afa1-0242ac120002"
    },
    operation_type="COPY_COLLECTION"
)

result = sdk.api.add_api_collection(
    request_body=request_body,
    api_id="90ca9f5a-c4c4-11ed-afa1-0242ac120002",
    accept="application/vnd.api.v10+json"
)

print(result)
```

## get_api_collection

Gets a collection attached to an API. You can use the `versionId` query parameter to get a collection published in a version.

**Note:**

The `versionId` query parameter is a required parameter for API viewers.

- HTTP Method: `GET`
- Endpoint: `/apis/{apiId}/collections/{collectionId}`

**Parameters**

| Name          | Type                          | Required | Description                                                                     |
| :------------ | :---------------------------- | :------- | :------------------------------------------------------------------------------ |
| api_id        | str                           | ✅       | The API's ID.                                                                   |
| collection_id | str                           | ✅       | The collection's unique ID.                                                     |
| accept        | [Accept](../models/Accept.md) | ✅       | The `application/vnd.api.v10+json` request header required to use the endpoint. |
| version_id    | str                           | ❌       | The API's version ID.                                                           |

**Return Type**

`dict`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import Accept

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.api.get_api_collection(
    api_id="90ca9f5a-c4c4-11ed-afa1-0242ac120002",
    collection_id="12345678-61867bcc-c4c1-11ed-afa1-0242ac120002",
    accept="application/vnd.api.v10+json",
    version_id="12ece9e1-2abf-4edc-8e34-de66e74114d2"
)

print(result)
```

## sync_collection_with_schema

Syncs a collection attached to an API with the API schema.

This is an asynchronous endpoint that returns an HTTP `202 Accepted` response. The response contains a polling link to the `/apis/{apiId}/tasks/{taskId}` endpoint in the `Location` header.

**Note:**

This endpoint only supports the OpenAPI 3 schema type.

- HTTP Method: `PUT`
- Endpoint: `/apis/{apiId}/collections/{collectionId}/sync-with-schema-tasks`

**Parameters**

| Name          | Type                          | Required | Description                                                                     |
| :------------ | :---------------------------- | :------- | :------------------------------------------------------------------------------ |
| api_id        | str                           | ✅       | The API's ID.                                                                   |
| collection_id | str                           | ✅       | The collection's unique ID.                                                     |
| accept        | [Accept](../models/Accept.md) | ✅       | The `application/vnd.api.v10+json` request header required to use the endpoint. |

**Return Type**

`SyncCollectionWithSchema`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import Accept

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.api.sync_collection_with_schema(
    api_id="90ca9f5a-c4c4-11ed-afa1-0242ac120002",
    collection_id="12345678-61867bcc-c4c1-11ed-afa1-0242ac120002",
    accept="application/vnd.api.v10+json"
)

print(result)
```

## get_api_comments

Gets all comments left by users in an API.

- HTTP Method: `GET`
- Endpoint: `/apis/{apiId}/comments`

**Parameters**

| Name   | Type | Required | Description   |
| :----- | :--- | :------- | :------------ |
| api_id | str  | ✅       | The API's ID. |

**Return Type**

`CommentResponse`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.api.get_api_comments(api_id="90ca9f5a-c4c4-11ed-afa1-0242ac120002")

print(result)
```

## create_api_comment

Creates a comment on an API.

**Note:**

This endpoint accepts a max of 10,000 characters.

- HTTP Method: `POST`
- Endpoint: `/apis/{apiId}/comments`

**Parameters**

| Name         | Type                                                    | Required | Description       |
| :----------- | :------------------------------------------------------ | :------- | :---------------- |
| request_body | [CommentCreateUpdate](../models/CommentCreateUpdate.md) | ✅       | The request body. |
| api_id       | str                                                     | ✅       | The API's ID.     |

**Return Type**

`CommentCreatedUpdated`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import CommentCreateUpdate

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = CommentCreateUpdate(
    body="This is an example.",
    tags={
        "user_name": {
            "type_": "user",
            "id_": 87654321
        }
    }
)

result = sdk.api.create_api_comment(
    request_body=request_body,
    api_id="90ca9f5a-c4c4-11ed-afa1-0242ac120002"
)

print(result)
```

## update_api_comment

Updates a comment on an API.

**Note:**

This endpoint accepts a max of 10,000 characters.

- HTTP Method: `PUT`
- Endpoint: `/apis/{apiId}/comments/{commentId}`

**Parameters**

| Name         | Type                                                    | Required | Description       |
| :----------- | :------------------------------------------------------ | :------- | :---------------- |
| request_body | [CommentCreateUpdate](../models/CommentCreateUpdate.md) | ✅       | The request body. |
| api_id       | str                                                     | ✅       | The API's ID.     |
| comment_id   | int                                                     | ✅       | The comment's ID. |

**Return Type**

`CommentCreatedUpdated`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import CommentCreateUpdate

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = CommentCreateUpdate(
    body="This is an example.",
    tags={
        "user_name": {
            "type_": "user",
            "id_": 87654321
        }
    }
)

result = sdk.api.update_api_comment(
    request_body=request_body,
    api_id="90ca9f5a-c4c4-11ed-afa1-0242ac120002",
    comment_id=46814
)

print(result)
```

## delete_api_comment

Deletes a comment from an API. On success, this returns an HTTP `204 No Content` response.

**Note:**

Deleting the first comment of a thread deletes all the comments in the thread.

- HTTP Method: `DELETE`
- Endpoint: `/apis/{apiId}/comments/{commentId}`

**Parameters**

| Name       | Type | Required | Description       |
| :--------- | :--- | :------- | :---------------- |
| api_id     | str  | ✅       | The API's ID.     |
| comment_id | int  | ✅       | The comment's ID. |

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.api.delete_api_comment(
    api_id="90ca9f5a-c4c4-11ed-afa1-0242ac120002",
    comment_id=46814
)

print(result)
```

## create_api_schema

Creates a schema for an API.

- HTTP Method: `POST`
- Endpoint: `/apis/{apiId}/schemas`

**Parameters**

| Name         | Type                                                          | Required | Description                                                                     |
| :----------- | :------------------------------------------------------------ | :------- | :------------------------------------------------------------------------------ |
| request_body | [CreateApiSchemaRequest](../models/CreateApiSchemaRequest.md) | ❌       | The request body.                                                               |
| api_id       | str                                                           | ✅       | The API's ID.                                                                   |
| accept       | [Accept](../models/Accept.md)                                 | ✅       | The `application/vnd.api.v10+json` request header required to use the endpoint. |

**Return Type**

`CreateApiSchemaOkResponse`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import CreateApiSchemaRequest, Accept

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = CreateApiSchemaRequest(
    type_="proto:2",
    files=[
        {
            "path": "common/Error.json",
            "root": {
                "enabled": True
            },
            "content": "content"
        }
    ]
)

result = sdk.api.create_api_schema(
    request_body=request_body,
    api_id="90ca9f5a-c4c4-11ed-afa1-0242ac120002",
    accept="application/vnd.api.v10+json"
)

print(result)
```

## get_api_schema

Gets information about API schema. You can use the `versionId` query parameter to get a schema published in an API version.

You can use this API to do the following:

- Get a schema's metadata.
- Get all the files in a schema. This only returns the first file in the schema. The endpoint response contains a link to the next set of response results.
- Get a schema's contents in multi-file or bundled format.

**Note:**

The `versionId` query parameter is a required parameter for API viewers.

- HTTP Method: `GET`
- Endpoint: `/apis/{apiId}/schemas/{schemaId}`

**Parameters**

| Name       | Type                          | Required | Description                                                                     |
| :--------- | :---------------------------- | :------- | :------------------------------------------------------------------------------ |
| api_id     | str                           | ✅       | The API's ID.                                                                   |
| schema_id  | str                           | ✅       | The API schema's ID.                                                            |
| accept     | [Accept](../models/Accept.md) | ✅       | The `application/vnd.api.v10+json` request header required to use the endpoint. |
| version_id | str                           | ❌       | The API's version ID.                                                           |
| bundled    | bool                          | ❌       | If true, return the schema in a bundled format.                                 |

**Return Type**

`GetApiSchema`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import Accept

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.api.get_api_schema(
    api_id="90ca9f5a-c4c4-11ed-afa1-0242ac120002",
    schema_id="5381f010-c4c1-11ed-afa1-0242ac120002",
    accept="application/vnd.api.v10+json",
    version_id="12ece9e1-2abf-4edc-8e34-de66e74114d2",
    bundled=True
)

print(result)
```

## get_api_schema_files

Gets the files in an API schema. You can use the `versionId` query parameter to get schema files published in an API version.

**Note:**

The `versionId` query parameter is a required parameter for API viewers.

- HTTP Method: `GET`
- Endpoint: `/apis/{apiId}/schemas/{schemaId}/files`

**Parameters**

| Name       | Type                          | Required | Description                                                                                                                                |
| :--------- | :---------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| api_id     | str                           | ✅       | The API's ID.                                                                                                                              |
| schema_id  | str                           | ✅       | The API schema's ID.                                                                                                                       |
| accept     | [Accept](../models/Accept.md) | ✅       | The `application/vnd.api.v10+json` request header required to use the endpoint.                                                            |
| version_id | str                           | ❌       | The API's version ID.                                                                                                                      |
| limit      | int                           | ❌       | The maximum number of rows to return in the response.                                                                                      |
| cursor     | str                           | ❌       | The pointer to the first record of the set of paginated results. To view the next response, use the `nextCursor` value for this parameter. |

**Return Type**

`GetApiSchemaFiles`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import Accept

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.api.get_api_schema_files(
    api_id="90ca9f5a-c4c4-11ed-afa1-0242ac120002",
    schema_id="5381f010-c4c1-11ed-afa1-0242ac120002",
    accept="application/vnd.api.v10+json",
    version_id="12ece9e1-2abf-4edc-8e34-de66e74114d2",
    limit=10,
    cursor="RnJpIEZlYiAyNCAyMDIzIDEzOjI0OjA5IEdNVCswMDAwIChDb29yZGluYXRlZCBVbml2ZXJzYWwgVGltZSk="
)

print(result)
```

## get_api_schema_file_contents

Gets an API schema file contents at the defined path. You can use the `versionId` query parameter to get schema file contents published in an API version.

**Note:**

The `versionId` query parameter is a required parameter for API viewers.

- HTTP Method: `GET`
- Endpoint: `/apis/{apiId}/schemas/{schemaId}/files/{file-path}`

**Parameters**

| Name       | Type                          | Required | Description                                                                     |
| :--------- | :---------------------------- | :------- | :------------------------------------------------------------------------------ |
| api_id     | str                           | ✅       | The API's ID.                                                                   |
| schema_id  | str                           | ✅       | The API schema's ID.                                                            |
| file_path  | str                           | ✅       | The path to the schema file.                                                    |
| accept     | [Accept](../models/Accept.md) | ✅       | The `application/vnd.api.v10+json` request header required to use the endpoint. |
| version_id | str                           | ❌       | The API's version ID.                                                           |

**Return Type**

`GetApiSchemaFileContents`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import Accept

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.api.get_api_schema_file_contents(
    api_id="90ca9f5a-c4c4-11ed-afa1-0242ac120002",
    schema_id="5381f010-c4c1-11ed-afa1-0242ac120002",
    file_path="postman/collection/c1.json",
    accept="application/vnd.api.v10+json",
    version_id="12ece9e1-2abf-4edc-8e34-de66e74114d2"
)

print(result)
```

## create_update_api_schema_file

Creates or updates an API schema file.

**Note:**

- If the provided file path exists, the file will be updated with the new contents.
- If the provided file path does not exist, then a new schema file will be created.
- If the file path contains a `/` (forward slash) character, then a folder is created. For example, if the file path is the `dir/schema.json` value, then a `dir` folder is created with the `schema.json` file inside.

- HTTP Method: `PUT`
- Endpoint: `/apis/{apiId}/schemas/{schemaId}/files/{file-path}`

**Parameters**

| Name         | Type                                                                              | Required | Description                                                                     |
| :----------- | :-------------------------------------------------------------------------------- | :------- | :------------------------------------------------------------------------------ |
| request_body | [CreateUpdateApiSchemaFileRequest](../models/CreateUpdateApiSchemaFileRequest.md) | ❌       | The request body.                                                               |
| api_id       | str                                                                               | ✅       | The API's ID.                                                                   |
| schema_id    | str                                                                               | ✅       | The API schema's ID.                                                            |
| file_path    | str                                                                               | ✅       | The path to the schema file.                                                    |
| accept       | [Accept](../models/Accept.md)                                                     | ✅       | The `application/vnd.api.v10+json` request header required to use the endpoint. |

**Return Type**

`CreateUpdateApiSchemaFileOkResponse`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import CreateUpdateApiSchemaFileRequest, Accept

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = CreateUpdateApiSchemaFileRequest(
    name="index.json",
    root={
        "enabled": True
    },
    content="{\n  \"type\": \"object\",\n  \"required\": [\n    \"id\",\n    \"name\"\n  ],\n  \"properties\": {\n    \"id\": {\n      \"type\": \"integer\",\n      \"format\": \"int64\"\n    },\n    \"name\": {\n      \"type\": \"string\"\n    },\n    \"tag\": {\n      \"type\": \"string\"\n    }\n  }\n}"
)

result = sdk.api.create_update_api_schema_file(
    request_body=request_body,
    api_id="90ca9f5a-c4c4-11ed-afa1-0242ac120002",
    schema_id="5381f010-c4c1-11ed-afa1-0242ac120002",
    file_path="postman/collection/c1.json",
    accept="application/vnd.api.v10+json"
)

print(result)
```

## delete_api_schema_file

Deletes a file in an API schema.

- HTTP Method: `DELETE`
- Endpoint: `/apis/{apiId}/schemas/{schemaId}/files/{file-path}`

**Parameters**

| Name      | Type                          | Required | Description                                                                     |
| :-------- | :---------------------------- | :------- | :------------------------------------------------------------------------------ |
| api_id    | str                           | ✅       | The API's ID.                                                                   |
| schema_id | str                           | ✅       | The API schema's ID.                                                            |
| file_path | str                           | ✅       | The path to the schema file.                                                    |
| accept    | [Accept](../models/Accept.md) | ✅       | The `application/vnd.api.v10+json` request header required to use the endpoint. |

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import Accept

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.api.delete_api_schema_file(
    api_id="90ca9f5a-c4c4-11ed-afa1-0242ac120002",
    schema_id="5381f010-c4c1-11ed-afa1-0242ac120002",
    file_path="postman/collection/c1.json",
    accept="application/vnd.api.v10+json"
)

print(result)
```

## get_status_of_an_async_task

Gets the status of an asynchronous task.

- HTTP Method: `GET`
- Endpoint: `/apis/{apiId}/tasks/{taskId}`

**Parameters**

| Name    | Type                          | Required | Description                                                                     |
| :------ | :---------------------------- | :------- | :------------------------------------------------------------------------------ |
| api_id  | str                           | ✅       | The API's ID.                                                                   |
| task_id | str                           | ✅       | The task's ID.                                                                  |
| accept  | [Accept](../models/Accept.md) | ✅       | The `application/vnd.api.v10+json` request header required to use the endpoint. |

**Return Type**

`GetStatusOfAnAsyncTask`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import Accept

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.api.get_status_of_an_async_task(
    api_id="90ca9f5a-c4c4-11ed-afa1-0242ac120002",
    task_id="90ca9f5a-c4c4-21ed-afa1-0242ac120002",
    accept="application/vnd.api.v10+json"
)

print(result)
```

## get_api_versions

Gets all the published versions of an API.

- HTTP Method: `GET`
- Endpoint: `/apis/{apiId}/versions`

**Parameters**

| Name   | Type                          | Required | Description                                                                                                                                |
| :----- | :---------------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| api_id | str                           | ✅       | The API's ID.                                                                                                                              |
| accept | [Accept](../models/Accept.md) | ✅       | The `application/vnd.api.v10+json` request header required to use the endpoint.                                                            |
| cursor | str                           | ❌       | The pointer to the first record of the set of paginated results. To view the next response, use the `nextCursor` value for this parameter. |
| limit  | int                           | ❌       | The maximum number of rows to return in the response.                                                                                      |

**Return Type**

`GetApiVersions`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import Accept

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.api.get_api_versions(
    api_id="90ca9f5a-c4c4-11ed-afa1-0242ac120002",
    accept="application/vnd.api.v10+json",
    cursor="RnJpIEZlYiAyNCAyMDIzIDEzOjI0OjA5IEdNVCswMDAwIChDb29yZGluYXRlZCBVbml2ZXJzYWwgVGltZSk=",
    limit=10
)

print(result)
```

## create_api_version

Creates a new API version asynchronously and immediately returns an HTTP `202 Accepted` response. The response contains a polling link to the task status API in the `Location` header.

This endpoint is equivalent to publishing a version in Postman app, which is the snapshot of API collections and schema at a given point in time.

- HTTP Method: `POST`
- Endpoint: `/apis/{apiId}/versions`

**Parameters**

| Name         | Type                                                            | Required | Description                                                                     |
| :----------- | :-------------------------------------------------------------- | :------- | :------------------------------------------------------------------------------ |
| request_body | [CreateApiVersionRequest](../models/CreateApiVersionRequest.md) | ❌       | The request body.                                                               |
| api_id       | str                                                             | ✅       | The API's ID.                                                                   |
| accept       | [Accept](../models/Accept.md)                                   | ✅       | The `application/vnd.api.v10+json` request header required to use the endpoint. |

**Return Type**

`CreateApiVersionAcceptedResponse`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import Accept
from postman_client.models.create_api_version_request import CreateApiVersion1

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = CreateApiVersion1(
    name="v1",
    schemas=[
        {
            "id_": "5381f010-c4c1-11ed-afa1-0242ac120002"
        }
    ],
    collections=[
        {
            "id_": "123456-12ece9e1-2abf-4edc-8e34-de66e74114d2"
        }
    ],
    release_notes="This is the first release."
)

result = sdk.api.create_api_version(
    request_body=request_body,
    api_id="90ca9f5a-c4c4-11ed-afa1-0242ac120002",
    accept="application/vnd.api.v10+json"
)

print(result)
```

## get_api_version

Gets information about an API version.

**Note:**

- For API editors, this endpoint returns an HTTP `302 Found` status code when the version status is pending. It also returns the `/apis/{apiId}/tasks/{taskId}` task status response header.
- For API viewers, this endpoint returns an HTTP `404 Not Found` when the version status is pending.

- HTTP Method: `GET`
- Endpoint: `/apis/{apiId}/versions/{versionId}`

**Parameters**

| Name       | Type                          | Required | Description                                                                     |
| :--------- | :---------------------------- | :------- | :------------------------------------------------------------------------------ |
| api_id     | str                           | ✅       | The API's ID.                                                                   |
| version_id | str                           | ✅       | The API's version ID.                                                           |
| accept     | [Accept](../models/Accept.md) | ✅       | The `application/vnd.api.v10+json` request header required to use the endpoint. |

**Return Type**

`GetApiVersion`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import Accept

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.api.get_api_version(
    api_id="90ca9f5a-c4c4-11ed-afa1-0242ac120002",
    version_id="12ece9e1-2abf-4edc-8e34-de66e74114d2",
    accept="application/vnd.api.v10+json"
)

print(result)
```

## update_api_version

Updates an API version.

**Note:**

This endpoint returns an HTTP `404 Not Found` response when an API version is pending publication.

- HTTP Method: `PUT`
- Endpoint: `/apis/{apiId}/versions/{versionId}`

**Parameters**

| Name         | Type                                                            | Required | Description                                                                     |
| :----------- | :-------------------------------------------------------------- | :------- | :------------------------------------------------------------------------------ |
| request_body | [UpdateApiVersionRequest](../models/UpdateApiVersionRequest.md) | ❌       | The request body.                                                               |
| api_id       | str                                                             | ✅       | The API's ID.                                                                   |
| version_id   | str                                                             | ✅       | The API's version ID.                                                           |
| accept       | [Accept](../models/Accept.md)                                   | ✅       | The `application/vnd.api.v10+json` request header required to use the endpoint. |

**Return Type**

`UpdateApiVersionOkResponse`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import UpdateApiVersionRequest, Accept

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = UpdateApiVersionRequest(
    name="Release 1.5",
    release_notes="This is the first public release update."
)

result = sdk.api.update_api_version(
    request_body=request_body,
    api_id="90ca9f5a-c4c4-11ed-afa1-0242ac120002",
    version_id="12ece9e1-2abf-4edc-8e34-de66e74114d2",
    accept="application/vnd.api.v10+json"
)

print(result)
```

## delete_api_version

Deletes an API version.

**Note:**

This endpoint returns an HTTP `404 Not Found` response when an API version is pending publication.

- HTTP Method: `DELETE`
- Endpoint: `/apis/{apiId}/versions/{versionId}`

**Parameters**

| Name       | Type                          | Required | Description                                                                     |
| :--------- | :---------------------------- | :------- | :------------------------------------------------------------------------------ |
| api_id     | str                           | ✅       | The API's ID.                                                                   |
| version_id | str                           | ✅       | The API's version ID.                                                           |
| accept     | [Accept](../models/Accept.md) | ✅       | The `application/vnd.api.v10+json` request header required to use the endpoint. |

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import Accept

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.api.delete_api_version(
    api_id="90ca9f5a-c4c4-11ed-afa1-0242ac120002",
    version_id="12ece9e1-2abf-4edc-8e34-de66e74114d2",
    accept="application/vnd.api.v10+json"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
