from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id"})
class Actor(BaseModel):
    """Information about the user who preformed the audit event.

    :param name: The user's name., defaults to None
    :type name: str, optional
    :param username: The user's username., defaults to None
    :type username: str, optional
    :param email: The user's email address., defaults to None
    :type email: str, optional
    :param id_: id_, defaults to None
    :type id_: float, optional
    :param active: If true, the user is active. If false, the user is deactivated., defaults to None
    :type active: bool, optional
    """

    def __init__(
        self,
        name: str = None,
        username: str = None,
        email: str = None,
        id_: float = None,
        active: bool = None,
    ):
        if name is not None:
            self.name = name
        if username is not None:
            self.username = username
        if email is not None:
            self.email = email
        if id_ is not None:
            self.id_ = id_
        if active is not None:
            self.active = active


@JsonMap({"id_": "id"})
class DataUser(BaseModel):
    """Information about the user.

    :param name: The user's name., defaults to None
    :type name: str, optional
    :param username: The user's username., defaults to None
    :type username: str, optional
    :param email: The user's email address., defaults to None
    :type email: str, optional
    :param id_: The user's ID., defaults to None
    :type id_: float, optional
    """

    def __init__(
        self,
        name: str = None,
        username: str = None,
        email: str = None,
        id_: float = None,
    ):
        if name is not None:
            self.name = name
        if username is not None:
            self.username = username
        if email is not None:
            self.email = email
        if id_ is not None:
            self.id_ = id_


@JsonMap({"id_": "id"})
class DataTeam(BaseModel):
    """The user's team information.

    :param name: The team's name., defaults to None
    :type name: str, optional
    :param id_: The team's ID., defaults to None
    :type id_: float, optional
    """

    def __init__(self, name: str = None, id_: float = None):
        if name is not None:
            self.name = name
        if id_ is not None:
            self.id_ = id_


@JsonMap({})
class TrailsData(BaseModel):
    """TrailsData

    :param actor: Information about the user who preformed the audit event., defaults to None
    :type actor: Actor, optional
    :param user: Information about the user., defaults to None
    :type user: DataUser, optional
    :param team: The user's team information., defaults to None
    :type team: DataTeam, optional
    :param variables: Additional information about the performed action., defaults to None
    :type variables: dict, optional
    """

    def __init__(
        self,
        actor: Actor = None,
        user: DataUser = None,
        team: DataTeam = None,
        variables: dict = None,
    ):
        if actor is not None:
            self.actor = self._define_object(actor, Actor)
        if user is not None:
            self.user = self._define_object(user, DataUser)
        if team is not None:
            self.team = self._define_object(team, DataTeam)
        if variables is not None:
            self.variables = variables


@JsonMap({"id_": "id", "user_agent": "userAgent"})
class Trails(BaseModel):
    """Trails

    :param id_: The audit event's ID., defaults to None
    :type id_: float, optional
    :param ip: The IP address of the user that performed the action., defaults to None
    :type ip: str, optional
    :param user_agent: The user agent information., defaults to None
    :type user_agent: str, optional
    :param action: The action performed by the user., defaults to None
    :type action: str, optional
    :param timestamp: The date and time at which the event occurred., defaults to None
    :type timestamp: str, optional
    :param message: The audit event's description., defaults to None
    :type message: str, optional
    :param data: data, defaults to None
    :type data: TrailsData, optional
    """

    def __init__(
        self,
        id_: float = None,
        ip: str = None,
        user_agent: str = None,
        action: str = None,
        timestamp: str = None,
        message: str = None,
        data: TrailsData = None,
    ):
        if id_ is not None:
            self.id_ = id_
        if ip is not None:
            self.ip = ip
        if user_agent is not None:
            self.user_agent = user_agent
        if action is not None:
            self.action = action
        if timestamp is not None:
            self.timestamp = timestamp
        if message is not None:
            self.message = message
        if data is not None:
            self.data = self._define_object(data, TrailsData)


@JsonMap({})
class GetAuditLogsOkResponse(BaseModel):
    """GetAuditLogsOkResponse

    :param trails: trails, defaults to None
    :type trails: List[Trails], optional
    """

    def __init__(self, trails: List[Trails] = None):
        if trails is not None:
            self.trails = self._define_list(trails, Trails)
