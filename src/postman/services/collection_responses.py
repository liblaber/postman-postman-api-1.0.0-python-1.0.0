from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.comment_response import CommentResponse
from ..models.comment_created_updated import CommentCreatedUpdated
from ..models.comment_create_update import CommentCreateUpdate


class CollectionResponsesService(BaseService):

    @cast_models
    def get_response_comments(
        self, collection_id: str, response_id: str
    ) -> CommentResponse:
        """Gets all comments left by users in a response.

        :param collection_id: The collection's unique ID.
        :type collection_id: str
        :param response_id: The response's unique ID.
        :type response_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: CommentResponse
        """

        Validator(str).validate(collection_id)
        Validator(str).validate(response_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/{{collectionId}}/responses/{{responseId}}/comments",
                self.get_default_headers(),
            )
            .add_path("collectionId", collection_id)
            .add_path("responseId", response_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return CommentResponse._unmap(response)

    @cast_models
    def create_response_comment(
        self, request_body: CommentCreateUpdate, collection_id: str, response_id: str
    ) -> CommentCreatedUpdated:
        """Creates a comment on a response.

        **Note:**

        This endpoint accepts a max of 10,000 characters.

        :param request_body: The request body.
        :type request_body: CommentCreateUpdate
        :param collection_id: The collection's unique ID.
        :type collection_id: str
        :param response_id: The response's unique ID.
        :type response_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Created
        :rtype: CommentCreatedUpdated
        """

        Validator(CommentCreateUpdate).validate(request_body)
        Validator(str).validate(collection_id)
        Validator(str).validate(response_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/{{collectionId}}/responses/{{responseId}}/comments",
                self.get_default_headers(),
            )
            .add_path("collectionId", collection_id)
            .add_path("responseId", response_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return CommentCreatedUpdated._unmap(response)

    @cast_models
    def update_response_comment(
        self,
        request_body: CommentCreateUpdate,
        collection_id: str,
        response_id: str,
        comment_id: int,
    ) -> CommentCreatedUpdated:
        """Updates a comment on a response.

        **Note:**

        This endpoint accepts a max of 10,000 characters.

        :param request_body: The request body.
        :type request_body: CommentCreateUpdate
        :param collection_id: The collection's unique ID.
        :type collection_id: str
        :param response_id: The response's unique ID.
        :type response_id: str
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
        Validator(str).validate(response_id)
        Validator(int).validate(comment_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/{{collectionId}}/responses/{{responseId}}/comments/{{commentId}}",
                self.get_default_headers(),
            )
            .add_path("collectionId", collection_id)
            .add_path("responseId", response_id)
            .add_path("commentId", comment_id)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return CommentCreatedUpdated._unmap(response)

    @cast_models
    def delete_response_comment(
        self, collection_id: str, response_id: str, comment_id: int
    ):
        """Deletes a comment from a response. On success, this returns an HTTP `204 No Content` response

        **Note:**

        Deleting the first comment of a thread deletes all the comments in the thread.

        :param collection_id: The collection's unique ID.
        :type collection_id: str
        :param response_id: The response's unique ID.
        :type response_id: str
        :param comment_id: The comment's ID.
        :type comment_id: int
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(collection_id)
        Validator(str).validate(response_id)
        Validator(int).validate(comment_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/{{collectionId}}/responses/{{responseId}}/comments/{{commentId}}",
                self.get_default_headers(),
            )
            .add_path("collectionId", collection_id)
            .add_path("responseId", response_id)
            .add_path("commentId", comment_id)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)

        return response
