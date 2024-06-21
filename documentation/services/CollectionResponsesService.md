# CollectionResponsesService

A list of all methods in the `CollectionResponsesService` service. Click on the method name to view detailed information about that method.

| Methods                                             | Description                                    |
| :-------------------------------------------------- | :--------------------------------------------- |
| [get_response_comments](#get_response_comments)     | Gets all comments left by users in a response. |
| [create_response_comment](#create_response_comment) | Creates a comment on a response.               |

**Note:**

This endpoint accepts a max of 10,000 characters.
|
|[update_response_comment](#update_response_comment)| Updates a comment on a response.

**Note:**

This endpoint accepts a max of 10,000 characters.
|
|[delete_response_comment](#delete_response_comment)| Deletes a comment from a response. On success, this returns an HTTP `204 No Content` response

**Note:**

Deleting the first comment of a thread deletes all the comments in the thread.
|

## get_response_comments

Gets all comments left by users in a response.

- HTTP Method: `GET`
- Endpoint: `/collections/{collectionId}/responses/{responseId}/comments`

**Parameters**

| Name          | Type | Required | Description                 |
| :------------ | :--- | :------- | :-------------------------- |
| collection_id | str  | ✅       | The collection's unique ID. |
| response_id   | str  | ✅       | The response's unique ID.   |

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

result = sdk.collection_responses.get_response_comments(
    collection_id="12345678-12ece9e1-2abf-4edc-8e34-de66e74114d2",
    response_id="12345678-cc364734-7dfd-4bfc-897d-be763dcdbb07"
)

print(result)
```

## create_response_comment

Creates a comment on a response.

**Note:**

This endpoint accepts a max of 10,000 characters.

- HTTP Method: `POST`
- Endpoint: `/collections/{collectionId}/responses/{responseId}/comments`

**Parameters**

| Name          | Type                                                    | Required | Description                 |
| :------------ | :------------------------------------------------------ | :------- | :-------------------------- |
| request_body  | [CommentCreateUpdate](../models/CommentCreateUpdate.md) | ✅       | The request body.           |
| collection_id | str                                                     | ✅       | The collection's unique ID. |
| response_id   | str                                                     | ✅       | The response's unique ID.   |

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

result = sdk.collection_responses.create_response_comment(
    request_body=request_body,
    collection_id="12345678-12ece9e1-2abf-4edc-8e34-de66e74114d2",
    response_id="12345678-cc364734-7dfd-4bfc-897d-be763dcdbb07"
)

print(result)
```

## update_response_comment

Updates a comment on a response.

**Note:**

This endpoint accepts a max of 10,000 characters.

- HTTP Method: `PUT`
- Endpoint: `/collections/{collectionId}/responses/{responseId}/comments/{commentId}`

**Parameters**

| Name          | Type                                                    | Required | Description                 |
| :------------ | :------------------------------------------------------ | :------- | :-------------------------- |
| request_body  | [CommentCreateUpdate](../models/CommentCreateUpdate.md) | ✅       | The request body.           |
| collection_id | str                                                     | ✅       | The collection's unique ID. |
| response_id   | str                                                     | ✅       | The response's unique ID.   |
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

result = sdk.collection_responses.update_response_comment(
    request_body=request_body,
    collection_id="12345678-12ece9e1-2abf-4edc-8e34-de66e74114d2",
    response_id="12345678-cc364734-7dfd-4bfc-897d-be763dcdbb07",
    comment_id=46814
)

print(result)
```

## delete_response_comment

Deletes a comment from a response. On success, this returns an HTTP `204 No Content` response

**Note:**

Deleting the first comment of a thread deletes all the comments in the thread.

- HTTP Method: `DELETE`
- Endpoint: `/collections/{collectionId}/responses/{responseId}/comments/{commentId}`

**Parameters**

| Name          | Type | Required | Description                 |
| :------------ | :--- | :------- | :-------------------------- |
| collection_id | str  | ✅       | The collection's unique ID. |
| response_id   | str  | ✅       | The response's unique ID.   |
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

result = sdk.collection_responses.delete_response_comment(
    collection_id="12345678-12ece9e1-2abf-4edc-8e34-de66e74114d2",
    response_id="12345678-cc364734-7dfd-4bfc-897d-be763dcdbb07",
    comment_id=46814
)

print(result)
```
