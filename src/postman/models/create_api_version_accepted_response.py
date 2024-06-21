from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap(
    {
        "id_": "id",
        "created_at": "createdAt",
        "updated_at": "updatedAt",
        "release_notes": "releaseNotes",
    }
)
class CreateApiVersionAcceptedResponse(BaseModel):
    """CreateApiVersionAcceptedResponse

    :param id_: The version's ID., defaults to None
    :type id_: str, optional
    :param created_at: The date and time at which the version was created., defaults to None
    :type created_at: str, optional
    :param updated_at: The date and time at which the version was last updated., defaults to None
    :type updated_at: str, optional
    :param name: The version's name., defaults to None
    :type name: str, optional
    :param release_notes: Information about the API version release. For example, changelog notes., defaults to None
    :type release_notes: str, optional
    """

    def __init__(
        self,
        id_: str = None,
        created_at: str = None,
        updated_at: str = None,
        name: str = None,
        release_notes: str = None,
    ):
        if id_ is not None:
            self.id_ = id_
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if name is not None:
            self.name = name
        if release_notes is not None:
            self.release_notes = release_notes
