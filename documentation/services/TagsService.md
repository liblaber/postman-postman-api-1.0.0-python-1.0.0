# TagsService

A list of all methods in the `TagsService` service. Click on the method name to view detailed information about that method.

| Methods                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| :------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [get_api_tags](#get_api_tags)                     | Gets all the tags associated with an API.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [update_api_tags](#update_api_tags)               | Updates an API's associated tags. This endpoint replaces all existing tags with those you pass in the request body.                                                                                                                                                                                                                                                                                                                                                     |
| [get_collection_tags](#get_collection_tags)       | Gets all the tags associated with a collection.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [update_collection_tags](#update_collection_tags) | Updates a collection's associated tags. This endpoint replaces all existing tags with those you pass in the request body.                                                                                                                                                                                                                                                                                                                                               |
| [get_tagged_entities](#get_tagged_entities)       | Gets Postman elements (entities) by a given tag. Tags enable you to organize and search [workspaces](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/managing-workspaces/#tagging-a-workspace), [APIs](https://learning.postman.com/docs/designing-and-developing-your-api/managing-apis/#tagging-apis), and [collections](https://learning.postman.com/docs/collections/using-collections/#tagging-a-collection) that contain shared tags. |

**Note:**

Tagging is available on Postman [**Enterprise** plans](https://www.postman.com/pricing/).
|
|[get_workspace_tags](#get_workspace_tags)| Gets all the tags associated with a workspace. |
|[update_workspace_tags](#update_workspace_tags)| Updates a workspace's associated tags. This endpoint replaces all existing tags with those you pass in the request body. |

## get_api_tags

Gets all the tags associated with an API.

- HTTP Method: `GET`
- Endpoint: `/apis/{apiId}/tags`

**Parameters**

| Name   | Type                          | Required | Description                                                                     |
| :----- | :---------------------------- | :------- | :------------------------------------------------------------------------------ |
| api_id | str                           | ✅       | The API's unique ID.                                                            |
| accept | [Accept](../models/Accept.md) | ✅       | The `application/vnd.api.v10+json` request header required to use the endpoint. |

**Return Type**

`TagGetPut`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import Accept

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.tags.get_api_tags(
    api_id="12345678-6fd634a3-79ba-451d-8f07-56a953f96667",
    accept="application/vnd.api.v10+json"
)

print(result)
```

## update_api_tags

Updates an API's associated tags. This endpoint replaces all existing tags with those you pass in the request body.

- HTTP Method: `PUT`
- Endpoint: `/apis/{apiId}/tags`

**Parameters**

| Name         | Type                                        | Required | Description                                                                     |
| :----------- | :------------------------------------------ | :------- | :------------------------------------------------------------------------------ |
| request_body | [TagUpdateTags](../models/TagUpdateTags.md) | ❌       | The request body.                                                               |
| api_id       | str                                         | ✅       | The API's unique ID.                                                            |
| accept       | [Accept](../models/Accept.md)               | ✅       | The `application/vnd.api.v10+json` request header required to use the endpoint. |

**Return Type**

`TagGetPut`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import TagUpdateTags, Accept

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = TagUpdateTags(
    tags=[
        {
            "slug": "needs-review"
        }
    ]
)

result = sdk.tags.update_api_tags(
    request_body=request_body,
    api_id="12345678-6fd634a3-79ba-451d-8f07-56a953f96667",
    accept="application/vnd.api.v10+json"
)

print(result)
```

## get_collection_tags

Gets all the tags associated with a collection.

- HTTP Method: `GET`
- Endpoint: `/collections/{collectionId}/tags`

**Parameters**

| Name          | Type | Required | Description                 |
| :------------ | :--- | :------- | :-------------------------- |
| collection_id | str  | ✅       | The collection's unique ID. |

**Return Type**

`TagGetPut`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.tags.get_collection_tags(collection_id="12345678-12ece9e1-2abf-4edc-8e34-de66e74114d2")

print(result)
```

## update_collection_tags

Updates a collection's associated tags. This endpoint replaces all existing tags with those you pass in the request body.

- HTTP Method: `PUT`
- Endpoint: `/collections/{collectionId}/tags`

**Parameters**

| Name          | Type                                        | Required | Description                 |
| :------------ | :------------------------------------------ | :------- | :-------------------------- |
| request_body  | [TagUpdateTags](../models/TagUpdateTags.md) | ❌       | The request body.           |
| collection_id | str                                         | ✅       | The collection's unique ID. |

**Return Type**

`TagGetPut`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import TagUpdateTags

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = TagUpdateTags(
    tags=[
        {
            "slug": "needs-review"
        }
    ]
)

result = sdk.tags.update_collection_tags(
    request_body=request_body,
    collection_id="12345678-12ece9e1-2abf-4edc-8e34-de66e74114d2"
)

print(result)
```

## get_tagged_entities

Gets Postman elements (entities) by a given tag. Tags enable you to organize and search [workspaces](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/managing-workspaces/#tagging-a-workspace), [APIs](https://learning.postman.com/docs/designing-and-developing-your-api/managing-apis/#tagging-apis), and [collections](https://learning.postman.com/docs/collections/using-collections/#tagging-a-collection) that contain shared tags.

**Note:**

Tagging is available on Postman [**Enterprise** plans](https://www.postman.com/pricing/).

- HTTP Method: `GET`
- Endpoint: `/tags/{slug}/entities`

**Parameters**

| Name        | Type                                                                    | Required | Description                                                                                                                                       |
| :---------- | :---------------------------------------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------ |
| slug        | str                                                                     | ✅       | The tag's ID within a team or individual (non-team) user scope.                                                                                   |
| limit       | int                                                                     | ❌       | The maximum number of tagged elements to return in a single call.                                                                                 |
| direction   | [AscDescDefaultDesc](../models/AscDescDefaultDesc.md)                   | ❌       | The ascending (`asc`) or descending (`desc`) order to sort the results by, based on the time of the entity's tagging.                             |
| cursor      | str                                                                     | ❌       | The cursor to get the next set of results in the paginated response. If you pass an invalid value, the API only returns the first set of results. |
| entity_type | [GetTaggedEntitiesEntityType](../models/GetTaggedEntitiesEntityType.md) | ❌       | Filter results for the given entity type.                                                                                                         |

**Return Type**

`GetTaggedEntities`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import AscDescDefaultDesc, GetTaggedEntitiesEntityType

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.tags.get_tagged_entities(
    slug="needs-review",
    limit=2,
    direction="asc",
    cursor="eyJpZCI6ODYsImVudGl0eVR5cGUiOiJhcGkifQ==",
    entity_type="api"
)

print(result)
```

## get_workspace_tags

Gets all the tags associated with a workspace.

- HTTP Method: `GET`
- Endpoint: `/workspaces/{workspaceId}/tags`

**Parameters**

| Name         | Type | Required | Description         |
| :----------- | :--- | :------- | :------------------ |
| workspace_id | str  | ✅       | The workspace's ID. |

**Return Type**

`TagGetPut`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.tags.get_workspace_tags(workspace_id="1f0df51a-8658-4ee8-a2a1-d2567dfa09a9")

print(result)
```

## update_workspace_tags

Updates a workspace's associated tags. This endpoint replaces all existing tags with those you pass in the request body.

- HTTP Method: `PUT`
- Endpoint: `/workspaces/{workspaceId}/tags`

**Parameters**

| Name         | Type                                        | Required | Description         |
| :----------- | :------------------------------------------ | :------- | :------------------ |
| request_body | [TagUpdateTags](../models/TagUpdateTags.md) | ❌       | The request body.   |
| workspace_id | str                                         | ✅       | The workspace's ID. |

**Return Type**

`TagGetPut`

**Example Usage Code Snippet**

```python
from postman_client import PostmanClient, Environment
from postman_client.models import TagUpdateTags

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = TagUpdateTags(
    tags=[
        {
            "slug": "needs-review"
        }
    ]
)

result = sdk.tags.update_workspace_tags(
    request_body=request_body,
    workspace_id="1f0df51a-8658-4ee8-a2a1-d2567dfa09a9"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
