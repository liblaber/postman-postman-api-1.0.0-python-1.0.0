# CollectionItemsService

A list of all methods in the `CollectionItemsService` service. Click on the method name to view detailed information about that method.

| Methods                                               | Description                                                                                                                                                                                              |
| :---------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_collection_folder](#create_collection_folder) | Creates a folder in a collection. For a complete list of properties, refer to "Folder" in the [collection.json schema file](https://schema.postman.com/collection/json/v2.1.0/draft-07/collection.json). |

You can use this endpoint to to import requests and responses into a newly-created folder. To do this, include the `requests` field and the list of request objects in the request body. For more information, see the provided example.

**Note:**

It is recommended that you pass the `name` property in the request body. If you do not, the system uses a null value. As a result, this creates a folder with a blank name.
|
|[create_collection_request](#create_collection_request)| Creates a request in a collection. For a complete list of properties, see the [Collection Format Request documentation](https://learning.postman.com/collection-format/reference/request/).

**Note:**

It is recommended that you pass the `name` property in the request body. If you do not, the system uses a null value. As a result, this creates a request with a blank name.
|
|[create_collection_response](#create_collection_response)| Creates a request response in a collection. For a complete list of request body properties, see the [Collection Format Response documentation](https://learning.postman.com/collection-format/reference/response/#reference-diagram).

**Note:**

It is recommended that you pass the `name` property in the request body. If you do not, the system uses a null value. As a result, this creates a response with a blank name.
|
|[get_collection_folder](#get_collection_folder)| Gets information about a folder in a collection. |
|[update_collection_folder](#update_collection_folder)| Updates a folder in a collection. For a complete list of properties, refer to "Folder" in the [collection.json schema file](https://schema.postman.com/collection/json/v2.1.0/draft-07/collection.json).

**Note:**

This endpoint acts like a PATCH method. It only updates the values that you pass in the request body (for example, the `name` property). The endpoint does not update the entire resource.
|
|[delete_collection_folder](#delete_collection_folder)| Deletes a folder in a collection. |
|[get_collection_request](#get_collection_request)| Gets information about a request in a collection. |
|[update_collection_request](#update_collection_request)| Updates a request in a collection. For a complete list of properties, see the [Collection Format Request documentation](https://learning.postman.com/collection-format/reference/request/).

**Note:**

- You must pass a collection ID (`12ece9e1-2abf-4edc-8e34-de66e74114d2`), not a collection(`12345678-12ece9e1-2abf-4edc-8e34-de66e74114d2`), in this endpoint.
- This endpoint does not support changing the folder of a request.
  |
  |[delete_collection_request](#delete_collection_request)| Deletes a request in a collection. |
  |[get_collection_response](#get_collection_response)| Gets information about a response in a collection. |
  |[update_collection_response](#update_collection_response)| Updates a response in a collection. For a complete list of properties, see the [Collection Format Response documentation](https://learning.postman.com/collection-format/reference/response/#reference-diagram).

**Note:**

- You must pass a collection ID (`12ece9e1-2abf-4edc-8e34-de66e74114d2`), not a collection UID (`12345678-12ece9e1-2abf-4edc-8e34-de66e74114d2`), in this endpoint.
- This endpoint acts like a PATCH method. It only updates the values that you pass in the request body (for example, the `name` property). The endpoint does not update the entire resource.
  |
  |[delete_collection_response](#delete_collection_response)| Deletes a response in a collection. |

## create_collection_folder

Creates a folder in a collection. For a complete list of properties, refer to "Folder" in the [collection.json schema file](https://schema.postman.com/collection/json/v2.1.0/draft-07/collection.json).

You can use this endpoint to to import requests and responses into a newly-created folder. To do this, include the `requests` field and the list of request objects in the request body. For more information, see the provided example.

**Note:**

It is recommended that you pass the `name` property in the request body. If you do not, the system uses a null value. As a result, this creates a folder with a blank name.

- HTTP Method: `POST`
- Endpoint: `/collections/{collectionId}/folders`

**Parameters**

| Name          | Type | Required | Description          |
| :------------ | :--- | :------- | :------------------- |
| request_body  | dict | ❌       | The request body.    |
| collection_id | str  | ✅       | The collection's ID. |

**Return Type**

`CreateCollectionFolderOkResponse`

**Example Usage Code Snippet**

```python
from postman import Postman, Environment
from postman.models import dict

sdk = Postman(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = {}

result = sdk.collection_items.create_collection_folder(
    request_body=request_body,
    collection_id="12ece9e1-2abf-4edc-8e34-de66e74114d2"
)

print(result)
```

## create_collection_request

Creates a request in a collection. For a complete list of properties, see the [Collection Format Request documentation](https://learning.postman.com/collection-format/reference/request/).

**Note:**

It is recommended that you pass the `name` property in the request body. If you do not, the system uses a null value. As a result, this creates a request with a blank name.

- HTTP Method: `POST`
- Endpoint: `/collections/{collectionId}/requests`

**Parameters**

| Name          | Type | Required | Description                                                                                                           |
| :------------ | :--- | :------- | :-------------------------------------------------------------------------------------------------------------------- |
| request_body  | dict | ❌       | The request body.                                                                                                     |
| collection_id | str  | ✅       | The collection's ID.                                                                                                  |
| folder_id     | str  | ❌       | The folder ID in which to create the request. By default, the system will create the request at the collection level. |

**Return Type**

`CreateCollectionRequestOkResponse`

**Example Usage Code Snippet**

```python
from postman import Postman, Environment
from postman.models import dict

sdk = Postman(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = {}

result = sdk.collection_items.create_collection_request(
    request_body=request_body,
    collection_id="12ece9e1-2abf-4edc-8e34-de66e74114d2",
    folder_id="65a99e60-8e0a-4b6e-b79c-7d8264cc5caa"
)

print(result)
```

## create_collection_response

Creates a request response in a collection. For a complete list of request body properties, see the [Collection Format Response documentation](https://learning.postman.com/collection-format/reference/response/#reference-diagram).

**Note:**

It is recommended that you pass the `name` property in the request body. If you do not, the system uses a null value. As a result, this creates a response with a blank name.

- HTTP Method: `POST`
- Endpoint: `/collections/{collectionId}/responses`

**Parameters**

| Name          | Type | Required | Description              |
| :------------ | :--- | :------- | :----------------------- |
| request_body  | dict | ❌       | The request body.        |
| collection_id | str  | ✅       | The collection's ID.     |
| request_id    | str  | ✅       | The parent request's ID. |

**Return Type**

`CreateCollectionResponseOkResponse`

**Example Usage Code Snippet**

```python
from postman import Postman, Environment
from postman.models import dict

sdk = Postman(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = {}

result = sdk.collection_items.create_collection_response(
    request_body=request_body,
    collection_id="12ece9e1-2abf-4edc-8e34-de66e74114d2",
    request_id="c82dd02c-4870-4907-8fcb-593a876cf05b"
)

print(result)
```

## get_collection_folder

Gets information about a folder in a collection.

- HTTP Method: `GET`
- Endpoint: `/collections/{collectionId}/folders/{folderId}`

**Parameters**

| Name          | Type | Required | Description                                                              |
| :------------ | :--- | :------- | :----------------------------------------------------------------------- |
| folder_id     | str  | ✅       | The folder's ID.                                                         |
| collection_id | str  | ✅       | The collection's ID.                                                     |
| ids           | bool | ❌       | If true, returns only properties that contain ID values in the response. |
| uid           | bool | ❌       | If true, returns all IDs in UID format (`userId`-`id`).                  |
| populate      | bool | ❌       | If true, returns all of the collection item's contents.                  |

**Return Type**

`GetCollectionFolderOkResponse`

**Example Usage Code Snippet**

```python
from postman import Postman, Environment

sdk = Postman(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.collection_items.get_collection_folder(
    folder_id="65a99e60-8e0a-4b6e-b79c-7d8264cc5caa",
    collection_id="12ece9e1-2abf-4edc-8e34-de66e74114d2",
    ids=True,
    uid=True,
    populate=True
)

print(result)
```

## update_collection_folder

Updates a folder in a collection. For a complete list of properties, refer to "Folder" in the [collection.json schema file](https://schema.postman.com/collection/json/v2.1.0/draft-07/collection.json).

**Note:**

This endpoint acts like a PATCH method. It only updates the values that you pass in the request body (for example, the `name` property). The endpoint does not update the entire resource.

- HTTP Method: `PUT`
- Endpoint: `/collections/{collectionId}/folders/{folderId}`

**Parameters**

| Name          | Type | Required | Description          |
| :------------ | :--- | :------- | :------------------- |
| request_body  | dict | ❌       | The request body.    |
| folder_id     | str  | ✅       | The folder's ID.     |
| collection_id | str  | ✅       | The collection's ID. |

**Return Type**

`UpdateCollectionFolderOkResponse`

**Example Usage Code Snippet**

```python
from postman import Postman, Environment
from postman.models import dict

sdk = Postman(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = {}

result = sdk.collection_items.update_collection_folder(
    request_body=request_body,
    folder_id="65a99e60-8e0a-4b6e-b79c-7d8264cc5caa",
    collection_id="12ece9e1-2abf-4edc-8e34-de66e74114d2"
)

print(result)
```

## delete_collection_folder

Deletes a folder in a collection.

- HTTP Method: `DELETE`
- Endpoint: `/collections/{collectionId}/folders/{folderId}`

**Parameters**

| Name          | Type | Required | Description          |
| :------------ | :--- | :------- | :------------------- |
| folder_id     | str  | ✅       | The folder's ID.     |
| collection_id | str  | ✅       | The collection's ID. |

**Return Type**

`DeleteCollectionFolderOkResponse`

**Example Usage Code Snippet**

```python
from postman import Postman, Environment

sdk = Postman(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.collection_items.delete_collection_folder(
    folder_id="65a99e60-8e0a-4b6e-b79c-7d8264cc5caa",
    collection_id="12ece9e1-2abf-4edc-8e34-de66e74114d2"
)

print(result)
```

## get_collection_request

Gets information about a request in a collection.

- HTTP Method: `GET`
- Endpoint: `/collections/{collectionId}/requests/{requestId}`

**Parameters**

| Name          | Type | Required | Description                                                              |
| :------------ | :--- | :------- | :----------------------------------------------------------------------- |
| request_id    | str  | ✅       | The request's ID.                                                        |
| collection_id | str  | ✅       | The collection's ID.                                                     |
| ids           | bool | ❌       | If true, returns only properties that contain ID values in the response. |
| uid           | bool | ❌       | If true, returns all IDs in UID format (`userId`-`id`).                  |
| populate      | bool | ❌       | If true, returns all of the collection item's contents.                  |

**Return Type**

`GetCollectionRequestOkResponse`

**Example Usage Code Snippet**

```python
from postman import Postman, Environment

sdk = Postman(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.collection_items.get_collection_request(
    request_id="c82dd02c-4870-4907-8fcb-593a876cf05b",
    collection_id="12ece9e1-2abf-4edc-8e34-de66e74114d2",
    ids=True,
    uid=True,
    populate=True
)

print(result)
```

## update_collection_request

Updates a request in a collection. For a complete list of properties, see the [Collection Format Request documentation](https://learning.postman.com/collection-format/reference/request/).

**Note:**

- You must pass a collection ID (`12ece9e1-2abf-4edc-8e34-de66e74114d2`), not a collection(`12345678-12ece9e1-2abf-4edc-8e34-de66e74114d2`), in this endpoint.
- This endpoint does not support changing the folder of a request.

- HTTP Method: `PUT`
- Endpoint: `/collections/{collectionId}/requests/{requestId}`

**Parameters**

| Name          | Type | Required | Description          |
| :------------ | :--- | :------- | :------------------- |
| request_body  | dict | ❌       | The request body.    |
| request_id    | str  | ✅       | The request's ID.    |
| collection_id | str  | ✅       | The collection's ID. |

**Return Type**

`UpdateCollectionRequestOkResponse`

**Example Usage Code Snippet**

```python
from postman import Postman, Environment
from postman.models import dict

sdk = Postman(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = {}

result = sdk.collection_items.update_collection_request(
    request_body=request_body,
    request_id="c82dd02c-4870-4907-8fcb-593a876cf05b",
    collection_id="12ece9e1-2abf-4edc-8e34-de66e74114d2"
)

print(result)
```

## delete_collection_request

Deletes a request in a collection.

- HTTP Method: `DELETE`
- Endpoint: `/collections/{collectionId}/requests/{requestId}`

**Parameters**

| Name          | Type | Required | Description          |
| :------------ | :--- | :------- | :------------------- |
| request_id    | str  | ✅       | The request's ID.    |
| collection_id | str  | ✅       | The collection's ID. |

**Return Type**

`DeleteCollectionRequestOkResponse`

**Example Usage Code Snippet**

```python
from postman import Postman, Environment

sdk = Postman(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.collection_items.delete_collection_request(
    request_id="c82dd02c-4870-4907-8fcb-593a876cf05b",
    collection_id="12ece9e1-2abf-4edc-8e34-de66e74114d2"
)

print(result)
```

## get_collection_response

Gets information about a response in a collection.

- HTTP Method: `GET`
- Endpoint: `/collections/{collectionId}/responses/{responseId}`

**Parameters**

| Name          | Type | Required | Description                                                              |
| :------------ | :--- | :------- | :----------------------------------------------------------------------- |
| response_id   | str  | ✅       | The response's ID.                                                       |
| collection_id | str  | ✅       | The collection's ID.                                                     |
| ids           | bool | ❌       | If true, returns only properties that contain ID values in the response. |
| uid           | bool | ❌       | If true, returns all IDs in UID format (`userId`-`id`).                  |
| populate      | bool | ❌       | If true, returns all of the collection item's contents.                  |

**Return Type**

`GetCollectionResponseOkResponse`

**Example Usage Code Snippet**

```python
from postman import Postman, Environment

sdk = Postman(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.collection_items.get_collection_response(
    response_id="cc364734-7dfd-4bfc-897d-be763dcdbb07",
    collection_id="12ece9e1-2abf-4edc-8e34-de66e74114d2",
    ids=True,
    uid=True,
    populate=True
)

print(result)
```

## update_collection_response

Updates a response in a collection. For a complete list of properties, see the [Collection Format Response documentation](https://learning.postman.com/collection-format/reference/response/#reference-diagram).

**Note:**

- You must pass a collection ID (`12ece9e1-2abf-4edc-8e34-de66e74114d2`), not a collection UID (`12345678-12ece9e1-2abf-4edc-8e34-de66e74114d2`), in this endpoint.
- This endpoint acts like a PATCH method. It only updates the values that you pass in the request body (for example, the `name` property). The endpoint does not update the entire resource.

- HTTP Method: `PUT`
- Endpoint: `/collections/{collectionId}/responses/{responseId}`

**Parameters**

| Name          | Type | Required | Description          |
| :------------ | :--- | :------- | :------------------- |
| request_body  | dict | ❌       | The request body.    |
| response_id   | str  | ✅       | The response's ID.   |
| collection_id | str  | ✅       | The collection's ID. |

**Return Type**

`UpdateCollectionResponseOkResponse`

**Example Usage Code Snippet**

```python
from postman import Postman, Environment
from postman.models import dict

sdk = Postman(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = {}

result = sdk.collection_items.update_collection_response(
    request_body=request_body,
    response_id="cc364734-7dfd-4bfc-897d-be763dcdbb07",
    collection_id="12ece9e1-2abf-4edc-8e34-de66e74114d2"
)

print(result)
```

## delete_collection_response

Deletes a response in a collection.

- HTTP Method: `DELETE`
- Endpoint: `/collections/{collectionId}/responses/{responseId}`

**Parameters**

| Name          | Type | Required | Description          |
| :------------ | :--- | :------- | :------------------- |
| response_id   | str  | ✅       | The response's ID.   |
| collection_id | str  | ✅       | The collection's ID. |

**Return Type**

`DeleteCollectionResponseOkResponse`

**Example Usage Code Snippet**

```python
from postman import Postman, Environment

sdk = Postman(
    access_token="YOUR_ACCESS_TOKEN",
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.collection_items.delete_collection_response(
    response_id="cc364734-7dfd-4bfc-897d-be763dcdbb07",
    collection_id="12ece9e1-2abf-4edc-8e34-de66e74114d2"
)

print(result)
```
