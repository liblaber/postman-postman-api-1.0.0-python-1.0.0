# PrivateApiNetworkService

A list of all methods in the `PrivateApiNetworkService` service. Click on the method name to view detailed information about that method.

| Methods                                                       | Description                                                                                                                                                                    |
| :------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [get_all_elements_and_folders](#get_all_elements_and_folders) | Gets information about the folders and their elements added to your [Private API Network](https://learning.postman.com/docs/collaborating-in-postman/adding-private-network/). |

**Note:**

The `limit` and `offset` parameters are separately applied to elements and folders. For example, if you query a `limit` value of `10` and an `offset` value `0`, the endpoint returns 10 elements and 10 folders for a total of 20 items. The `totalCount` property in the `meta` response is the total count of both elements and folders.
|
|[post_pan_element_or_folder](#post_pan_element_or_folder)| Publishes a element or creates a folder in your [Private API Network](https://learning.postman.com/docs/collaborating-in-postman/adding-private-network/). An element is a Postman API, collection, or workspace.

**Note:**

You can only pass one element object type per call. For example, you cannot pass both `api` and `collection` in a single request.
|
|[update_pan_element_or_folder](#update_pan_element_or_folder)| Updates an element or folder in your [Private API Network](https://learning.postman.com/docs/collaborating-in-postman/adding-private-network/).

**Note:**

You can only pass one element object type per call. For example, you cannot pass both `api` and `collection` in a single request.
|
|[delete_pan_element_or_folder](#delete_pan_element_or_folder)| Removes an element or delete a folder from your [Private API Network](https://learning.postman.com/docs/collaborating-in-postman/adding-private-network/).
**Note:**
Removing an API, collection, or workspace element does not delete it. It only removes it from the Private API Network folder.
|
|[get_all_pan_add_element_requests](#get_all_pan_add_element_requests)| Gets a list requests to add elements to the [Private API Network](https://learning.postman.com/docs/collaborating-in-postman/adding-private-network/). |
|[respond_pan_element_add_request](#respond_pan_element_add_request)| Responds to a request to add an element to the [Private API Network](https://learning.postman.com/docs/collaborating-in-postman/adding-private-network/). Only managers can approve or deny a request. Once approved, the element will appear in the team's Private API Network. |

## get_all_elements_and_folders

Gets information about the folders and their elements added to your [Private API Network](https://learning.postman.com/docs/collaborating-in-postman/adding-private-network/).

**Note:**

The `limit` and `offset` parameters are separately applied to elements and folders. For example, if you query a `limit` value of `10` and an `offset` value `0`, the endpoint returns 10 elements and 10 folders for a total of 20 items. The `totalCount` property in the `meta` response is the total count of both elements and folders.

- HTTP Method: `GET`
- Endpoint: `/network/private`

**Parameters**

| Name             | Type                                                                      | Required | Description                                                                                                                                                                              |
| :--------------- | :------------------------------------------------------------------------ | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| since            | str                                                                       | ❌       | Return only results created since the given time, in [ISO 8601](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) format. This value cannot be later than the `until` value.    |
| until            | str                                                                       | ❌       | Return only results created until this given time, in [ISO 8601](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) format. This value cannot be earlier than the `since` value. |
| added_by         | int                                                                       | ❌       | Return only elements published by the given user ID.                                                                                                                                     |
| name             | str                                                                       | ❌       | Return only elements whose name includes the given value. Matching is not case-sensitive.                                                                                                |
| summary          | str                                                                       | ❌       | Return only elements whose summary includes the given value. Matching is not case-sensitive.                                                                                             |
| description      | str                                                                       | ❌       | Return only elements whose description includes the given value. Matching is not case-sensitive.                                                                                         |
| sort             | [GetAllElementsAndFoldersSort](../models/GetAllElementsAndFoldersSort.md) | ❌       | Sort the results by the given value. If you use this query parameter, you must also use the `direction` parameter.                                                                       |
| direction        | [AscDesc](../models/AscDesc.md)                                           | ❌       | Sort in ascending (`asc`) or descending (`desc`) order. Matching is not case-sensitive. If you use this query parameter, you must also use the `sort` parameter.                         |
| created_by       | int                                                                       | ❌       | Return only results created by the given user ID.                                                                                                                                        |
| offset           | int                                                                       | ❌       | The zero-based offset of the first item to return.                                                                                                                                       |
| limit            | int                                                                       | ❌       | The maximum number of elements to return. If the value exceeds the maximum value of `1000`, then the system uses the `1000` value.                                                       |
| parent_folder_id | int                                                                       | ❌       | Return the folders and elements in a specific folder. If this value is `0`, then the endpoint only returns the root folder's elements.                                                   |
| type\_           | [GetAllElementsAndFoldersType](../models/GetAllElementsAndFoldersType.md) | ❌       | Filter by the element type.                                                                                                                                                              |

**Return Type**

`GetPanElementsAndFolders`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import GetAllElementsAndFoldersSort, AscDesc, GetAllElementsAndFoldersType

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.private_api_network.get_all_elements_and_folders(
    since="2022-06-01T00:00:00.000Z",
    until="2022-06-15T00:00:00.000Z",
    added_by=12345678,
    name="billing",
    summary="payments",
    description="payments",
    sort="createdAt",
    direction="asc",
    created_by=12345678,
    offset=5,
    limit=10,
    parent_folder_id=1,
    type_="api"
)

print(result)
```

## post_pan_element_or_folder

Publishes a element or creates a folder in your [Private API Network](https://learning.postman.com/docs/collaborating-in-postman/adding-private-network/). An element is a Postman API, collection, or workspace.

**Note:**

You can only pass one element object type per call. For example, you cannot pass both `api` and `collection` in a single request.

- HTTP Method: `POST`
- Endpoint: `/network/private`

**Parameters**

| Name         | Type                                                                        | Required | Description       |
| :----------- | :-------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [PostPanElementOrFolderRequest](../models/PostPanElementOrFolderRequest.md) | ✅       | The request body. |

**Return Type**

`PostPanElementOrFolderCreatedResponse`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models.post_pan_element_or_folder_request import PanCreateApi

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = PanCreateApi(
    api={
        "id_": "5360b75f-447e-467c-9299-12fd6c92450d",
        "parent_folder_id": 1
    }
)

result = sdk.private_api_network.post_pan_element_or_folder(request_body=request_body)

print(result)
```

## update_pan_element_or_folder

Updates an element or folder in your [Private API Network](https://learning.postman.com/docs/collaborating-in-postman/adding-private-network/).

**Note:**

You can only pass one element object type per call. For example, you cannot pass both `api` and `collection` in a single request.

- HTTP Method: `PUT`
- Endpoint: `/network/private/{elementType}/{elementId}`

**Parameters**

| Name         | Type                                                                                    | Required | Description                                                                                                           |
| :----------- | :-------------------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------- |
| request_body | [UpdatePanElementOrFolderRequest](../models/UpdatePanElementOrFolderRequest.md)         | ✅       | The request body.                                                                                                     |
| element_id   | str                                                                                     | ✅       | The element's ID or UUID. For Postman Collections you must pass the collection's UID (`userId`-`collectionId`) value. |
| element_type | [UpdatePanElementOrFolderElementType](../models/UpdatePanElementOrFolderElementType.md) | ✅       | The element type.                                                                                                     |

**Return Type**

`UpdatePanElementOrFolderOkResponse`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import UpdatePanElementOrFolderElementType
from postman_client.models.update_pan_element_or_folder_request import UpdatePanApi

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = UpdatePanApi(
    api={
        "parent_folder_id": 1
    }
)

result = sdk.private_api_network.update_pan_element_or_folder(
    request_body=request_body,
    element_id="5360b75f-447e-467c-9299-12fd6c92450d",
    element_type="api"
)

print(result)
```

## delete_pan_element_or_folder

Removes an element or delete a folder from your [Private API Network](https://learning.postman.com/docs/collaborating-in-postman/adding-private-network/).
**Note:**
Removing an API, collection, or workspace element does not delete it. It only removes it from the Private API Network folder.

- HTTP Method: `DELETE`
- Endpoint: `/network/private/{elementType}/{elementId}`

**Parameters**

| Name         | Type                                                                                    | Required | Description                                                                                                           |
| :----------- | :-------------------------------------------------------------------------------------- | :------- | :-------------------------------------------------------------------------------------------------------------------- |
| element_id   | str                                                                                     | ✅       | The element's ID or UUID. For Postman Collections you must pass the collection's UID (`userId`-`collectionId`) value. |
| element_type | [UpdatePanElementOrFolderElementType](../models/UpdatePanElementOrFolderElementType.md) | ✅       | The element type.                                                                                                     |

**Return Type**

`DeletePanElementOrFolder`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import UpdatePanElementOrFolderElementType

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.private_api_network.delete_pan_element_or_folder(
    element_id="5360b75f-447e-467c-9299-12fd6c92450d",
    element_type="api"
)

print(result)
```

## get_all_pan_add_element_requests

Gets a list requests to add elements to the [Private API Network](https://learning.postman.com/docs/collaborating-in-postman/adding-private-network/).

- HTTP Method: `GET`
- Endpoint: `/network/private/network-entity/request/all`

**Parameters**

| Name         | Type                                                                                | Required | Description                                                                                                                                                                              |
| :----------- | :---------------------------------------------------------------------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| since        | str                                                                                 | ❌       | Return only results created since the given time, in [ISO 8601](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) format. This value cannot be later than the `until` value.    |
| until        | str                                                                                 | ❌       | Return only results created until this given time, in [ISO 8601](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) format. This value cannot be earlier than the `since` value. |
| requested_by | int                                                                                 | ❌       | Return a user's element requests by their user ID.                                                                                                                                       |
| type\_       | [GetAllElementsAndFoldersType](../models/GetAllElementsAndFoldersType.md)           | ❌       | Filter by the element type.                                                                                                                                                              |
| status       | [GetAllPanAddElementRequestsStatus](../models/GetAllPanAddElementRequestsStatus.md) | ❌       | Filter by the request status.                                                                                                                                                            |
| name         | str                                                                                 | ❌       | Return only elements whose name includes the given value. Matching is not case-sensitive.                                                                                                |
| sort         | [GetAllElementsAndFoldersSort](../models/GetAllElementsAndFoldersSort.md)           | ❌       | Sort the results by the given value. If you use this query parameter, you must also use the `direction` parameter.                                                                       |
| direction    | [AscDesc](../models/AscDesc.md)                                                     | ❌       | Sort in ascending (`asc`) or descending (`desc`) order. Matching is not case-sensitive. If you use this query parameter, you must also use the `sort` parameter.                         |
| offset       | int                                                                                 | ❌       | The zero-based offset of the first item to return.                                                                                                                                       |
| limit        | int                                                                                 | ❌       | The maximum number of elements to return. If the value exceeds the maximum value of `1000`, then the system uses the `1000` value.                                                       |

**Return Type**

`GetAllPanAddElementRequests`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import GetAllElementsAndFoldersType, GetAllPanAddElementRequestsStatus, GetAllElementsAndFoldersSort, AscDesc

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.private_api_network.get_all_pan_add_element_requests(
    since="2022-06-01T00:00:00.000Z",
    until="2022-06-15T00:00:00.000Z",
    requested_by=12345678,
    type_="api",
    status="pending",
    name="billing",
    sort="createdAt",
    direction="asc",
    offset=5,
    limit=10
)

print(result)
```

## respond_pan_element_add_request

Responds to a request to add an element to the [Private API Network](https://learning.postman.com/docs/collaborating-in-postman/adding-private-network/). Only managers can approve or deny a request. Once approved, the element will appear in the team's Private API Network.

- HTTP Method: `PUT`
- Endpoint: `/network/private/network-entity/request/{requestId}`

**Parameters**

| Name         | Type                                                                                                                      | Required | Description               |
| :----------- | :------------------------------------------------------------------------------------------------------------------------ | :------- | :------------------------ |
| request_body | [PrivateApiNetworkRespondPanElementAddRequestRequest1](../models/PrivateApiNetworkRespondPanElementAddRequestRequest1.md) | ❌       | The request body.         |
| request_id   | int                                                                                                                       | ✅       | The element request's ID. |

**Return Type**

`RespondPanElementAddRequestOkResponse`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import PrivateApiNetworkRespondPanElementAddRequestRequest1

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = PrivateApiNetworkRespondPanElementAddRequestRequest1(
    response={
        "message": "The requested collection has a lot of governance violations. Please fix them."
    },
    status="denied"
)

result = sdk.private_api_network.respond_pan_element_add_request(
    request_body=request_body,
    request_id=232
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
