from typing import List
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.update_mock_server_response_request import UpdateMockServerResponseRequest
from ..models.update_mock_request import UpdateMockRequest
from ..models.unpublish_mock_ok_response import UnpublishMockOkResponse
from ..models.publish_mock_ok_response import PublishMockOkResponse
from ..models.get_mocks_ok_response import GetMocksOkResponse
from ..models.get_mock_server_responses_ok_response import (
    GetMockServerResponsesOkResponse,
)
from ..models.get_mock_ok_response import GetMockOkResponse
from ..models.get_mock_call_logs_sort import GetMockCallLogsSort
from ..models.get_mock_call_logs_ok_response import GetMockCallLogsOkResponse
from ..models.delete_mock_server_response_ok_response import (
    DeleteMockServerResponseOkResponse,
)
from ..models.delete_mock_ok_response import DeleteMockOkResponse
from ..models.create_mock_server_response_request import CreateMockServerResponseRequest
from ..models.create_mock_request import CreateMockRequest
from ..models.create_mock_ok_response import CreateMockOkResponse
from ..models.asc_desc import AscDesc


class MocksService(BaseService):

    @cast_models
    def get_mocks(
        self, team_id: str = None, workspace: str = None
    ) -> GetMocksOkResponse:
        """Gets all mock servers. By default, this endpoint returns only mock servers you created across all workspaces.

        **Note:**

        If you pass both the `teamId` and `workspace` query parameters, this endpoint only accepts the `workspace` query.

        :param team_id: Return only results that belong to the given team ID., defaults to None
        :type team_id: str, optional
        :param workspace: Return only results found in the given workspace., defaults to None
        :type workspace: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: GetMocksOkResponse
        """

        Validator(str).is_optional().validate(team_id)
        Validator(str).is_optional().validate(workspace)

        serialized_request = (
            Serializer(f"{self.base_url}/mocks", self.get_default_headers())
            .add_query("teamId", team_id)
            .add_query("workspace", workspace)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetMocksOkResponse._unmap(response)

    @cast_models
    def create_mock(
        self, request_body: CreateMockRequest, workspace_id: str = None
    ) -> CreateMockOkResponse:
        """Creates a mock server in a collection.

        **Note:**

        - If you do not include the `workspaceId` query parameter, the system creates the mock server in your [Personal
        workspace](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/creating-workspaces/).
        - You cannot create mocks for collections added to an API definition.

        :param request_body: The request body.
        :type request_body: CreateMockRequest
        :param workspace_id: The workspace's ID., defaults to None
        :type workspace_id: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: CreateMockOkResponse
        """

        Validator(CreateMockRequest).validate(request_body)
        Validator(str).is_optional().validate(workspace_id)

        serialized_request = (
            Serializer(f"{self.base_url}/mocks", self.get_default_headers())
            .add_query("workspaceId", workspace_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return CreateMockOkResponse._unmap(response)

    @cast_models
    def get_mock(self, mock_id: str) -> GetMockOkResponse:
        """Gets information about a mock server.

        :param mock_id: The mock's ID.
        :type mock_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: GetMockOkResponse
        """

        Validator(str).validate(mock_id)

        serialized_request = (
            Serializer(f"{self.base_url}/mocks/{{mockId}}", self.get_default_headers())
            .add_path("mockId", mock_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetMockOkResponse._unmap(response)

    @cast_models
    def update_mock(
        self, mock_id: str, request_body: UpdateMockRequest = None
    ) -> CreateMockOkResponse:
        """Updates a mock server.

        :param request_body: The request body., defaults to None
        :type request_body: UpdateMockRequest, optional
        :param mock_id: The mock's ID.
        :type mock_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: CreateMockOkResponse
        """

        Validator(UpdateMockRequest).is_optional().validate(request_body)
        Validator(str).validate(mock_id)

        serialized_request = (
            Serializer(f"{self.base_url}/mocks/{{mockId}}", self.get_default_headers())
            .add_path("mockId", mock_id)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return CreateMockOkResponse._unmap(response)

    @cast_models
    def delete_mock(self, mock_id: str) -> DeleteMockOkResponse:
        """Deletes a mock server.

        :param mock_id: The mock's ID.
        :type mock_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: DeleteMockOkResponse
        """

        Validator(str).validate(mock_id)

        serialized_request = (
            Serializer(f"{self.base_url}/mocks/{{mockId}}", self.get_default_headers())
            .add_path("mockId", mock_id)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)

        return DeleteMockOkResponse._unmap(response)

    @cast_models
    def get_mock_call_logs(
        self,
        mock_id: str,
        limit: float = None,
        cursor: str = None,
        until: str = None,
        since: str = None,
        response_status_code: float = None,
        response_type: str = None,
        request_method: str = None,
        request_path: str = None,
        sort: GetMockCallLogsSort = None,
        direction: AscDesc = None,
        include: str = None,
    ) -> GetMockCallLogsOkResponse:
        """Gets a mock server's call logs. You can get a maximum of 6.5MB of call logs or a total of 100 call logs, whichever limit is met first in one API call.

        Call logs contain exchanged request and response data made to mock servers. The logs provide visibility into how the mock servers are being used. You can log data to debug, test, analyze, and more, depending upon the use case.

        :param mock_id: The mock's ID.
        :type mock_id: str
        :param limit: The maximum number of rows to return in the response., defaults to None
        :type limit: float, optional
        :param cursor: The pointer to the first record of the set of paginated results. To view the next response, use the `nextCursor` value for this parameter., defaults to None
        :type cursor: str, optional
        :param until: Return only results created until this given time, in [ISO 8601](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) format. This value cannot be earlier than the `since` value., defaults to None
        :type until: str, optional
        :param since: Return only results created since the given time, in [ISO 8601](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) format. This value cannot be later than the `until` value., defaults to None
        :type since: str, optional
        :param response_status_code: Return only call logs that match the given HTTP response status code., defaults to None
        :type response_status_code: float, optional
        :param response_type: Return only call logs that match the given response type. Matching is not case-sensitive., defaults to None
        :type response_type: str, optional
        :param request_method: Return only call logs that match the given HTTP method. Matching is not case-sensitive., defaults to None
        :type request_method: str, optional
        :param request_path: Return only call logs that match the given request path. Matching is not case-sensitive., defaults to None
        :type request_path: str, optional
        :param sort: Sort the results by the given value. If you use this query parameter, you must also use the `direction` parameter., defaults to None
        :type sort: GetMockCallLogsSort, optional
        :param direction: Sort in ascending (`asc`) or descending (`desc`) order. Matching is not case-sensitive. If you use this query parameter, you must also use the `sort` parameter., defaults to None
        :type direction: AscDesc, optional
        :param include: Include call log records with header and body data. This query parameter accepts the `request.headers`, `request.body`, `response.headers`, and `response.body` values. For multiple include types, comma-separate each value., defaults to None
        :type include: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: GetMockCallLogsOkResponse
        """

        Validator(str).validate(mock_id)
        Validator(float).is_optional().validate(limit)
        Validator(str).is_optional().validate(cursor)
        Validator(str).is_optional().validate(until)
        Validator(str).is_optional().validate(since)
        Validator(float).is_optional().validate(response_status_code)
        Validator(str).is_optional().validate(response_type)
        Validator(str).is_optional().validate(request_method)
        Validator(str).is_optional().validate(request_path)
        Validator(GetMockCallLogsSort).is_optional().validate(sort)
        Validator(AscDesc).is_optional().validate(direction)
        Validator(str).is_optional().validate(include)

        serialized_request = (
            Serializer(
                f"{self.base_url}/mocks/{{mockId}}/call-logs",
                self.get_default_headers(),
            )
            .add_path("mockId", mock_id)
            .add_query("limit", limit)
            .add_query("cursor", cursor)
            .add_query("until", until)
            .add_query("since", since)
            .add_query("responseStatusCode", response_status_code)
            .add_query("responseType", response_type)
            .add_query("requestMethod", request_method)
            .add_query("requestPath", request_path)
            .add_query("sort", sort)
            .add_query("direction", direction)
            .add_query("include", include)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetMockCallLogsOkResponse._unmap(response)

    @cast_models
    def publish_mock(self, mock_id: str) -> PublishMockOkResponse:
        """Publishes a mock server. Publishing a mock server sets its **Access Control** configuration setting to public.

        :param mock_id: The mock's ID.
        :type mock_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: PublishMockOkResponse
        """

        Validator(str).validate(mock_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/mocks/{{mockId}}/publish", self.get_default_headers()
            )
            .add_path("mockId", mock_id)
            .serialize()
            .set_method("POST")
        )

        response = self.send_request(serialized_request)

        return PublishMockOkResponse._unmap(response)

    @cast_models
    def unpublish_mock(self, mock_id: str) -> UnpublishMockOkResponse:
        """Unpublishes a mock server. Unpublishing a mock server sets its **Access Control** configuration setting to private.

        :param mock_id: The mock's ID.
        :type mock_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: UnpublishMockOkResponse
        """

        Validator(str).validate(mock_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/mocks/{{mockId}}/unpublish",
                self.get_default_headers(),
            )
            .add_path("mockId", mock_id)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)

        return UnpublishMockOkResponse._unmap(response)

    @cast_models
    def get_mock_server_responses(
        self, mock_id: str
    ) -> List[GetMockServerResponsesOkResponse]:
        """Gets all of a mock server's server responses.

        :param mock_id: The mock's ID.
        :type mock_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: List[GetMockServerResponsesOkResponse]
        """

        Validator(str).validate(mock_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/mocks/{{mockId}}/server-responses",
                self.get_default_headers(),
            )
            .add_path("mockId", mock_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return [GetMockServerResponsesOkResponse._unmap(item) for item in response]

    @cast_models
    def create_mock_server_response(
        self, request_body: CreateMockServerResponseRequest, mock_id: str
    ) -> dict:
        """Creates a server response. Server responses let you simulate 5xx server-level responses, such as 500 or 503.

        Server-level responses are agnostic to application-level logic. Server responses let you simulate this behavior on a mock server. You do not need to define each error for all exposed paths on the mock server.

        If you set a server response as active, then all the calls to the mock server return with that active server response.

        **Note:**

        You can create multiple server responses for a mock server, but only one mock server can be set as active.

        :param request_body: The request body.
        :type request_body: CreateMockServerResponseRequest
        :param mock_id: The mock's ID.
        :type mock_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: dict
        """

        Validator(CreateMockServerResponseRequest).validate(request_body)
        Validator(str).validate(mock_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/mocks/{{mockId}}/server-responses",
                self.get_default_headers(),
            )
            .add_path("mockId", mock_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return response

    @cast_models
    def get_mock_server_response(self, mock_id: str, server_response_id: str) -> dict:
        """Gets information about a server response.

        :param mock_id: The mock's ID.
        :type mock_id: str
        :param server_response_id: The server response's ID.
        :type server_response_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: dict
        """

        Validator(str).validate(mock_id)
        Validator(str).validate(server_response_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/mocks/{{mockId}}/server-responses/{{serverResponseId}}",
                self.get_default_headers(),
            )
            .add_path("mockId", mock_id)
            .add_path("serverResponseId", server_response_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return response

    @cast_models
    def update_mock_server_response(
        self,
        request_body: UpdateMockServerResponseRequest,
        mock_id: str,
        server_response_id: str,
    ) -> dict:
        """Updates a server response.

        :param request_body: The request body.
        :type request_body: UpdateMockServerResponseRequest
        :param mock_id: The mock's ID.
        :type mock_id: str
        :param server_response_id: The server response's ID.
        :type server_response_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: dict
        """

        Validator(UpdateMockServerResponseRequest).validate(request_body)
        Validator(str).validate(mock_id)
        Validator(str).validate(server_response_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/mocks/{{mockId}}/server-responses/{{serverResponseId}}",
                self.get_default_headers(),
            )
            .add_path("mockId", mock_id)
            .add_path("serverResponseId", server_response_id)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return response

    @cast_models
    def delete_mock_server_response(
        self, mock_id: str, server_response_id: str
    ) -> DeleteMockServerResponseOkResponse:
        """Deletes a mock server's server response.

        :param mock_id: The mock's ID.
        :type mock_id: str
        :param server_response_id: The server response's ID.
        :type server_response_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: DeleteMockServerResponseOkResponse
        """

        Validator(str).validate(mock_id)
        Validator(str).validate(server_response_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/mocks/{{mockId}}/server-responses/{{serverResponseId}}",
                self.get_default_headers(),
            )
            .add_path("mockId", mock_id)
            .add_path("serverResponseId", server_response_id)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)

        return DeleteMockServerResponseOkResponse._unmap(response)
