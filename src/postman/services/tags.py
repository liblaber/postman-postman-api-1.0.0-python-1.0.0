from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.update_api_tags_request import UpdateApiTagsRequest
from ..models.get_tagged_entities_ok_response import GetTaggedEntitiesOkResponse
from ..models.get_tagged_entities_entity_type import GetTaggedEntitiesEntityType
from ..models.get_api_tags_ok_response import GetApiTagsOkResponse
from ..models.asc_desc_default_desc import AscDescDefaultDesc
from ..models.accept import Accept


class TagsService(BaseService):

    @cast_models
    def get_api_tags(self, api_id: str, accept: Accept) -> GetApiTagsOkResponse:
        """Gets all the tags associated with an API.

        :param api_id: The API's unique ID.
        :type api_id: str
        :param accept: The `application/vnd.api.v10+json` request header required to use the endpoint.
        :type accept: Accept
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Success Response
        :rtype: GetApiTagsOkResponse
        """

        Validator(str).validate(api_id)
        Validator(Accept).validate(accept)

        serialized_request = (
            Serializer(
                f"{self.base_url}/apis/{{apiId}}/tags", self.get_default_headers()
            )
            .add_header("Accept", accept)
            .add_path("apiId", api_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetApiTagsOkResponse._unmap(response)

    @cast_models
    def update_api_tags(
        self, api_id: str, accept: Accept, request_body: UpdateApiTagsRequest = None
    ) -> GetApiTagsOkResponse:
        """Updates an API's associated tags. This endpoint replaces all existing tags with those you pass in the request body.

        :param request_body: The request body., defaults to None
        :type request_body: UpdateApiTagsRequest, optional
        :param api_id: The API's unique ID.
        :type api_id: str
        :param accept: The `application/vnd.api.v10+json` request header required to use the endpoint.
        :type accept: Accept
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Success Response
        :rtype: GetApiTagsOkResponse
        """

        Validator(UpdateApiTagsRequest).is_optional().validate(request_body)
        Validator(str).validate(api_id)
        Validator(Accept).validate(accept)

        serialized_request = (
            Serializer(
                f"{self.base_url}/apis/{{apiId}}/tags", self.get_default_headers()
            )
            .add_header("Accept", accept)
            .add_path("apiId", api_id)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return GetApiTagsOkResponse._unmap(response)

    @cast_models
    def get_collection_tags(self, collection_id: str) -> GetApiTagsOkResponse:
        """Gets all the tags associated with a collection.

        :param collection_id: The collection's unique ID.
        :type collection_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Success Response
        :rtype: GetApiTagsOkResponse
        """

        Validator(str).validate(collection_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/{{collectionId}}/tags",
                self.get_default_headers(),
            )
            .add_path("collectionId", collection_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetApiTagsOkResponse._unmap(response)

    @cast_models
    def update_collection_tags(
        self, collection_id: str, request_body: UpdateApiTagsRequest = None
    ) -> GetApiTagsOkResponse:
        """Updates a collection's associated tags. This endpoint replaces all existing tags with those you pass in the request body.

        :param request_body: The request body., defaults to None
        :type request_body: UpdateApiTagsRequest, optional
        :param collection_id: The collection's unique ID.
        :type collection_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Success Response
        :rtype: GetApiTagsOkResponse
        """

        Validator(UpdateApiTagsRequest).is_optional().validate(request_body)
        Validator(str).validate(collection_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/{{collectionId}}/tags",
                self.get_default_headers(),
            )
            .add_path("collectionId", collection_id)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return GetApiTagsOkResponse._unmap(response)

    @cast_models
    def get_tagged_entities(
        self,
        slug: str,
        limit: int = None,
        direction: AscDescDefaultDesc = None,
        cursor: str = None,
        entity_type: GetTaggedEntitiesEntityType = None,
    ) -> GetTaggedEntitiesOkResponse:
        """Gets Postman elements (entities) by a given tag. Tags enable you to organize and search [workspaces](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/managing-workspaces/#tagging-a-workspace), [APIs](https://learning.postman.com/docs/designing-and-developing-your-api/managing-apis/#tagging-apis), and [collections](https://learning.postman.com/docs/collections/using-collections/#tagging-a-collection) that contain shared tags.

        **Note:**

        Tagging is available on Postman [**Enterprise** plans](https://www.postman.com/pricing/).

        :param slug: The tag's ID within a team or individual (non-team) user scope.
        :type slug: str
        :param limit: The maximum number of tagged elements to return in a single call., defaults to None
        :type limit: int, optional
        :param direction: The ascending (`asc`) or descending (`desc`) order to sort the results by, based on the time of the entity's tagging., defaults to None
        :type direction: AscDescDefaultDesc, optional
        :param cursor: The cursor to get the next set of results in the paginated response. If you pass an invalid value, the API only returns the first set of results., defaults to None
        :type cursor: str, optional
        :param entity_type: Filter results for the given entity type., defaults to None
        :type entity_type: GetTaggedEntitiesEntityType, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: GetTaggedEntitiesOkResponse
        """

        Validator(str).min_length(2).max_length(64).pattern(
            "^[a-z][a-z0-9-]*[a-z0-9]+$"
        ).validate(slug)
        Validator(int).is_optional().max(50).validate(limit)
        Validator(AscDescDefaultDesc).is_optional().validate(direction)
        Validator(str).is_optional().validate(cursor)
        Validator(GetTaggedEntitiesEntityType).is_optional().validate(entity_type)

        serialized_request = (
            Serializer(
                f"{self.base_url}/tags/{{slug}}/entities", self.get_default_headers()
            )
            .add_path("slug", slug)
            .add_query("limit", limit)
            .add_query("direction", direction)
            .add_query("cursor", cursor)
            .add_query("entityType", entity_type)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetTaggedEntitiesOkResponse._unmap(response)

    @cast_models
    def get_workspace_tags(self, workspace_id: str) -> GetApiTagsOkResponse:
        """Gets all the tags associated with a workspace.

        :param workspace_id: The workspace's ID.
        :type workspace_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Success Response
        :rtype: GetApiTagsOkResponse
        """

        Validator(str).validate(workspace_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/workspaces/{{workspaceId}}/tags",
                self.get_default_headers(),
            )
            .add_path("workspaceId", workspace_id)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetApiTagsOkResponse._unmap(response)

    @cast_models
    def update_workspace_tags(
        self, workspace_id: str, request_body: UpdateApiTagsRequest = None
    ) -> GetApiTagsOkResponse:
        """Updates a workspace's associated tags. This endpoint replaces all existing tags with those you pass in the request body.

        :param request_body: The request body., defaults to None
        :type request_body: UpdateApiTagsRequest, optional
        :param workspace_id: The workspace's ID.
        :type workspace_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Success Response
        :rtype: GetApiTagsOkResponse
        """

        Validator(UpdateApiTagsRequest).is_optional().validate(request_body)
        Validator(str).validate(workspace_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/workspaces/{{workspaceId}}/tags",
                self.get_default_headers(),
            )
            .add_path("workspaceId", workspace_id)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return GetApiTagsOkResponse._unmap(response)
