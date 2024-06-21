from typing import List
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.update_api_version_request import UpdateApiVersionRequest
from ..models.update_api_version_ok_response import UpdateApiVersionOkResponse
from ..models.update_api_request import UpdateApiRequest
from ..models.update_api_ok_response import UpdateApiOkResponse
from ..models.sync_collection_with_schema_accepted_response import (
    SyncCollectionWithSchemaAcceptedResponse,
)
from ..models.get_status_of_an_async_task_ok_response import (
    GetStatusOfAnAsyncTaskOkResponse,
)
from ..models.get_apis_ok_response import GetApisOkResponse
from ..models.get_api_versions_ok_response import GetApiVersionsOkResponse
from ..models.get_api_version_ok_response import GetApiVersionOkResponse
from ..models.get_api_schema_ok_response import (
    GetApiSchemaOkResponse,
    GetApiSchemaOkResponseGuard,
)
from ..models.get_api_schema_files_ok_response import GetApiSchemaFilesOkResponse
from ..models.get_api_schema_file_contents_ok_response import (
    GetApiSchemaFileContentsOkResponse,
)
from ..models.get_api_ok_response import GetApiOkResponse, GetApiOkResponseGuard
from ..models.get_api_include import GetApiInclude
from ..models.create_update_api_schema_file_request import (
    CreateUpdateApiSchemaFileRequest,
)
from ..models.create_update_api_schema_file_ok_response import (
    CreateUpdateApiSchemaFileOkResponse,
)
from ..models.create_api_version_request import CreateApiVersionRequest
from ..models.create_api_version_accepted_response import (
    CreateApiVersionAcceptedResponse,
)
from ..models.create_api_schema_request import CreateApiSchemaRequest
from ..models.create_api_schema_ok_response import CreateApiSchemaOkResponse
from ..models.create_api_request import CreateApiRequest
from ..models.create_api_ok_response import CreateApiOkResponse
from ..models.comment_response import CommentResponse
from ..models.comment_created_updated import CommentCreatedUpdated
from ..models.comment_create_update import CommentCreateUpdate
from ..models.add_api_collection_request import AddApiCollectionRequest
from ..models.add_api_collection_ok_response import AddApiCollectionOkResponse
from ..models.accept import Accept


