from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.get_authenticated_user_ok_response import GetAuthenticatedUserOkResponse


class UserService(BaseService):

    @cast_models
    def get_authenticated_user(self) -> GetAuthenticatedUserOkResponse:
        """Gets information about the authenticated user.

        **Note:**

        This API returns a different response for users with the [Guest role](https://learning.postman.com/docs/collaborating-in-postman/roles-and-permissions/#team-roles).

        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: GetAuthenticatedUserOkResponse
        """

        serialized_request = (
            Serializer(f"{self.base_url}/me", self.get_default_headers())
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetAuthenticatedUserOkResponse._unmap(response)
