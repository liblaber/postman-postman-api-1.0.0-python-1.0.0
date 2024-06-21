from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.create_webhook_request import CreateWebhookRequest
from ..models.create_webhook_ok_response import CreateWebhookOkResponse


class WebhooksService(BaseService):

    @cast_models
    def create_webhook(
        self, request_body: CreateWebhookRequest = None, workspace: str = None
    ) -> CreateWebhookOkResponse:
        """Creates a webhook that triggers a collection with a custom payload. You can get the webhook's URL from the `webhookUrl` property in the endpoint's response.

        :param request_body: The request body., defaults to None
        :type request_body: CreateWebhookRequest, optional
        :param workspace: The workspace's ID., defaults to None
        :type workspace: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: CreateWebhookOkResponse
        """

        Validator(CreateWebhookRequest).is_optional().validate(request_body)
        Validator(str).is_optional().validate(workspace)

        serialized_request = (
            Serializer(f"{self.base_url}/webhooks", self.get_default_headers())
            .add_query("workspace", workspace)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return CreateWebhookOkResponse._unmap(response)
