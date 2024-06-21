from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class TransformCollectionToOpenApiOkResponse(BaseModel):
    """TransformCollectionToOpenApiOkResponse

    :param output: The collection's transformed output, in a stringified OpenAPI format., defaults to None
    :type output: str, optional
    """

    def __init__(self, output: str = None):
        if output is not None:
            self.output = output
