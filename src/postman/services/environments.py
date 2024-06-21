from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.update_environment_request import UpdateEnvironmentRequest
from ..models.update_environment_ok_response import UpdateEnvironmentOkResponse
from ..models.pull_environment_request import PullEnvironmentRequest
from ..models.pull_environment_ok_response import PullEnvironmentOkResponse
from ..models.merge_environment_fork_request import MergeEnvironmentForkRequest
from ..models.merge_environment_fork_ok_response import MergeEnvironmentForkOkResponse
from ..models.get_environments_ok_response import GetEnvironmentsOkResponse
from ..models.get_environment_ok_response import GetEnvironmentOkResponse
from ..models.get_environment_forks_sort import GetEnvironmentForksSort
from ..models.get_environment_forks_ok_response import GetEnvironmentForksOkResponse
from ..models.fork_environment_request import ForkEnvironmentRequest
from ..models.fork_environment_ok_response import ForkEnvironmentOkResponse
from ..models.delete_environment_ok_response import DeleteEnvironmentOkResponse
from ..models.create_environment_request import CreateEnvironmentRequest
from ..models.create_environment_ok_response import CreateEnvironmentOkResponse
from ..models.asc_desc import AscDesc


class EnvironmentsService(BaseService):

    @cast_models
    def get_environments(self, workspace: str = None) -> GetEnvironmentsOkResponse:
        """Gets information about all of your [environments](https://learning.postman.com/docs/sending-requests/managing-environments/).

        :param workspace: The workspace's ID., defaults to None
        :type workspace: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: GetEnvironmentsOkResponse
        """

        Validator(str).is_optional().validate(workspace)

        serialized_request = (
            Serializer(f"{self.base_url}/environments", self.get_default_headers())
            .add_query("workspace", workspace)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetEnvironmentsOkResponse._unmap(response)

    @cast_models
    def create_environment(
        self, request_body: CreateEnvironmentRequest = None, workspace: str = None
    ) -> CreateEnvironmentOkResponse:
        """Creates an environment.

        :param request_body: The request body., defaults to None
        :type request_body: CreateEnvironmentRequest, optional
        :param workspace: The workspace's ID., defaults to None
        :type workspace: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: CreateEnvironmentOkResponse
        """

        Validator(CreateEnvironmentRequest).is_optional().validate(request_body)
        Validator(str).is_optional().validate(workspace)

        serialized_request = (
            Serializer(f"{self.base_url}/environments", self.get_default_headers())
            .add_query("workspace", workspace)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return CreateEnvironmentOkResponse._unmap(response)

    @cast_models
    def get_environment(self, environment_id: str) -> GetEnvironmentOkResponse:
        """Gets information about an environment.

        :param environment_id: The environment's ID.
        :type environment_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: GetEnvironmentOkResponse
        """

        Validator(str).validate(environment_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/environments/{{environmentId}}",
                self.get_default_headers(),
            )
            .add_path("environmentId", environment_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetEnvironmentOkResponse._unmap(response)

    @cast_models
    def update_environment(
        self, environment_id: str, request_body: UpdateEnvironmentRequest = None
    ) -> UpdateEnvironmentOkResponse:
        """Updates an environment.

        :param request_body: The request body., defaults to None
        :type request_body: UpdateEnvironmentRequest, optional
        :param environment_id: The environment's ID.
        :type environment_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: UpdateEnvironmentOkResponse
        """

        Validator(UpdateEnvironmentRequest).is_optional().validate(request_body)
        Validator(str).validate(environment_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/environments/{{environmentId}}",
                self.get_default_headers(),
            )
            .add_path("environmentId", environment_id)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return UpdateEnvironmentOkResponse._unmap(response)

    @cast_models
    def delete_environment(self, environment_id: str) -> DeleteEnvironmentOkResponse:
        """Deletes an environment.

        :param environment_id: The environment's ID.
        :type environment_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: DeleteEnvironmentOkResponse
        """

        Validator(str).validate(environment_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/environments/{{environmentId}}",
                self.get_default_headers(),
            )
            .add_path("environmentId", environment_id)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)

        return DeleteEnvironmentOkResponse._unmap(response)

    @cast_models
    def get_environment_forks(
        self,
        environment_id: str,
        cursor: str = None,
        direction: AscDesc = None,
        limit: int = None,
        sort: GetEnvironmentForksSort = None,
    ) -> GetEnvironmentForksOkResponse:
        """Gets all of an environment's forked environments.

        :param environment_id: The environment's unique ID.
        :type environment_id: str
        :param cursor: The pointer to the first record of the set of paginated results. To view the next response, use the `nextCursor` value for this parameter., defaults to None
        :type cursor: str, optional
        :param direction: Sort results in ascending (`asc`) or descending (`desc`) order., defaults to None
        :type direction: AscDesc, optional
        :param limit: The maximum number of rows to return in the response., defaults to None
        :type limit: int, optional
        :param sort: Sort the results by the date and time of creation., defaults to None
        :type sort: GetEnvironmentForksSort, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: GetEnvironmentForksOkResponse
        """

        Validator(str).validate(environment_id)
        Validator(str).is_optional().validate(cursor)
        Validator(AscDesc).is_optional().validate(direction)
        Validator(int).is_optional().validate(limit)
        Validator(GetEnvironmentForksSort).is_optional().validate(sort)

        serialized_request = (
            Serializer(
                f"{self.base_url}/environments/{{environmentId}}/forks",
                self.get_default_headers(),
            )
            .add_path("environmentId", environment_id)
            .add_query("cursor", cursor)
            .add_query("direction", direction)
            .add_query("limit", limit)
            .add_query("sort", sort)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetEnvironmentForksOkResponse._unmap(response)

    @cast_models
    def fork_environment(
        self,
        environment_id: str,
        workspace_id: str,
        request_body: ForkEnvironmentRequest = None,
    ) -> ForkEnvironmentOkResponse:
        """Creates a [fork](https://learning.postman.com/docs/collaborating-in-postman/using-version-control/forking-elements/) of an existing environment.

        :param request_body: The request body., defaults to None
        :type request_body: ForkEnvironmentRequest, optional
        :param environment_id: The environment's unique ID.
        :type environment_id: str
        :param workspace_id: The workspace's ID.
        :type workspace_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: ForkEnvironmentOkResponse
        """

        Validator(ForkEnvironmentRequest).is_optional().validate(request_body)
        Validator(str).validate(environment_id)
        Validator(str).validate(workspace_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/environments/{{environmentId}}/forks",
                self.get_default_headers(),
            )
            .add_path("environmentId", environment_id)
            .add_query("workspaceId", workspace_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return ForkEnvironmentOkResponse._unmap(response)

    @cast_models
    def merge_environment_fork(
        self, environment_id: str, request_body: MergeEnvironmentForkRequest = None
    ) -> MergeEnvironmentForkOkResponse:
        """[Merges](https://learning.postman.com/docs/collaborating-in-postman/using-version-control/forking-elements/#merge-changes-from-a-fork) a forked environment back into its parent environment.

        :param request_body: The request body., defaults to None
        :type request_body: MergeEnvironmentForkRequest, optional
        :param environment_id: The environment's unique ID.
        :type environment_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: MergeEnvironmentForkOkResponse
        """

        Validator(MergeEnvironmentForkRequest).is_optional().validate(request_body)
        Validator(str).validate(environment_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/environments/{{environmentId}}/merges",
                self.get_default_headers(),
            )
            .add_path("environmentId", environment_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return MergeEnvironmentForkOkResponse._unmap(response)

    @cast_models
    def pull_environment(
        self, environment_id: str, request_body: PullEnvironmentRequest = None
    ) -> PullEnvironmentOkResponse:
        """[Pulls](https://learning.postman.com/docs/collaborating-in-postman/using-version-control/forking-elements/#pull-updates-from-a-parent-element) the changes from a parent (source) environment into the forked environment.

        :param request_body: The request body., defaults to None
        :type request_body: PullEnvironmentRequest, optional
        :param environment_id: The environment's unique ID.
        :type environment_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: PullEnvironmentOkResponse
        """

        Validator(PullEnvironmentRequest).is_optional().validate(request_body)
        Validator(str).validate(environment_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/environments/{{environmentId}}/pulls",
                self.get_default_headers(),
            )
            .add_path("environmentId", environment_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return PullEnvironmentOkResponse._unmap(response)
