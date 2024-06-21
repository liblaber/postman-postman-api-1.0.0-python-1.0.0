from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id"})
class DeletePanElementOrFolderOkResponseElementType(BaseModel):
    """The Private API Network element type. The name of the object is the element `api`, `collection`, `workspace`, or `folder` type.

    :param id_: The element's ID., defaults to None
    :type id_: str, optional
    """

    def __init__(self, id_: str = None):
        if id_ is not None:
            self.id_ = id_


@JsonMap({"element_type": "elementType"})
class DeletePanElementOrFolderOkResponse(BaseModel):
    """DeletePanElementOrFolderOkResponse

    :param element_type: The Private API Network element type. The name of the object is the element `api`, `collection`, `workspace`, or `folder` type., defaults to None
    :type element_type: DeletePanElementOrFolderOkResponseElementType, optional
    """

    def __init__(
        self, element_type: DeletePanElementOrFolderOkResponseElementType = None
    ):
        if element_type is not None:
            self.element_type = self._define_object(
                element_type, DeletePanElementOrFolderOkResponseElementType
            )
