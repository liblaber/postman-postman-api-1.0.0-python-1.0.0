from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap(
    {
        "created_at": "createdAt",
        "created_by": "createdBy",
        "destination_id": "destinationId",
        "id_": "id",
        "source_id": "sourceId",
        "updated_at": "updatedAt",
    }
)
class CreateCollectionPullRequestOkResponse(BaseModel):
    """CreateCollectionPullRequestOkResponse

    :param created_at: The date and time at which the pull request was created., defaults to None
    :type created_at: str, optional
    :param created_by: The ID of the user who created the pull request., defaults to None
    :type created_by: str, optional
    :param description: The pull request's description., defaults to None
    :type description: str, optional
    :param destination_id: The pull request's merge destination ID., defaults to None
    :type destination_id: str, optional
    :param id_: The pull request's ID., defaults to None
    :type id_: str, optional
    :param source_id: The pull request's source (parent) ID., defaults to None
    :type source_id: str, optional
    :param status: The pull request's current status., defaults to None
    :type status: str, optional
    :param title: The pull request's title., defaults to None
    :type title: str, optional
    :param updated_at: The date and time at which the pull request was updated., defaults to None
    :type updated_at: str, optional
    """

    def __init__(
        self,
        created_at: str = None,
        created_by: str = None,
        description: str = None,
        destination_id: str = None,
        id_: str = None,
        source_id: str = None,
        status: str = None,
        title: str = None,
        updated_at: str = None,
    ):
        if created_at is not None:
            self.created_at = created_at
        if created_by is not None:
            self.created_by = created_by
        if description is not None:
            self.description = description
        if destination_id is not None:
            self.destination_id = destination_id
        if id_ is not None:
            self.id_ = id_
        if source_id is not None:
            self.source_id = source_id
        if status is not None:
            self.status = status
        if title is not None:
            self.title = title
        if updated_at is not None:
            self.updated_at = updated_at
