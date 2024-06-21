from typing import List
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.update_scim_user_state_request import UpdateScimUserStateRequest
from ..models.update_scim_user_request import UpdateScimUserRequest
from ..models.scim_update_group_request import ScimUpdateGroupRequest
from ..models.scim_update_group_ok_response import ScimUpdateGroupOkResponse
from ..models.get_scim_user_resources_ok_response import GetScimUserResourcesOkResponse
from ..models.get_scim_user_resource_ok_response import GetScimUserResourceOkResponse
from ..models.get_scim_service_provider_config_ok_response import (
    GetScimServiceProviderConfigOkResponse,
)
from ..models.get_scim_resource_types_ok_response import GetScimResourceTypesOkResponse
from ..models.get_scim_group_resources_ok_response import (
    GetScimGroupResourcesOkResponse,
)
from ..models.get_scim_group_resource_ok_response import GetScimGroupResourceOkResponse
from ..models.create_scim_user_request import CreateScimUserRequest
from ..models.create_scim_user_created_response import CreateScimUserCreatedResponse
from ..models.create_scim_group_request import CreateScimGroupRequest
from ..models.create_scim_group_created_response import CreateScimGroupCreatedResponse


class ScimService(BaseService):

    @cast_models
    def get_scim_group_resources(
        self, start_index: float = None, count: float = None, filter: str = None
    ) -> GetScimGroupResourcesOkResponse:
        """Gets information about all Postman team members.

        :param start_index: The index entry by which to begin the list of returned results., defaults to None
        :type start_index: float, optional
        :param count: Limit the number of results returned in a single response., defaults to None
        :type count: float, optional
        :param filter: Filter results by a specific word or phrase. This query parameter only supports the `displayName` filter and has the following requirements:
        - Filter values are case-sensitive.
        - Special characters and spaces must be URL encoded., defaults to None
        :type filter: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: GetScimGroupResourcesOkResponse
        """

        Validator(float).is_optional().validate(start_index)
        Validator(float).is_optional().validate(count)
        Validator(str).is_optional().validate(filter)

        serialized_request = (
            Serializer(f"{self.base_url}/scim/v2/Groups", self.get_default_headers())
            .add_query("startIndex", start_index)
            .add_query("count", count)
            .add_query("filter", filter)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetScimGroupResourcesOkResponse._unmap(response)

    @cast_models
    def create_scim_group(
        self, request_body: CreateScimGroupRequest = None
    ) -> CreateScimGroupCreatedResponse:
        """Creates a new user group in Postman and creates a new account for each group member.

        Each account is added to your Postman team and authentication is activated for each user. If an existing Postman account uses an email that matches a group member's email ID, an [email invite](https://postman.postman.co/docs/administration/managing-your-team/managing-your-team/#invites) to join your Postman team is sent to that user. Once the user accepts the invite, they'll be added to your team.

        By default, the system assigns new users the developer role. You can [update user roles in Postman](https://learning.postman.com/docs/administration/managing-your-team/managing-your-team/#managing-team-roles).

        :param request_body: The request body., defaults to None
        :type request_body: CreateScimGroupRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Created
        :rtype: CreateScimGroupCreatedResponse
        """

        Validator(CreateScimGroupRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(f"{self.base_url}/scim/v2/Groups", self.get_default_headers())
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return CreateScimGroupCreatedResponse._unmap(response)

    @cast_models
    def get_scim_group_resource(self, group_id: str) -> GetScimGroupResourceOkResponse:
        """Gets information about a Postman group within the team.

        :param group_id: The group's ID.
        :type group_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: GetScimGroupResourceOkResponse
        """

        Validator(str).validate(group_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/scim/v2/Groups/{{groupId}}",
                self.get_default_headers(),
            )
            .add_path("groupId", group_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetScimGroupResourceOkResponse._unmap(response)

    @cast_models
    def scim_update_group(
        self, group_id: str, request_body: ScimUpdateGroupRequest = None
    ) -> ScimUpdateGroupOkResponse:
        """Updates a group's information. Using this endpoint you can:

        - Update a group's name.
        - Add or remove members from a Postman group.

        :param request_body: The request body., defaults to None
        :type request_body: ScimUpdateGroupRequest, optional
        :param group_id: The group's ID.
        :type group_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: ScimUpdateGroupOkResponse
        """

        Validator(ScimUpdateGroupRequest).is_optional().validate(request_body)
        Validator(str).validate(group_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/scim/v2/Groups/{{groupId}}",
                self.get_default_headers(),
            )
            .add_path("groupId", group_id)
            .serialize()
            .set_method("PATCH")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return ScimUpdateGroupOkResponse._unmap(response)

    @cast_models
    def delete_scim_group(self, group_id: str):
        """Deletes a group in Postman.

        User accounts that were in the deleted group are deactivated in Postman if the app is assigned to the user only with the deleted group.

        User accounts and the data corresponding to them are not deleted. To permanently delete user accounts and their data, [contact Postman support](https://www.postman.com/support/).

        :param group_id: The group's ID.
        :type group_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(group_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/scim/v2/Groups/{{groupId}}",
                self.get_default_headers(),
            )
            .add_path("groupId", group_id)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)

        return response

    @cast_models
    def get_scim_resource_types(self) -> List[GetScimResourceTypesOkResponse]:
        """Gets all the resource types supported by Postman's SCIM API.

        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: List[GetScimResourceTypesOkResponse]
        """

        serialized_request = (
            Serializer(
                f"{self.base_url}/scim/v2/ResourceTypes", self.get_default_headers()
            )
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return [GetScimResourceTypesOkResponse._unmap(item) for item in response]

    @cast_models
    def get_scim_service_provider_config(
        self,
    ) -> GetScimServiceProviderConfigOkResponse:
        """Gets the Postman SCIM API configuration information. This includes a list of supported operations.

        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: GetScimServiceProviderConfigOkResponse
        """

        serialized_request = (
            Serializer(
                f"{self.base_url}/scim/v2/ServiceProviderConfig",
                self.get_default_headers(),
            )
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetScimServiceProviderConfigOkResponse._unmap(response)

    @cast_models
    def get_scim_user_resources(
        self, start_index: float = None, count: float = None, filter: str = None
    ) -> GetScimUserResourcesOkResponse:
        """Gets information about all Postman team members.

        :param start_index: The index entry by which to begin the list of returned results., defaults to None
        :type start_index: float, optional
        :param count: Limit the number of results returned in a single response., defaults to None
        :type count: float, optional
        :param filter: Filter results by a specific word or phrase. This query parameter only supports the `userName` filter and has the following requirements:
        - Filter values are case-sensitive.
        - Special characters and spaces must be URL encoded., defaults to None
        :type filter: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: GetScimUserResourcesOkResponse
        """

        Validator(float).is_optional().validate(start_index)
        Validator(float).is_optional().validate(count)
        Validator(str).is_optional().validate(filter)

        serialized_request = (
            Serializer(f"{self.base_url}/scim/v2/Users", self.get_default_headers())
            .add_query("startIndex", start_index)
            .add_query("count", count)
            .add_query("filter", filter)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetScimUserResourcesOkResponse._unmap(response)

    @cast_models
    def create_scim_user(
        self, request_body: CreateScimUserRequest = None
    ) -> CreateScimUserCreatedResponse:
        """Creates a new user account in Postman and adds the user to your organization's Postman team. If the account does not already exist, this also activates the user so they can authenticate in to your Postman team.

        If the account already exists, the system sends the user an [email invite](https://learning.postman.com/docs/administration/managing-your-team/managing-your-team/#inviting-users) to join the Postman team. The user joins the team once they accept the invite.

        By default, the system assigns new users the developer role. You can [update user roles in Postman](https://learning.postman.com/docs/administration/managing-your-team/managing-your-team/#managing-team-roles).

        :param request_body: The request body., defaults to None
        :type request_body: CreateScimUserRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Created
        :rtype: CreateScimUserCreatedResponse
        """

        Validator(CreateScimUserRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(f"{self.base_url}/scim/v2/Users", self.get_default_headers())
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return CreateScimUserCreatedResponse._unmap(response)

    @cast_models
    def get_scim_user_resource(self, user_id: str) -> GetScimUserResourceOkResponse:
        """Gets information about a Postman team member.

        :param user_id: The user's SCIM ID.
        :type user_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: GetScimUserResourceOkResponse
        """

        Validator(str).validate(user_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/scim/v2/Users/{{userId}}", self.get_default_headers()
            )
            .add_path("userId", user_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetScimUserResourceOkResponse._unmap(response)

    @cast_models
    def update_scim_user(
        self, user_id: str, request_body: UpdateScimUserRequest = None
    ) -> GetScimUserResourceOkResponse:
        """Updates a user's first and last name in Postman.

        **Note:**

        You can only use the SCIM API to update a user's first and last name. You cannot update any other user attributes with the API.

        :param request_body: The request body., defaults to None
        :type request_body: UpdateScimUserRequest, optional
        :param user_id: The user's SCIM ID.
        :type user_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: GetScimUserResourceOkResponse
        """

        Validator(UpdateScimUserRequest).is_optional().validate(request_body)
        Validator(str).validate(user_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/scim/v2/Users/{{userId}}", self.get_default_headers()
            )
            .add_path("userId", user_id)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return GetScimUserResourceOkResponse._unmap(response)

    @cast_models
    def update_scim_user_state(
        self, user_id: str, request_body: UpdateScimUserStateRequest = None
    ) -> GetScimUserResourceOkResponse:
        """Updates a user's active state in Postman.

        **Reactivating a user**

        By setting the `active` property from `false` to `true`, this reactivates an account. This allows the account to authenticate in to Postman and adds the account back on to your Postman team.

        :param request_body: The request body., defaults to None
        :type request_body: UpdateScimUserStateRequest, optional
        :param user_id: The user's SCIM ID.
        :type user_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: GetScimUserResourceOkResponse
        """

        Validator(UpdateScimUserStateRequest).is_optional().validate(request_body)
        Validator(str).validate(user_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/scim/v2/Users/{{userId}}", self.get_default_headers()
            )
            .add_path("userId", user_id)
            .serialize()
            .set_method("PATCH")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return GetScimUserResourceOkResponse._unmap(response)
