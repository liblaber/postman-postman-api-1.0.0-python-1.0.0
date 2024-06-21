from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.update_pan_element_or_folder_request import (
    UpdatePanElementOrFolderRequest,
)
from ..models.update_pan_element_or_folder_ok_response import (
    UpdatePanElementOrFolderOkResponse,
    UpdatePanElementOrFolderOkResponseGuard,
)
from ..models.update_pan_element_or_folder_element_type import (
    UpdatePanElementOrFolderElementType,
)
from ..models.respond_pan_element_add_request_request import (
    RespondPanElementAddRequestRequest,
)
from ..models.respond_pan_element_add_request_ok_response import (
    RespondPanElementAddRequestOkResponse,
)
from ..models.post_pan_element_or_folder_request import PostPanElementOrFolderRequest
from ..models.post_pan_element_or_folder_created_response import (
    PostPanElementOrFolderCreatedResponse,
    PostPanElementOrFolderCreatedResponseGuard,
)
from ..models.get_all_pan_add_element_requests_status import (
    GetAllPanAddElementRequestsStatus,
)
from ..models.get_all_pan_add_element_requests_ok_response import (
    GetAllPanAddElementRequestsOkResponse,
)
from ..models.get_all_elements_and_folders_type import GetAllElementsAndFoldersType
from ..models.get_all_elements_and_folders_sort import GetAllElementsAndFoldersSort
from ..models.get_all_elements_and_folders_ok_response import (
    GetAllElementsAndFoldersOkResponse,
)
from ..models.delete_pan_element_or_folder_ok_response import (
    DeletePanElementOrFolderOkResponse,
)
from ..models.asc_desc import AscDesc


