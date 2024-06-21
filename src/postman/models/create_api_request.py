from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class CreateApiRequest(BaseModel):
    """Information about the API.

    :param name: The API's name.
    :type name: str
    :param summary: The API's short summary., defaults to None
    :type summary: str, optional
    :param description: The API's description. This supports Markdown formatting., defaults to None
    :type description: str, optional
    """

    def __init__(self, name: str, summary: str = None, description: str = None):
        self.name = name
        if summary is not None:
            self.summary = summary
        if description is not None:
            self.description = description
