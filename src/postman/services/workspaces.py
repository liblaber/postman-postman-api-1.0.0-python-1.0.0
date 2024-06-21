from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.update_workspace_roles_request import UpdateWorkspaceRolesRequest
from ..models.update_workspace_roles_ok_response import UpdateWorkspaceRolesOkResponse
from ..models.update_workspace_request import UpdateWorkspaceRequest
from ..models.update_workspace_ok_response import UpdateWorkspaceOkResponse
from ..models.update_workspace_global_variables_request import (
    UpdateWorkspaceGlobalVariablesRequest,
)
from ..models.update_workspace_global_variables_ok_response import (
    UpdateWorkspaceGlobalVariablesOkResponse,
)
from ..models.get_workspaces_type import GetWorkspacesType
from ..models.get_workspaces_ok_response import GetWorkspacesOkResponse
from ..models.get_workspaces_include import GetWorkspacesInclude
from ..models.get_workspace_roles_ok_response import GetWorkspaceRolesOkResponse
from ..models.get_workspace_ok_response import GetWorkspaceOkResponse
from ..models.get_workspace_global_variables_ok_response import (
    GetWorkspaceGlobalVariablesOkResponse,
)
from ..models.delete_workspace_ok_response import DeleteWorkspaceOkResponse
from ..models.create_workspace_request import CreateWorkspaceRequest
from ..models.create_workspace_ok_response import CreateWorkspaceOkResponse


