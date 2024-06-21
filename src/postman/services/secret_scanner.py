from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.update_detected_secret_resolutions_request import (
    UpdateDetectedSecretResolutionsRequest,
)
from ..models.update_detected_secret_resolutions_ok_response import (
    UpdateDetectedSecretResolutionsOkResponse,
)
from ..models.get_secret_types_ok_response import GetSecretTypesOkResponse
from ..models.get_detected_secrets_locations_ok_response import (
    GetDetectedSecretsLocationsOkResponse,
)
from ..models.detected_secrets_queries_request import DetectedSecretsQueriesRequest
from ..models.detected_secrets_queries_ok_response import (
    DetectedSecretsQueriesOkResponse,
)


class SecretScannerService(BaseService):

    @cast_models
    def detected_secrets_queries(
        self,
        request_body: DetectedSecretsQueriesRequest = None,
        limit: int = None,
        cursor: str = None,
        include: str = None,
    ) -> DetectedSecretsQueriesOkResponse:
        """Returns all secrets detected by Postman's [Secret Scanner](https://learning.postman.com/docs/administration/secret-scanner/), grouped by workspace. If you pass an empty request body, this endpoint returns all results.

        :param request_body: The request body., defaults to None
        :type request_body: DetectedSecretsQueriesRequest, optional
        :param limit: The maximum number of rows to return in the response., defaults to None
        :type limit: int, optional
        :param cursor: The pointer to the first record of the set of paginated results. To view the next response, use the `nextCursor` value for this parameter., defaults to None
        :type cursor: str, optional
        :param include: The additional fields to be included as a part of the request., defaults to None
        :type include: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: DetectedSecretsQueriesOkResponse
        """

        Validator(DetectedSecretsQueriesRequest).is_optional().validate(request_body)
        Validator(int).is_optional().validate(limit)
        Validator(str).is_optional().validate(cursor)
        Validator(str).is_optional().validate(include)

        serialized_request = (
            Serializer(
                f"{self.base_url}/detected-secrets-queries", self.get_default_headers()
            )
            .add_query("limit", limit)
            .add_query("cursor", cursor)
            .add_query("include", include)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return DetectedSecretsQueriesOkResponse._unmap(response)

    @cast_models
    def update_detected_secret_resolutions(
        self,
        secret_id: str,
        request_body: UpdateDetectedSecretResolutionsRequest = None,
    ) -> UpdateDetectedSecretResolutionsOkResponse:
        """Updates the resolution status of a secret detected in a workspace.

        :param request_body: The request body., defaults to None
        :type request_body: UpdateDetectedSecretResolutionsRequest, optional
        :param secret_id: The secret's ID.
        :type secret_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: UpdateDetectedSecretResolutionsOkResponse
        """

        Validator(UpdateDetectedSecretResolutionsRequest).is_optional().validate(
            request_body
        )
        Validator(str).validate(secret_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/detected-secrets/{{secretId}}",
                self.get_default_headers(),
            )
            .add_path("secretId", secret_id)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return UpdateDetectedSecretResolutionsOkResponse._unmap(response)

    @cast_models
    def get_detected_secrets_locations(
        self, secret_id: str, workspace_id: str, limit: int = None, cursor: str = None
    ) -> GetDetectedSecretsLocationsOkResponse:
        """Gets the locations of secrets detected by Postman's [Secret Scanner](https://learning.postman.com/docs/administration/secret-scanner/).

        :param secret_id: The secret's ID.
        :type secret_id: str
        :param workspace_id: The workspace's ID.
        :type workspace_id: str
        :param limit: The maximum number of rows to return in the response., defaults to None
        :type limit: int, optional
        :param cursor: The pointer to the first record of the set of paginated results. To view the next response, use the `nextCursor` value for this parameter., defaults to None
        :type cursor: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: GetDetectedSecretsLocationsOkResponse
        """

        Validator(str).validate(secret_id)
        Validator(str).validate(workspace_id)
        Validator(int).is_optional().validate(limit)
        Validator(str).is_optional().validate(cursor)

        serialized_request = (
            Serializer(
                f"{self.base_url}/detected-secrets/{{secretId}}/locations",
                self.get_default_headers(),
            )
            .add_path("secretId", secret_id)
            .add_query("limit", limit)
            .add_query("cursor", cursor)
            .add_query("workspaceId", workspace_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetDetectedSecretsLocationsOkResponse._unmap(response)

    @cast_models
    def get_secret_types(self) -> GetSecretTypesOkResponse:
        """Gets the metadata of the secret types supported by Postman's [Secret Scanner](https://learning.postman.com/docs/administration/secret-scanner/). You can use a secret type's ID in the response to query data with the POST `/detected-secrets/{secretId}` endpoint.

        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: GetSecretTypesOkResponse
        """

        serialized_request = (
            Serializer(f"{self.base_url}/secret-types", self.get_default_headers())
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetSecretTypesOkResponse._unmap(response)
