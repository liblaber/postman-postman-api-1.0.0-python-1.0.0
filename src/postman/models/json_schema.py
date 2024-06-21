from enum import Enum
from .utils.json_map import JsonMap
from .base import BaseModel


class JsonSchemaType(Enum):
    """An enumeration representing different categories.

    :cvar JSON: "json"
    :vartype JSON: str
    """

    JSON = "json"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, JsonSchemaType._member_map_.values()))


@JsonMap({"type_": "type"})
class JsonSchema(BaseModel):
    """JsonSchema

    :param type_: The OpenAPI definition type.
    :type type_: JsonSchemaType
    :param input: An object that contains a valid JSON OpenAPI definition. For more information, read the [OpenAPI documentation](https://swagger.io/docs/specification/basic-structure/).
    :type input: dict
    :param options: An object that contains advanced creation options and their values. You can find a complete list of properties and their values in Postman's [OpenAPI 3.0 to Postman Collection v2.1.0 Converter OPTIONS documentation](https://github.com/postmanlabs/openapi-to-postman/blob/develop/OPTIONS.md). These properties are case-sensitive., defaults to None
    :type options: dict, optional
    """

    def __init__(self, type_: JsonSchemaType, input: dict, options: dict = None):
        self.type_ = self._enum_matching(type_, JsonSchemaType.list(), "type_")
        self.input = input
        if options is not None:
            self.options = options
