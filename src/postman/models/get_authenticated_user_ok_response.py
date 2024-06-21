from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap(
    {
        "id_": "id",
        "full_name": "fullName",
        "is_public": "isPublic",
        "team_id": "teamId",
        "team_name": "teamName",
        "team_domain": "teamDomain",
    }
)
class GetAuthenticatedUserOkResponseUser(BaseModel):
    """Information about the authenticated user.

    :param id_: The user's Postman ID., defaults to None
    :type id_: float, optional
    :param username: The user's username., defaults to None
    :type username: str, optional
    :param email: The user's email address., defaults to None
    :type email: str, optional
    :param full_name: The user's full name., defaults to None
    :type full_name: str, optional
    :param avatar: The user's avatar image URL., defaults to None
    :type avatar: str, optional
    :param is_public: If true, the user's information is public and visible to all users., defaults to None
    :type is_public: bool, optional
    :param team_id: The team ID the user is assigned to. This returns a `0` value if the user is not assigned to a team., defaults to None
    :type team_id: int, optional
    :param team_name: The name of the team the user is assigned to., defaults to None
    :type team_name: str, optional
    :param team_domain: The team's Postman domain ID., defaults to None
    :type team_domain: str, optional
    :param roles: A list of the user's assigned [roles](https://learning.postman.com/docs/collaborating-in-postman/roles-and-permissions/#team-roles)., defaults to None
    :type roles: List[str], optional
    """

    def __init__(
        self,
        id_: float = None,
        username: str = None,
        email: str = None,
        full_name: str = None,
        avatar: str = None,
        is_public: bool = None,
        team_id: int = None,
        team_name: str = None,
        team_domain: str = None,
        roles: List[str] = None,
    ):
        if id_ is not None:
            self.id_ = id_
        if username is not None:
            self.username = username
        if email is not None:
            self.email = email
        if full_name is not None:
            self.full_name = full_name
        if avatar is not None:
            self.avatar = avatar
        if is_public is not None:
            self.is_public = is_public
        if team_id is not None:
            self.team_id = team_id
        if team_name is not None:
            self.team_name = team_name
        if team_domain is not None:
            self.team_domain = team_domain
        if roles is not None:
            self.roles = roles


@JsonMap({})
class GetAuthenticatedUserOkResponseOperations(BaseModel):
    """GetAuthenticatedUserOkResponseOperations

    :param limit: The operation's limit value., defaults to None
    :type limit: float, optional
    :param name: The operation's name., defaults to None
    :type name: str, optional
    :param overage: The operation's overage value., defaults to None
    :type overage: float, optional
    :param usage: The operation's current usage value., defaults to None
    :type usage: float, optional
    """

    def __init__(
        self,
        limit: float = None,
        name: str = None,
        overage: float = None,
        usage: float = None,
    ):
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if overage is not None:
            self.overage = overage
        if usage is not None:
            self.usage = usage


@JsonMap({})
class GetAuthenticatedUserOkResponse(BaseModel):
    """GetAuthenticatedUserOkResponse

    :param user: Information about the authenticated user., defaults to None
    :type user: GetAuthenticatedUserOkResponseUser, optional
    :param operations: Information about operations and their usage limits. This object does not return for users with the [Guest role](https://learning.postman.com/docs/collaborating-in-postman/roles-and-permissions/#team-roles)., defaults to None
    :type operations: List[GetAuthenticatedUserOkResponseOperations], optional
    """

    def __init__(
        self,
        user: GetAuthenticatedUserOkResponseUser = None,
        operations: List[GetAuthenticatedUserOkResponseOperations] = None,
    ):
        if user is not None:
            self.user = self._define_object(user, GetAuthenticatedUserOkResponseUser)
        if operations is not None:
            self.operations = self._define_list(
                operations, GetAuthenticatedUserOkResponseOperations
            )
