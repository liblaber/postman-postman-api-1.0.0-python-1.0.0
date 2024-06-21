from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


class CreateApiSchemaRequestType(Enum):
    """An enumeration representing different categories.

    :cvar PROTO_2: "proto:2"
    :vartype PROTO_2: str
    :cvar PROTO_3: "proto:3"
    :vartype PROTO_3: str
    :cvar GRAPHQL: "graphql"
    :vartype GRAPHQL: str
    :cvar OPENAPI_3_1: "openapi:3_1"
    :vartype OPENAPI_3_1: str
    :cvar OPENAPI_3: "openapi:3"
    :vartype OPENAPI_3: str
    :cvar OPENAPI_2: "openapi:2"
    :vartype OPENAPI_2: str
    :cvar OPENAPI_1: "openapi:1"
    :vartype OPENAPI_1: str
    :cvar RAML_1: "raml:1"
    :vartype RAML_1: str
    :cvar RAML_0_8: "raml:0_8"
    :vartype RAML_0_8: str
    :cvar WSDL_2: "wsdl:2"
    :vartype WSDL_2: str
    :cvar WSDL_1: "wsdl:1"
    :vartype WSDL_1: str
    :cvar ASYNCAPI_2: "asyncapi:2"
    :vartype ASYNCAPI_2: str
    """

    PROTO_2 = "proto:2"
    PROTO_3 = "proto:3"
    GRAPHQL = "graphql"
    OPENAPI_3_1 = "openapi:3_1"
    OPENAPI_3 = "openapi:3"
    OPENAPI_2 = "openapi:2"
    OPENAPI_1 = "openapi:1"
    RAML_1 = "raml:1"
    RAML_0_8 = "raml:0_8"
    WSDL_2 = "wsdl:2"
    WSDL_1 = "wsdl:1"
    ASYNCAPI_2 = "asyncapi:2"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, CreateApiSchemaRequestType._member_map_.values())
        )


class Enabled(Enum):
    """An enumeration representing different categories.

    :cvar TRUE: "true"
    :vartype TRUE: str
    """

    TRUE = "true"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Enabled._member_map_.values()))


@JsonMap({})
class FilesRoot(BaseModel):
    """Information about the schema's root file.

    :param enabled: If true, tag the file as the root file. The root tag is only allowed for protobuf specifications., defaults to None
    :type enabled: Enabled, optional
    """

    def __init__(self, enabled: Enabled = None):
        if enabled is not None:
            self.enabled = self._enum_matching(enabled, Enabled.list(), "enabled")


@JsonMap({})
class CreateApiSchemaRequestFiles(BaseModel):
    """CreateApiSchemaRequestFiles

    :param path: The schema's file path., defaults to None
    :type path: str, optional
    :param root: Information about the schema's root file., defaults to None
    :type root: FilesRoot, optional
    :param content: The schema file's stringified contents., defaults to None
    :type content: str, optional
    """

    def __init__(self, path: str = None, root: FilesRoot = None, content: str = None):
        if path is not None:
            self.path = path
        if root is not None:
            self.root = self._define_object(root, FilesRoot)
        if content is not None:
            self.content = content


@JsonMap({"type_": "type"})
class CreateApiSchemaRequest(BaseModel):
    """Information about the API schema.

    :param type_: The schema's type.
    :type type_: CreateApiSchemaRequestType
    :param files: The list of files that are part of the schema.
    :type files: List[CreateApiSchemaRequestFiles]
    """

    def __init__(
        self,
        type_: CreateApiSchemaRequestType,
        files: List[CreateApiSchemaRequestFiles],
    ):
        self.type_ = self._enum_matching(
            type_, CreateApiSchemaRequestType.list(), "type_"
        )
        self.files = self._define_list(files, CreateApiSchemaRequestFiles)
