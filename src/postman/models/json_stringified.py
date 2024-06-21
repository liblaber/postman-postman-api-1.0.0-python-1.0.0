from enum import Enum
from .utils.json_map import JsonMap
from .base import BaseModel


class JsonStringifiedType(Enum):
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
        return list(map(lambda x: x.value, JsonStringifiedType._member_map_.values()))


@JsonMap({"type_": "type"})
class JsonStringified(BaseModel):
    """JsonStringified

    :param type_: The OpenAPI definition type., defaults to None
    :type type_: JsonStringifiedType, optional
    :param input: The stringified OpenAPI definition., defaults to None
    :type input: str, optional
    :param options: An object that contains advanced creation options and their values. You can find a complete list of properties and their values in Postman's [OpenAPI 3.0 to Postman Collection v2.1.0 Converter OPTIONS documentation](https://github.com/postmanlabs/openapi-to-postman/blob/develop/OPTIONS.md). These properties are case-sensitive., defaults to None
    :type options: dict, optional
    """

    def __init__(
        self, type_: JsonStringifiedType = None, input: str = None, options: dict = None
    ):
        if type_ is not None:
            self.type_ = self._enum_matching(type_, JsonStringifiedType.list(), "type_")
        if input is not None:
            self.input = input
        if options is not None:
            self.options = options
