from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.update_monitor_request import UpdateMonitorRequest
from ..models.update_monitor_ok_response import UpdateMonitorOkResponse
from ..models.run_monitor_ok_response import RunMonitorOkResponse
from ..models.get_monitors_ok_response import GetMonitorsOkResponse
from ..models.get_monitor_ok_response import GetMonitorOkResponse
from ..models.delete_monitor_ok_response import DeleteMonitorOkResponse
from ..models.create_monitor_request import CreateMonitorRequest
from ..models.create_monitor_ok_response import CreateMonitorOkResponse


class MonitorsService(BaseService):

    @cast_models
    def get_monitors(self, workspace: str = None) -> GetMonitorsOkResponse:
        """Gets all monitors.

        :param workspace: Return only results found in the given workspace., defaults to None
        :type workspace: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: GetMonitorsOkResponse
        """

        Validator(str).is_optional().validate(workspace)

        serialized_request = (
            Serializer(f"{self.base_url}/monitors", self.get_default_headers())
            .add_query("workspace", workspace)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetMonitorsOkResponse._unmap(response)

    @cast_models
    def create_monitor(
        self, request_body: CreateMonitorRequest = None, workspace: str = None
    ) -> CreateMonitorOkResponse:
        """Creates a monitor.

        **Note:**

        You cannot create monitors for collections added to an API definition.

        :param request_body: The request body., defaults to None
        :type request_body: CreateMonitorRequest, optional
        :param workspace: The workspace's ID., defaults to None
        :type workspace: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: CreateMonitorOkResponse
        """

        Validator(CreateMonitorRequest).is_optional().validate(request_body)
        Validator(str).is_optional().validate(workspace)

        serialized_request = (
            Serializer(f"{self.base_url}/monitors", self.get_default_headers())
            .add_query("workspace", workspace)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return CreateMonitorOkResponse._unmap(response)

    @cast_models
    def get_monitor(self, monitor_id: str) -> GetMonitorOkResponse:
        """Gets information about a monitor.

        :param monitor_id: The monitor's ID.
        :type monitor_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: GetMonitorOkResponse
        """

        Validator(str).validate(monitor_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/monitors/{{monitorId}}", self.get_default_headers()
            )
            .add_path("monitorId", monitor_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetMonitorOkResponse._unmap(response)

    @cast_models
    def update_monitor(
        self, monitor_id: str, request_body: UpdateMonitorRequest = None
    ) -> UpdateMonitorOkResponse:
        """Updates a monitor.

        :param request_body: The request body., defaults to None
        :type request_body: UpdateMonitorRequest, optional
        :param monitor_id: The monitor's ID.
        :type monitor_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: UpdateMonitorOkResponse
        """

        Validator(UpdateMonitorRequest).is_optional().validate(request_body)
        Validator(str).validate(monitor_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/monitors/{{monitorId}}", self.get_default_headers()
            )
            .add_path("monitorId", monitor_id)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return UpdateMonitorOkResponse._unmap(response)

    @cast_models
    def delete_monitor(self, monitor_id: str) -> DeleteMonitorOkResponse:
        """Deletes a monitor.

        :param monitor_id: The monitor's ID.
        :type monitor_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: DeleteMonitorOkResponse
        """

        Validator(str).validate(monitor_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/monitors/{{monitorId}}", self.get_default_headers()
            )
            .add_path("monitorId", monitor_id)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)

        return DeleteMonitorOkResponse._unmap(response)

    @cast_models
    def run_monitor(self, monitor_id: str) -> RunMonitorOkResponse:
        """Runs a monitor and returns its run results.

        :param monitor_id: The monitor's ID.
        :type monitor_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: RunMonitorOkResponse
        """

        Validator(str).validate(monitor_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/monitors/{{monitorId}}/run",
                self.get_default_headers(),
            )
            .add_path("monitorId", monitor_id)
            .serialize()
            .set_method("POST")
        )

        response = self.send_request(serialized_request)

        return RunMonitorOkResponse._unmap(response)
