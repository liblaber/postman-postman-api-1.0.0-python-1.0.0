from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id", "display_name": "displayName"})
class RolesUser(BaseModel):
    """Information about the user role.

    :param id_: The role's ID., defaults to None
    :type id_: int, optional
    :param description: The role's description., defaults to None
    :type description: str, optional
    :param display_name: The role's display name., defaults to None
    :type display_name: str, optional
    """

    def __init__(
        self, id_: int = None, description: str = None, display_name: str = None
    ):
        if id_ is not None:
            self.id_ = id_
        if description is not None:
            self.description = description
        if display_name is not None:
            self.display_name = display_name


@JsonMap({"id_": "id", "display_name": "displayName"})
class Usergroup(BaseModel):
    """Information about the user group in the workspace.

    :param id_: The role's ID., defaults to None
    :type id_: int, optional
    :param description: The role's description., defaults to None
    :type description: str, optional
    :param display_name: The role's display name., defaults to None
    :type display_name: str, optional
    """

    def __init__(
        self, id_: int = None, description: str = None, display_name: str = None
    ):
        if id_ is not None:
            self.id_ = id_
        if description is not None:
            self.description = description
        if display_name is not None:
            self.display_name = display_name


@JsonMap({})
class GetWorkspaceRolesOkResponseRoles(BaseModel):
    """Information about the workspace's [user roles](https://learning.postman.com/docs/collaborating-in-postman/roles-and-permissions/#team-roles).

    :param user: The list of user roles in the workspace., defaults to None
    :type user: List[RolesUser], optional
    :param usergroup: Information about the workspace's [user group roles](https://learning.postman.com/docs/collaborating-in-postman/user-groups/)., defaults to None
    :type usergroup: List[Usergroup], optional
    """

    def __init__(self, user: List[RolesUser] = None, usergroup: List[Usergroup] = None):
        if user is not None:
            self.user = self._define_list(user, RolesUser)
        if usergroup is not None:
            self.usergroup = self._define_list(usergroup, Usergroup)


@JsonMap({})
class GetWorkspaceRolesOkResponse(BaseModel):
    """GetWorkspaceRolesOkResponse

    :param roles: Information about the workspace's [user roles](https://learning.postman.com/docs/collaborating-in-postman/roles-and-permissions/#team-roles)., defaults to None
    :type roles: GetWorkspaceRolesOkResponseRoles, optional
    """

    def __init__(self, roles: GetWorkspaceRolesOkResponseRoles = None):
        if roles is not None:
            self.roles = self._define_object(roles, GetWorkspaceRolesOkResponseRoles)
