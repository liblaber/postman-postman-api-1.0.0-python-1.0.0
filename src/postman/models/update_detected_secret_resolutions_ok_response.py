from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


class HistoryResolution(Enum):
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
        return list(map(lambda x: x.value, HistoryResolution._member_map_.values()))


@JsonMap({"created_at": "createdAt"})
class History(BaseModel):
    """History

    :param actor: The ID of the user that updated the secret's resolution status., defaults to None
    :type actor: float, optional
    :param created_at: The date and time at which the resolution status was updated., defaults to None
    :type created_at: str, optional
    :param resolution: The secret's updated resolution status:<br/>- `ACTIVE` — The secret is active.<br/>- `FALSE_POSITIVE` — The discovered secret is not an actual secret.<br/>- `REVOKED` — The secret is valid, but the user rotated their key to resolve the issue.<br/>- `ACCEPTED_RISK` — The Secret Scanner found the secret, but user accepts the risk of publishing it.<br/>, defaults to None
    :type resolution: HistoryResolution, optional
    """

    def __init__(
        self,
        actor: float = None,
        created_at: str = None,
        resolution: HistoryResolution = None,
    ):
        if actor is not None:
            self.actor = actor
        if created_at is not None:
            self.created_at = created_at
        if resolution is not None:
            self.resolution = self._enum_matching(
                resolution, HistoryResolution.list(), "resolution"
            )


class UpdateDetectedSecretResolutionsOkResponseResolution(Enum):
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
        return list(
            map(
                lambda x: x.value,
                UpdateDetectedSecretResolutionsOkResponseResolution._member_map_.values(),
            )
        )


@JsonMap({"secret_hash": "secretHash", "workspace_id": "workspaceId"})
class UpdateDetectedSecretResolutionsOkResponse(BaseModel):
    """UpdateDetectedSecretResolutionsOkResponse

    :param history: The history of the secret's resolution status changes., defaults to None
    :type history: List[History], optional
    :param resolution: The secret's current resolution status:<br/>- `ACTIVE` — The secret is active.<br/>- `FALSE_POSITIVE` — The discovered secret is not an actual secret.<br/>- `REVOKED` — The secret is valid, but the user rotated their key to resolve the issue.<br/>- `ACCEPTED_RISK` — The Secret Scanner found the secret, but user accepts the risk of publishing it.<br/>, defaults to None
    :type resolution: UpdateDetectedSecretResolutionsOkResponseResolution, optional
    :param secret_hash: The SHA-256 hash of the detected secret., defaults to None
    :type secret_hash: str, optional
    :param workspace_id: The ID of the workspace that contains the secret., defaults to None
    :type workspace_id: str, optional
    """

    def __init__(
        self,
        history: List[History] = None,
        resolution: UpdateDetectedSecretResolutionsOkResponseResolution = None,
        secret_hash: str = None,
        workspace_id: str = None,
    ):
        if history is not None:
            self.history = self._define_list(history, History)
        if resolution is not None:
            self.resolution = self._enum_matching(
                resolution,
                UpdateDetectedSecretResolutionsOkResponseResolution.list(),
                "resolution",
            )
        if secret_hash is not None:
            self.secret_hash = secret_hash
        if workspace_id is not None:
            self.workspace_id = workspace_id
