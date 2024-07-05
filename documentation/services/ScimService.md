# ScimService

A list of all methods in the `ScimService` service. Click on the method name to view detailed information about that method.

| Methods                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [get_scim_group_resources](#get_scim_group_resources)                 | Gets information about all Postman team members.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [create_scim_group](#create_scim_group)                               | Creates a new user group in Postman and creates a new account for each group member. Each account is added to your Postman team and authentication is activated for each user. If an existing Postman account uses an email that matches a group member's email ID, an [email invite](https://postman.postman.co/docs/administration/managing-your-team/managing-your-team/#invites) to join your Postman team is sent to that user. Once the user accepts the invite, they'll be added to your team. By default, the system assigns new users the developer role. You can [update user roles in Postman](https://learning.postman.com/docs/administration/managing-your-team/managing-your-team/#managing-team-roles). |
| [get_scim_group_resource](#get_scim_group_resource)                   | Gets information about a Postman group within the team.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [scim_update_group](#scim_update_group)                               | Updates a group's information. Using this endpoint you can: - Update a group's name. - Add or remove members from a Postman group.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [delete_scim_group](#delete_scim_group)                               | Deletes a group in Postman. User accounts that were in the deleted group are deactivated in Postman if the app is assigned to the user only with the deleted group. User accounts and the data corresponding to them are not deleted. To permanently delete user accounts and their data, [contact Postman support](https://www.postman.com/support/).                                                                                                                                                                                                                                                                                                                                                                  |
| [get_scim_resource_types](#get_scim_resource_types)                   | Gets all the resource types supported by Postman's SCIM API.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [get_scim_service_provider_config](#get_scim_service_provider_config) | Gets the Postman SCIM API configuration information. This includes a list of supported operations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [get_scim_user_resources](#get_scim_user_resources)                   | Gets information about all Postman team members.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [create_scim_user](#create_scim_user)                                 | Creates a new user account in Postman and adds the user to your organization's Postman team. If the account does not already exist, this also activates the user so they can authenticate in to your Postman team. If the account already exists, the system sends the user an [email invite](https://learning.postman.com/docs/administration/managing-your-team/managing-your-team/#inviting-users) to join the Postman team. The user joins the team once they accept the invite. By default, the system assigns new users the developer role. You can [update user roles in Postman](https://learning.postman.com/docs/administration/managing-your-team/managing-your-team/#managing-team-roles).                  |
| [get_scim_user_resource](#get_scim_user_resource)                     | Gets information about a Postman team member.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [update_scim_user](#update_scim_user)                                 | Updates a user's first and last name in Postman. **Note:** You can only use the SCIM API to update a user's first and last name. You cannot update any other user attributes with the API.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [update_scim_user_state](#update_scim_user_state)                     | Updates a user's active state in Postman. **Reactivating a user** By setting the `active` property from `false` to `true`, this reactivates an account. This allows the account to authenticate in to Postman and adds the account back on to your Postman team.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

## get_scim_group_resources

Gets information about all Postman team members.

- HTTP Method: `GET`
- Endpoint: `/scim/v2/Groups`

**Parameters**

| Name        | Type  | Required | Description                                                                                                                                                                                                                                 |
| :---------- | :---- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| start_index | float | ❌       | The index entry by which to begin the list of returned results.                                                                                                                                                                             |
| count       | float | ❌       | Limit the number of results returned in a single response.                                                                                                                                                                                  |
| filter      | str   | ❌       | Filter results by a specific word or phrase. This query parameter only supports the `displayName` filter and has the following requirements:<br>- Filter values are case-sensitive.<br>- Special characters and spaces must be URL encoded. |

**Return Type**

`GetScimGroupResources`

**Example Usage Code Snippet**

```python
from postman_restapi import PostmanRestapi, Environment

sdk = PostmanRestapi(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.scim.get_scim_group_resources(
    start_index=1,
    count=2,
    filter="displayName eq \"Test-API\""
)

print(result)
```

## create_scim_group

Creates a new user group in Postman and creates a new account for each group member. Each account is added to your Postman team and authentication is activated for each user. If an existing Postman account uses an email that matches a group member's email ID, an [email invite](https://postman.postman.co/docs/administration/managing-your-team/managing-your-team/#invites) to join your Postman team is sent to that user. Once the user accepts the invite, they'll be added to your team. By default, the system assigns new users the developer role. You can [update user roles in Postman](https://learning.postman.com/docs/administration/managing-your-team/managing-your-team/#managing-team-roles).

- HTTP Method: `POST`
- Endpoint: `/scim/v2/Groups`

**Parameters**

| Name         | Type                                                          | Required | Description       |
| :----------- | :------------------------------------------------------------ | :------- | :---------------- |
| request_body | [CreateScimGroupRequest](../models/CreateScimGroupRequest.md) | ❌       | The request body. |

**Return Type**

`CreateScimGroupCreatedResponse`

**Example Usage Code Snippet**

```python
from postman_restapi import PostmanRestapi, Environment
from postman_restapi.models import CreateScimGroupRequest

sdk = PostmanRestapi(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = CreateScimGroupRequest(
    schemas=[
        "urn:ietf:params:scim:schemas:core:2.0:Group"
    ],
    display_name="Test-API",
    members=[
        {
            "value": "405775fe15ed41872a8eea4c8aa2b38cda9749812cc55c99",
            "display": "Taylor Lee"
        }
    ]
)

result = sdk.scim.create_scim_group(request_body=request_body)

print(result)
```

## get_scim_group_resource

Gets information about a Postman group within the team.

- HTTP Method: `GET`
- Endpoint: `/scim/v2/Groups/{groupId}`

**Parameters**

| Name     | Type | Required | Description     |
| :------- | :--- | :------- | :-------------- |
| group_id | str  | ✅       | The group's ID. |

**Return Type**

`GetScimGroupResource`

**Example Usage Code Snippet**

```python
from postman_restapi import PostmanRestapi, Environment

sdk = PostmanRestapi(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.scim.get_scim_group_resource(group_id="405775fe15ed41872a8eea4c8aa2b38cda9749812cc55c99")

print(result)
```

## scim_update_group

Updates a group's information. Using this endpoint you can: - Update a group's name. - Add or remove members from a Postman group.

- HTTP Method: `PATCH`
- Endpoint: `/scim/v2/Groups/{groupId}`

**Parameters**

| Name         | Type                                                          | Required | Description       |
| :----------- | :------------------------------------------------------------ | :------- | :---------------- |
| request_body | [ScimUpdateGroupRequest](../models/ScimUpdateGroupRequest.md) | ❌       | The request body. |
| group_id     | str                                                           | ✅       | The group's ID.   |

**Return Type**

`ScimUpdateGroupOkResponse`

**Example Usage Code Snippet**

```python
from postman_restapi import PostmanRestapi, Environment
from postman_restapi.models import ScimUpdateGroupRequest

sdk = PostmanRestapi(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = ScimUpdateGroupRequest(
    schemas=[
        "urn:ietf:params:scim:api:messages:2.0:PatchOp"
    ],
    operations=[
        {
            "op": "replace",
            "path": "members",
            "value": {
                "id_": "561631fq14ed41872a8eea4c8aa2b38cda9749812cc55c00",
                "display_name": "Test-API"
            }
        }
    ]
)

result = sdk.scim.scim_update_group(
    request_body=request_body,
    group_id="405775fe15ed41872a8eea4c8aa2b38cda9749812cc55c99"
)

print(result)
```

## delete_scim_group

Deletes a group in Postman. User accounts that were in the deleted group are deactivated in Postman if the app is assigned to the user only with the deleted group. User accounts and the data corresponding to them are not deleted. To permanently delete user accounts and their data, [contact Postman support](https://www.postman.com/support/).

- HTTP Method: `DELETE`
- Endpoint: `/scim/v2/Groups/{groupId}`

**Parameters**

| Name     | Type | Required | Description     |
| :------- | :--- | :------- | :-------------- |
| group_id | str  | ✅       | The group's ID. |

**Example Usage Code Snippet**

```python
from postman_restapi import PostmanRestapi, Environment

sdk = PostmanRestapi(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.scim.delete_scim_group(group_id="405775fe15ed41872a8eea4c8aa2b38cda9749812cc55c99")

print(result)
```

## get_scim_resource_types

Gets all the resource types supported by Postman's SCIM API.

- HTTP Method: `GET`
- Endpoint: `/scim/v2/ResourceTypes`

**Return Type**

`List[GetScimResourceTypes]`

**Example Usage Code Snippet**

```python
from postman_restapi import PostmanRestapi, Environment

sdk = PostmanRestapi(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.scim.get_scim_resource_types()

print(result)
```

## get_scim_service_provider_config

Gets the Postman SCIM API configuration information. This includes a list of supported operations.

- HTTP Method: `GET`
- Endpoint: `/scim/v2/ServiceProviderConfig`

**Return Type**

`GetScimServiceProviderConfig`

**Example Usage Code Snippet**

```python
from postman_restapi import PostmanRestapi, Environment

sdk = PostmanRestapi(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.scim.get_scim_service_provider_config()

print(result)
```

## get_scim_user_resources

Gets information about all Postman team members.

- HTTP Method: `GET`
- Endpoint: `/scim/v2/Users`

**Parameters**

| Name        | Type  | Required | Description                                                                                                                                                                                                                              |
| :---------- | :---- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| start_index | float | ❌       | The index entry by which to begin the list of returned results.                                                                                                                                                                          |
| count       | float | ❌       | Limit the number of results returned in a single response.                                                                                                                                                                               |
| filter      | str   | ❌       | Filter results by a specific word or phrase. This query parameter only supports the `userName` filter and has the following requirements:<br>- Filter values are case-sensitive.<br>- Special characters and spaces must be URL encoded. |

**Return Type**

`GetScimUserResources`

**Example Usage Code Snippet**

```python
from postman_restapi import PostmanRestapi, Environment

sdk = PostmanRestapi(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.scim.get_scim_user_resources(
    start_index=1,
    count=2,
    filter="filter"
)

print(result)
```

## create_scim_user

Creates a new user account in Postman and adds the user to your organization's Postman team. If the account does not already exist, this also activates the user so they can authenticate in to your Postman team. If the account already exists, the system sends the user an [email invite](https://learning.postman.com/docs/administration/managing-your-team/managing-your-team/#inviting-users) to join the Postman team. The user joins the team once they accept the invite. By default, the system assigns new users the developer role. You can [update user roles in Postman](https://learning.postman.com/docs/administration/managing-your-team/managing-your-team/#managing-team-roles).

- HTTP Method: `POST`
- Endpoint: `/scim/v2/Users`

**Parameters**

| Name         | Type                                                        | Required | Description       |
| :----------- | :---------------------------------------------------------- | :------- | :---------------- |
| request_body | [CreateScimUserRequest](../models/CreateScimUserRequest.md) | ❌       | The request body. |

**Return Type**

`CreateScimUserCreatedResponse`

**Example Usage Code Snippet**

```python
from postman_restapi import PostmanRestapi, Environment
from postman_restapi.models import CreateScimUserRequest

sdk = PostmanRestapi(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = CreateScimUserRequest(
    schemas=[
        "urn:ietf:params:scim:schemas:core:2.0:User"
    ],
    user_name="taylor.lee@example.com",
    active=True,
    external_id="12345678",
    groups=[
        "Test Group"
    ],
    locale="en-US",
    name={
        "given_name": "Taylor",
        "family_name": "Lee"
    }
)

result = sdk.scim.create_scim_user(request_body=request_body)

print(result)
```

## get_scim_user_resource

Gets information about a Postman team member.

- HTTP Method: `GET`
- Endpoint: `/scim/v2/Users/{userId}`

**Parameters**

| Name    | Type | Required | Description         |
| :------ | :--- | :------- | :------------------ |
| user_id | str  | ✅       | The user's SCIM ID. |

**Return Type**

`GetScimUserResourceOkResponse`

**Example Usage Code Snippet**

```python
from postman_restapi import PostmanRestapi, Environment

sdk = PostmanRestapi(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

result = sdk.scim.get_scim_user_resource(user_id="405775fe15ed41872a8eea4c8aa2b38cda9749812cc55c99")

print(result)
```

## update_scim_user

Updates a user's first and last name in Postman. **Note:** You can only use the SCIM API to update a user's first and last name. You cannot update any other user attributes with the API.

- HTTP Method: `PUT`
- Endpoint: `/scim/v2/Users/{userId}`

**Parameters**

| Name         | Type                                          | Required | Description         |
| :----------- | :-------------------------------------------- | :------- | :------------------ |
| request_body | [UpdateScimUser](../models/UpdateScimUser.md) | ❌       | The request body.   |
| user_id      | str                                           | ✅       | The user's SCIM ID. |

**Return Type**

`GetScimUserResourceOkResponse`

**Example Usage Code Snippet**

```python
from postman_restapi import PostmanRestapi, Environment
from postman_restapi.models import UpdateScimUser

sdk = PostmanRestapi(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = UpdateScimUser(
    schemas=[
        "urn:ietf:params:scim:schemas:core:2.0:User"
    ],
    name={
        "given_name": "Taylor",
        "family_name": "Lee"
    }
)

result = sdk.scim.update_scim_user(
    request_body=request_body,
    user_id="405775fe15ed41872a8eea4c8aa2b38cda9749812cc55c99"
)

print(result)
```

## update_scim_user_state

Updates a user's active state in Postman. **Reactivating a user** By setting the `active` property from `false` to `true`, this reactivates an account. This allows the account to authenticate in to Postman and adds the account back on to your Postman team.

- HTTP Method: `PATCH`
- Endpoint: `/scim/v2/Users/{userId}`

**Parameters**

| Name         | Type                                                    | Required | Description         |
| :----------- | :------------------------------------------------------ | :------- | :------------------ |
| request_body | [UpdateScimUserState](../models/UpdateScimUserState.md) | ❌       | The request body.   |
| user_id      | str                                                     | ✅       | The user's SCIM ID. |

**Return Type**

`GetScimUserResourceOkResponse`

**Example Usage Code Snippet**

```python
from postman_restapi import PostmanRestapi, Environment
from postman_restapi.models import UpdateScimUserState

sdk = PostmanRestapi(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value
)

request_body = UpdateScimUserState(
    schemas=[
        "urn:ietf:params:scim:api:messages:2.0:PatchOp"
    ],
    operations=[
        {
            "op": "replace",
            "value": {
                "active": True
            }
        }
    ]
)

result = sdk.scim.update_scim_user_state(
    request_body=request_body,
    user_id="405775fe15ed41872a8eea4c8aa2b38cda9749812cc55c99"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
