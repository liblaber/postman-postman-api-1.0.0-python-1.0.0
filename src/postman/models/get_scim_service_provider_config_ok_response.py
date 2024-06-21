from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class Patch(BaseModel):
    """Information about patch configuration.

    :param supported: If true, the feature is supported., defaults to None
    :type supported: bool, optional
    """

    def __init__(self, supported: bool = None):
        if supported is not None:
            self.supported = supported


@JsonMap({"max_operations": "maxOperations", "max_payload_size": "maxPayloadSize"})
class Bulk(BaseModel):
    """Information about bulk configuration.

    :param max_operations: The total number of maximum operations allowed for bulk operations., defaults to None
    :type max_operations: float, optional
    :param max_payload_size: The maximum payload allowed for bulk operations., defaults to None
    :type max_payload_size: float, optional
    :param supported: If true, the feature is supported., defaults to None
    :type supported: bool, optional
    """

    def __init__(
        self,
        max_operations: float = None,
        max_payload_size: float = None,
        supported: bool = None,
    ):
        if max_operations is not None:
            self.max_operations = max_operations
        if max_payload_size is not None:
            self.max_payload_size = max_payload_size
        if supported is not None:
            self.supported = supported


@JsonMap({"max_results": "maxResults"})
class Filter(BaseModel):
    """Information about the filter configuration.

    :param max_results: The total number of maximum results allowed for filter operations., defaults to None
    :type max_results: float, optional
    :param supported: If true, the feature is supported., defaults to None
    :type supported: bool, optional
    """

    def __init__(self, max_results: float = None, supported: bool = None):
        if max_results is not None:
            self.max_results = max_results
        if supported is not None:
            self.supported = supported


@JsonMap({})
class ChangePassword(BaseModel):
    """Information about the change password configuration.

    :param supported: If true, the feature is supported., defaults to None
    :type supported: bool, optional
    """

    def __init__(self, supported: bool = None):
        if supported is not None:
            self.supported = supported


@JsonMap({})
class GetScimServiceProviderConfigOkResponseSort(BaseModel):
    """Information about the sort configuration.

    :param supported: If true, the feature is supported., defaults to None
    :type supported: bool, optional
    """

    def __init__(self, supported: bool = None):
        if supported is not None:
            self.supported = supported


@JsonMap({"spec_uri": "specUri", "type_": "type"})
class AuthenticationSchemes(BaseModel):
    """Information about the scheme.

    :param description: The scheme's description., defaults to None
    :type description: str, optional
    :param name: The scheme's friendly name., defaults to None
    :type name: str, optional
    :param spec_uri: A link to the scheme's specification documentation., defaults to None
    :type spec_uri: str, optional
    :param type_: The scheme's type., defaults to None
    :type type_: str, optional
    """

    def __init__(
        self,
        description: str = None,
        name: str = None,
        spec_uri: str = None,
        type_: str = None,
    ):
        if description is not None:
            self.description = description
        if name is not None:
            self.name = name
        if spec_uri is not None:
            self.spec_uri = spec_uri
        if type_ is not None:
            self.type_ = type_


@JsonMap({})
class Etag(BaseModel):
    """Information about the [entity tag](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag) (Etag) HTTP response header configuration.

    :param supported: If true, the feature is supported., defaults to None
    :type supported: bool, optional
    """

    def __init__(self, supported: bool = None):
        if supported is not None:
            self.supported = supported


@JsonMap({"resource_type": "resourceType"})
class GetScimServiceProviderConfigOkResponseMeta(BaseModel):
    """The response's non-standard meta information.

    :param resource_type: resource_type, defaults to None
    :type resource_type: str, optional
    :param location: location, defaults to None
    :type location: str, optional
    """

    def __init__(self, resource_type: str = None, location: str = None):
        if resource_type is not None:
            self.resource_type = resource_type
        if location is not None:
            self.location = location


@JsonMap(
    {
        "documentation_uri": "documentationUri",
        "change_password": "changePassword",
        "authentication_schemes": "authenticationSchemes",
    }
)
class GetScimServiceProviderConfigOkResponse(BaseModel):
    """Information about Postman's SCIM API configurations and supported operations.

    :param schemas: The [SCIM schema URI](https://www.iana.org/assignments/scim/scim.xhtml)., defaults to None
    :type schemas: List[str], optional
    :param documentation_uri: A link to the URI's documentation., defaults to None
    :type documentation_uri: str, optional
    :param patch: Information about patch configuration., defaults to None
    :type patch: Patch, optional
    :param bulk: Information about bulk configuration., defaults to None
    :type bulk: Bulk, optional
    :param filter: Information about the filter configuration., defaults to None
    :type filter: Filter, optional
    :param change_password: Information about the change password configuration., defaults to None
    :type change_password: ChangePassword, optional
    :param sort: Information about the sort configuration., defaults to None
    :type sort: GetScimServiceProviderConfigOkResponseSort, optional
    :param authentication_schemes: A list of authentication schemes., defaults to None
    :type authentication_schemes: List[AuthenticationSchemes], optional
    :param etag: Information about the [entity tag](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag) (Etag) HTTP response header configuration., defaults to None
    :type etag: Etag, optional
    :param meta: The response's non-standard meta information., defaults to None
    :type meta: GetScimServiceProviderConfigOkResponseMeta, optional
    """

    def __init__(
        self,
        schemas: List[str] = None,
        documentation_uri: str = None,
        patch: Patch = None,
        bulk: Bulk = None,
        filter: Filter = None,
        change_password: ChangePassword = None,
        sort: GetScimServiceProviderConfigOkResponseSort = None,
        authentication_schemes: List[AuthenticationSchemes] = None,
        etag: Etag = None,
        meta: GetScimServiceProviderConfigOkResponseMeta = None,
    ):
        if schemas is not None:
            self.schemas = schemas
        if documentation_uri is not None:
            self.documentation_uri = documentation_uri
        if patch is not None:
            self.patch = self._define_object(patch, Patch)
        if bulk is not None:
            self.bulk = self._define_object(bulk, Bulk)
        if filter is not None:
            self.filter = self._define_object(filter, Filter)
        if change_password is not None:
            self.change_password = self._define_object(change_password, ChangePassword)
        if sort is not None:
            self.sort = self._define_object(
                sort, GetScimServiceProviderConfigOkResponseSort
            )
        if authentication_schemes is not None:
            self.authentication_schemes = self._define_list(
                authentication_schemes, AuthenticationSchemes
            )
        if etag is not None:
            self.etag = self._define_object(etag, Etag)
        if meta is not None:
            self.meta = self._define_object(
                meta, GetScimServiceProviderConfigOkResponseMeta
            )
