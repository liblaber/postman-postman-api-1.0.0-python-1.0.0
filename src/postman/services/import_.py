from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.import_open_api_definition_request import ImportOpenApiDefinitionRequest
from ..models.import_open_api_definition_ok_response import (
    ImportOpenApiDefinitionOkResponse,
)


class ImportService(BaseService):

    @cast_models
    def import_open_api_definition(
        self, request_body: ImportOpenApiDefinitionRequest = None, workspace: str = None
    ) -> ImportOpenApiDefinitionOkResponse:
        """Imports an OpenAPI definition into Postman as a new [Postman Collection](https://learning.postman.com/docs/getting-started/creating-the-first-collection/).

        :param request_body: The request body., defaults to None
        :type request_body: ImportOpenApiDefinitionRequest, optional
        :param workspace: The workspace's ID., defaults to None
        :type workspace: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: ImportOpenApiDefinitionOkResponse
        """

        Validator(ImportOpenApiDefinitionRequest).is_optional().validate(request_body)
        Validator(str).is_optional().validate(workspace)

        serialized_request = (
            Serializer(f"{self.base_url}/import/openapi", self.get_default_headers())
            .add_query("workspace", workspace)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return ImportOpenApiDefinitionOkResponse._unmap(response)
