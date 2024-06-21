from enum import Enum
from .utils.json_map import JsonMap
from .base import BaseModel


class SchemaLanguage(Enum):
    """An enumeration representing different categories.

    :cvar JSON: "json"
    :vartype JSON: str
    :cvar YAML: "yaml"
    :vartype YAML: str
    """

    JSON = "json"
    YAML = "yaml"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, SchemaLanguage._member_map_.values()))


class SchemaType(Enum):
    """An enumeration representing different categories.

    :cvar OPENAPI3: "openapi3"
    :vartype OPENAPI3: str
    :cvar OPENAPI2: "openapi2"
    :vartype OPENAPI2: str
    """

    OPENAPI3 = "openapi3"
    OPENAPI2 = "openapi2"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, SchemaType._member_map_.values()))


@JsonMap({"type_": "type"})
class SchemaSecurityValidationRequestSchema(BaseModel):
    """SchemaSecurityValidationRequestSchema

    :param language: The definition format.
    :type language: SchemaLanguage
    :param schema: The stringified API definition.
    :type schema: str
    :param type_: The definition type.
    :type type_: SchemaType
    """

    def __init__(self, language: SchemaLanguage, schema: str, type_: SchemaType):
        self.language = self._enum_matching(language, SchemaLanguage.list(), "language")
        self.schema = schema
        self.type_ = self._enum_matching(type_, SchemaType.list(), "type_")


@JsonMap({})
class SchemaSecurityValidationRequest(BaseModel):
    """SchemaSecurityValidationRequest

    :param schema: schema, defaults to None
    :type schema: SchemaSecurityValidationRequestSchema, optional
    """

    def __init__(self, schema: SchemaSecurityValidationRequestSchema = None):
        if schema is not None:
            self.schema = self._define_object(
                schema, SchemaSecurityValidationRequestSchema
            )
