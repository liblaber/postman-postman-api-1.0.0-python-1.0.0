# This file was generated by liblab | https://liblab.com/

from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


class Mode(Enum):
    """An enumeration representing different categories.

    :cvar COPY: "copy"
    :vartype COPY: str
    :cvar MOVE: "move"
    :vartype MOVE: str
    """

    COPY = "copy"
    MOVE = "move"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Mode._member_map_.values()))


class TargetModel(Enum):
    """An enumeration representing different categories.

    :cvar COLLECTION: "collection"
    :vartype COLLECTION: str
    :cvar FOLDER: "folder"
    :vartype FOLDER: str
    :cvar REQUEST: "request"
    :vartype REQUEST: str
    """

    COLLECTION = "collection"
    FOLDER = "folder"
    REQUEST = "request"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, TargetModel._member_map_.values()))


@JsonMap({"id_": "id"})
class Target(BaseModel):
    """Information about the item transfer's destination location.

    :param id_: The UID of the destination collection, folder, or request.
    :type id_: str
    :param model: The collection, folder, or request the items will be transferred to. For response transfers, use the `request` value.
    :type model: TargetModel
    """

    def __init__(self, id_: str, model: TargetModel):
        """Information about the item transfer's destination location.

        :param id_: The UID of the destination collection, folder, or request.
        :type id_: str
        :param model: The collection, folder, or request the items will be transferred to. For response transfers, use the `request` value.
        :type model: TargetModel
        """
        self.id_ = id_
        self.model = self._enum_matching(model, TargetModel.list(), "model")


class Position(Enum):
    """An enumeration representing different categories.

    :cvar START: "start"
    :vartype START: str
    :cvar END: "end"
    :vartype END: str
    :cvar BEFORE: "before"
    :vartype BEFORE: str
    :cvar AFTER: "after"
    :vartype AFTER: str
    """

    START = "start"
    END = "end"
    BEFORE = "before"
    AFTER = "after"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Position._member_map_.values()))


@JsonMap({"id_": "id"})
class Location(BaseModel):
    """The transferred items' placement in the target destination:
    - For `start` or `end` — Do not include the `model` and `id` values.
    - For `before` or `after` — Include the `model` and `id` properties.


    :param id_: For `before` or `after` positions, the model's UID., defaults to None
    :type id_: str, optional
    :param model: For `before` or `after` positions, the type of item (model) that the transferred item will be positioned by. One of: `folder`, `request`, or `response.` , defaults to None
    :type model: str, optional
    :param position: The transferred item's position within the destination object.
    :type position: Position
    """

    def __init__(self, position: Position, id_: str = None, model: str = None):
        """The transferred items' placement in the target destination:
        - For `start` or `end` — Do not include the `model` and `id` values.
        - For `before` or `after` — Include the `model` and `id` properties.


        :param id_: For `before` or `after` positions, the model's UID., defaults to None
        :type id_: str, optional
        :param model: For `before` or `after` positions, the type of item (model) that the transferred item will be positioned by. One of: `folder`, `request`, or `response.` , defaults to None
        :type model: str, optional
        :param position: The transferred item's position within the destination object.
        :type position: Position
        """
        if id_ is not None:
            self.id_ = self._define_str("id_", id_, nullable=True)
        if model is not None:
            self.model = self._define_str("model", model, nullable=True)
        self.position = self._enum_matching(position, Position.list(), "position")


@JsonMap({})
class TransferCollectionItems(BaseModel):
    """TransferCollectionItems

    :param ids: A list of collection request, response, or folder UIDs to transfer.
    :type ids: List[str]
    :param mode: The transfer operation to perform.
    :type mode: Mode
    :param target: Information about the item transfer's destination location.
    :type target: Target
    :param location: The transferred items' placement in the target destination: - For `start` or `end` — Do not include the `model` and `id` values. - For `before` or `after` — Include the `model` and `id` properties.
    :type location: Location
    """

    def __init__(self, ids: List[str], mode: Mode, target: Target, location: Location):
        """TransferCollectionItems

        :param ids: A list of collection request, response, or folder UIDs to transfer.
        :type ids: List[str]
        :param mode: The transfer operation to perform.
        :type mode: Mode
        :param target: Information about the item transfer's destination location.
        :type target: Target
        :param location: The transferred items' placement in the target destination: - For `start` or `end` — Do not include the `model` and `id` values. - For `before` or `after` — Include the `model` and `id` properties.
        :type location: Location
        """
        self.ids = ids
        self.mode = self._enum_matching(mode, Mode.list(), "mode")
        self.target = self._define_object(target, Target)
        self.location = self._define_object(location, Location)
