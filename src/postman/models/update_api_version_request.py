from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"release_notes": "releaseNotes"})
class UpdateApiVersionRequest(BaseModel):
    """Information about the API version.

    :param name: The version's name.
    :type name: str
    :param release_notes: The version's Markdown-supported release notes., defaults to None
    :type release_notes: str, optional
    """

    def __init__(self, name: str, release_notes: str = None):
        self.name = name
        if release_notes is not None:
            self.release_notes = release_notes
