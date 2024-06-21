# CollectionsService

A list of all methods in the `CollectionsService` service. Click on the method name to view detailed information about that method.

| Methods                                 | Description                                                                                                                              |
| :-------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------- |
| [get_collections](#get_collections)     | Gets all of your [collections](https://www.getpostman.com/docs/collections). The response includes all of your subscribed collections.   |
| [create_collection](#create_collection) | Creates a collection using the [Postman Collection v2 schema format](https://schema.postman.com/json/collection/v2.1.0/docs/index.html). |

For more information about the Collection Format, see the [Postman Collection Format documentation](https://learning.postman.com/collection-format/getting-started/overview/).

**Note:**

- For a complete list of available property values for this endpoint, use the following references available in the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json):
  - `info` object — Use the `definitions.info` entry.
  - `item` object — Use the `definitions.items` entry.
- For all other possible values, refer to the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json).
  |
  |[create_collection_fork](#create_collection_fork)| Creates a [fork](https://learning.postman.com/docs/collaborating-in-postman/version-control/#creating-a-fork) from an existing collection into a workspace. |
  |[merge_collection_fork](#merge_collection_fork)| Merges a forked collection back into its parent collection. |
  |[get_collection](#get_collection)| Gets information about a collection. For a complete list of this endpoint's possible values, use the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json). |
  |[put_collection](#put_collection)| Replaces the contents of a collection using the [Postman Collection v2 schema format](https://schema.postman.com/json/collection/v2.1.0/docs/index.html). Include the collection's ID values in the request body. If you do not, the endpoint removes the existing items and creates new items.

> The maximum collection size this endpoint accepts cannot exceed 20 MB.

For a complete list of available property values for this endpoint, use the following references available in the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json):

- `info` object — Use `../definitions/info"`.
- `item` object — Use `../definitions/item"`.

For all other possible values, refer to the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json). For more information about the Collection Format, see the [Postman Collection Format documentation](https://learning.postman.com/collection-format/getting-started/overview/).

**Note:**

To copy another collection's contents to the given collection, remove all ID values before you pass it in this endpoint. If you do not, this endpoint returns an error. These values include the `id`, `uid`, and `postman_id` values.
|
|[patch_collection](#patch_collection)| Updates specific collection information, such as its name, events, or its variables. For more information about the `auth`, `variables`, and `events` properties, refer to the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json):

- For `variables`, refer to `../definitions/variable"`.
- For `auth`, refer to `../definitions/auth-attribute"`.
- For `events`, refer to `../definitions/event"`.

For more information about the Collection Format, see the [Postman Collection Format documentation](https://learning.postman.com/collection-format/getting-started/overview/).
|
|[delete_collection](#delete_collection)| Deletes a collection. |
|[get_collections_forked_by_user](#get_collections_forked_by_user)| Gets a list of all the authenticated user's forked collections. |
|[get_collection_comments](#get_collection_comments)| Gets all comments left by users in a collection. |
|[create_collection_comment](#create_collection_comment)| Creates a comment on a collection.

**Note:**

This endpoint accepts a max of 10,000 characters.
|
|[update_collection_comment](#update_collection_comment)| Updates a comment on a collection.

**Note:**

This endpoint accepts a max of 10,000 characters.
|
|[delete_collection_comment](#delete_collection_comment)| Deletes a comment from a collection. On success, this returns an HTTP `204 No Content` response

**Note:**

Deleting the first comment of a thread deletes all the comments in the thread.
|
|[get_collection_forks](#get_collection_forks)| Gets a collection's forked collections. The response returns data for each fork, such as the fork's ID, the user who forked it, and the fork's creation date. |
|[pull_collection_changes](#pull_collection_changes)| Pulls the changes from a parent (source) collection into the forked collection. In the endpoint's response:

- The `destinationId` is the ID of the forked collection.
- The `sourceId` is the ID of the source collection.
  |
  |[get_collection_pull_requests](#get_collection_pull_requests)| Gets information about a collection's pull requests, such as the source and destination IDs, status of the pull requests, and a URL link to the pull requests. |
  |[create_collection_pull_request](#create_collection_pull_request)| Creates a pull request for a forked collection into its parent collection. |
  |[get_collection_roles](#get_collection_roles)| Gets information about all roles in a collection. The response returns the IDs of all users, teams, and groups with access to view or edit the collection. |
  |[update_collection_roles](#update_collection_roles)| Updates the roles of users, groups, or teams in a collection. On success, this returns a `204 No Content` response.

**Note:**

- Only users assigned the EDITOR [role](https://learning.postman.com/docs/collaborating-in-postman/roles-and-permissions/#collection-roles) in the collection can use this endpoint.
- This endpoint does not support the external [Partner or Guest roles](https://learning.postman.com/docs/collaborating-in-postman/roles-and-permissions/#team-roles).
  |
  |[get_source_collection_status](#get_source_collection_status)| Checks whether there is a change between the forked collection and its parent (source) collection.

If the value of the `isSourceAhead` property is `true` in the response, then there is a difference between the forked collection and its source collection.

**Note:**

This endpoint may take a few minutes to return an updated `isSourceAhead` status.
|
|[transform_collection_to_open_api](#transform_collection_to_open_api)| Transforms an existing Postman Collection into a stringified OpenAPI definition.

**Note:**

This does not create an API.
|
|[transfer_collection_folders](#transfer_collection_folders)| Copies or moves folders into a collection or folder. |
|[transfer_collection_requests](#transfer_collection_requests)| Copies or moves requests into a collection or folder. |
|[transfer_collection_responses](#transfer_collection_responses)| Copies or moves responses into a request. |

## get_collections

Gets all of your [collections](https://www.getpostman.com/docs/collections). The response includes all of your subscribed collections.

- HTTP Method: `GET`
- Endpoint: `/collections`

**Parameters**

| Name      | Type | Required | Description                                              |
| :-------- | :--- | :------- | :------------------------------------------------------- |
| workspace | str  | ❌       | The workspace's ID.                                      |
| name      | str  | ❌       | Filter results by collections that match the given name. |

**Return Type**

`GetCollectionsOkResponse`

**Example Usage Code Snippet**

```python
from postman import Postman, Environment

sdk = Postman(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.collections.get_collections(
    workspace="1f0df51a-8658-4ee8-a2a1-d2567dfa09a9",
    name="Test Collection"
)

print(result)
```

## create_collection

Creates a collection using the [Postman Collection v2 schema format](https://schema.postman.com/json/collection/v2.1.0/docs/index.html).

For more information about the Collection Format, see the [Postman Collection Format documentation](https://learning.postman.com/collection-format/getting-started/overview/).

**Note:**

- For a complete list of available property values for this endpoint, use the following references available in the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json):
  - `info` object — Use the `definitions.info` entry.
  - `item` object — Use the `definitions.items` entry.
- For all other possible values, refer to the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json).

- HTTP Method: `POST`
- Endpoint: `/collections`

**Parameters**

| Name         | Type                                                            | Required | Description         |
| :----------- | :-------------------------------------------------------------- | :------- | :------------------ |
| request_body | [CreateCollectionRequest](../models/CreateCollectionRequest.md) | ❌       | The request body.   |
| workspace    | str                                                             | ❌       | The workspace's ID. |

**Return Type**

`CreateCollectionOkResponse`

**Example Usage Code Snippet**

```python
from postman import Postman, Environment
from postman.models import CreateCollectionRequest

sdk = Postman(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = CreateCollectionRequest(
    collection={
        "info": {
            "name": "Test Collection",
            "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
        },
        "item": [
            {
                "request": {}
            }
        ]
    }
)

result = sdk.collections.create_collection(
    request_body=request_body,
    workspace="1f0df51a-8658-4ee8-a2a1-d2567dfa09a9"
)

print(result)
```

## create_collection_fork

Creates a [fork](https://learning.postman.com/docs/collaborating-in-postman/version-control/#creating-a-fork) from an existing collection into a workspace.

- HTTP Method: `POST`
- Endpoint: `/collections/fork/{collectionId}`

**Parameters**

| Name          | Type                                                                    | Required | Description                                   |
| :------------ | :---------------------------------------------------------------------- | :------- | :-------------------------------------------- |
| request_body  | [CreateCollectionForkRequest](../models/CreateCollectionForkRequest.md) | ❌       | The request body.                             |
| collection_id | str                                                                     | ✅       | The collection's ID.                          |
| workspace     | str                                                                     | ✅       | The workspace ID in which to create the fork. |

**Return Type**

`CreateCollectionForkOkResponse`

**Example Usage Code Snippet**

```python
from postman import Postman, Environment
from postman.models import CreateCollectionForkRequest

sdk = Postman(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = CreateCollectionForkRequest(
    label="Test Fork"
)

result = sdk.collections.create_collection_fork(
    request_body=request_body,
    collection_id="12ece9e1-2abf-4edc-8e34-de66e74114d2",
    workspace="1f0df51a-8658-4ee8-a2a1-d2567dfa09a9"
)

print(result)
```

## merge_collection_fork

Merges a forked collection back into its parent collection.

- HTTP Method: `POST`
- Endpoint: `/collections/merge`

**Parameters**

| Name         | Type                                                                  | Required | Description       |
| :----------- | :-------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [MergeCollectionForkRequest](../models/MergeCollectionForkRequest.md) | ❌       | The request body. |

**Return Type**

`MergeCollectionForkOkResponse`

**Example Usage Code Snippet**

```python
from postman import Postman, Environment
from postman.models import MergeCollectionForkRequest

sdk = Postman(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = MergeCollectionForkRequest(
    destination="12345678-12ece9e1-2abf-4edc-8e34-de66e74114d2",
    source="12345678-12ece9e1-2abf-4edc-8e34-de66e74114d2",
    strategy="deleteSource"
)

result = sdk.collections.merge_collection_fork(request_body=request_body)

print(result)
```

## get_collection

Gets information about a collection. For a complete list of this endpoint's possible values, use the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json).

- HTTP Method: `GET`
- Endpoint: `/collections/{collectionId}`

**Parameters**

| Name          | Type                                                  | Required | Description                                                                                                                                                      |
| :------------ | :---------------------------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| collection_id | str                                                   | ✅       | The collection's ID.                                                                                                                                             |
| access_key    | str                                                   | ❌       | A collection's read-only access key. Using this query parameter does not require an API key to call the endpoint.                                                |
| model         | [GetCollectionModel](../models/GetCollectionModel.md) | ❌       | Return a list of only the collection's root-level request (`rootLevelRequests`) and folder (`rootLevelFolders`) IDs instead of the full collection element data. |

**Return Type**

`GetCollectionOkResponse`

**Example Usage Code Snippet**

```python
from postman import Postman, Environment
from postman.models import GetCollectionModel

sdk = Postman(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.collections.get_collection(
    collection_id="12ece9e1-2abf-4edc-8e34-de66e74114d2",
    access_key="PMAT-XXXXXXXXXXXXXXXXXXXXXXXXXX",
    model="minimal"
)

print(result)
```

## put_collection

Replaces the contents of a collection using the [Postman Collection v2 schema format](https://schema.postman.com/json/collection/v2.1.0/docs/index.html). Include the collection's ID values in the request body. If you do not, the endpoint removes the existing items and creates new items.

> The maximum collection size this endpoint accepts cannot exceed 20 MB.

For a complete list of available property values for this endpoint, use the following references available in the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json):

- `info` object — Use `../definitions/info"`.
- `item` object — Use `../definitions/item"`.

For all other possible values, refer to the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json). For more information about the Collection Format, see the [Postman Collection Format documentation](https://learning.postman.com/collection-format/getting-started/overview/).

**Note:**

To copy another collection's contents to the given collection, remove all ID values before you pass it in this endpoint. If you do not, this endpoint returns an error. These values include the `id`, `uid`, and `postman_id` values.

- HTTP Method: `PUT`
- Endpoint: `/collections/{collectionId}`

**Parameters**

| Name          | Type                                                      | Required | Description          |
| :------------ | :-------------------------------------------------------- | :------- | :------------------- |
| request_body  | [PutCollectionRequest](../models/PutCollectionRequest.md) | ❌       | The request body.    |
| collection_id | str                                                       | ✅       | The collection's ID. |

**Return Type**

`PutCollectionOkResponse`

**Example Usage Code Snippet**

```python
from postman import Postman, Environment
from postman.models import PutCollectionRequest

sdk = Postman(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = PutCollectionRequest(
    collection={
        "info": {},
        "item": [
            {}
        ]
    }
)

result = sdk.collections.put_collection(
    request_body=request_body,
    collection_id="12ece9e1-2abf-4edc-8e34-de66e74114d2"
)

print(result)
```

## patch_collection

Updates specific collection information, such as its name, events, or its variables. For more information about the `auth`, `variables`, and `events` properties, refer to the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json):

- For `variables`, refer to `../definitions/variable"`.
- For `auth`, refer to `../definitions/auth-attribute"`.
- For `events`, refer to `../definitions/event"`.

For more information about the Collection Format, see the [Postman Collection Format documentation](https://learning.postman.com/collection-format/getting-started/overview/).

- HTTP Method: `PATCH`
- Endpoint: `/collections/{collectionId}`

**Parameters**

| Name          | Type                                                          | Required | Description          |
| :------------ | :------------------------------------------------------------ | :------- | :------------------- |
| request_body  | [PatchCollectionRequest](../models/PatchCollectionRequest.md) | ❌       | The request body.    |
| collection_id | str                                                           | ✅       | The collection's ID. |

**Return Type**

`PatchCollectionOkResponse`

**Example Usage Code Snippet**

```python
from postman import Postman, Environment
from postman.models import PatchCollectionRequest

sdk = Postman(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = PatchCollectionRequest(
    collection={
        "info": {
            "name": "Test Collection v2",
            "description": "This collection makes a request to the Postman Echo service to get a list of request headers sent by an HTTP client."
        },
        "variables": {},
        "auth": {},
        "events": {}
    }
)

result = sdk.collections.patch_collection(
    request_body=request_body,
    collection_id="12ece9e1-2abf-4edc-8e34-de66e74114d2"
)

print(result)
```

## delete_collection

Deletes a collection.

- HTTP Method: `DELETE`
- Endpoint: `/collections/{collectionId}`

**Parameters**

| Name          | Type | Required | Description          |
| :------------ | :--- | :------- | :------------------- |
| collection_id | str  | ✅       | The collection's ID. |

**Return Type**

`DeleteCollectionOkResponse`

**Example Usage Code Snippet**

```python
from postman import Postman, Environment

sdk = Postman(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.collections.delete_collection(collection_id="12ece9e1-2abf-4edc-8e34-de66e74114d2")

print(result)
```

## get_collections_forked_by_user

Gets a list of all the authenticated user's forked collections.

- HTTP Method: `GET`
- Endpoint: `/collections/{collectionId}/collection-forks`

**Parameters**

| Name          | Type                            | Required | Description                                                                                                                                |
| :------------ | :------------------------------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| collection_id | str                             | ✅       | The collection's ID.                                                                                                                       |
| cursor        | str                             | ❌       | The pointer to the first record of the set of paginated results. To view the next response, use the `nextCursor` value for this parameter. |
| limit         | int                             | ❌       | The maximum number of rows to return in the response.                                                                                      |
| direction     | [AscDesc](../models/AscDesc.md) | ❌       | Sort the results by creation date in ascending (`asc`) or descending (`desc`) order.                                                       |

**Return Type**

`GetCollectionsForkedByUserOkResponse`

**Example Usage Code Snippet**

```python
from postman import Postman, Environment
from postman.models import AscDesc

sdk = Postman(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.collections.get_collections_forked_by_user(
    collection_id="12ece9e1-2abf-4edc-8e34-de66e74114d2",
    cursor="RnJpIEZlYiAyNCAyMDIzIDEzOjI0OjA5IEdNVCswMDAwIChDb29yZGluYXRlZCBVbml2ZXJzYWwgVGltZSk=",
    limit=10,
    direction="asc"
)

print(result)
```

## get_collection_comments

Gets all comments left by users in a collection.

- HTTP Method: `GET`
- Endpoint: `/collections/{collectionId}/comments`

**Parameters**

| Name          | Type | Required | Description                 |
| :------------ | :--- | :------- | :-------------------------- |
| collection_id | str  | ✅       | The collection's unique ID. |

**Return Type**

`CommentResponse`

**Example Usage Code Snippet**

```python
from postman import Postman, Environment

sdk = Postman(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.collections.get_collection_comments(collection_id="12345678-12ece9e1-2abf-4edc-8e34-de66e74114d2")

print(result)
```

## create_collection_comment

Creates a comment on a collection.

**Note:**

This endpoint accepts a max of 10,000 characters.

- HTTP Method: `POST`
- Endpoint: `/collections/{collectionId}/comments`

**Parameters**

| Name          | Type                                                    | Required | Description                 |
| :------------ | :------------------------------------------------------ | :------- | :-------------------------- |
| request_body  | [CommentCreateUpdate](../models/CommentCreateUpdate.md) | ✅       | The request body.           |
| collection_id | str                                                     | ✅       | The collection's unique ID. |

**Return Type**

`CommentCreatedUpdated`

**Example Usage Code Snippet**

```python
from postman import Postman, Environment
from postman.models import CommentCreateUpdate

sdk = Postman(
    access_token="YOUR_ACCESS_TOKEN",
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

result = sdk.collections.create_collection_comment(
    request_body=request_body,
    collection_id="12345678-12ece9e1-2abf-4edc-8e34-de66e74114d2"
)

print(result)
```

## update_collection_comment

Updates a comment on a collection.

**Note:**

This endpoint accepts a max of 10,000 characters.

- HTTP Method: `PUT`
- Endpoint: `/collections/{collectionId}/comments/{commentId}`

**Parameters**

| Name          | Type                                                    | Required | Description                 |
| :------------ | :------------------------------------------------------ | :------- | :-------------------------- |
| request_body  | [CommentCreateUpdate](../models/CommentCreateUpdate.md) | ✅       | The request body.           |
| collection_id | str                                                     | ✅       | The collection's unique ID. |
| comment_id    | int                                                     | ✅       | The comment's ID.           |

**Return Type**

`CommentCreatedUpdated`

**Example Usage Code Snippet**

```python
from postman import Postman, Environment
from postman.models import CommentCreateUpdate

sdk = Postman(
    access_token="YOUR_ACCESS_TOKEN",
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

result = sdk.collections.update_collection_comment(
    request_body=request_body,
    collection_id="12345678-12ece9e1-2abf-4edc-8e34-de66e74114d2",
    comment_id=46814
)

print(result)
```

## delete_collection_comment

Deletes a comment from a collection. On success, this returns an HTTP `204 No Content` response

**Note:**

Deleting the first comment of a thread deletes all the comments in the thread.

- HTTP Method: `DELETE`
- Endpoint: `/collections/{collectionId}/comments/{commentId}`

**Parameters**

| Name          | Type | Required | Description                 |
| :------------ | :--- | :------- | :-------------------------- |
| collection_id | str  | ✅       | The collection's unique ID. |
| comment_id    | int  | ✅       | The comment's ID.           |

**Example Usage Code Snippet**

```python
from postman import Postman, Environment

sdk = Postman(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.collections.delete_collection_comment(
    collection_id="12345678-12ece9e1-2abf-4edc-8e34-de66e74114d2",
    comment_id=46814
)

print(result)
```

## get_collection_forks

Gets a collection's forked collections. The response returns data for each fork, such as the fork's ID, the user who forked it, and the fork's creation date.

- HTTP Method: `GET`
- Endpoint: `/collections/{collectionId}/forks`

**Parameters**

| Name          | Type                            | Required | Description                                                                                                                                |
| :------------ | :------------------------------ | :------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| collection_id | str                             | ✅       | The collection's ID.                                                                                                                       |
| cursor        | str                             | ❌       | The pointer to the first record of the set of paginated results. To view the next response, use the `nextCursor` value for this parameter. |
| limit         | int                             | ❌       | The maximum number of rows to return in the response.                                                                                      |
| direction     | [AscDesc](../models/AscDesc.md) | ❌       | Sort the results by creation date in ascending (`asc`) or descending (`desc`) order.                                                       |

**Return Type**

`GetCollectionForksOkResponse`

**Example Usage Code Snippet**

```python
from postman import Postman, Environment
from postman.models import AscDesc

sdk = Postman(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.collections.get_collection_forks(
    collection_id="12ece9e1-2abf-4edc-8e34-de66e74114d2",
    cursor="RnJpIEZlYiAyNCAyMDIzIDEzOjI0OjA5IEdNVCswMDAwIChDb29yZGluYXRlZCBVbml2ZXJzYWwgVGltZSk=",
    limit=10,
    direction="asc"
)

print(result)
```

## pull_collection_changes

Pulls the changes from a parent (source) collection into the forked collection. In the endpoint's response:

- The `destinationId` is the ID of the forked collection.
- The `sourceId` is the ID of the source collection.

- HTTP Method: `PUT`
- Endpoint: `/collections/{collectionId}/pulls`

**Parameters**

| Name          | Type | Required | Description          |
| :------------ | :--- | :------- | :------------------- |
| collection_id | str  | ✅       | The collection's ID. |

**Return Type**

`PullCollectionChangesOkResponse`

**Example Usage Code Snippet**

```python
from postman import Postman, Environment

sdk = Postman(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.collections.pull_collection_changes(collection_id="12ece9e1-2abf-4edc-8e34-de66e74114d2")

print(result)
```

## get_collection_pull_requests

Gets information about a collection's pull requests, such as the source and destination IDs, status of the pull requests, and a URL link to the pull requests.

- HTTP Method: `GET`
- Endpoint: `/collections/{collectionId}/pull-requests`

**Parameters**

| Name          | Type | Required | Description                 |
| :------------ | :--- | :------- | :-------------------------- |
| collection_id | str  | ✅       | The collection's unique ID. |

**Return Type**

`GetCollectionPullRequestsOkResponse`

**Example Usage Code Snippet**

```python
from postman import Postman, Environment

sdk = Postman(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.collections.get_collection_pull_requests(collection_id="12345678-12ece9e1-2abf-4edc-8e34-de66e74114d2")

print(result)
```

## create_collection_pull_request

Creates a pull request for a forked collection into its parent collection.

- HTTP Method: `POST`
- Endpoint: `/collections/{collectionId}/pull-requests`

**Parameters**

| Name          | Type                                                                                  | Required | Description                 |
| :------------ | :------------------------------------------------------------------------------------ | :------- | :-------------------------- |
| request_body  | [CreateCollectionPullRequestRequest](../models/CreateCollectionPullRequestRequest.md) | ❌       | The request body.           |
| collection_id | str                                                                                   | ✅       | The collection's unique ID. |

**Return Type**

`CreateCollectionPullRequestOkResponse`

**Example Usage Code Snippet**

```python
from postman import Postman, Environment
from postman.models import CreateCollectionPullRequestRequest

sdk = Postman(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = CreateCollectionPullRequestRequest(
    title="Test PR",
    description="This is a test pull request.",
    reviewers=[
        "87654321"
    ],
    destination_id="12345678-ec548788-unftw-rgn8-83b8-0b59798648e4"
)

result = sdk.collections.create_collection_pull_request(
    request_body=request_body,
    collection_id="12345678-12ece9e1-2abf-4edc-8e34-de66e74114d2"
)

print(result)
```

## get_collection_roles

Gets information about all roles in a collection. The response returns the IDs of all users, teams, and groups with access to view or edit the collection.

- HTTP Method: `GET`
- Endpoint: `/collections/{collectionId}/roles`

**Parameters**

| Name          | Type | Required | Description          |
| :------------ | :--- | :------- | :------------------- |
| collection_id | str  | ✅       | The collection's ID. |

**Return Type**

`GetCollectionRolesOkResponse`

**Example Usage Code Snippet**

```python
from postman import Postman, Environment

sdk = Postman(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.collections.get_collection_roles(collection_id="12ece9e1-2abf-4edc-8e34-de66e74114d2")

print(result)
```

## update_collection_roles

Updates the roles of users, groups, or teams in a collection. On success, this returns a `204 No Content` response.

**Note:**

- Only users assigned the EDITOR [role](https://learning.postman.com/docs/collaborating-in-postman/roles-and-permissions/#collection-roles) in the collection can use this endpoint.
- This endpoint does not support the external [Partner or Guest roles](https://learning.postman.com/docs/collaborating-in-postman/roles-and-permissions/#team-roles).

- HTTP Method: `PATCH`
- Endpoint: `/collections/{collectionId}/roles`

**Parameters**

| Name          | Type                                                                      | Required | Description          |
| :------------ | :------------------------------------------------------------------------ | :------- | :------------------- |
| request_body  | [UpdateCollectionRolesRequest](../models/UpdateCollectionRolesRequest.md) | ❌       | The request body.    |
| collection_id | str                                                                       | ✅       | The collection's ID. |

**Example Usage Code Snippet**

```python
from postman import Postman, Environment
from postman.models import UpdateCollectionRolesRequest

sdk = Postman(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = UpdateCollectionRolesRequest(
    roles=[
        {
            "op": "update",
            "path": "/user",
            "value": [
                {
                    "id_": 12345678,
                    "role": "VIEWER"
                }
            ]
        }
    ]
)

result = sdk.collections.update_collection_roles(
    request_body=request_body,
    collection_id="12ece9e1-2abf-4edc-8e34-de66e74114d2"
)

print(result)
```

## get_source_collection_status

Checks whether there is a change between the forked collection and its parent (source) collection.

If the value of the `isSourceAhead` property is `true` in the response, then there is a difference between the forked collection and its source collection.

**Note:**

This endpoint may take a few minutes to return an updated `isSourceAhead` status.

- HTTP Method: `GET`
- Endpoint: `/collections/{collectionId}/source-status`

**Parameters**

| Name          | Type | Required | Description          |
| :------------ | :--- | :------- | :------------------- |
| collection_id | str  | ✅       | The collection's ID. |

**Return Type**

`GetSourceCollectionStatusOkResponse`

**Example Usage Code Snippet**

```python
from postman import Postman, Environment

sdk = Postman(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.collections.get_source_collection_status(collection_id="12ece9e1-2abf-4edc-8e34-de66e74114d2")

print(result)
```

## transform_collection_to_open_api

Transforms an existing Postman Collection into a stringified OpenAPI definition.

**Note:**

This does not create an API.

- HTTP Method: `GET`
- Endpoint: `/collections/{collectionId}/transformations`

**Parameters**

| Name          | Type                          | Required | Description                                        |
| :------------ | :---------------------------- | :------- | :------------------------------------------------- |
| collection_id | str                           | ✅       | The collection's ID.                               |
| format        | [Format](../models/Format.md) | ❌       | Return the OpenAPI definition in the given format. |

**Return Type**

`TransformCollectionToOpenApiOkResponse`

**Example Usage Code Snippet**

```python
from postman import Postman, Environment
from postman.models import Format

sdk = Postman(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.collections.transform_collection_to_open_api(
    collection_id="12ece9e1-2abf-4edc-8e34-de66e74114d2",
    format="json"
)

print(result)
```

## transfer_collection_folders

Copies or moves folders into a collection or folder.

- HTTP Method: `POST`
- Endpoint: `/collection-folders-transfers`

**Parameters**

| Name         | Type                                                            | Required | Description       |
| :----------- | :-------------------------------------------------------------- | :------- | :---------------- |
| request_body | [TransferCollectionItems](../models/TransferCollectionItems.md) | ❌       | The request body. |

**Return Type**

`TransferCollectionFoldersOkResponse`

**Example Usage Code Snippet**

```python
from postman import Postman, Environment
from postman.models import TransferCollectionItems

sdk = Postman(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = TransferCollectionItems(
    ids=[
        "12345678-a9b481c1-3e78-4af7-8db0-dce3f3f3c105"
    ],
    mode="copy",
    target={
        "id_": "12345678-b91270fa-048d-4f5f-a033-8b5523bf053f",
        "model": "collection"
    },
    location={
        "id_": "12345678-80812b16-ac27-45b3-b3eb-793f78530d32",
        "model": "response",
        "position": "start"
    }
)

result = sdk.collections.transfer_collection_folders(request_body=request_body)

print(result)
```

## transfer_collection_requests

Copies or moves requests into a collection or folder.

- HTTP Method: `POST`
- Endpoint: `/collection-requests-transfers`

**Parameters**

| Name         | Type                                                            | Required | Description       |
| :----------- | :-------------------------------------------------------------- | :------- | :---------------- |
| request_body | [TransferCollectionItems](../models/TransferCollectionItems.md) | ❌       | The request body. |

**Return Type**

`TransferCollectionFoldersOkResponse`

**Example Usage Code Snippet**

```python
from postman import Postman, Environment
from postman.models import TransferCollectionItems

sdk = Postman(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = TransferCollectionItems(
    ids=[
        "12345678-a9b481c1-3e78-4af7-8db0-dce3f3f3c105"
    ],
    mode="copy",
    target={
        "id_": "12345678-b91270fa-048d-4f5f-a033-8b5523bf053f",
        "model": "collection"
    },
    location={
        "id_": "12345678-80812b16-ac27-45b3-b3eb-793f78530d32",
        "model": "response",
        "position": "start"
    }
)

result = sdk.collections.transfer_collection_requests(request_body=request_body)

print(result)
```

## transfer_collection_responses

Copies or moves responses into a request.

- HTTP Method: `POST`
- Endpoint: `/collection-responses-transfers`

**Parameters**

| Name         | Type                                                            | Required | Description       |
| :----------- | :-------------------------------------------------------------- | :------- | :---------------- |
| request_body | [TransferCollectionItems](../models/TransferCollectionItems.md) | ❌       | The request body. |

**Return Type**

`TransferCollectionFoldersOkResponse`

**Example Usage Code Snippet**

```python
from postman import Postman, Environment
from postman.models import TransferCollectionItems

sdk = Postman(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = TransferCollectionItems(
    ids=[
        "12345678-a9b481c1-3e78-4af7-8db0-dce3f3f3c105"
    ],
    mode="copy",
    target={
        "id_": "12345678-b91270fa-048d-4f5f-a033-8b5523bf053f",
        "model": "collection"
    },
    location={
        "id_": "12345678-80812b16-ac27-45b3-b3eb-793f78530d32",
        "model": "response",
        "position": "start"
    }
)

result = sdk.collections.transfer_collection_responses(request_body=request_body)

print(result)
```
