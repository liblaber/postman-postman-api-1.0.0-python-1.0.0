from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


class Statuses(Enum):
    """An enumeration representing different categories.

    :cvar FALSE_POSITIVE: "FALSE_POSITIVE"
    :vartype FALSE_POSITIVE: str
    :cvar ACCEPTED_RISK: "ACCEPTED_RISK"
    :vartype ACCEPTED_RISK: str
    :cvar REVOKED: "REVOKED"
    :vartype REVOKED: str
    """

    FALSE_POSITIVE = "FALSE_POSITIVE"
    ACCEPTED_RISK = "ACCEPTED_RISK"
    REVOKED = "REVOKED"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Statuses._member_map_.values()))


class WorkspaceVisiblities(Enum):
    """An enumeration representing different categories.

    :cvar TEAM: "team"
    :vartype TEAM: str
    :cvar PUBLIC: "public"
    :vartype PUBLIC: str
    """

    TEAM = "team"
    PUBLIC = "public"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, WorkspaceVisiblities._member_map_.values()))


@JsonMap(
    {
        "secret_types": "secretTypes",
        "workspace_ids": "workspaceIds",
        "workspace_visiblities": "workspaceVisiblities",
    }
)
class DetectedSecretsQueriesRequest(BaseModel):
    """DetectedSecretsQueriesRequest

    :param resolved: If true, return secrets with a `resolved` status., defaults to None
    :type resolved: bool, optional
    :param secret_types: A list of secrets types to query. For a list of valid IDs, use the GET `/secret-types` endpoint., defaults to None
    :type secret_types: List[str], optional
    :param statuses: A list of the types of resolution statuses to query., defaults to None
    :type statuses: List[Statuses], optional
    :param workspace_ids: A list of workspaces IDs to query., defaults to None
    :type workspace_ids: List[str], optional
    :param workspace_visiblities: A list of workspace [visibility settings](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/managing-workspaces/#changing-workspace-visibility) to query. This currently supports the `team` and `public` settings., defaults to None
    :type workspace_visiblities: List[WorkspaceVisiblities], optional
    """

    def __init__(
        self,
        resolved: bool = None,
        secret_types: List[str] = None,
        statuses: List[Statuses] = None,
        workspace_ids: List[str] = None,
        workspace_visiblities: List[WorkspaceVisiblities] = None,
    ):
        if resolved is not None:
            self.resolved = resolved
        if secret_types is not None:
            self.secret_types = secret_types
        if statuses is not None:
            self.statuses = self._define_list(statuses, Statuses)
        if workspace_ids is not None:
            self.workspace_ids = workspace_ids
        if workspace_visiblities is not None:
            self.workspace_visiblities = self._define_list(
                workspace_visiblities, WorkspaceVisiblities
            )
