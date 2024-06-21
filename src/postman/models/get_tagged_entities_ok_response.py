from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


class EntitiesEntityType(Enum):
    """An enumeration representing different categories.

    :cvar API: "api"
    :vartype API: str
    :cvar COLLECTION: "collection"
    :vartype COLLECTION: str
    :cvar WORKSPACE: "workspace"
    :vartype WORKSPACE: str
    """

    API = "api"
    COLLECTION = "collection"
    WORKSPACE = "workspace"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, EntitiesEntityType._member_map_.values()))


@JsonMap({"entity_id": "entityId", "entity_type": "entityType"})
class Entities(BaseModel):
    """Entities

    :param entity_id: The element's unique ID., defaults to None
    :type entity_id: str, optional
    :param entity_type: The type of Postman element., defaults to None
    :type entity_type: EntitiesEntityType, optional
    """

    def __init__(self, entity_id: str = None, entity_type: EntitiesEntityType = None):
        if entity_id is not None:
            self.entity_id = entity_id
        if entity_type is not None:
            self.entity_type = self._enum_matching(
                entity_type, EntitiesEntityType.list(), "entity_type"
            )


@JsonMap({})
class GetTaggedEntitiesOkResponseData(BaseModel):
    """An object containing the paginated elements.

    :param entities: A list of the Postman elements that contain the given tag.
    :type entities: List[Entities]
    """

    def __init__(self, entities: List[Entities]):
        self.entities = self._define_list(entities, Entities)


@JsonMap({"next_cursor": "nextCursor"})
class GetTaggedEntitiesOkResponseMeta(BaseModel):
    """The response's pagination information.

    :param count: The number of tagged elements returned in the response.
    :type count: int
    :param next_cursor: The pagination cursor that points to the next record in the results set., defaults to None
    :type next_cursor: str, optional
    """

    def __init__(self, count: int, next_cursor: str = None):
        self.count = count
        if next_cursor is not None:
            self.next_cursor = next_cursor


@JsonMap({})
class GetTaggedEntitiesOkResponse(BaseModel):
    """GetTaggedEntitiesOkResponse

    :param data: An object containing the paginated elements., defaults to None
    :type data: GetTaggedEntitiesOkResponseData, optional
    :param meta: The response's pagination information., defaults to None
    :type meta: GetTaggedEntitiesOkResponseMeta, optional
    """

    def __init__(
        self,
        data: GetTaggedEntitiesOkResponseData = None,
        meta: GetTaggedEntitiesOkResponseMeta = None,
    ):
        if data is not None:
            self.data = self._define_object(data, GetTaggedEntitiesOkResponseData)
        if meta is not None:
            self.meta = self._define_object(meta, GetTaggedEntitiesOkResponseMeta)