class PrivateApiNetworkService(BaseService):

    @cast_models
    def get_all_elements_and_folders(
        self,
        since: str = None,
        until: str = None,
        added_by: int = None,
        name: str = None,
        summary: str = None,
        description: str = None,
        sort: GetAllElementsAndFoldersSort = None,
        direction: AscDesc = None,
        created_by: int = None,
        offset: int = None,
        limit: int = None,
        parent_folder_id: int = None,
        type_: GetAllElementsAndFoldersType = None,
    ) -> GetAllElementsAndFoldersOkResponse:
        """Gets information about the folders and their elements added to your [Private API Network](https://learning.postman.com/docs/collaborating-in-postman/adding-private-network/).

        **Note:**

        The `limit` and `offset` parameters are separately applied to elements and folders. For example, if you query a `limit` value of `10` and an `offset` value `0`, the endpoint returns 10 elements and 10 folders for a total of 20 items. The `totalCount` property in the `meta` response is the total count of both elements and folders.

        :param since: Return only results created since the given time, in [ISO 8601](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) format. This value cannot be later than the `until` value., defaults to None
        :type since: str, optional
        :param until: Return only results created until this given time, in [ISO 8601](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) format. This value cannot be earlier than the `since` value., defaults to None
        :type until: str, optional
        :param added_by: Return only elements published by the given user ID., defaults to None
        :type added_by: int, optional
        :param name: Return only elements whose name includes the given value. Matching is not case-sensitive., defaults to None
        :type name: str, optional
        :param summary: Return only elements whose summary includes the given value. Matching is not case-sensitive., defaults to None
        :type summary: str, optional
        :param description: Return only elements whose description includes the given value. Matching is not case-sensitive., defaults to None
        :type description: str, optional
        :param sort: Sort the results by the given value. If you use this query parameter, you must also use the `direction` parameter., defaults to None
        :type sort: GetAllElementsAndFoldersSort, optional
        :param direction: Sort in ascending (`asc`) or descending (`desc`) order. Matching is not case-sensitive. If you use this query parameter, you must also use the `sort` parameter., defaults to None
        :type direction: AscDesc, optional
        :param created_by: Return only results created by the given user ID., defaults to None
        :type created_by: int, optional
        :param offset: The zero-based offset of the first item to return., defaults to None
        :type offset: int, optional
        :param limit: The maximum number of elements to return. If the value exceeds the maximum value of `1000`, then the system uses the `1000` value., defaults to None
        :type limit: int, optional
        :param parent_folder_id: Return the folders and elements in a specific folder. If this value is `0`, then the endpoint only returns the root folder's elements., defaults to None
        :type parent_folder_id: int, optional
        :param type_: Filter by the element type., defaults to None
        :type type_: GetAllElementsAndFoldersType, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: GetAllElementsAndFoldersOkResponse
        """

        Validator(str).is_optional().validate(since)
        Validator(str).is_optional().validate(until)
        Validator(int).is_optional().validate(added_by)
        Validator(str).is_optional().validate(name)
        Validator(str).is_optional().validate(summary)
        Validator(str).is_optional().validate(description)
        Validator(GetAllElementsAndFoldersSort).is_optional().validate(sort)
        Validator(AscDesc).is_optional().validate(direction)
        Validator(int).is_optional().validate(created_by)
        Validator(int).is_optional().validate(offset)
        Validator(int).is_optional().validate(limit)
        Validator(int).is_optional().validate(parent_folder_id)
        Validator(GetAllElementsAndFoldersType).is_optional().validate(type_)

        serialized_request = (
            Serializer(f"{self.base_url}/network/private", self.get_default_headers())
            .add_query("since", since)
            .add_query("until", until)
            .add_query("addedBy", added_by)
            .add_query("name", name)
            .add_query("summary", summary)
            .add_query("description", description)
            .add_query("sort", sort)
            .add_query("direction", direction)
            .add_query("createdBy", created_by)
            .add_query("offset", offset)
            .add_query("limit", limit)
            .add_query("parentFolderId", parent_folder_id)
            .add_query("type", type_)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetAllElementsAndFoldersOkResponse._unmap(response)

    @cast_models
    def post_pan_element_or_folder(
        self, request_body: PostPanElementOrFolderRequest
    ) -> PostPanElementOrFolderCreatedResponse:
        """Publishes a element or creates a folder in your [Private API Network](https://learning.postman.com/docs/collaborating-in-postman/adding-private-network/). An element is a Postman API, collection, or workspace.

        **Note:**

        You can only pass one element object type per call. For example, you cannot pass both `api` and `collection` in a single request.

        :param request_body: The request body.
        :type request_body: PostPanElementOrFolderRequest
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Created
        :rtype: PostPanElementOrFolderCreatedResponse
        """

        Validator(PostPanElementOrFolderRequest).validate(request_body)

        serialized_request = (
            Serializer(f"{self.base_url}/network/private", self.get_default_headers())
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return PostPanElementOrFolderCreatedResponseGuard.return_one_of(response)

    @cast_models
    def update_pan_element_or_folder(
        self,
        request_body: UpdatePanElementOrFolderRequest,
        element_id: str,
        element_type: UpdatePanElementOrFolderElementType,
    ) -> UpdatePanElementOrFolderOkResponse:
        """Updates an element or folder in your [Private API Network](https://learning.postman.com/docs/collaborating-in-postman/adding-private-network/).

        **Note:**

        You can only pass one element object type per call. For example, you cannot pass both `api` and `collection` in a single request.

        :param request_body: The request body.
        :type request_body: UpdatePanElementOrFolderRequest
        :param element_id: The element's ID or UUID. For Postman Collections you must pass the collection's UID (`userId`-`collectionId`) value.
        :type element_id: str
        :param element_type: The element type.
        :type element_type: UpdatePanElementOrFolderElementType
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: UpdatePanElementOrFolderOkResponse
        """

        Validator(UpdatePanElementOrFolderRequest).validate(request_body)
        Validator(str).validate(element_id)
        Validator(UpdatePanElementOrFolderElementType).validate(element_type)

        serialized_request = (
            Serializer(
                f"{self.base_url}/network/private/{{elementType}}/{{elementId}}",
                self.get_default_headers(),
            )
            .add_path("elementId", element_id)
            .add_path("elementType", element_type)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return UpdatePanElementOrFolderOkResponseGuard.return_one_of(response)

    @cast_models
    def delete_pan_element_or_folder(
        self, element_id: str, element_type: UpdatePanElementOrFolderElementType
    ) -> DeletePanElementOrFolderOkResponse:
        """Removes an element or delete a folder from your [Private API Network](https://learning.postman.com/docs/collaborating-in-postman/adding-private-network/).
        **Note:**
        Removing an API, collection, or workspace element does not delete it. It only removes it from the Private API Network folder.

        :param element_id: The element's ID or UUID. For Postman Collections you must pass the collection's UID (`userId`-`collectionId`) value.
        :type element_id: str
        :param element_type: The element type.
        :type element_type: UpdatePanElementOrFolderElementType
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: DeletePanElementOrFolderOkResponse
        """

        Validator(str).validate(element_id)
        Validator(UpdatePanElementOrFolderElementType).validate(element_type)

        serialized_request = (
            Serializer(
                f"{self.base_url}/network/private/{{elementType}}/{{elementId}}",
                self.get_default_headers(),
            )
            .add_path("elementId", element_id)
            .add_path("elementType", element_type)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)

        return DeletePanElementOrFolderOkResponse._unmap(response)

    @cast_models
    def get_all_pan_add_element_requests(
        self,
        since: str = None,
        until: str = None,
        requested_by: int = None,
        type_: GetAllElementsAndFoldersType = None,
        status: GetAllPanAddElementRequestsStatus = None,
        name: str = None,
        sort: GetAllElementsAndFoldersSort = None,
        direction: AscDesc = None,
        offset: int = None,
        limit: int = None,
    ) -> GetAllPanAddElementRequestsOkResponse:
        """Gets a list requests to add elements to the [Private API Network](https://learning.postman.com/docs/collaborating-in-postman/adding-private-network/).

        :param since: Return only results created since the given time, in [ISO 8601](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) format. This value cannot be later than the `until` value., defaults to None
        :type since: str, optional
        :param until: Return only results created until this given time, in [ISO 8601](https://datatracker.ietf.org/doc/html/rfc3339#section-5.6) format. This value cannot be earlier than the `since` value., defaults to None
        :type until: str, optional
        :param requested_by: Return a user's element requests by their user ID., defaults to None
        :type requested_by: int, optional
        :param type_: Filter by the element type., defaults to None
        :type type_: GetAllElementsAndFoldersType, optional
        :param status: Filter by the request status., defaults to None
        :type status: GetAllPanAddElementRequestsStatus, optional
        :param name: Return only elements whose name includes the given value. Matching is not case-sensitive., defaults to None
        :type name: str, optional
        :param sort: Sort the results by the given value. If you use this query parameter, you must also use the `direction` parameter., defaults to None
        :type sort: GetAllElementsAndFoldersSort, optional
        :param direction: Sort in ascending (`asc`) or descending (`desc`) order. Matching is not case-sensitive. If you use this query parameter, you must also use the `sort` parameter., defaults to None
        :type direction: AscDesc, optional
        :param offset: The zero-based offset of the first item to return., defaults to None
        :type offset: int, optional
        :param limit: The maximum number of elements to return. If the value exceeds the maximum value of `1000`, then the system uses the `1000` value., defaults to None
        :type limit: int, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: GetAllPanAddElementRequestsOkResponse
        """

        Validator(str).is_optional().validate(since)
        Validator(str).is_optional().validate(until)
        Validator(int).is_optional().validate(requested_by)
        Validator(GetAllElementsAndFoldersType).is_optional().validate(type_)
        Validator(GetAllPanAddElementRequestsStatus).is_optional().validate(status)
        Validator(str).is_optional().validate(name)
        Validator(GetAllElementsAndFoldersSort).is_optional().validate(sort)
        Validator(AscDesc).is_optional().validate(direction)
        Validator(int).is_optional().validate(offset)
        Validator(int).is_optional().validate(limit)

        serialized_request = (
            Serializer(
                f"{self.base_url}/network/private/network-entity/request/all",
                self.get_default_headers(),
            )
            .add_query("since", since)
            .add_query("until", until)
            .add_query("requestedBy", requested_by)
            .add_query("type", type_)
            .add_query("status", status)
            .add_query("name", name)
            .add_query("sort", sort)
            .add_query("direction", direction)
            .add_query("offset", offset)
            .add_query("limit", limit)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetAllPanAddElementRequestsOkResponse._unmap(response)

    @cast_models
    def respond_pan_element_add_request(
        self, request_id: int, request_body: RespondPanElementAddRequestRequest = None
    ) -> RespondPanElementAddRequestOkResponse:
        """Responds to a request to add an element to the [Private API Network](https://learning.postman.com/docs/collaborating-in-postman/adding-private-network/). Only managers can approve or deny a request. Once approved, the element will appear in the team's Private API Network.

        :param request_body: The request body., defaults to None
        :type request_body: RespondPanElementAddRequestRequest, optional
        :param request_id: The element request's ID.
        :type request_id: int
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: RespondPanElementAddRequestOkResponse
        """

        Validator(RespondPanElementAddRequestRequest).is_optional().validate(
            request_body
        )
        Validator(int).validate(request_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/network/private/network-entity/request/{{requestId}}",
                self.get_default_headers(),
            )
            .add_path("requestId", request_id)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return RespondPanElementAddRequestOkResponse._unmap(response)
