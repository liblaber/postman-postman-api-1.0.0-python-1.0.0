from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.update_collection_roles_request import UpdateCollectionRolesRequest
from ..models.transform_collection_to_open_api_ok_response import (
    TransformCollectionToOpenApiOkResponse,
)
from ..models.transfer_collection_items import TransferCollectionItems
from ..models.transfer_collection_folders_ok_response import (
    TransferCollectionFoldersOkResponse,
)
from ..models.put_collection_request import PutCollectionRequest
from ..models.put_collection_ok_response import PutCollectionOkResponse
from ..models.pull_collection_changes_ok_response import PullCollectionChangesOkResponse
from ..models.patch_collection_request import PatchCollectionRequest
from ..models.patch_collection_ok_response import PatchCollectionOkResponse
from ..models.merge_collection_fork_request import MergeCollectionForkRequest
from ..models.merge_collection_fork_ok_response import MergeCollectionForkOkResponse
from ..models.get_source_collection_status_ok_response import (
    GetSourceCollectionStatusOkResponse,
)
from ..models.get_collections_ok_response import GetCollectionsOkResponse
from ..models.get_collections_forked_by_user_ok_response import (
    GetCollectionsForkedByUserOkResponse,
)
from ..models.get_collection_roles_ok_response import GetCollectionRolesOkResponse
from ..models.get_collection_pull_requests_ok_response import (
    GetCollectionPullRequestsOkResponse,
)
from ..models.get_collection_ok_response import GetCollectionOkResponse
from ..models.get_collection_model import GetCollectionModel
from ..models.get_collection_forks_ok_response import GetCollectionForksOkResponse
from ..models.format import Format
from ..models.delete_collection_ok_response import DeleteCollectionOkResponse
from ..models.create_collection_request import CreateCollectionRequest
from ..models.create_collection_pull_request_request import (
    CreateCollectionPullRequestRequest,
)
from ..models.create_collection_pull_request_ok_response import (
    CreateCollectionPullRequestOkResponse,
)
from ..models.create_collection_ok_response import CreateCollectionOkResponse
from ..models.create_collection_fork_request import CreateCollectionForkRequest
from ..models.create_collection_fork_ok_response import CreateCollectionForkOkResponse
from ..models.comment_response import CommentResponse
from ..models.comment_created_updated import CommentCreatedUpdated
from ..models.comment_create_update import CommentCreateUpdate
from ..models.asc_desc import AscDesc


