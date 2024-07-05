# This file was generated by liblab | https://liblab.com/

from enum import Enum
from typing import Union
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .base import OneOfBaseModel


class MetaModel(Enum):
    """An enumeration representing different categories.

    :cvar COLLECTION: "collection"
    :vartype COLLECTION: str
    :cvar API_VERSION: "api-version"
    :vartype API_VERSION: str
    """

    COLLECTION = "collection"
    API_VERSION = "api-version"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, MetaModel._member_map_.values()))


class Action(Enum):
    """An enumeration representing different categories.

    :cvar UPDATE: "update"
    :vartype UPDATE: str
    :cvar CREATE: "create"
    :vartype CREATE: str
    """

    UPDATE = "update"
    CREATE = "create"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Action._member_map_.values()))


@JsonMap({})
class GetStatusOfAnAsyncTaskMeta(BaseModel):
    """The response's non-standard meta information.

    :param url: The endpoint URL that created the task., defaults to None
    :type url: str, optional
    :param model: The model for which the task is performing the operation., defaults to None
    :type model: MetaModel, optional
    :param action: The task's action., defaults to None
    :type action: Action, optional
    """

    def __init__(self, url: str = None, model: MetaModel = None, action: Action = None):
        if url is not None:
            self.url = url
        if model is not None:
            self.model = self._enum_matching(model, MetaModel.list(), "model")
        if action is not None:
            self.action = self._enum_matching(action, Action.list(), "action")


class GetStatusOfAnAsyncTaskStatus(Enum):
    """An enumeration representing different categories.

    :cvar PENDING: "pending"
    :vartype PENDING: str
    :cvar FAILED: "failed"
    :vartype FAILED: str
    :cvar COMPLETED: "completed"
    :vartype COMPLETED: str
    """

    PENDING = "pending"
    FAILED = "failed"
    COMPLETED = "completed"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, GetStatusOfAnAsyncTaskStatus._member_map_.values())
        )


@JsonMap({"id_": "id"})
class Details1Resources(BaseModel):
    """Details1Resources

    :param id_: The ID of the assigned resource., defaults to None
    :type id_: str, optional
    :param url: The task's assigned resource URL., defaults to None
    :type url: str, optional
    """

    def __init__(self, id_: str = None, url: str = None):
        if id_ is not None:
            self.id_ = id_
        if url is not None:
            self.url = url


@JsonMap({})
class Details1(BaseModel):
    """Information about the task's resources.

    :param resources: resources, defaults to None
    :type resources: List[Details1Resources], optional
    """

    def __init__(self, resources: List[Details1Resources] = None):
        if resources is not None:
            self.resources = self._define_list(resources, Details1Resources)


@JsonMap({})
class Error(BaseModel):
    """Error

    :param message: The task's error message., defaults to None
    :type message: str, optional
    """

    def __init__(self, message: str = None):
        if message is not None:
            self.message = message


@JsonMap({})
class Details2(BaseModel):
    """Information about the error that occurred during the task's processing.

    :param error: error, defaults to None
    :type error: Error, optional
    """

    def __init__(self, error: Error = None):
        if error is not None:
            self.error = self._define_object(error, Error)


class DetailsGuard(OneOfBaseModel):
    class_list = {"Details1": Details1, "Details2": Details2}


Details = Union[Details1, Details2]


@JsonMap({"id_": "id", "created_at": "createdAt", "updated_at": "updatedAt"})
class GetStatusOfAnAsyncTask(BaseModel):
    """GetStatusOfAnAsyncTask

    :param id_: The task's ID., defaults to None
    :type id_: str, optional
    :param meta: The response's non-standard meta information., defaults to None
    :type meta: GetStatusOfAnAsyncTaskMeta, optional
    :param status: The task's current status., defaults to None
    :type status: GetStatusOfAnAsyncTaskStatus, optional
    :param details: details, defaults to None
    :type details: Details, optional
    :param created_at: The date and time at which the task was created., defaults to None
    :type created_at: str, optional
    :param updated_at: The date and time at which the task was last updated., defaults to None
    :type updated_at: str, optional
    """

    def __init__(
        self,
        id_: str = None,
        meta: GetStatusOfAnAsyncTaskMeta = None,
        status: GetStatusOfAnAsyncTaskStatus = None,
        details: Details = None,
        created_at: str = None,
        updated_at: str = None,
    ):
        if id_ is not None:
            self.id_ = id_
        if meta is not None:
            self.meta = self._define_object(meta, GetStatusOfAnAsyncTaskMeta)
        if status is not None:
            self.status = self._enum_matching(
                status, GetStatusOfAnAsyncTaskStatus.list(), "status"
            )
        if details is not None:
            self.details = DetailsGuard.return_one_of(details)
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
