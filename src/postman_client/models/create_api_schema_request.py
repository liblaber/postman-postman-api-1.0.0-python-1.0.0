# This file was generated by liblab | https://liblab.com/

from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


class CreateApiSchemaType1(Enum):
    """An enumeration representing different categories.

    :cvar PROTO2: "proto:2"
    :vartype PROTO2: str
    :cvar PROTO3: "proto:3"
    :vartype PROTO3: str
    :cvar GRAPHQL: "graphql"
    :vartype GRAPHQL: str
    :cvar OPENAPI3_1: "openapi:3_1"
    :vartype OPENAPI3_1: str
    :cvar OPENAPI3: "openapi:3"
    :vartype OPENAPI3: str
    :cvar OPENAPI2: "openapi:2"
    :vartype OPENAPI2: str
    :cvar OPENAPI1: "openapi:1"
    :vartype OPENAPI1: str
    :cvar RAML1: "raml:1"
    :vartype RAML1: str
    :cvar RAML0_8: "raml:0_8"
    :vartype RAML0_8: str
    :cvar WSDL2: "wsdl:2"
    :vartype WSDL2: str
    :cvar WSDL1: "wsdl:1"
    :vartype WSDL1: str
    :cvar ASYNCAPI2: "asyncapi:2"
    :vartype ASYNCAPI2: str
    """

    PROTO2 = "proto:2"
    PROTO3 = "proto:3"
    GRAPHQL = "graphql"
    OPENAPI3_1 = "openapi:3_1"
    OPENAPI3 = "openapi:3"
    OPENAPI2 = "openapi:2"
    OPENAPI1 = "openapi:1"
    RAML1 = "raml:1"
    RAML0_8 = "raml:0_8"
    WSDL2 = "wsdl:2"
    WSDL1 = "wsdl:1"
    ASYNCAPI2 = "asyncapi:2"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, CreateApiSchemaType1._member_map_.values()))


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
        """Information about the schema's root file.

        :param enabled: If true, tag the file as the root file. The root tag is only allowed for protobuf specifications., defaults to None
        :type enabled: Enabled, optional
        """
        if enabled is not None:
            self.enabled = self._enum_matching(enabled, Enabled.list(), "enabled")


@JsonMap({})
class CreateApiSchemaFiles1(BaseModel):
    """CreateApiSchemaFiles1

    :param path: The schema's file path., defaults to None
    :type path: str, optional
    :param root: Information about the schema's root file., defaults to None
    :type root: FilesRoot, optional
    :param content: The schema file's stringified contents., defaults to None
    :type content: str, optional
    """

    def __init__(self, path: str = None, root: FilesRoot = None, content: str = None):
        """CreateApiSchemaFiles1

        :param path: The schema's file path., defaults to None
        :type path: str, optional
        :param root: Information about the schema's root file., defaults to None
        :type root: FilesRoot, optional
        :param content: The schema file's stringified contents., defaults to None
        :type content: str, optional
        """
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
    :type type_: CreateApiSchemaType1
    :param files: The list of files that are part of the schema.
    :type files: List[CreateApiSchemaFiles1]
    """

    def __init__(self, type_: CreateApiSchemaType1, files: List[CreateApiSchemaFiles1]):
        """Information about the API schema.

        :param type_: The schema's type.
        :type type_: CreateApiSchemaType1
        :param files: The list of files that are part of the schema.
        :type files: List[CreateApiSchemaFiles1]
        """
        self.type_ = self._enum_matching(type_, CreateApiSchemaType1.list(), "type_")
        self.files = self._define_list(files, CreateApiSchemaFiles1)
