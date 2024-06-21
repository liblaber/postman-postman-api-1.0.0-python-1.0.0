from enum import Enum
from .utils.json_map import JsonMap
from .base import BaseModel


class UpdateDetectedSecretResolutionsRequestResolution(Enum):
    """An enumeration representing different categories.

    :cvar FALSE_POSITIVE: "FALSE_POSITIVE"
    :vartype FALSE_POSITIVE: str
    :cvar REVOKED: "REVOKED"
    :vartype REVOKED: str
    :cvar ACCEPTED_RISK: "ACCEPTED_RISK"
    :vartype ACCEPTED_RISK: str
    """

    FALSE_POSITIVE = "FALSE_POSITIVE"
    REVOKED = "REVOKED"
    ACCEPTED_RISK = "ACCEPTED_RISK"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                UpdateDetectedSecretResolutionsRequestResolution._member_map_.values(),
            )
        )


@JsonMap({"workspace_id": "workspaceId"})
class UpdateDetectedSecretResolutionsRequest(BaseModel):
    """UpdateDetectedSecretResolutionsRequest

    :param resolution: The secret's updated resolution status:<br/>- `FALSE_POSITIVE` — The discovered secret is not an actual secret.<br/>- `REVOKED` — The secret is valid, but the user rotated their key to resolve the issue.<br/>- `ACCEPTED_RISK` — The Secret Scanner found the secret, but user accepts the risk of publishing it.<br/>
    :type resolution: UpdateDetectedSecretResolutionsRequestResolution
    :param workspace_id: The ID of the workspace that contains the secret.
    :type workspace_id: str
    """

    def __init__(
        self,
        resolution: UpdateDetectedSecretResolutionsRequestResolution,
        workspace_id: str,
    ):
        self.resolution = self._enum_matching(
            resolution,
            UpdateDetectedSecretResolutionsRequestResolution.list(),
            "resolution",
        )
        self.workspace_id = workspace_id