class WorkspacesService(BaseService):

    @cast_models
    def get_workspaces(
        self,
        type_: GetWorkspacesType = None,
        created_by: int = None,
        include: GetWorkspacesInclude = None,
    ) -> GetWorkspacesOkResponse:
        """Gets all [workspaces](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/creating-workspaces/). The response includes your workspaces and any workspaces that you have access to.

        **Note:**

        This endpoint's response contains the visibility field. Visibility determines who can access the workspace:
        - `personal` — Only you can access the workspace.
        - `team` — All team members can access the workspace.
        - `private` — Only invited team members can access the workspace ([**Professional** and **Enterprise** plans only](https://www.postman.com/pricing)).
        - `public` — Everyone can access the workspace.
        - `partner` — Only invited team members and [partners](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/partner-workspaces/) can access the workspace ([**Professional** and **Enterprise** plans only](https://www.postman.com/pricing)).

        :param type_: The type of workspace to filter the response by., defaults to None
        :type type_: GetWorkspacesType, optional
        :param created_by: Return only workspaces created by a specific user ID. For multiple users, pass this value as a comma-separated list of user IDs. The response only returns workspaces that you have access to., defaults to None
        :type created_by: int, optional
        :param include: Include the following information in the endpoint's response:
        - `mocks:deactivated` — Include all deactivated mock servers in the response., defaults to None
        :type include: GetWorkspacesInclude, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: GetWorkspacesOkResponse
        """

        Validator(GetWorkspacesType).is_optional().validate(type_)
        Validator(int).is_optional().validate(created_by)
        Validator(GetWorkspacesInclude).is_optional().validate(include)

        serialized_request = (
            Serializer(f"{self.base_url}/workspaces", self.get_default_headers())
            .add_query("type", type_)
            .add_query("createdBy", created_by)
            .add_query("include", include)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetWorkspacesOkResponse._unmap(response)

    @cast_models
    def create_workspace(
        self, request_body: CreateWorkspaceRequest = None
    ) -> CreateWorkspaceOkResponse:
        """Creates a new [workspace](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/creating-workspaces/).

        **Note:**

        This endpoint returns a 403 `Forbidden` response if the user does not have permission to create workspaces. [Admins and Super Admins](https://learning.postman.com/docs/collaborating-in-postman/roles-and-permissions/#team-roles) can configure workspace permissions to restrict users and/or user groups from creating workspaces or require approvals for the creation of team workspaces.

        ### Important

        We deprecated linking collections or environments between workspaces. We do not recommend that you do this.

        If you have a linked collection or environment, note the following:
        - The endpoint does not create a clone of a collection or environment.
        - Any changes you make to a linked collection or environment changes them in all workspaces.
        - If you delete a collection or environment linked between workspaces, the system deletes it in all the workspaces.

        :param request_body: The request body., defaults to None
        :type request_body: CreateWorkspaceRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: CreateWorkspaceOkResponse
        """

        Validator(CreateWorkspaceRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(f"{self.base_url}/workspaces", self.get_default_headers())
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return CreateWorkspaceOkResponse._unmap(response)

    @cast_models
    def get_workspace_roles(self) -> GetWorkspaceRolesOkResponse:
        """Gets information about all roles in a workspace, based on the team's [plan](https://www.postman.com/pricing/).

        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: GetWorkspaceRolesOkResponse
        """

        serialized_request = (
            Serializer(f"{self.base_url}/workspaces-roles", self.get_default_headers())
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetWorkspaceRolesOkResponse._unmap(response)

    @cast_models
    def get_workspace(self, workspace_id: str) -> GetWorkspaceOkResponse:
        """Gets information about a workspace.

        **Note:**

        This endpoint's response contains the `visibility` field. [Visibility](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/managing-workspaces/#changing-workspace-visibility) determines who can access the workspace:
        - `personal` — Only you can access the workspace.
        - `team` — All team members can access the workspace.
        - `private` — Only invited team members can access the workspace ([**Professional** and **Enterprise** plans only](https://www.postman.com/pricing)).
        - `public` — Everyone can access the workspace.
        - `partner` — Only invited team members and [partners](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/partner-workspaces/) can access the workspace ([**Professional** and **Enterprise** plans only](https://www.postman.com/pricing)).

        ### Important

        We have deprecated the `name` and `uid` responses in the following array of objects:
        - `collections`
        - `environments`
        - `mocks`
        - `monitors`
        - `apis`

        :param workspace_id: The workspace's ID.
        :type workspace_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: GetWorkspaceOkResponse
        """

        Validator(str).validate(workspace_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/workspaces/{{workspaceId}}",
                self.get_default_headers(),
            )
            .add_path("workspaceId", workspace_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetWorkspaceOkResponse._unmap(response)

    @cast_models
    def update_workspace(
        self, workspace_id: str, request_body: UpdateWorkspaceRequest = None
    ) -> UpdateWorkspaceOkResponse:
        """Updates a workspace.

        ### Important

        We deprecated linking collections or environments between workspaces. We do not recommend that you do this.

        If you have a linked collection or environment, note the following:
        - The endpoint does not create a clone of a collection or environment.
        - Any changes you make to a linked collection or environment changes them in all workspaces.
        - If you delete a collection or environment linked between workspaces, the system deletes it in all the workspaces.

        :param request_body: The request body., defaults to None
        :type request_body: UpdateWorkspaceRequest, optional
        :param workspace_id: The workspace's ID.
        :type workspace_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: UpdateWorkspaceOkResponse
        """

        Validator(UpdateWorkspaceRequest).is_optional().validate(request_body)
        Validator(str).validate(workspace_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/workspaces/{{workspaceId}}",
                self.get_default_headers(),
            )
            .add_path("workspaceId", workspace_id)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return UpdateWorkspaceOkResponse._unmap(response)

    @cast_models
    def delete_workspace(self, workspace_id: str) -> DeleteWorkspaceOkResponse:
        """Deletes an existing workspace.

        ### Important

        If you delete a workspace that has a linked collection or environment with another workspace, this will delete the collection and environment in all workspaces.

        :param workspace_id: The workspace's ID.
        :type workspace_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: DeleteWorkspaceOkResponse
        """

        Validator(str).validate(workspace_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/workspaces/{{workspaceId}}",
                self.get_default_headers(),
            )
            .add_path("workspaceId", workspace_id)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)

        return DeleteWorkspaceOkResponse._unmap(response)

    @cast_models
    def get_workspace_global_variables(
        self, workspace_id: str
    ) -> GetWorkspaceGlobalVariablesOkResponse:
        """Gets a workspace's global [variables](https://learning.postman.com/docs/sending-requests/variables/#variable-scopes).

        :param workspace_id: The workspace's ID.
        :type workspace_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: GetWorkspaceGlobalVariablesOkResponse
        """

        Validator(str).validate(workspace_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/workspaces/{{workspaceId}}/global-variables",
                self.get_default_headers(),
            )
            .add_path("workspaceId", workspace_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetWorkspaceGlobalVariablesOkResponse._unmap(response)

    @cast_models
    def update_workspace_global_variables(
        self,
        workspace_id: str,
        request_body: UpdateWorkspaceGlobalVariablesRequest = None,
    ) -> UpdateWorkspaceGlobalVariablesOkResponse:
        """Updates and replaces a workspace's global [variables](https://learning.postman.com/docs/sending-requests/variables/#variable-scopes). This endpoint replaces all existing global variables with the variables you pass in the request body.

        :param request_body: The request body., defaults to None
        :type request_body: UpdateWorkspaceGlobalVariablesRequest, optional
        :param workspace_id: The workspace's ID.
        :type workspace_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: UpdateWorkspaceGlobalVariablesOkResponse
        """

        Validator(UpdateWorkspaceGlobalVariablesRequest).is_optional().validate(
            request_body
        )
        Validator(str).validate(workspace_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/workspaces/{{workspaceId}}/global-variables",
                self.get_default_headers(),
            )
            .add_path("workspaceId", workspace_id)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return UpdateWorkspaceGlobalVariablesOkResponse._unmap(response)

    @cast_models
    def update_workspace_roles(
        self, workspace_id: str, request_body: UpdateWorkspaceRolesRequest = None
    ) -> UpdateWorkspaceRolesOkResponse:
        """Updates the roles of [users](https://learning.postman.com/docs/collaborating-in-postman/roles-and-permissions/#team-roles) or [user groups](https://learning.postman.com/docs/collaborating-in-postman/user-groups/) in a workspace. To get a list of roles, use the `GET /workspace-roles` endpoint.

        **Note:**

        - This endpoint does not support the external [Partner or Guest roles](https://learning.postman.com/docs/collaborating-in-postman/roles-and-permissions/#team-roles).
        - This endpoint is restricted to 50 operations per call.
        - The request body must contain one unique action per user or user group. For example, you cannot add and remove multiple roles for a user in the same request body.

        :param request_body: The request body., defaults to None
        :type request_body: UpdateWorkspaceRolesRequest, optional
        :param workspace_id: The workspace's ID.
        :type workspace_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: UpdateWorkspaceRolesOkResponse
        """

        Validator(UpdateWorkspaceRolesRequest).is_optional().validate(request_body)
        Validator(str).validate(workspace_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/workspaces/{{workspaceId}}/roles",
                self.get_default_headers(),
            )
            .add_path("workspaceId", workspace_id)
            .serialize()
            .set_method("PATCH")
            .set_body(request_body, "application/json-patch+json")
        )

        response = self.send_request(serialized_request)

        return UpdateWorkspaceRolesOkResponse._unmap(response)
