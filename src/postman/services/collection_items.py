from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.update_collection_response_ok_response import (
    UpdateCollectionResponseOkResponse,
)
from ..models.update_collection_request_ok_response import (
    UpdateCollectionRequestOkResponse,
)
from ..models.update_collection_folder_ok_response import (
    UpdateCollectionFolderOkResponse,
)
from ..models.get_collection_response_ok_response import GetCollectionResponseOkResponse
from ..models.get_collection_request_ok_response import GetCollectionRequestOkResponse
from ..models.get_collection_folder_ok_response import GetCollectionFolderOkResponse
from ..models.delete_collection_response_ok_response import (
    DeleteCollectionResponseOkResponse,
)
from ..models.delete_collection_request_ok_response import (
    DeleteCollectionRequestOkResponse,
)
from ..models.delete_collection_folder_ok_response import (
    DeleteCollectionFolderOkResponse,
)
from ..models.create_collection_response_ok_response import (
    CreateCollectionResponseOkResponse,
)
from ..models.create_collection_request_ok_response import (
    CreateCollectionRequestOkResponse,
)
from ..models.create_collection_folder_ok_response import (
    CreateCollectionFolderOkResponse,
)


class CollectionItemsService(BaseService):

    @cast_models
    def create_collection_folder(
        self, collection_id: str, request_body: dict = None
    ) -> CreateCollectionFolderOkResponse:
        """Creates a folder in a collection. For a complete list of properties, refer to "Folder" in the [collection.json schema file](https://schema.postman.com/collection/json/v2.1.0/draft-07/collection.json).

        You can use this endpoint to to import requests and responses into a newly-created folder. To do this, include the `requests` field and the list of request objects in the request body. For more information, see the provided example.

        **Note:**

        It is recommended that you pass the `name` property in the request body. If you do not, the system uses a null value. As a result, this creates a folder with a blank name.

        :param request_body: The request body., defaults to None
        :type request_body: dict, optional
        :param collection_id: The collection's ID.
        :type collection_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: CreateCollectionFolderOkResponse
        """

        Validator(dict).is_optional().validate(request_body)
        Validator(str).validate(collection_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/{{collectionId}}/folders",
                self.get_default_headers(),
            )
            .add_path("collectionId", collection_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return CreateCollectionFolderOkResponse._unmap(response)

    @cast_models
    def create_collection_request(
        self, collection_id: str, request_body: dict = None, folder_id: str = None
    ) -> CreateCollectionRequestOkResponse:
        """Creates a request in a collection. For a complete list of properties, see the [Collection Format Request documentation](https://learning.postman.com/collection-format/reference/request/).

        **Note:**

        It is recommended that you pass the `name` property in the request body. If you do not, the system uses a null value. As a result, this creates a request with a blank name.

        :param request_body: The request body., defaults to None
        :type request_body: dict, optional
        :param collection_id: The collection's ID.
        :type collection_id: str
        :param folder_id: The folder ID in which to create the request. By default, the system will create the request at the collection level., defaults to None
        :type folder_id: str, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: CreateCollectionRequestOkResponse
        """

        Validator(dict).is_optional().validate(request_body)
        Validator(str).validate(collection_id)
        Validator(str).is_optional().validate(folder_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/{{collectionId}}/requests",
                self.get_default_headers(),
            )
            .add_path("collectionId", collection_id)
            .add_query("folderId", folder_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return CreateCollectionRequestOkResponse._unmap(response)

    @cast_models
    def create_collection_response(
        self, collection_id: str, request_id: str, request_body: dict = None
    ) -> CreateCollectionResponseOkResponse:
        """Creates a request response in a collection. For a complete list of request body properties, see the [Collection Format Response documentation](https://learning.postman.com/collection-format/reference/response/#reference-diagram).

        **Note:**

        It is recommended that you pass the `name` property in the request body. If you do not, the system uses a null value. As a result, this creates a response with a blank name.

        :param request_body: The request body., defaults to None
        :type request_body: dict, optional
        :param collection_id: The collection's ID.
        :type collection_id: str
        :param request_id: The parent request's ID.
        :type request_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: CreateCollectionResponseOkResponse
        """

        Validator(dict).is_optional().validate(request_body)
        Validator(str).validate(collection_id)
        Validator(str).validate(request_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/{{collectionId}}/responses",
                self.get_default_headers(),
            )
            .add_path("collectionId", collection_id)
            .add_query("requestId", request_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return CreateCollectionResponseOkResponse._unmap(response)

    @cast_models
    def get_collection_folder(
        self,
        folder_id: str,
        collection_id: str,
        ids: bool = None,
        uid: bool = None,
        populate: bool = None,
    ) -> GetCollectionFolderOkResponse:
        """Gets information about a folder in a collection.

        :param folder_id: The folder's ID.
        :type folder_id: str
        :param collection_id: The collection's ID.
        :type collection_id: str
        :param ids: If true, returns only properties that contain ID values in the response., defaults to None
        :type ids: bool, optional
        :param uid: If true, returns all IDs in UID format (`userId`-`id`)., defaults to None
        :type uid: bool, optional
        :param populate: If true, returns all of the collection item's contents., defaults to None
        :type populate: bool, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: GetCollectionFolderOkResponse
        """

        Validator(str).validate(folder_id)
        Validator(str).validate(collection_id)
        Validator(bool).is_optional().validate(ids)
        Validator(bool).is_optional().validate(uid)
        Validator(bool).is_optional().validate(populate)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/{{collectionId}}/folders/{{folderId}}",
                self.get_default_headers(),
            )
            .add_path("folderId", folder_id)
            .add_path("collectionId", collection_id)
            .add_query("ids", ids)
            .add_query("uid", uid)
            .add_query("populate", populate)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetCollectionFolderOkResponse._unmap(response)

    @cast_models
    def update_collection_folder(
        self, folder_id: str, collection_id: str, request_body: dict = None
    ) -> UpdateCollectionFolderOkResponse:
        """Updates a folder in a collection. For a complete list of properties, refer to "Folder" in the [collection.json schema file](https://schema.postman.com/collection/json/v2.1.0/draft-07/collection.json).

        **Note:**

        This endpoint acts like a PATCH method. It only updates the values that you pass in the request body (for example, the `name` property). The endpoint does not update the entire resource.

        :param request_body: The request body., defaults to None
        :type request_body: dict, optional
        :param folder_id: The folder's ID.
        :type folder_id: str
        :param collection_id: The collection's ID.
        :type collection_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: UpdateCollectionFolderOkResponse
        """

        Validator(dict).is_optional().validate(request_body)
        Validator(str).validate(folder_id)
        Validator(str).validate(collection_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/{{collectionId}}/folders/{{folderId}}",
                self.get_default_headers(),
            )
            .add_path("folderId", folder_id)
            .add_path("collectionId", collection_id)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return UpdateCollectionFolderOkResponse._unmap(response)

    @cast_models
    def delete_collection_folder(
        self, folder_id: str, collection_id: str
    ) -> DeleteCollectionFolderOkResponse:
        """Deletes a folder in a collection.

        :param folder_id: The folder's ID.
        :type folder_id: str
        :param collection_id: The collection's ID.
        :type collection_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: DeleteCollectionFolderOkResponse
        """

        Validator(str).validate(folder_id)
        Validator(str).validate(collection_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/{{collectionId}}/folders/{{folderId}}",
                self.get_default_headers(),
            )
            .add_path("folderId", folder_id)
            .add_path("collectionId", collection_id)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)

        return DeleteCollectionFolderOkResponse._unmap(response)

    @cast_models
    def get_collection_request(
        self,
        request_id: str,
        collection_id: str,
        ids: bool = None,
        uid: bool = None,
        populate: bool = None,
    ) -> GetCollectionRequestOkResponse:
        """Gets information about a request in a collection.

        :param request_id: The request's ID.
        :type request_id: str
        :param collection_id: The collection's ID.
        :type collection_id: str
        :param ids: If true, returns only properties that contain ID values in the response., defaults to None
        :type ids: bool, optional
        :param uid: If true, returns all IDs in UID format (`userId`-`id`)., defaults to None
        :type uid: bool, optional
        :param populate: If true, returns all of the collection item's contents., defaults to None
        :type populate: bool, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: GetCollectionRequestOkResponse
        """

        Validator(str).validate(request_id)
        Validator(str).validate(collection_id)
        Validator(bool).is_optional().validate(ids)
        Validator(bool).is_optional().validate(uid)
        Validator(bool).is_optional().validate(populate)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/{{collectionId}}/requests/{{requestId}}",
                self.get_default_headers(),
            )
            .add_path("requestId", request_id)
            .add_path("collectionId", collection_id)
            .add_query("ids", ids)
            .add_query("uid", uid)
            .add_query("populate", populate)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetCollectionRequestOkResponse._unmap(response)

    @cast_models
    def update_collection_request(
        self, request_id: str, collection_id: str, request_body: dict = None
    ) -> UpdateCollectionRequestOkResponse:
        """Updates a request in a collection. For a complete list of properties, see the [Collection Format Request documentation](https://learning.postman.com/collection-format/reference/request/).

        **Note:**

        - You must pass a collection ID (`12ece9e1-2abf-4edc-8e34-de66e74114d2`), not a collection(`12345678-12ece9e1-2abf-4edc-8e34-de66e74114d2`), in this endpoint.
        - This endpoint does not support changing the folder of a request.

        :param request_body: The request body., defaults to None
        :type request_body: dict, optional
        :param request_id: The request's ID.
        :type request_id: str
        :param collection_id: The collection's ID.
        :type collection_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: UpdateCollectionRequestOkResponse
        """

        Validator(dict).is_optional().validate(request_body)
        Validator(str).validate(request_id)
        Validator(str).validate(collection_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/{{collectionId}}/requests/{{requestId}}",
                self.get_default_headers(),
            )
            .add_path("requestId", request_id)
            .add_path("collectionId", collection_id)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return UpdateCollectionRequestOkResponse._unmap(response)

    @cast_models
    def delete_collection_request(
        self, request_id: str, collection_id: str
    ) -> DeleteCollectionRequestOkResponse:
        """Deletes a request in a collection.

        :param request_id: The request's ID.
        :type request_id: str
        :param collection_id: The collection's ID.
        :type collection_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: DeleteCollectionRequestOkResponse
        """

        Validator(str).validate(request_id)
        Validator(str).validate(collection_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/{{collectionId}}/requests/{{requestId}}",
                self.get_default_headers(),
            )
            .add_path("requestId", request_id)
            .add_path("collectionId", collection_id)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)

        return DeleteCollectionRequestOkResponse._unmap(response)

    @cast_models
    def get_collection_response(
        self,
        response_id: str,
        collection_id: str,
        ids: bool = None,
        uid: bool = None,
        populate: bool = None,
    ) -> GetCollectionResponseOkResponse:
        """Gets information about a response in a collection.

        :param response_id: The response's ID.
        :type response_id: str
        :param collection_id: The collection's ID.
        :type collection_id: str
        :param ids: If true, returns only properties that contain ID values in the response., defaults to None
        :type ids: bool, optional
        :param uid: If true, returns all IDs in UID format (`userId`-`id`)., defaults to None
        :type uid: bool, optional
        :param populate: If true, returns all of the collection item's contents., defaults to None
        :type populate: bool, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: GetCollectionResponseOkResponse
        """

        Validator(str).validate(response_id)
        Validator(str).validate(collection_id)
        Validator(bool).is_optional().validate(ids)
        Validator(bool).is_optional().validate(uid)
        Validator(bool).is_optional().validate(populate)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/{{collectionId}}/responses/{{responseId}}",
                self.get_default_headers(),
            )
            .add_path("responseId", response_id)
            .add_path("collectionId", collection_id)
            .add_query("ids", ids)
            .add_query("uid", uid)
            .add_query("populate", populate)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetCollectionResponseOkResponse._unmap(response)

    @cast_models
    def update_collection_response(
        self, response_id: str, collection_id: str, request_body: dict = None
    ) -> UpdateCollectionResponseOkResponse:
        """Updates a response in a collection. For a complete list of properties, see the [Collection Format Response documentation](https://learning.postman.com/collection-format/reference/response/#reference-diagram).

        **Note:**

        - You must pass a collection ID (`12ece9e1-2abf-4edc-8e34-de66e74114d2`), not a collection UID (`12345678-12ece9e1-2abf-4edc-8e34-de66e74114d2`), in this endpoint.
        - This endpoint acts like a PATCH method. It only updates the values that you pass in the request body (for example, the `name` property). The endpoint does not update the entire resource.

        :param request_body: The request body., defaults to None
        :type request_body: dict, optional
        :param response_id: The response's ID.
        :type response_id: str
        :param collection_id: The collection's ID.
        :type collection_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: UpdateCollectionResponseOkResponse
        """

        Validator(dict).is_optional().validate(request_body)
        Validator(str).validate(response_id)
        Validator(str).validate(collection_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/{{collectionId}}/responses/{{responseId}}",
                self.get_default_headers(),
            )
            .add_path("responseId", response_id)
            .add_path("collectionId", collection_id)
            .serialize()
            .set_method("PUT")
            .set_body(request_body)
        )

        response = self.send_request(serialized_request)

        return UpdateCollectionResponseOkResponse._unmap(response)

    @cast_models
    def delete_collection_response(
        self, response_id: str, collection_id: str
    ) -> DeleteCollectionResponseOkResponse:
        """Deletes a response in a collection.

        :param response_id: The response's ID.
        :type response_id: str
        :param collection_id: The collection's ID.
        :type collection_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: DeleteCollectionResponseOkResponse
        """

        Validator(str).validate(response_id)
        Validator(str).validate(collection_id)

        serialized_request = (
            Serializer(
                f"{self.base_url}/collections/{{collectionId}}/responses/{{responseId}}",
                self.get_default_headers(),
            )
            .add_path("responseId", response_id)
            .add_path("collectionId", collection_id)
            .serialize()
            .set_method("DELETE")
        )

        response = self.send_request(serialized_request)

        return DeleteCollectionResponseOkResponse._unmap(response)