class ApiService(BaseService):

    @cast_models
    def get_apis(
        self,
        workspace_id: str,
        accept: Accept,
        created_by: int = None,
        cursor: str = None,
        description: str = None,
        limit: int = None,
    ) -> GetApisOkResponse:
        """Gets information about all APIs in a workspace.

        :param workspace_id: The workspace's ID.
        :type workspace_id: str
        :param accept: The `application/vnd.api.v10+json` request header required to use the endpoint.
        :type accept: Accept
        :param created_by: Return only results created by the given user ID., defaults to None
        :type created_by: int, optional
        :param cursor: The pointer to the first record of the set of paginated results. To view the next response, use the `nextCursor` value for this parameter., defaults to None
        :type cursor: str, optional
        :param description: Return only APIs whose description includes the given value. Matching is not case-sensitive., defaults to None
        :type description: str, optional
        :param limit: The maximum number of rows to return in the response., defaults to None
        :type limit: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: GetApisOkResponse
        """

        Validator(str).validate(workspace_id)
        Validator(Accept).validate(accept)
        Validator(int).is_optional().validate(created_by)
        Validator(str).is_optional().validate(cursor)
        Validator(str).is_optional().validate(description)
        Validator(int).is_optional().validate(limit)

        serialized_request = (
            Serializer(f"{self.base_url}/apis", self.get_default_headers())
            .add_header("Accept", accept)
            .add_query("workspaceId", workspace_id)
            .add_query("createdBy", created_by)
            .add_query("cursor", cursor)
            .add_query("description", description)
            .add_query("limit", limit)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetApisOkResponse._unmap(response)

    @cast_models
    def create_api(
        self, workspace_id: str, accept: Accept, request_body: CreateApiRequest = None
    ) -> CreateApiOkResponse:
        """Creates an API.

        :param request_body: The request body., defaults to None
        :type request_body: CreateApiRequest, optional
        :param workspace_id: The workspace's ID.
        :type workspace_id: str
        :param accept: The `application/vnd.api.v10+json` request header required to use the endpoint.
        :type accept: Accept
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: CreateApiOkResponse
        """

        Validator(CreateApiRequest).is_optional().validate(request_body)
        Validator(str).validate(workspace_id)
        Validator(Accept).validate(accept)

        serialized_request = (
            Serializer(f"{self.base_url}/apis", self.get_default_headers())
            .add_header("Accept", accept)
            .add_query("workspaceId", workspace_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return CreateApiOkResponse._unmap(response)

    @cast_models
    def get_api(
        self, api_id: str, accept: Accept, include: List[GetApiInclude] = None
    ) -> GetApiOkResponse:
        """Gets information about an API.

        **Note:**

        - Git-connected APIs will only return the `versions` and `gitInfo` query responses. This is because schema and collection information is stored in the connected Git repository. The `gitInfo` object only lists the repository and folder locations of the files.
        - API viewers can only use the `versions` option in the `include` query parameter.

        :param api_id: The API's ID.
        :type api_id: str
        :param accept: The `application/vnd.api.v10+json` request header required to use the endpoint.
        :type accept: Accept
        :param include: An array that contains additional resources to include in the response. Use this parameter to query for element links to the API, such as  collections and schemas:
        - `collections` — Query for linked Postman collections.
        - `versions` — Query for linked versions.
        - `schemas` — Query for linked schemas.
        - `gitInfo` — Query for information about the API's git-linked repository. This query only returns the linked repository and folder locations of the files. It does not return `collections` or `schemas` information.

        **Note:**

        API viewers can only use the `versions` option., defaults to None
        :type include: List[GetApiInclude], optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: GetApiOkResponse
        """

        Validator(str).validate(api_id)
        Validator(Accept).validate(accept)
        Validator(GetApiInclude).is_array().is_optional().validate(include)

        serialized_request = (
            Serializer(f"{self.base_url}/apis/{{apiId}}", self.get_default_headers())
            .add_header("Accept", accept)
            .add_path("apiId", api_id)
            .add_query("include", include)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetApiOkResponseGuard.return_one_of(response)

    @cast_models
    def update_api(
        self, api_id: str, accept: Accept, request_body: UpdateApiRequest = None
    ) -> UpdateApiOkResponse:
        """Updates an API.

        :param request_body: The request body., defaults to None
        :type request_body: UpdateApiRequest, optional
        :param api_id: The API's ID.
        :type api_id: str
        :param accept: The `application/vnd.api.v10+json` request header required to use the endpoint.
        :type accept: Accept
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: UpdateApiOkResponse
        """

        Validator(UpdateApiRequest).is_optional().validate(request_body)
        Validator(str).validate(api_id)
        Validator(Accept).validate(accept)

        serialized_request = (
            Serializer(f"{self.base_url}/apis/{{apiId}}", self.get_default_headers())
            .add_header("Accept", accept)
            .add_path("apiId", api_id)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return UpdateApiOkResponse._unmap(response)

    @cast_models
    def delete_api(self, api_id: str, accept: Accept):
        """Deletes an API.

        :param api_id: The API's ID.
        :type api_id: str
        :param accept: The `application/vnd.api.v10+json` request header required to use the endpoint.
        :type accept: Accept
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(api_id)
        Validator(Accept).validate(accept)

        serialized_request = (
            Serializer(f"{self.base_url}/apis/{{apiId}}", self.get_default_headers())
            .add_header("Accept", accept)
            .add_path("apiId", api_id)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)

        return response

    @cast_models
    def add_api_collection(
        self, api_id: str, accept: Accept, request_body: AddApiCollectionRequest = None
    ) -> AddApiCollectionOkResponse:
        """Adds a collection to an API. To do this, use the following `operationType` values:

        - `COPY_COLLECTION` — Copies a collection from the workspace and adds it to an API.
        - `CREATE_NEW` — Creates a new collection by providing the new collection's content.
        - `GENERATE_FROM_SCHEMA` — Generates the collection from an API schema.
            - `options` — An object that contains advanced creation options and their values. You can find a complete list of properties and their values in Postman's [OpenAPI 3.0 to Postman Collection v2.1.0 Converter OPTIONS documentation](https://github.com/postmanlabs/openapi-to-postman/blob/develop/OPTIONS.md). These properties are case-sensitive.

        :param request_body: The request body., defaults to None
        :type request_body: AddApiCollectionRequest, optional
        :param api_id: The API's ID.
        :type api_id: str
        :param accept: The `application/vnd.api.v10+json` request header required to use the endpoint.
        :type accept: Accept
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Created
        :rtype: AddApiCollectionOkResponse
        """

        Validator(AddApiCollectionRequest).is_optional().validate(request_body)
        Validator(str).validate(api_id)
        Validator(Accept).validate(accept)

        serialized_request = (
            Serializer(
                f"{self.base_url}/apis/{{apiId}}/collections",
                self.get_default_headers(),
            )
            .add_header("Accept", accept)
            .add_path("apiId", api_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return AddApiCollectionOkResponse._unmap(response)

    @cast_models
    def get_api_collection(
        self, api_id: str, collection_id: str, accept: Accept, version_id: str = None
    ) -> dict:
        """Gets a collection attached to an API. You can use the `versionId` query parameter to get a collection published in a version.

        **Note:**

        The `versionId` query parameter is a required parameter for API viewers.

        :param api_id: The API's ID.
        :type api_id: str
        :param collection_id: The collection's unique ID.
        :type collection_id: str
        :param accept: The `application/vnd.api.v10+json` request header required to use the endpoint.
        :type accept: Accept
        :param version_id: The API's version ID., defaults to None
        :type version_id: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: dict
        """

        Validator(str).validate(api_id)
        Validator(str).validate(collection_id)
        Validator(Accept).validate(accept)
        Validator(str).is_optional().validate(version_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/apis/{{apiId}}/collections/{{collectionId}}",
                self.get_default_headers(),
            )
            .add_header("Accept", accept)
            .add_path("apiId", api_id)
            .add_path("collectionId", collection_id)
            .add_query("versionId", version_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return response

    @cast_models
    def sync_collection_with_schema(
        self, api_id: str, collection_id: str, accept: Accept
    ) -> SyncCollectionWithSchemaAcceptedResponse:
        """Syncs a collection attached to an API with the API schema.

        This is an asynchronous endpoint that returns an HTTP `202 Accepted` response. The response contains a polling link to the `/apis/{apiId}/tasks/{taskId}` endpoint in the `Location` header.

        **Note:**

        This endpoint only supports the OpenAPI 3 schema type.

        :param api_id: The API's ID.
        :type api_id: str
        :param collection_id: The collection's unique ID.
        :type collection_id: str
        :param accept: The `application/vnd.api.v10+json` request header required to use the endpoint.
        :type accept: Accept
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Accepted
        :rtype: SyncCollectionWithSchemaAcceptedResponse
        """

        Validator(str).validate(api_id)
        Validator(str).validate(collection_id)
        Validator(Accept).validate(accept)

        serialized_request = (
            Serializer(
                f"{self.base_url}/apis/{{apiId}}/collections/{{collectionId}}/sync-with-schema-tasks",
                self.get_default_headers(),
            )
            .add_header("Accept", accept)
            .add_path("apiId", api_id)
            .add_path("collectionId", collection_id)
            .serialize()
            .set_method("PUT")
        )

        response = self.send_request(serialized_request)

        return SyncCollectionWithSchemaAcceptedResponse._unmap(response)

    @cast_models
    def get_api_comments(self, api_id: str) -> CommentResponse:
        """Gets all comments left by users in an API.

        :param api_id: The API's ID.
        :type api_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: CommentResponse
        """

        Validator(str).validate(api_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/apis/{{apiId}}/comments", self.get_default_headers()
            )
            .add_path("apiId", api_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return CommentResponse._unmap(response)

    @cast_models
    def create_api_comment(
        self, request_body: CommentCreateUpdate, api_id: str
    ) -> CommentCreatedUpdated:
        """Creates a comment on an API.

        **Note:**

        This endpoint accepts a max of 10,000 characters.

        :param request_body: The request body.
        :type request_body: CommentCreateUpdate
        :param api_id: The API's ID.
        :type api_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Created
        :rtype: CommentCreatedUpdated
        """

        Validator(CommentCreateUpdate).validate(request_body)
        Validator(str).validate(api_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/apis/{{apiId}}/comments", self.get_default_headers()
            )
            .add_path("apiId", api_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return CommentCreatedUpdated._unmap(response)

    @cast_models
    def update_api_comment(
        self, request_body: CommentCreateUpdate, api_id: str, comment_id: int
    ) -> CommentCreatedUpdated:
        """Updates a comment on an API.

        **Note:**

        This endpoint accepts a max of 10,000 characters.

        :param request_body: The request body.
        :type request_body: CommentCreateUpdate
        :param api_id: The API's ID.
        :type api_id: str
        :param comment_id: The comment's ID.
        :type comment_id: int
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: CommentCreatedUpdated
        """

        Validator(CommentCreateUpdate).validate(request_body)
        Validator(str).validate(api_id)
        Validator(int).validate(comment_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/apis/{{apiId}}/comments/{{commentId}}",
                self.get_default_headers(),
            )
            .add_path("apiId", api_id)
            .add_path("commentId", comment_id)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return CommentCreatedUpdated._unmap(response)

    @cast_models
    def delete_api_comment(self, api_id: str, comment_id: int):
        """Deletes a comment from an API. On success, this returns an HTTP `204 No Content` response.

        **Note:**

        Deleting the first comment of a thread deletes all the comments in the thread.

        :param api_id: The API's ID.
        :type api_id: str
        :param comment_id: The comment's ID.
        :type comment_id: int
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(api_id)
        Validator(int).validate(comment_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/apis/{{apiId}}/comments/{{commentId}}",
                self.get_default_headers(),
            )
            .add_path("apiId", api_id)
            .add_path("commentId", comment_id)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)

        return response

    @cast_models
    def create_api_schema(
        self, api_id: str, accept: Accept, request_body: CreateApiSchemaRequest = None
    ) -> CreateApiSchemaOkResponse:
        """Creates a schema for an API.

        :param request_body: The request body., defaults to None
        :type request_body: CreateApiSchemaRequest, optional
        :param api_id: The API's ID.
        :type api_id: str
        :param accept: The `application/vnd.api.v10+json` request header required to use the endpoint.
        :type accept: Accept
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Created
        :rtype: CreateApiSchemaOkResponse
        """

        Validator(CreateApiSchemaRequest).is_optional().validate(request_body)
        Validator(str).validate(api_id)
        Validator(Accept).validate(accept)

        serialized_request = (
            Serializer(
                f"{self.base_url}/apis/{{apiId}}/schemas", self.get_default_headers()
            )
            .add_header("Accept", accept)
            .add_path("apiId", api_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return CreateApiSchemaOkResponse._unmap(response)

    @cast_models
    def get_api_schema(
        self,
        api_id: str,
        schema_id: str,
        accept: Accept,
        version_id: str = None,
        bundled: bool = None,
    ) -> GetApiSchemaOkResponse:
        """Gets information about API schema. You can use the `versionId` query parameter to get a schema published in an API version.

        You can use this API to do the following:

        - Get a schema's metadata.
        - Get all the files in a schema. This only returns the first file in the schema. The endpoint response contains a link to the next set of response results.
        - Get a schema's contents in multi-file or bundled format.

        **Note:**

        The `versionId` query parameter is a required parameter for API viewers.

        :param api_id: The API's ID.
        :type api_id: str
        :param schema_id: The API schema's ID.
        :type schema_id: str
        :param accept: The `application/vnd.api.v10+json` request header required to use the endpoint.
        :type accept: Accept
        :param version_id: The API's version ID., defaults to None
        :type version_id: str, optional
        :param bundled: If true, return the schema in a bundled format., defaults to None
        :type bundled: bool, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: GetApiSchemaOkResponse
        """

        Validator(str).validate(api_id)
        Validator(str).validate(schema_id)
        Validator(Accept).validate(accept)
        Validator(str).is_optional().validate(version_id)
        Validator(bool).is_optional().validate(bundled)

        serialized_request = (
            Serializer(
                f"{self.base_url}/apis/{{apiId}}/schemas/{{schemaId}}",
                self.get_default_headers(),
            )
            .add_header("Accept", accept)
            .add_path("apiId", api_id)
            .add_path("schemaId", schema_id)
            .add_query("versionId", version_id)
            .add_query("bundled", bundled)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetApiSchemaOkResponseGuard.return_one_of(response)

    @cast_models
    def get_api_schema_files(
        self,
        api_id: str,
        schema_id: str,
        accept: Accept,
        version_id: str = None,
        limit: int = None,
        cursor: str = None,
    ) -> GetApiSchemaFilesOkResponse:
        """Gets the files in an API schema. You can use the `versionId` query parameter to get schema files published in an API version.

        **Note:**

        The `versionId` query parameter is a required parameter for API viewers.

        :param api_id: The API's ID.
        :type api_id: str
        :param schema_id: The API schema's ID.
        :type schema_id: str
        :param accept: The `application/vnd.api.v10+json` request header required to use the endpoint.
        :type accept: Accept
        :param version_id: The API's version ID., defaults to None
        :type version_id: str, optional
        :param limit: The maximum number of rows to return in the response., defaults to None
        :type limit: int, optional
        :param cursor: The pointer to the first record of the set of paginated results. To view the next response, use the `nextCursor` value for this parameter., defaults to None
        :type cursor: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: GetApiSchemaFilesOkResponse
        """

        Validator(str).validate(api_id)
        Validator(str).validate(schema_id)
        Validator(Accept).validate(accept)
        Validator(str).is_optional().validate(version_id)
        Validator(int).is_optional().validate(limit)
        Validator(str).is_optional().validate(cursor)

        serialized_request = (
            Serializer(
                f"{self.base_url}/apis/{{apiId}}/schemas/{{schemaId}}/files",
                self.get_default_headers(),
            )
            .add_header("Accept", accept)
            .add_path("apiId", api_id)
            .add_path("schemaId", schema_id)
            .add_query("versionId", version_id)
            .add_query("limit", limit)
            .add_query("cursor", cursor)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetApiSchemaFilesOkResponse._unmap(response)

    @cast_models
    def get_api_schema_file_contents(
        self,
        api_id: str,
        schema_id: str,
        file_path: str,
        accept: Accept,
        version_id: str = None,
    ) -> GetApiSchemaFileContentsOkResponse:
        """Gets an API schema file contents at the defined path. You can use the `versionId` query parameter to get schema file contents published in an API version.

        **Note:**

        The `versionId` query parameter is a required parameter for API viewers.

        :param api_id: The API's ID.
        :type api_id: str
        :param schema_id: The API schema's ID.
        :type schema_id: str
        :param file_path: The path to the schema file.
        :type file_path: str
        :param accept: The `application/vnd.api.v10+json` request header required to use the endpoint.
        :type accept: Accept
        :param version_id: The API's version ID., defaults to None
        :type version_id: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: GetApiSchemaFileContentsOkResponse
        """

        Validator(str).validate(api_id)
        Validator(str).validate(schema_id)
        Validator(str).validate(file_path)
        Validator(Accept).validate(accept)
        Validator(str).is_optional().validate(version_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/apis/{{apiId}}/schemas/{{schemaId}}/files/{{file-path}}",
                self.get_default_headers(),
            )
            .add_header("Accept", accept)
            .add_path("apiId", api_id)
            .add_path("schemaId", schema_id)
            .add_path("file-path", file_path)
            .add_query("versionId", version_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetApiSchemaFileContentsOkResponse._unmap(response)

    @cast_models
    def create_update_api_schema_file(
        self,
        api_id: str,
        schema_id: str,
        file_path: str,
        accept: Accept,
        request_body: CreateUpdateApiSchemaFileRequest = None,
    ) -> CreateUpdateApiSchemaFileOkResponse:
        """Creates or updates an API schema file.

        **Note:**

        - If the provided file path exists, the file will be updated with the new contents.
        - If the provided file path does not exist, then a new schema file will be created.
        - If the file path contains a `/` (forward slash) character, then a folder is created. For example, if the file path is the `dir/schema.json` value, then a `dir` folder is created with the `schema.json` file inside.

        :param request_body: The request body., defaults to None
        :type request_body: CreateUpdateApiSchemaFileRequest, optional
        :param api_id: The API's ID.
        :type api_id: str
        :param schema_id: The API schema's ID.
        :type schema_id: str
        :param file_path: The path to the schema file.
        :type file_path: str
        :param accept: The `application/vnd.api.v10+json` request header required to use the endpoint.
        :type accept: Accept
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: CreateUpdateApiSchemaFileOkResponse
        """

        Validator(CreateUpdateApiSchemaFileRequest).is_optional().validate(request_body)
        Validator(str).validate(api_id)
        Validator(str).validate(schema_id)
        Validator(str).validate(file_path)
        Validator(Accept).validate(accept)

        serialized_request = (
            Serializer(
                f"{self.base_url}/apis/{{apiId}}/schemas/{{schemaId}}/files/{{file-path}}",
                self.get_default_headers(),
            )
            .add_header("Accept", accept)
            .add_path("apiId", api_id)
            .add_path("schemaId", schema_id)
            .add_path("file-path", file_path)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return CreateUpdateApiSchemaFileOkResponse._unmap(response)

    @cast_models
    def delete_api_schema_file(
        self, api_id: str, schema_id: str, file_path: str, accept: Accept
    ):
        """Deletes a file in an API schema.

        :param api_id: The API's ID.
        :type api_id: str
        :param schema_id: The API schema's ID.
        :type schema_id: str
        :param file_path: The path to the schema file.
        :type file_path: str
        :param accept: The `application/vnd.api.v10+json` request header required to use the endpoint.
        :type accept: Accept
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(api_id)
        Validator(str).validate(schema_id)
        Validator(str).validate(file_path)
        Validator(Accept).validate(accept)

        serialized_request = (
            Serializer(
                f"{self.base_url}/apis/{{apiId}}/schemas/{{schemaId}}/files/{{file-path}}",
                self.get_default_headers(),
            )
            .add_header("Accept", accept)
            .add_path("apiId", api_id)
            .add_path("schemaId", schema_id)
            .add_path("file-path", file_path)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)

        return response

    @cast_models
    def get_status_of_an_async_task(
        self, api_id: str, task_id: str, accept: Accept
    ) -> GetStatusOfAnAsyncTaskOkResponse:
        """Gets the status of an asynchronous task.

        :param api_id: The API's ID.
        :type api_id: str
        :param task_id: The task's ID.
        :type task_id: str
        :param accept: The `application/vnd.api.v10+json` request header required to use the endpoint.
        :type accept: Accept
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: GetStatusOfAnAsyncTaskOkResponse
        """

        Validator(str).validate(api_id)
        Validator(str).validate(task_id)
        Validator(Accept).validate(accept)

        serialized_request = (
            Serializer(
                f"{self.base_url}/apis/{{apiId}}/tasks/{{taskId}}",
                self.get_default_headers(),
            )
            .add_header("Accept", accept)
            .add_path("apiId", api_id)
            .add_path("taskId", task_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetStatusOfAnAsyncTaskOkResponse._unmap(response)

    @cast_models
    def get_api_versions(
        self, api_id: str, accept: Accept, cursor: str = None, limit: int = None
    ) -> GetApiVersionsOkResponse:
        """Gets all the published versions of an API.

        :param api_id: The API's ID.
        :type api_id: str
        :param accept: The `application/vnd.api.v10+json` request header required to use the endpoint.
        :type accept: Accept
        :param cursor: The pointer to the first record of the set of paginated results. To view the next response, use the `nextCursor` value for this parameter., defaults to None
        :type cursor: str, optional
        :param limit: The maximum number of rows to return in the response., defaults to None
        :type limit: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: GetApiVersionsOkResponse
        """

        Validator(str).validate(api_id)
        Validator(Accept).validate(accept)
        Validator(str).is_optional().validate(cursor)
        Validator(int).is_optional().validate(limit)

        serialized_request = (
            Serializer(
                f"{self.base_url}/apis/{{apiId}}/versions", self.get_default_headers()
            )
            .add_header("Accept", accept)
            .add_path("apiId", api_id)
            .add_query("cursor", cursor)
            .add_query("limit", limit)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetApiVersionsOkResponse._unmap(response)

    @cast_models
    def create_api_version(
        self, api_id: str, accept: Accept, request_body: CreateApiVersionRequest = None
    ) -> CreateApiVersionAcceptedResponse:
        """Creates a new API version asynchronously and immediately returns an HTTP `202 Accepted` response. The response contains a polling link to the task status API in the `Location` header.

        This endpoint is equivalent to publishing a version in Postman app, which is the snapshot of API collections and schema at a given point in time.

        :param request_body: The request body., defaults to None
        :type request_body: CreateApiVersionRequest, optional
        :param api_id: The API's ID.
        :type api_id: str
        :param accept: The `application/vnd.api.v10+json` request header required to use the endpoint.
        :type accept: Accept
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Accepted
        :rtype: CreateApiVersionAcceptedResponse
        """

        Validator(CreateApiVersionRequest).is_optional().validate(request_body)
        Validator(str).validate(api_id)
        Validator(Accept).validate(accept)

        serialized_request = (
            Serializer(
                f"{self.base_url}/apis/{{apiId}}/versions", self.get_default_headers()
            )
            .add_header("Accept", accept)
            .add_path("apiId", api_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return CreateApiVersionAcceptedResponse._unmap(response)

    @cast_models
    def get_api_version(
        self, api_id: str, version_id: str, accept: Accept
    ) -> GetApiVersionOkResponse:
        """Gets information about an API version.

        **Note:**

        - For API editors, this endpoint returns an HTTP `302 Found` status code when the version status is pending. It also returns the `/apis/{apiId}/tasks/{taskId}` task status response header.
        - For API viewers, this endpoint returns an HTTP `404 Not Found` when the version status is pending.

        :param api_id: The API's ID.
        :type api_id: str
        :param version_id: The API's version ID.
        :type version_id: str
        :param accept: The `application/vnd.api.v10+json` request header required to use the endpoint.
        :type accept: Accept
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: GetApiVersionOkResponse
        """

        Validator(str).validate(api_id)
        Validator(str).validate(version_id)
        Validator(Accept).validate(accept)

        serialized_request = (
            Serializer(
                f"{self.base_url}/apis/{{apiId}}/versions/{{versionId}}",
                self.get_default_headers(),
            )
            .add_header("Accept", accept)
            .add_path("apiId", api_id)
            .add_path("versionId", version_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetApiVersionOkResponse._unmap(response)

    @cast_models
    def update_api_version(
        self,
        api_id: str,
        version_id: str,
        accept: Accept,
        request_body: UpdateApiVersionRequest = None,
    ) -> UpdateApiVersionOkResponse:
        """Updates an API version.

        **Note:**

        This endpoint returns an HTTP `404 Not Found` response when an API version is pending publication.

        :param request_body: The request body., defaults to None
        :type request_body: UpdateApiVersionRequest, optional
        :param api_id: The API's ID.
        :type api_id: str
        :param version_id: The API's version ID.
        :type version_id: str
        :param accept: The `application/vnd.api.v10+json` request header required to use the endpoint.
        :type accept: Accept
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: UpdateApiVersionOkResponse
        """

        Validator(UpdateApiVersionRequest).is_optional().validate(request_body)
        Validator(str).validate(api_id)
        Validator(str).validate(version_id)
        Validator(Accept).validate(accept)

        serialized_request = (
            Serializer(
                f"{self.base_url}/apis/{{apiId}}/versions/{{versionId}}",
                self.get_default_headers(),
            )
            .add_header("Accept", accept)
            .add_path("apiId", api_id)
            .add_path("versionId", version_id)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return UpdateApiVersionOkResponse._unmap(response)

    @cast_models
    def delete_api_version(self, api_id: str, version_id: str, accept: Accept):
        """Deletes an API version.

        **Note:**

        This endpoint returns an HTTP `404 Not Found` response when an API version is pending publication.

        :param api_id: The API's ID.
        :type api_id: str
        :param version_id: The API's version ID.
        :type version_id: str
        :param accept: The `application/vnd.api.v10+json` request header required to use the endpoint.
        :type accept: Accept
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(api_id)
        Validator(str).validate(version_id)
        Validator(Accept).validate(accept)

        serialized_request = (
            Serializer(
                f"{self.base_url}/apis/{{apiId}}/versions/{{versionId}}",
                self.get_default_headers(),
            )
            .add_header("Accept", accept)
            .add_path("apiId", api_id)
            .add_path("versionId", version_id)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)

        return response
