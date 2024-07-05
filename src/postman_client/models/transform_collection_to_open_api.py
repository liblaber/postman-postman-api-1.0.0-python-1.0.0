# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class TransformCollectionToOpenApi(BaseModel):
    """TransformCollectionToOpenApi

    :param output: The collection's transformed output, in a stringified OpenAPI format., defaults to None
    :type output: str, optional
    """

    def __init__(self, output: str = None):
        if output is not None:
            self.output = output
