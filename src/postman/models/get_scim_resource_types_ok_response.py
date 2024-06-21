from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class SchemaExtensions(BaseModel):
    """SchemaExtensions

    :param schema: The [SCIM schema URI](https://www.iana.org/assignments/scim/scim.xhtml)., defaults to None
    :type schema: str, optional
    :param required: If true, the resource must include this schema extension., defaults to None
    :type required: bool, optional
    """

    def __init__(self, schema: str = None, required: bool = None):
        if schema is not None:
            self.schema = schema
        if required is not None:
            self.required = required


@JsonMap({"id_": "id", "schema_extensions": "schemaExtensions"})
class GetScimResourceTypesOkResponse(BaseModel):
    """GetScimResourceTypesOkResponse

    :param schemas: The [SCIM schema URI](https://www.iana.org/assignments/scim/scim.xhtml)., defaults to None
    :type schemas: List[str], optional
    :param id_: The resource's ID., defaults to None
    :type id_: str, optional
    :param name: The resource's friendly name., defaults to None
    :type name: str, optional
    :param endpoint: The resource's endpoint., defaults to None
    :type endpoint: str, optional
    :param description: The resource's description., defaults to None
    :type description: str, optional
    :param schema: The [SCIM schema URI](https://www.iana.org/assignments/scim/scim.xhtml)., defaults to None
    :type schema: str, optional
    :param schema_extensions: Information about the resource's schema extensions., defaults to None
    :type schema_extensions: List[SchemaExtensions], optional
    """

    def __init__(
        self,
        schemas: List[str] = None,
        id_: str = None,
        name: str = None,
        endpoint: str = None,
        description: str = None,
        schema: str = None,
        schema_extensions: List[SchemaExtensions] = None,
    ):
        if schemas is not None:
            self.schemas = schemas
        if id_ is not None:
            self.id_ = id_
        if name is not None:
            self.name = name
        if endpoint is not None:
            self.endpoint = endpoint
        if description is not None:
            self.description = description
        if schema is not None:
            self.schema = schema
        if schema_extensions is not None:
            self.schema_extensions = self._define_list(
                schema_extensions, SchemaExtensions
            )
