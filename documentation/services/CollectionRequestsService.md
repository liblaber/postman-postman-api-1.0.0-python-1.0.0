# CollectionRequestsService

A list of all methods in the `CollectionRequestsService` service. Click on the method name to view detailed information about that method.

| Methods                                           | Description                                   |
| :------------------------------------------------ | :-------------------------------------------- |
| [get_request_comments](#get_request_comments)     | Gets all comments left by users in a request. |
| [create_request_comment](#create_request_comment) | Creates a comment on a request.               |

**Note:**

This endpoint accepts a max of 10,000 characters.
|
|[update_request_comment](#update_request_comment)| Updates a comment on a request.

**Note:**

This endpoint accepts a max of 10,000 characters.
|
|[delete_request_comment](#delete_request_comment)| Deletes a comment from a request. On success, this returns an HTTP `204 No Content` response

**Note:**

Deleting the first comment of a thread deletes all the comments in the thread.
|

## get_request_comments

Gets all comments left by users in a request.

- HTTP Method: `GET`
- Endpoint: `/collections/{collectionId}/requests/{requestId}/comments`

**Parameters**

| Name          | Type | Required | Description                 |
| :------------ | :--- | :------- | :-------------------------- |
| collection_id | str  | ✅       | The collection's unique ID. |
| request_id    | str  | ✅       | The request's unique ID.    |

**Return Type**

`CommentResponse`

**Example Usage Code Snippet**

```python
from postman import Postman, Environment

sdk = Postman(
<<<<<<< HEAD
    access_token="YOUR_ACCESS_TOKEN",
=======
>>>>>>> 95da91c (initial commit)
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.collection_requests.get_request_comments(
    collection_id="12345678-12ece9e1-2abf-4edc-8e34-de66e74114d2",
    request_id="12345678-c82dd02c-4870-4907-8fcb-593a876cf05b"
)

print(result)
```

## create_request_comment

Creates a comment on a request.

**Note:**

This endpoint accepts a max of 10,000 characters.

- HTTP Method: `POST`
- Endpoint: `/collections/{collectionId}/requests/{requestId}/comments`

**Parameters**

| Name          | Type                                                    | Required | Description                 |
| :------------ | :------------------------------------------------------ | :------- | :-------------------------- |
| request_body  | [CommentCreateUpdate](../models/CommentCreateUpdate.md) | ✅       | The request body.           |
| collection_id | str                                                     | ✅       | The collection's unique ID. |
| request_id    | str                                                     | ✅       | The request's unique ID.    |

**Return Type**

`CommentCreatedUpdated`

**Example Usage Code Snippet**

```python
from postman import Postman, Environment
from postman.models import CommentCreateUpdate

sdk = Postman(
<<<<<<< HEAD
    access_token="YOUR_ACCESS_TOKEN",
=======
>>>>>>> 95da91c (initial commit)
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

result = sdk.collection_requests.create_request_comment(
    request_body=request_body,
    collection_id="12345678-12ece9e1-2abf-4edc-8e34-de66e74114d2",
    request_id="12345678-c82dd02c-4870-4907-8fcb-593a876cf05b"
)

print(result)
```

## update_request_comment

Updates a comment on a request.

**Note:**

This endpoint accepts a max of 10,000 characters.

- HTTP Method: `PUT`
- Endpoint: `/collections/{collectionId}/requests/{requestId}/comments/{commentId}`

**Parameters**

| Name          | Type                                                    | Required | Description                 |
| :------------ | :------------------------------------------------------ | :------- | :-------------------------- |
| request_body  | [CommentCreateUpdate](../models/CommentCreateUpdate.md) | ✅       | The request body.           |
| collection_id | str                                                     | ✅       | The collection's unique ID. |
| request_id    | str                                                     | ✅       | The request's unique ID.    |
| comment_id    | int                                                     | ✅       | The comment's ID.           |

**Return Type**

`CommentCreatedUpdated`

**Example Usage Code Snippet**

```python
from postman import Postman, Environment
from postman.models import CommentCreateUpdate

sdk = Postman(
<<<<<<< HEAD
    access_token="YOUR_ACCESS_TOKEN",
=======
>>>>>>> 95da91c (initial commit)
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

result = sdk.collection_requests.update_request_comment(
    request_body=request_body,
    collection_id="12345678-12ece9e1-2abf-4edc-8e34-de66e74114d2",
    request_id="12345678-c82dd02c-4870-4907-8fcb-593a876cf05b",
    comment_id=46814
)

print(result)
```

## delete_request_comment

Deletes a comment from a request. On success, this returns an HTTP `204 No Content` response

**Note:**

Deleting the first comment of a thread deletes all the comments in the thread.

- HTTP Method: `DELETE`
- Endpoint: `/collections/{collectionId}/requests/{requestId}/comments/{commentId}`

**Parameters**

| Name          | Type | Required | Description                 |
| :------------ | :--- | :------- | :-------------------------- |
| collection_id | str  | ✅       | The collection's unique ID. |
| request_id    | str  | ✅       | The request's unique ID.    |
| comment_id    | int  | ✅       | The comment's ID.           |

**Example Usage Code Snippet**

```python
from postman import Postman, Environment

sdk = Postman(
<<<<<<< HEAD
    access_token="YOUR_ACCESS_TOKEN",
=======
>>>>>>> 95da91c (initial commit)
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.collection_requests.delete_request_comment(
    collection_id="12345678-12ece9e1-2abf-4edc-8e34-de66e74114d2",
    request_id="12345678-c82dd02c-4870-4907-8fcb-593a876cf05b",
    comment_id=46814
)

print(result)
```
<<<<<<< HEAD
=======

<!-- This file was generated by liblab | https://liblab.com/ -->
>>>>>>> 95da91c (initial commit)
