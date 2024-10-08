# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap(
    {
        "id_": "id",
        "created_at": "createdAt",
        "created_by": "createdBy",
        "updated_at": "updatedAt",
        "updated_by": "updatedBy",
    }
)
class UpdateApiOkResponse(BaseModel):
    """Information about the API.

    :param id_: The API's ID., defaults to None
    :type id_: str, optional
    :param name: The API's name.
    :type name: str
    :param summary: The API's summary., defaults to None
    :type summary: str, optional
    :param created_at: The date and time at which the API was created., defaults to None
    :type created_at: str, optional
    :param created_by: The user ID of the user that created the API., defaults to None
    :type created_by: str, optional
    :param updated_at: The date and time at which the API was last updated., defaults to None
    :type updated_at: str, optional
    :param updated_by: The user ID of the user that updated the API., defaults to None
    :type updated_by: str, optional
    :param description: The API's description. This supports Markdown formatting., defaults to None
    :type description: str, optional
    """

    def __init__(
        self,
        name: str,
        id_: str = None,
        summary: str = None,
        created_at: str = None,
        created_by: str = None,
        updated_at: str = None,
        updated_by: str = None,
        description: str = None,
    ):
        """Information about the API.

        :param id_: The API's ID., defaults to None
        :type id_: str, optional
        :param name: The API's name.
        :type name: str
        :param summary: The API's summary., defaults to None
        :type summary: str, optional
        :param created_at: The date and time at which the API was created., defaults to None
        :type created_at: str, optional
        :param created_by: The user ID of the user that created the API., defaults to None
        :type created_by: str, optional
        :param updated_at: The date and time at which the API was last updated., defaults to None
        :type updated_at: str, optional
        :param updated_by: The user ID of the user that updated the API., defaults to None
        :type updated_by: str, optional
        :param description: The API's description. This supports Markdown formatting., defaults to None
        :type description: str, optional
        """
        if id_ is not None:
            self.id_ = id_
        self.name = name
        if summary is not None:
            self.summary = summary
        if created_at is not None:
            self.created_at = created_at
        if created_by is not None:
            self.created_by = created_by
        if updated_at is not None:
            self.updated_at = updated_at
        if updated_by is not None:
            self.updated_by = updated_by
        if description is not None:
            self.description = description
