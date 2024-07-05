# This file was generated by liblab | https://liblab.com/

from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


class DataResourceType(Enum):
    """An enumeration representing different categories.

    :cvar COLLECTION: "collection"
    :vartype COLLECTION: str
    :cvar FOLDER: "folder"
    :vartype FOLDER: str
    :cvar REQUEST: "request"
    :vartype REQUEST: str
    :cvar EXAMPLE: "example"
    :vartype EXAMPLE: str
    :cvar ENVIRONMENT: "environment"
    :vartype ENVIRONMENT: str
    :cvar GLOBALS: "globals"
    :vartype GLOBALS: str
    :cvar API: "api"
    :vartype API: str
    """

    COLLECTION = "collection"
    FOLDER = "folder"
    REQUEST = "request"
    EXAMPLE = "example"
    ENVIRONMENT = "environment"
    GLOBALS = "globals"
    API = "api"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, DataResourceType._member_map_.values()))


@JsonMap(
    {
        "is_resource_deleted": "isResourceDeleted",
        "leaked_by": "leakedBy",
        "parent_resource_id": "parentResourceId",
        "resource_id": "resourceId",
        "resource_type": "resourceType",
        "detected_at": "detectedAt",
    }
)
class GetSecretsLocationsData(BaseModel):
    """Information about the secret finding locations.

    :param is_resource_deleted: If true, the resource in which the secret was found was deleted., defaults to None
    :type is_resource_deleted: bool, optional
    :param leaked_by: The ID of the user who exposed the secret., defaults to None
    :type leaked_by: int, optional
    :param location: The location where the secret was found., defaults to None
    :type location: str, optional
    :param occurrences: The number of times the secret occurs in the location., defaults to None
    :type occurrences: int, optional
    :param parent_resource_id: The parent resource's unique ID. If the resource is a request, folder, or example, this value is a collection ID. If the resource is a collection, globals, or environment, this is the resource's ID., defaults to None
    :type parent_resource_id: str, optional
    :param resource_id: The unique ID of the resource where the secret was detected., defaults to None
    :type resource_id: str, optional
    :param resource_type: The type of resource in which the secret was detected., defaults to None
    :type resource_type: DataResourceType, optional
    :param detected_at: The date and time at which the secret was detected., defaults to None
    :type detected_at: str, optional
    :param url: The URL to the resource that contains the secret., defaults to None
    :type url: str, optional
    """

    def __init__(
        self,
        is_resource_deleted: bool = None,
        leaked_by: int = None,
        location: str = None,
        occurrences: int = None,
        parent_resource_id: str = None,
        resource_id: str = None,
        resource_type: DataResourceType = None,
        detected_at: str = None,
        url: str = None,
    ):
        if is_resource_deleted is not None:
            self.is_resource_deleted = is_resource_deleted
        if leaked_by is not None:
            self.leaked_by = leaked_by
        if location is not None:
            self.location = location
        if occurrences is not None:
            self.occurrences = occurrences
        if parent_resource_id is not None:
            self.parent_resource_id = parent_resource_id
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_type is not None:
            self.resource_type = self._enum_matching(
                resource_type, DataResourceType.list(), "resource_type"
            )
        if detected_at is not None:
            self.detected_at = detected_at
        if url is not None:
            self.url = url


class ActivityFeedStatus(Enum):
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
        return list(map(lambda x: x.value, ActivityFeedStatus._member_map_.values()))


@JsonMap({"resolved_at": "resolvedAt", "resolved_by": "resolvedBy"})
class ActivityFeed(BaseModel):
    """ActivityFeed

    :param resolved_at: The date and time at which the resolution status was last updated., defaults to None
    :type resolved_at: str, optional
    :param resolved_by: The ID of the user that updated the secret's resolution status., defaults to None
    :type resolved_by: int, optional
    :param status: The secret's current resolution status:<br>- `ACTIVE` — The secret is active.<br>- `FALSE_POSITIVE` — The discovered secret is not an actual secret.<br>- `REVOKED` — The secret is valid, but the user rotated their key to resolve the issue.<br>- `ACCEPTED_RISK` — The Secret Scanner found the secret, but user accepts the risk of publishing it.<br>, defaults to None
    :type status: ActivityFeedStatus, optional
    """

    def __init__(
        self,
        resolved_at: str = None,
        resolved_by: int = None,
        status: ActivityFeedStatus = None,
    ):
        if resolved_at is not None:
            self.resolved_at = resolved_at
        if resolved_by is not None:
            self.resolved_by = resolved_by
        if status is not None:
            self.status = self._enum_matching(
                status, ActivityFeedStatus.list(), "status"
            )


@JsonMap(
    {
        "activity_feed": "activityFeed",
        "next_cursor": "nextCursor",
        "obfuscated_secret": "obfuscatedSecret",
        "secret_hash": "secretHash",
        "secret_type": "secretType",
    }
)
class GetSecretsLocationsMeta(BaseModel):
    """GetSecretsLocationsMeta

    :param activity_feed: The history of the secret's resolution status changes., defaults to None
    :type activity_feed: List[ActivityFeed], optional
    :param cursor: The pointer to the first record of the set of paginated results., defaults to None
    :type cursor: str, optional
    :param limit: The maximum number of rows to return in the response., defaults to None
    :type limit: int, optional
    :param next_cursor: The Base64-encoded value that points to the next record in the results set., defaults to None
    :type next_cursor: str, optional
    :param obfuscated_secret: The secret's obfuscated value., defaults to None
    :type obfuscated_secret: str, optional
    :param secret_hash: The secret's SHA-256 hash., defaults to None
    :type secret_hash: str, optional
    :param secret_type: The type of thesecret., defaults to None
    :type secret_type: str, optional
    :param total: The total number of discovered secret locations., defaults to None
    :type total: int, optional
    """

    def __init__(
        self,
        activity_feed: List[ActivityFeed] = None,
        cursor: str = None,
        limit: int = None,
        next_cursor: str = None,
        obfuscated_secret: str = None,
        secret_hash: str = None,
        secret_type: str = None,
        total: int = None,
    ):
        if activity_feed is not None:
            self.activity_feed = self._define_list(activity_feed, ActivityFeed)
        if cursor is not None:
            self.cursor = cursor
        if limit is not None:
            self.limit = limit
        if next_cursor is not None:
            self.next_cursor = next_cursor
        if obfuscated_secret is not None:
            self.obfuscated_secret = obfuscated_secret
        if secret_hash is not None:
            self.secret_hash = secret_hash
        if secret_type is not None:
            self.secret_type = secret_type
        if total is not None:
            self.total = total


@JsonMap({})
class GetSecretsLocations(BaseModel):
    """GetSecretsLocations

    :param data: data, defaults to None
    :type data: List[GetSecretsLocationsData], optional
    :param meta: meta, defaults to None
    :type meta: GetSecretsLocationsMeta, optional
    """

    def __init__(
        self,
        data: List[GetSecretsLocationsData] = None,
        meta: GetSecretsLocationsMeta = None,
    ):
        if data is not None:
            self.data = self._define_list(data, GetSecretsLocationsData)
        if meta is not None:
            self.meta = self._define_object(meta, GetSecretsLocationsMeta)
