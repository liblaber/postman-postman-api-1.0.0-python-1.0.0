from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


class WorkspaceType2(Enum):
    """An enumeration representing different categories.

    :cvar PERSONAL: "personal"
    :vartype PERSONAL: str
    :cvar TEAM: "team"
    :vartype TEAM: str
    :cvar PRIVATE: "private"
    :vartype PRIVATE: str
    :cvar PUBLIC: "public"
    :vartype PUBLIC: str
    :cvar PARTNER: "partner"
    :vartype PARTNER: str
    """

    PERSONAL = "personal"
    TEAM = "team"
    PRIVATE = "private"
    PUBLIC = "public"
    PARTNER = "partner"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, WorkspaceType2._member_map_.values()))


class WorkspaceVisibility(Enum):
    """An enumeration representing different categories.

    :cvar PERSONAL: "personal"
    :vartype PERSONAL: str
    :cvar TEAM: "team"
    :vartype TEAM: str
    :cvar PRIVATE: "private"
    :vartype PRIVATE: str
    :cvar PUBLIC: "public"
    :vartype PUBLIC: str
    :cvar PARTNER: "partner"
    :vartype PARTNER: str
    """

    PERSONAL = "personal"
    TEAM = "team"
    PRIVATE = "private"
    PUBLIC = "public"
    PARTNER = "partner"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, WorkspaceVisibility._member_map_.values()))


@JsonMap({"id_": "id"})
class WorkspaceCollections(BaseModel):
    """Information about the collection.

    :param id_: The collection's ID., defaults to None
    :type id_: str, optional
    :param name: The collection's name., defaults to None
    :type name: str, optional
    :param uid: The collection's unique ID., defaults to None
    :type uid: str, optional
    """

    def __init__(self, id_: str = None, name: str = None, uid: str = None):
        if id_ is not None:
            self.id_ = id_
        if name is not None:
            self.name = name
        if uid is not None:
            self.uid = uid


@JsonMap({"id_": "id"})
class WorkspaceEnvironments(BaseModel):
    """Information about the environment.

    :param id_: The environment's ID., defaults to None
    :type id_: str, optional
    :param name: The environment's name., defaults to None
    :type name: str, optional
    :param uid: The environment's unique ID., defaults to None
    :type uid: str, optional
    """

    def __init__(self, id_: str = None, name: str = None, uid: str = None):
        if id_ is not None:
            self.id_ = id_
        if name is not None:
            self.name = name
        if uid is not None:
            self.uid = uid


@JsonMap({"id_": "id"})
class WorkspaceMocks(BaseModel):
    """Information about the mock server.

    :param id_: The mock server's ID., defaults to None
    :type id_: str, optional
    :param name: The mock server's name., defaults to None
    :type name: str, optional
    :param uid: The mock server's unique ID., defaults to None
    :type uid: str, optional
    :param deactivated: If true, the mock server is not active. Mock servers deactivate when a linked collection or environment is deleted., defaults to None
    :type deactivated: bool, optional
    """

    def __init__(
        self,
        id_: str = None,
        name: str = None,
        uid: str = None,
        deactivated: bool = None,
    ):
        if id_ is not None:
            self.id_ = id_
        if name is not None:
            self.name = name
        if uid is not None:
            self.uid = uid
        if deactivated is not None:
            self.deactivated = deactivated


@JsonMap({"id_": "id"})
class WorkspaceMonitors(BaseModel):
    """Information about the monitor.

    :param id_: The monitor's ID., defaults to None
    :type id_: str, optional
    :param name: The monitor's name., defaults to None
    :type name: str, optional
    :param uid: The monitor's unique ID., defaults to None
    :type uid: str, optional
    """

    def __init__(self, id_: str = None, name: str = None, uid: str = None):
        if id_ is not None:
            self.id_ = id_
        if name is not None:
            self.name = name
        if uid is not None:
            self.uid = uid


@JsonMap({"id_": "id"})
class WorkspaceApis(BaseModel):
    """Information about the API.

    :param id_: The API's ID., defaults to None
    :type id_: str, optional
    :param name: The API's name., defaults to None
    :type name: str, optional
    :param uid: The API's unique ID., defaults to None
    :type uid: str, optional
    """

    def __init__(self, id_: str = None, name: str = None, uid: str = None):
        if id_ is not None:
            self.id_ = id_
        if name is not None:
            self.name = name
        if uid is not None:
            self.uid = uid