class CollectionsService(BaseService):

    @cast_models
    def get_collections(
        self, workspace: str = None, name: str = None
    ) -> GetCollectionsOkResponse:
        """Gets all of your [collections](https://www.getpostman.com/docs/collections). The response includes all of your subscribed collections.

        :param workspace: The workspace's ID., defaults to None
        :type workspace: str, optional
        :param name: Filter results by collections that match the given name., defaults to None
        :type name: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: GetCollectionsOkResponse
        """

        Validator(str).is_optional().validate(workspace)
        Validator(str).is_optional().validate(name)

        serialized_request = (
            Serializer(f"{self.base_url}/collections", self.get_default_headers())
            .add_query("workspace", workspace)
            .add_query("name", name)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetCollectionsOkResponse._unmap(response)

    @cast_models
    def create_collection(
        self, request_body: CreateCollectionRequest = None, workspace: str = None
    ) -> CreateCollectionOkResponse:
        """Creates a collection using the [Postman Collection v2 schema format](https://schema.postman.com/json/collection/v2.1.0/docs/index.html).

        For more information about the Collection Format, see the [Postman Collection Format documentation](https://learning.postman.com/collection-format/getting-started/overview/).

        **Note:**

        - For a complete list of available property values for this endpoint, use the following references available in the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json):
            - `info` object — Use the `definitions.info` entry.
            - `item` object — Use the `definitions.items` entry.
        - For all other possible values, refer to the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json).

        :param request_body: The request body., defaults to None
        :type request_body: CreateCollectionRequest, optional
        :param workspace: The workspace's ID., defaults to None
        :type workspace: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: CreateCollectionOkResponse
        """

        Validator(CreateCollectionRequest).is_optional().validate(request_body)
        Validator(str).is_optional().validate(workspace)

        serialized_request = (
            Serializer(f"{self.base_url}/collections", self.get_default_headers())
            .add_query("workspace", workspace)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return CreateCollectionOkResponse._unmap(response)

    @cast_models
    def create_collection_fork(
        self,
        collection_id: str,
        workspace: str,
        request_body: CreateCollectionForkRequest = None,
    ) -> CreateCollectionForkOkResponse:
        """Creates a [fork](https://learning.postman.com/docs/collaborating-in-postman/version-control/#creating-a-fork) from an existing collection into a workspace.

        :param request_body: The request body., defaults to None
        :type request_body: CreateCollectionForkRequest, optional
        :param collection_id: The collection's ID.
        :type collection_id: str
        :param workspace: The workspace ID in which to create the fork.
        :type workspace: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: CreateCollectionForkOkResponse
        """

        Validator(CreateCollectionForkRequest).is_optional().validate(request_body)
        Validator(str).validate(collection_id)
        Validator(str).validate(workspace)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/fork/{{collectionId}}",
                self.get_default_headers(),
            )
            .add_path("collectionId", collection_id)
            .add_query("workspace", workspace)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return CreateCollectionForkOkResponse._unmap(response)

    @cast_models
    def merge_collection_fork(
        self, request_body: MergeCollectionForkRequest = None
    ) -> MergeCollectionForkOkResponse:
        """Merges a forked collection back into its parent collection.

        :param request_body: The request body., defaults to None
        :type request_body: MergeCollectionForkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: MergeCollectionForkOkResponse
        """

        Validator(MergeCollectionForkRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(f"{self.base_url}/collections/merge", self.get_default_headers())
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return MergeCollectionForkOkResponse._unmap(response)

    @cast_models
    def get_collection(
        self,
        collection_id: str,
        access_key: str = None,
        model: GetCollectionModel = None,
    ) -> GetCollectionOkResponse:
        """Gets information about a collection. For a complete list of this endpoint's possible values, use the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json).

        :param collection_id: The collection's ID.
        :type collection_id: str
        :param access_key: A collection's read-only access key. Using this query parameter does not require an API key to call the endpoint., defaults to None
        :type access_key: str, optional
        :param model: Return a list of only the collection's root-level request (`rootLevelRequests`) and folder (`rootLevelFolders`) IDs instead of the full collection element data., defaults to None
        :type model: GetCollectionModel, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: GetCollectionOkResponse
        """

        Validator(str).validate(collection_id)
        Validator(str).is_optional().validate(access_key)
        Validator(GetCollectionModel).is_optional().validate(model)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/{{collectionId}}",
                self.get_default_headers(),
            )
            .add_path("collectionId", collection_id)
            .add_query("access_key", access_key)
            .add_query("model", model)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetCollectionOkResponse._unmap(response)

    @cast_models
    def put_collection(
        self, collection_id: str, request_body: PutCollectionRequest = None
    ) -> PutCollectionOkResponse:
        """Replaces the contents of a collection using the [Postman Collection v2 schema format](https://schema.postman.com/json/collection/v2.1.0/docs/index.html). Include the collection's ID values in the request body. If you do not, the endpoint removes the existing items and creates new items.

        > The maximum collection size this endpoint accepts cannot exceed 20 MB.

        For a complete list of available property values for this endpoint, use the following references available in the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json):
        - `info` object — Use `../definitions/info"`.
        - `item` object — Use `../definitions/item"`.

        For all other possible values, refer to the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json). For more information about the Collection Format, see the [Postman Collection Format documentation](https://learning.postman.com/collection-format/getting-started/overview/).

        **Note:**

        To copy another collection's contents to the given collection, remove all ID values before you pass it in this endpoint. If you do not, this endpoint returns an error. These values include the `id`, `uid`, and `postman_id` values.

        :param request_body: The request body., defaults to None
        :type request_body: PutCollectionRequest, optional
        :param collection_id: The collection's ID.
        :type collection_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: PutCollectionOkResponse
        """

        Validator(PutCollectionRequest).is_optional().validate(request_body)
        Validator(str).validate(collection_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/{{collectionId}}",
                self.get_default_headers(),
            )
            .add_path("collectionId", collection_id)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return PutCollectionOkResponse._unmap(response)

    @cast_models
    def patch_collection(
        self, collection_id: str, request_body: PatchCollectionRequest = None
    ) -> PatchCollectionOkResponse:
        """Updates specific collection information, such as its name, events, or its variables. For more information about the `auth`, `variables`, and `events` properties, refer to the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json):
        - For `variables`, refer to `../definitions/variable"`.
        - For `auth`, refer to `../definitions/auth-attribute"`.
        - For `events`, refer to `../definitions/event"`.

        For more information about the Collection Format, see the [Postman Collection Format documentation](https://learning.postman.com/collection-format/getting-started/overview/).

        :param request_body: The request body., defaults to None
        :type request_body: PatchCollectionRequest, optional
        :param collection_id: The collection's ID.
        :type collection_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: PatchCollectionOkResponse
        """

        Validator(PatchCollectionRequest).is_optional().validate(request_body)
        Validator(str).validate(collection_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/{{collectionId}}",
                self.get_default_headers(),
            )
            .add_path("collectionId", collection_id)
            .serialize()
            .set_method("PATCH")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return PatchCollectionOkResponse._unmap(response)

    @cast_models
    def delete_collection(self, collection_id: str) -> DeleteCollectionOkResponse:
        """Deletes a collection.

        :param collection_id: The collection's ID.
        :type collection_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: DeleteCollectionOkResponse
        """

        Validator(str).validate(collection_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/{{collectionId}}",
                self.get_default_headers(),
            )
            .add_path("collectionId", collection_id)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)

        return DeleteCollectionOkResponse._unmap(response)

    @cast_models
    def get_collections_forked_by_user(
        self,
        collection_id: str,
        cursor: str = None,
        limit: int = None,
        direction: AscDesc = None,
    ) -> GetCollectionsForkedByUserOkResponse:
        """Gets a list of all the authenticated user's forked collections.

        :param collection_id: The collection's ID.
        :type collection_id: str
        :param cursor: The pointer to the first record of the set of paginated results. To view the next response, use the `nextCursor` value for this parameter., defaults to None
        :type cursor: str, optional
        :param limit: The maximum number of rows to return in the response., defaults to None
        :type limit: int, optional
        :param direction: Sort the results by creation date in ascending (`asc`) or descending (`desc`) order., defaults to None
        :type direction: AscDesc, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: GetCollectionsForkedByUserOkResponse
        """

        Validator(str).validate(collection_id)
        Validator(str).is_optional().validate(cursor)
        Validator(int).is_optional().validate(limit)
        Validator(AscDesc).is_optional().validate(direction)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/{{collectionId}}/collection-forks",
                self.get_default_headers(),
            )
            .add_path("collectionId", collection_id)
            .add_query("cursor", cursor)
            .add_query("limit", limit)
            .add_query("direction", direction)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetCollectionsForkedByUserOkResponse._unmap(response)

    @cast_models
    def get_collection_comments(self, collection_id: str) -> CommentResponse:
        """Gets all comments left by users in a collection.

        :param collection_id: The collection's unique ID.
        :type collection_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: CommentResponse
        """

        Validator(str).validate(collection_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/{{collectionId}}/comments",
                self.get_default_headers(),
            )
            .add_path("collectionId", collection_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return CommentResponse._unmap(response)

    @cast_models
    def create_collection_comment(
        self, request_body: CommentCreateUpdate, collection_id: str
    ) -> CommentCreatedUpdated:
        """Creates a comment on a collection.

        **Note:**

        This endpoint accepts a max of 10,000 characters.

        :param request_body: The request body.
        :type request_body: CommentCreateUpdate
        :param collection_id: The collection's unique ID.
        :type collection_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Created
        :rtype: CommentCreatedUpdated
        """

        Validator(CommentCreateUpdate).validate(request_body)
        Validator(str).validate(collection_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/{{collectionId}}/comments",
                self.get_default_headers(),
            )
            .add_path("collectionId", collection_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return CommentCreatedUpdated._unmap(response)

    @cast_models
    def update_collection_comment(
        self, request_body: CommentCreateUpdate, collection_id: str, comment_id: int
    ) -> CommentCreatedUpdated:
        """Updates a comment on a collection.

        **Note:**

        This endpoint accepts a max of 10,000 characters.

        :param request_body: The request body.
        :type request_body: CommentCreateUpdate
        :param collection_id: The collection's unique ID.
        :type collection_id: str
        :param comment_id: The comment's ID.
        :type comment_id: int
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: CommentCreatedUpdated
        """

        Validator(CommentCreateUpdate).validate(request_body)
        Validator(str).validate(collection_id)
        Validator(int).validate(comment_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/{{collectionId}}/comments/{{commentId}}",
                self.get_default_headers(),
            )
            .add_path("collectionId", collection_id)
            .add_path("commentId", comment_id)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return CommentCreatedUpdated._unmap(response)

    @cast_models
    def delete_collection_comment(self, collection_id: str, comment_id: int):
        """Deletes a comment from a collection. On success, this returns an HTTP `204 No Content` response

        **Note:**

        Deleting the first comment of a thread deletes all the comments in the thread.

        :param collection_id: The collection's unique ID.
        :type collection_id: str
        :param comment_id: The comment's ID.
        :type comment_id: int
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(collection_id)
        Validator(int).validate(comment_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/{{collectionId}}/comments/{{commentId}}",
                self.get_default_headers(),
            )
            .add_path("collectionId", collection_id)
            .add_path("commentId", comment_id)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)

        return response

    @cast_models
    def get_collection_forks(
        self,
        collection_id: str,
        cursor: str = None,
        limit: int = None,
        direction: AscDesc = None,
    ) -> GetCollectionForksOkResponse:
        """Gets a collection's forked collections. The response returns data for each fork, such as the fork's ID, the user who forked it, and the fork's  creation date.

        :param collection_id: The collection's ID.
        :type collection_id: str
        :param cursor: The pointer to the first record of the set of paginated results. To view the next response, use the `nextCursor` value for this parameter., defaults to None
        :type cursor: str, optional
        :param limit: The maximum number of rows to return in the response., defaults to None
        :type limit: int, optional
        :param direction: Sort the results by creation date in ascending (`asc`) or descending (`desc`) order., defaults to None
        :type direction: AscDesc, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: GetCollectionForksOkResponse
        """

        Validator(str).validate(collection_id)
        Validator(str).is_optional().validate(cursor)
        Validator(int).is_optional().validate(limit)
        Validator(AscDesc).is_optional().validate(direction)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/{{collectionId}}/forks",
                self.get_default_headers(),
            )
            .add_path("collectionId", collection_id)
            .add_query("cursor", cursor)
            .add_query("limit", limit)
            .add_query("direction", direction)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetCollectionForksOkResponse._unmap(response)

    @cast_models
    def pull_collection_changes(
        self, collection_id: str
    ) -> PullCollectionChangesOkResponse:
        """Pulls the changes from a parent (source) collection into the forked collection. In the endpoint's response:

        - The `destinationId` is the ID of the forked collection.
        - The `sourceId` is the ID of the source collection.

        :param collection_id: The collection's ID.
        :type collection_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: PullCollectionChangesOkResponse
        """

        Validator(str).validate(collection_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/{{collectionId}}/pulls",
                self.get_default_headers(),
            )
            .add_path("collectionId", collection_id)
            .serialize()
            .set_method("PUT")
        )

        response = self.send_request(serialized_request)

        return PullCollectionChangesOkResponse._unmap(response)

    @cast_models
    def get_collection_pull_requests(
        self, collection_id: str
    ) -> GetCollectionPullRequestsOkResponse:
        """Gets information about a collection's pull requests, such as the source and destination IDs, status of the pull requests, and a URL link to the pull requests.

        :param collection_id: The collection's unique ID.
        :type collection_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: GetCollectionPullRequestsOkResponse
        """

        Validator(str).validate(collection_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/{{collectionId}}/pull-requests",
                self.get_default_headers(),
            )
            .add_path("collectionId", collection_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetCollectionPullRequestsOkResponse._unmap(response)

    @cast_models
    def create_collection_pull_request(
        self,
        collection_id: str,
        request_body: CreateCollectionPullRequestRequest = None,
    ) -> CreateCollectionPullRequestOkResponse:
        """Creates a pull request for a forked collection into its parent collection.

        :param request_body: The request body., defaults to None
        :type request_body: CreateCollectionPullRequestRequest, optional
        :param collection_id: The collection's unique ID.
        :type collection_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: CreateCollectionPullRequestOkResponse
        """

        Validator(CreateCollectionPullRequestRequest).is_optional().validate(
            request_body
        )
        Validator(str).validate(collection_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/{{collectionId}}/pull-requests",
                self.get_default_headers(),
            )
            .add_path("collectionId", collection_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return CreateCollectionPullRequestOkResponse._unmap(response)

    @cast_models
    def get_collection_roles(self, collection_id: str) -> GetCollectionRolesOkResponse:
        """Gets information about all roles in a collection. The response returns the IDs of all users, teams, and groups with access to view or edit the collection.

        :param collection_id: The collection's ID.
        :type collection_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: GetCollectionRolesOkResponse
        """

        Validator(str).validate(collection_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/{{collectionId}}/roles",
                self.get_default_headers(),
            )
            .add_path("collectionId", collection_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetCollectionRolesOkResponse._unmap(response)

    @cast_models
    def update_collection_roles(
        self, collection_id: str, request_body: UpdateCollectionRolesRequest = None
    ):
        """Updates the roles of users, groups, or teams in a collection. On success, this returns a `204 No Content` response.

        **Note:**

        - Only users assigned the EDITOR [role](https://learning.postman.com/docs/collaborating-in-postman/roles-and-permissions/#collection-roles) in the collection can use this endpoint.
        - This endpoint does not support the external [Partner or Guest roles](https://learning.postman.com/docs/collaborating-in-postman/roles-and-permissions/#team-roles).

        :param request_body: The request body., defaults to None
        :type request_body: UpdateCollectionRolesRequest, optional
        :param collection_id: The collection's ID.
        :type collection_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(UpdateCollectionRolesRequest).is_optional().validate(request_body)
        Validator(str).validate(collection_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/{{collectionId}}/roles",
                self.get_default_headers(),
            )
            .add_path("collectionId", collection_id)
            .serialize()
            .set_method("PATCH")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return response

    @cast_models
    def get_source_collection_status(
        self, collection_id: str
    ) -> GetSourceCollectionStatusOkResponse:
        """Checks whether there is a change between the forked collection and its parent (source) collection.

        If the value of the `isSourceAhead` property is `true` in the response, then there is a difference between the forked collection and its source collection.

        **Note:**

        This endpoint may take a few minutes to return an updated `isSourceAhead` status.

        :param collection_id: The collection's ID.
        :type collection_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: GetSourceCollectionStatusOkResponse
        """

        Validator(str).validate(collection_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/{{collectionId}}/source-status",
                self.get_default_headers(),
            )
            .add_path("collectionId", collection_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetSourceCollectionStatusOkResponse._unmap(response)

    @cast_models
    def transform_collection_to_open_api(
        self, collection_id: str, format: Format = None
    ) -> TransformCollectionToOpenApiOkResponse:
        """Transforms an existing Postman Collection into a stringified OpenAPI definition.

        **Note:**

        This does not create an API.

        :param collection_id: The collection's ID.
        :type collection_id: str
        :param format: Return the OpenAPI definition in the given format., defaults to None
        :type format: Format, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: TransformCollectionToOpenApiOkResponse
        """

        Validator(str).validate(collection_id)
        Validator(Format).is_optional().validate(format)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/{{collectionId}}/transformations",
                self.get_default_headers(),
            )
            .add_path("collectionId", collection_id)
            .add_query("format", format)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return TransformCollectionToOpenApiOkResponse._unmap(response)

    @cast_models
    def transfer_collection_folders(
        self, request_body: TransferCollectionItems = None
    ) -> TransferCollectionFoldersOkResponse:
        """Copies or moves folders into a collection or folder.

        :param request_body: The request body., defaults to None
        :type request_body: TransferCollectionItems, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: TransferCollectionFoldersOkResponse
        """

        Validator(TransferCollectionItems).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collection-folders-transfers",
                self.get_default_headers(),
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return TransferCollectionFoldersOkResponse._unmap(response)

    @cast_models
    def transfer_collection_requests(
        self, request_body: TransferCollectionItems = None
    ) -> TransferCollectionFoldersOkResponse:
        """Copies or moves requests into a collection or folder.

        :param request_body: The request body., defaults to None
        :type request_body: TransferCollectionItems, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: TransferCollectionFoldersOkResponse
        """

        Validator(TransferCollectionItems).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collection-requests-transfers",
                self.get_default_headers(),
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return TransferCollectionFoldersOkResponse._unmap(response)

    @cast_models
    def transfer_collection_responses(
        self, request_body: TransferCollectionItems = None
    ) -> TransferCollectionFoldersOkResponse:
        """Copies or moves responses into a request.

        :param request_body: The request body., defaults to None
        :type request_body: TransferCollectionItems, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: TransferCollectionFoldersOkResponse
        """

        Validator(TransferCollectionItems).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collection-responses-transfers",
                self.get_default_headers(),
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return TransferCollectionFoldersOkResponse._unmap(response)
