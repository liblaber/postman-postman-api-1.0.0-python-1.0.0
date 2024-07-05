# CollectionFoldersService

A list of all methods in the `CollectionFoldersService` service. Click on the method name to view detailed information about that method.

| Methods                                         | Description                                                                                                                                                                          |
| :---------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [get_folder_comments](#get_folder_comments)     | Gets all comments left by users in a folder.                                                                                                                                         |
| [create_folder_comment](#create_folder_comment) | Creates a comment on a folder. **Note:** This endpoint accepts a max of 10,000 characters.                                                                                           |
| [update_folder_comment](#update_folder_comment) | Updates a comment on a folder. **Note:** This endpoint accepts a max of 10,000 characters.                                                                                           |
| [delete_folder_comment](#delete_folder_comment) | Deletes a comment from a folder. On success, this returns an HTTP `204 No Content` response **Note:** Deleting the first comment of a thread deletes all the comments in the thread. |

## get_folder_comments

Gets all comments left by users in a folder.

- HTTP Method: `GET`
- Endpoint: `/collections/{collectionId}/folders/{folderId}/comments`

**Parameters**

| Name          | Type | Required | Description                 |
| :------------ | :--- | :------- | :-------------------------- |
| collection_id | str  | ✅       | The collection's unique ID. |
| folder_id     | str  | ✅       | The folder's unique ID.     |

**Return Type**

`CommentResponse`

**Example Usage Code Snippet**

```python
from postman_restapi import PostmanRestapi, Environment

sdk = PostmanRestapi(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.collection_folders.get_folder_comments(
    collection_id="12345678-12ece9e1-2abf-4edc-8e34-de66e74114d2",
    folder_id="12345678-65a99e60-8e0a-4b6e-b79c-7d8264cc5caa"
)

print(result)
```

## create_folder_comment

Creates a comment on a folder. **Note:** This endpoint accepts a max of 10,000 characters.

- HTTP Method: `POST`
- Endpoint: `/collections/{collectionId}/folders/{folderId}/comments`

**Parameters**

| Name          | Type                                                    | Required | Description                 |
| :------------ | :------------------------------------------------------ | :------- | :-------------------------- |
| request_body  | [CommentCreateUpdate](../models/CommentCreateUpdate.md) | ✅       | The request body.           |
| collection_id | str                                                     | ✅       | The collection's unique ID. |
| folder_id     | str                                                     | ✅       | The folder's unique ID.     |

**Return Type**

`CommentCreatedUpdated`

**Example Usage Code Snippet**

```python
from postman_restapi import PostmanRestapi, Environment
from postman_restapi.models import CommentCreateUpdate

sdk = PostmanRestapi(
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

result = sdk.collection_folders.create_folder_comment(
    request_body=request_body,
    collection_id="12345678-12ece9e1-2abf-4edc-8e34-de66e74114d2",
    folder_id="12345678-65a99e60-8e0a-4b6e-b79c-7d8264cc5caa"
)

print(result)
```

## update_folder_comment

Updates a comment on a folder. **Note:** This endpoint accepts a max of 10,000 characters.

- HTTP Method: `PUT`
- Endpoint: `/collections/{collectionId}/folders/{folderId}/comments/{commentId}`

**Parameters**

| Name          | Type                                                    | Required | Description                 |
| :------------ | :------------------------------------------------------ | :------- | :-------------------------- |
| request_body  | [CommentCreateUpdate](../models/CommentCreateUpdate.md) | ✅       | The request body.           |
| collection_id | str                                                     | ✅       | The collection's unique ID. |
| folder_id     | str                                                     | ✅       | The folder's unique ID.     |
| comment_id    | int                                                     | ✅       | The comment's ID.           |

**Return Type**

`CommentCreatedUpdated`

**Example Usage Code Snippet**

```python
from postman_restapi import PostmanRestapi, Environment
from postman_restapi.models import CommentCreateUpdate

sdk = PostmanRestapi(
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

result = sdk.collection_folders.update_folder_comment(
    request_body=request_body,
    collection_id="12345678-12ece9e1-2abf-4edc-8e34-de66e74114d2",
    folder_id="12345678-65a99e60-8e0a-4b6e-b79c-7d8264cc5caa",
    comment_id=46814
)

print(result)
```

## delete_folder_comment

Deletes a comment from a folder. On success, this returns an HTTP `204 No Content` response **Note:** Deleting the first comment of a thread deletes all the comments in the thread.

- HTTP Method: `DELETE`
- Endpoint: `/collections/{collectionId}/folders/{folderId}/comments/{commentId}`

**Parameters**

| Name          | Type | Required | Description                 |
| :------------ | :--- | :------- | :-------------------------- |
| collection_id | str  | ✅       | The collection's unique ID. |
| folder_id     | str  | ✅       | The folder's unique ID.     |
| comment_id    | int  | ✅       | The comment's ID.           |

**Example Usage Code Snippet**

```python
from postman_restapi import PostmanRestapi, Environment

sdk = PostmanRestapi(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.collection_folders.delete_folder_comment(
    collection_id="12345678-12ece9e1-2abf-4edc-8e34-de66e74114d2",
    folder_id="12345678-65a99e60-8e0a-4b6e-b79c-7d8264cc5caa",
    comment_id=46814
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
