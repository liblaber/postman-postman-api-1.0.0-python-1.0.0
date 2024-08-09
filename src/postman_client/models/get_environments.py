# This file was generated by liblab | https://liblab.com/

from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap(
    {
        "id_": "id",
        "created_at": "createdAt",
        "updated_at": "updatedAt",
        "is_public": "isPublic",
    }
)
class GetEnvironmentsEnvironments(BaseModel):
    """GetEnvironmentsEnvironments

    :param id_: The environment's ID., defaults to None
    :type id_: str, optional
    :param name: The environment's name., defaults to None
    :type name: str, optional
    :param created_at: The date and time at which the environment was created., defaults to None
    :type created_at: str, optional
    :param updated_at: The date and time at which the environment was last updated., defaults to None
    :type updated_at: str, optional
    :param owner: The environment owner's ID., defaults to None
    :type owner: str, optional
    :param uid: The environment's unique ID., defaults to None
    :type uid: str, optional
    :param is_public: If true, the environment is public and visible to all users., defaults to None
    :type is_public: bool, optional
    """

    def __init__(
        self,
        id_: str = None,
        name: str = None,
        created_at: str = None,
        updated_at: str = None,
        owner: str = None,
        uid: str = None,
        is_public: bool = None,
    ):
        """GetEnvironmentsEnvironments

        :param id_: The environment's ID., defaults to None
        :type id_: str, optional
        :param name: The environment's name., defaults to None
        :type name: str, optional
        :param created_at: The date and time at which the environment was created., defaults to None
        :type created_at: str, optional
        :param updated_at: The date and time at which the environment was last updated., defaults to None
        :type updated_at: str, optional
        :param owner: The environment owner's ID., defaults to None
        :type owner: str, optional
        :param uid: The environment's unique ID., defaults to None
        :type uid: str, optional
        :param is_public: If true, the environment is public and visible to all users., defaults to None
        :type is_public: bool, optional
        """
        if id_ is not None:
            self.id_ = id_
        if name is not None:
            self.name = name
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if owner is not None:
            self.owner = owner
        if uid is not None:
            self.uid = uid
        if is_public is not None:
            self.is_public = is_public


@JsonMap({})
class GetEnvironments(BaseModel):
    """GetEnvironments

    :param environments: environments, defaults to None
    :type environments: List[GetEnvironmentsEnvironments], optional
    """

    def __init__(self, environments: List[GetEnvironmentsEnvironments] = None):
        """GetEnvironments

        :param environments: environments, defaults to None
        :type environments: List[GetEnvironmentsEnvironments], optional
        """
        if environments is not None:
            self.environments = self._define_list(
                environments, GetEnvironmentsEnvironments
            )