@JsonMap(
    {
        "id_": "id",
        "type_": "type",
        "created_by": "createdBy",
        "updated_by": "updatedBy",
        "created_at": "createdAt",
        "updated_at": "updatedAt",
    }
)
class GetWorkspaceOkResponseWorkspace(BaseModel):
    """Information about the workspace.

    :param id_: The workspace's ID., defaults to None
    :type id_: str, optional
    :param name: The workspace's name., defaults to None
    :type name: str, optional
    :param type_: The type of workspace., defaults to None
    :type type_: WorkspaceType2, optional
    :param description: The workspace's description., defaults to None
    :type description: str, optional
    :param visibility: The workspace's visibility. [Visibility](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/managing-workspaces/#changing-workspace-visibility) determines who can access the workspace:<br/>- `personal` — Only you can access the workspace.<br/>- `team` — All team members can access the workspace.<br/>- `private` — Only invited team members can access the workspace ([**Professional** and **Enterprise** plans only](https://www.postman.com/pricing)).<br/>- `public` — Everyone can access the workspace.<br/>- `partner` — Only invited team members and [partners](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/partner-workspaces/) can access the workspace ([**Professional** and **Enterprise** plans only](https://www.postman.com/pricing)).<br/>, defaults to None
    :type visibility: WorkspaceVisibility, optional
    :param created_by: The user ID of the user who created the workspace., defaults to None
    :type created_by: str, optional
    :param updated_by: The user ID of the user who last updated the workspace., defaults to None
    :type updated_by: str, optional
    :param created_at: The date and time at which the workspace was created., defaults to None
    :type created_at: str, optional
    :param updated_at: The date and time at which the workspace was last updated., defaults to None
    :type updated_at: str, optional
    :param collections: The workspace's collections., defaults to None
    :type collections: List[WorkspaceCollections], optional
    :param environments: The workspace's environments., defaults to None
    :type environments: List[WorkspaceEnvironments], optional
    :param mocks: The workspace's mock servers., defaults to None
    :type mocks: List[WorkspaceMocks], optional
    :param monitors: The workspace's monitors., defaults to None
    :type monitors: List[WorkspaceMonitors], optional
    :param apis: The workspace's APIs., defaults to None
    :type apis: List[WorkspaceApis], optional
    """

    def __init__(
        self,
        id_: str = None,
        name: str = None,
        type_: WorkspaceType2 = None,
        description: str = None,
        visibility: WorkspaceVisibility = None,
        created_by: str = None,
        updated_by: str = None,
        created_at: str = None,
        updated_at: str = None,
        collections: List[WorkspaceCollections] = None,
        environments: List[WorkspaceEnvironments] = None,
        mocks: List[WorkspaceMocks] = None,
        monitors: List[WorkspaceMonitors] = None,
        apis: List[WorkspaceApis] = None,
    ):
        if id_ is not None:
            self.id_ = id_
        if name is not None:
            self.name = name
        if type_ is not None:
            self.type_ = self._enum_matching(type_, WorkspaceType2.list(), "type_")
        if description is not None:
            self.description = description
        if visibility is not None:
            self.visibility = self._enum_matching(
                visibility, WorkspaceVisibility.list(), "visibility"
            )
        if created_by is not None:
            self.created_by = created_by
        if updated_by is not None:
            self.updated_by = updated_by
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if collections is not None:
            self.collections = self._define_list(collections, WorkspaceCollections)
        if environments is not None:
            self.environments = self._define_list(environments, WorkspaceEnvironments)
        if mocks is not None:
            self.mocks = self._define_list(mocks, WorkspaceMocks)
        if monitors is not None:
            self.monitors = self._define_list(monitors, WorkspaceMonitors)
        if apis is not None:
            self.apis = self._define_list(apis, WorkspaceApis)


@JsonMap({})
class GetWorkspaceOkResponse(BaseModel):
    """GetWorkspaceOkResponse

    :param workspace: Information about the workspace., defaults to None
    :type workspace: GetWorkspaceOkResponseWorkspace, optional
    """

    def __init__(self, workspace: GetWorkspaceOkResponseWorkspace = None):
        if workspace is not None:
            self.workspace = self._define_object(
                workspace, GetWorkspaceOkResponseWorkspace
            )
