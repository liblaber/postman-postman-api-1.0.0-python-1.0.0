from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


class DataResolution(Enum):
    """An enumeration representing different categories.

    :cvar FALSE_POSITIVE: "FALSE_POSITIVE"
    :vartype FALSE_POSITIVE: str
    :cvar ACCEPTED_RISK: "ACCEPTED_RISK"
    :vartype ACCEPTED_RISK: str
    :cvar REVOKED: "REVOKED"
    :vartype REVOKED: str
    :cvar ACTIVE: "ACTIVE"
    :vartype ACTIVE: str
    """

    FALSE_POSITIVE = "FALSE_POSITIVE"
    ACCEPTED_RISK = "ACCEPTED_RISK"
    REVOKED = "REVOKED"
    ACTIVE = "ACTIVE"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, DataResolution._member_map_.values()))


class DataWorkspaceVisibility(Enum):
    """An enumeration representing different categories.

    :cvar PERSONAL: "personal"
    :vartype PERSONAL: str
    :cvar PRIVATE: "private"
    :vartype PRIVATE: str
    :cvar TEAM: "team"
    :vartype TEAM: str
    :cvar PUBLIC: "public"
    :vartype PUBLIC: str
    """

    PERSONAL = "personal"
    PRIVATE = "private"
    TEAM = "team"
    PUBLIC = "public"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, DataWorkspaceVisibility._member_map_.values())
        )


@JsonMap(
    {
        "obfuscated_secret": "obfuscatedSecret",
        "secret_hash": "secretHash",
        "secret_id": "secretId",
        "secret_type": "secretType",
        "detected_at": "detectedAt",
        "workspace_id": "workspaceId",
        "workspace_visibility": "workspaceVisibility",
    }
)
class DetectedSecretsQueriesOkResponseData(BaseModel):
    """Information about the secret finding.

    :param obfuscated_secret: The secret's obfuscated value., defaults to None
    :type obfuscated_secret: str, optional
    :param occurrences: The number of times the secret was found in the workspace., defaults to None
    :type occurrences: float, optional
    :param resolution: The secret's current status:<br/>- `ACTIVE` — The secret is active.<br/>- `FALSE_POSITIVE` — The discovered secret is not an actual secret.<br/>- `REVOKED` — The secret is valid, but the user rotated their key to resolve the issue.<br/>- `ACCEPTED_RISK` — The Secret Scanner found the secret, but user accepts the risk of publishing it.<br/>, defaults to None
    :type resolution: DataResolution, optional
    :param secret_hash: The SHA-256 hash of the detected secret., defaults to None
    :type secret_hash: str, optional
    :param secret_id: The detected secret's ID., defaults to None
    :type secret_id: str, optional
    :param secret_type: The type of the secret., defaults to None
    :type secret_type: str, optional
    :param detected_at: The date and time at which the secret was first detected., defaults to None
    :type detected_at: str, optional
    :param workspace_id: The ID of the workspace that contains the secret., defaults to None
    :type workspace_id: str, optional
    :param workspace_visibility: The workspace's [visibility setting](https://learning.postman.com/docs/collaborating-in-postman/using-workspaces/managing-workspaces/#changing-workspace-visibility)., defaults to None
    :type workspace_visibility: DataWorkspaceVisibility, optional
    """

    def __init__(
        self,
        obfuscated_secret: str = None,
        occurrences: float = None,
        resolution: DataResolution = None,
        secret_hash: str = None,
        secret_id: str = None,
        secret_type: str = None,
        detected_at: str = None,
        workspace_id: str = None,
        workspace_visibility: DataWorkspaceVisibility = None,
    ):
        if obfuscated_secret is not None:
            self.obfuscated_secret = obfuscated_secret
        if occurrences is not None:
            self.occurrences = occurrences
        if resolution is not None:
            self.resolution = self._enum_matching(
                resolution, DataResolution.list(), "resolution"
            )
        if secret_hash is not None:
            self.secret_hash = secret_hash
        if secret_id is not None:
            self.secret_id = secret_id
        if secret_type is not None:
            self.secret_type = secret_type
        if detected_at is not None:
            self.detected_at = detected_at
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if workspace_visibility is not None:
            self.workspace_visibility = self._enum_matching(
                workspace_visibility,
                DataWorkspaceVisibility.list(),
                "workspace_visibility",
            )


@JsonMap({"next_cursor": "nextCursor"})
class DetectedSecretsQueriesOkResponseMeta(BaseModel):
    """The response's meta information for paginated results.

    :param limit: The maximum number of records in the paginated response., defaults to None
    :type limit: float, optional
    :param next_cursor: The pagination cursor that points to the next record in the results set., defaults to None
    :type next_cursor: str, optional
    :param total: The number of records that match the defined criteria. This will only be present if the `include` query parameter is specified with the `meta.total` value., defaults to None
    :type total: float, optional
    """

    def __init__(
        self, limit: float = None, next_cursor: str = None, total: float = None
    ):
        if limit is not None:
            self.limit = limit
        if next_cursor is not None:
            self.next_cursor = next_cursor
        if total is not None:
            self.total = total


@JsonMap({})
class DetectedSecretsQueriesOkResponse(BaseModel):
    """DetectedSecretsQueriesOkResponse

    :param data: data, defaults to None
    :type data: List[DetectedSecretsQueriesOkResponseData], optional
    :param meta: The response's meta information for paginated results., defaults to None
    :type meta: DetectedSecretsQueriesOkResponseMeta, optional
    """

    def __init__(
        self,
        data: List[DetectedSecretsQueriesOkResponseData] = None,
        meta: DetectedSecretsQueriesOkResponseMeta = None,
    ):
        if data is not None:
            self.data = self._define_list(data, DetectedSecretsQueriesOkResponseData)
        if meta is not None:
            self.meta = self._define_object(meta, DetectedSecretsQueriesOkResponseMeta)
