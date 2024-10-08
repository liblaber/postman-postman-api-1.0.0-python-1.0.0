# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap(
    {
        "id_": "id",
        "status_code": "statusCode",
        "created_at": "createdAt",
        "updated_at": "updatedAt",
        "created_by": "createdBy",
        "updated_by": "updatedBy",
    }
)
class GetMockServerResponses(BaseModel):
    """Information about the server response.

    :param id_: The server response's ID., defaults to None
    :type id_: str, optional
    :param name: The server response's name., defaults to None
    :type name: str, optional
    :param status_code: The server response's 5xx HTTP response code., defaults to None
    :type status_code: float, optional
    :param created_at: The date and time at which the server response was created., defaults to None
    :type created_at: str, optional
    :param updated_at: The date and time at which the server response was last updated., defaults to None
    :type updated_at: str, optional
    :param created_by: The user ID of the user who created the server response., defaults to None
    :type created_by: str, optional
    :param updated_by: The user ID of the user who last updated the server response., defaults to None
    :type updated_by: str, optional
    """

    def __init__(
        self,
        id_: str = None,
        name: str = None,
        status_code: float = None,
        created_at: str = None,
        updated_at: str = None,
        created_by: str = None,
        updated_by: str = None,
    ):
        """Information about the server response.

        :param id_: The server response's ID., defaults to None
        :type id_: str, optional
        :param name: The server response's name., defaults to None
        :type name: str, optional
        :param status_code: The server response's 5xx HTTP response code., defaults to None
        :type status_code: float, optional
        :param created_at: The date and time at which the server response was created., defaults to None
        :type created_at: str, optional
        :param updated_at: The date and time at which the server response was last updated., defaults to None
        :type updated_at: str, optional
        :param created_by: The user ID of the user who created the server response., defaults to None
        :type created_by: str, optional
        :param updated_by: The user ID of the user who last updated the server response., defaults to None
        :type updated_by: str, optional
        """
        if id_ is not None:
            self.id_ = id_
        if name is not None:
            self.name = name
        if status_code is not None:
            self.status_code = status_code
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if created_by is not None:
            self.created_by = created_by
        if updated_by is not None:
            self.updated_by = updated_by
