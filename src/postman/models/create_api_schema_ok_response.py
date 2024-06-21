from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


class CreateApiSchemaOkResponseType(Enum):
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
            map(lambda x: x.value, CreateApiSchemaOkResponseType._member_map_.values())
        )


@JsonMap(
    {
        "id_": "id",
        "created_at": "createdAt",
        "created_by": "createdBy",
        "updated_at": "updatedAt",
        "updated_by": "updatedBy",
    }
)
class CreateApiSchemaOkResponseFiles(BaseModel):
    """Information about the schema file.

    :param id_: The schema file's ID., defaults to None
    :type id_: str, optional
    :param name: The schema file's name., defaults to None
    :type name: str, optional
    :param path: The file system path to the schema file., defaults to None
    :type path: str, optional
    :param created_at: The date and time at which the file was created., defaults to None
    :type created_at: str, optional
    :param created_by: The user ID of the user that created the file., defaults to None
    :type created_by: str, optional
    :param updated_at: The date and time at which the file was last updated., defaults to None
    :type updated_at: str, optional
    :param updated_by: The user ID of the user that last updated the file., defaults to None
    :type updated_by: str, optional
    """

    def __init__(
        self,
        id_: str = None,
        name: str = None,
        path: str = None,
        created_at: str = None,
        created_by: str = None,
        updated_at: str = None,
        updated_by: str = None,
    ):
        if id_ is not None:
            self.id_ = id_
        if name is not None:
            self.name = name
        if path is not None:
            self.path = path
        if created_at is not None:
            self.created_at = created_at
        if created_by is not None:
            self.created_by = created_by
        if updated_at is not None:
            self.updated_at = updated_at
        if updated_by is not None:
            self.updated_by = updated_by


@JsonMap(
    {
        "id_": "id",
        "type_": "type",
        "created_at": "createdAt",
        "created_by": "createdBy",
        "updated_at": "updatedAt",
        "updated_by": "updatedBy",
    }
)
class CreateApiSchemaOkResponse(BaseModel):
    """Information about the created API schema.

    :param id_: The schema's ID., defaults to None
    :type id_: str, optional
    :param type_: The schema's type., defaults to None
    :type type_: CreateApiSchemaOkResponseType, optional
    :param files: The list of the schema's files., defaults to None
    :type files: List[CreateApiSchemaOkResponseFiles], optional
    :param created_at: The date and time at which the schema was created., defaults to None
    :type created_at: str, optional
    :param created_by: The user ID of the user that created the schema., defaults to None
    :type created_by: str, optional
    :param updated_at: The date and time at which the schema was last updated., defaults to None
    :type updated_at: str, optional
    :param updated_by: The user ID of the user that updated the schema., defaults to None
    :type updated_by: str, optional
    """

    def __init__(
        self,
        id_: str = None,
        type_: CreateApiSchemaOkResponseType = None,
        files: List[CreateApiSchemaOkResponseFiles] = None,
        created_at: str = None,
        created_by: str = None,
        updated_at: str = None,
        updated_by: str = None,
    ):
        if id_ is not None:
            self.id_ = id_
        if type_ is not None:
            self.type_ = self._enum_matching(
                type_, CreateApiSchemaOkResponseType.list(), "type_"
            )
        if files is not None:
            self.files = self._define_list(files, CreateApiSchemaOkResponseFiles)
        if created_at is not None:
            self.created_at = created_at
        if created_by is not None:
            self.created_by = created_by
        if updated_at is not None:
            self.updated_at = updated_at
        if updated_by is not None:
            self.updated_by = updated_by
