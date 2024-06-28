<<<<<<< HEAD
=======
# This file was generated by liblab | https://liblab.com/

>>>>>>> 95da91c (initial commit)
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.update_pull_request_request import UpdatePullRequestRequest
from ..models.pull_request_updated import PullRequestUpdated
from ..models.pull_request_get import PullRequestGet


class PullRequestsService(BaseService):

    @cast_models
    def get_pull_request(self, pull_request_id: str) -> PullRequestGet:
        """Gets information about a pull request, such as the source and destination details, who reviewed the pull request, the merge's current status, and whether the element is accessible.

        :param pull_request_id: The pull request's ID.
        :type pull_request_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: PullRequestGet
        """

        Validator(str).validate(pull_request_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/pull-requests/{{pullRequestId}}",
                self.get_default_headers(),
            )
            .add_path("pullRequestId", pull_request_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return PullRequestGet._unmap(response)

    @cast_models
    def update_pull_request(
        self, pull_request_id: str, request_body: UpdatePullRequestRequest = None
    ) -> PullRequestUpdated:
        """Updates an open pull request.

        :param request_body: The request body., defaults to None
        :type request_body: UpdatePullRequestRequest, optional
        :param pull_request_id: The pull request's ID.
        :type pull_request_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: PullRequestUpdated
        """

        Validator(UpdatePullRequestRequest).is_optional().validate(request_body)
        Validator(str).validate(pull_request_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/pull-requests/{{pullRequestId}}",
                self.get_default_headers(),
            )
            .add_path("pullRequestId", pull_request_id)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return PullRequestUpdated._unmap(response)
