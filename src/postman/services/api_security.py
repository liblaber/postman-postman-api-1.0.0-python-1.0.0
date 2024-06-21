from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.schema_security_validation_request import SchemaSecurityValidationRequest
from ..models.schema_security_validation_ok_response import (
    SchemaSecurityValidationOkResponse,
)


class ApiSecurityService(BaseService):

    @cast_models
    def schema_security_validation(
        self, request_body: SchemaSecurityValidationRequest = None
    ) -> SchemaSecurityValidationOkResponse:
        """Performs an analysis on the given definition and returns any issues based on your [predefined rulesets](https://learning.postman.com/docs/api-governance/configurable-rules/configurable-rules-overview/). This endpoint can help you understand the violations' impact and offers solutions to help you resolve any errors. You can include this endpoint to your CI/CD process to automate schema validation.

        For more information, see our [Rule violations in the API definition](https://learning.postman.com/docs/api-governance/api-definition/api-definition-warnings/) documentation.

        **Note:**

        - The maximum allowed size of the definition is 10 MB.
        - You must [import and enable](https://learning.postman.com/docs/api-governance/configurable-rules/configuring-api-security-rules/) [Postman's OWASP security rules](https://postman.postman.co/api-governance/libraries/postman_owasp/view) in Postman for this endpoint to return any security rule violations.

        :param request_body: The request body., defaults to None
        :type request_body: SchemaSecurityValidationRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: SchemaSecurityValidationOkResponse
        """

        Validator(SchemaSecurityValidationRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url}/security/api-validation", self.get_default_headers()
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return SchemaSecurityValidationOkResponse._unmap(response)
