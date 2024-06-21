from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id"})
class DeleteCollectionResponseOkResponseData(BaseModel):
    """The response's information.

    :param id_: The response's ID., defaults to None
    :type id_: str, optional
    :param owner: The user ID of the request's owner., defaults to None
    :type owner: str, optional
    """

    def __init__(self, id_: str = None, owner: str = None):
        if id_ is not None:
            self.id_ = id_
        if owner is not None:
            self.owner = owner


@JsonMap({})
class DeleteCollectionResponseOkResponse(BaseModel):
    """DeleteCollectionResponseOkResponse

    :param model_id: The response's ID., defaults to None
    :type model_id: str, optional
    :param meta: A Postman-specific response that contains information about the internal performed operation., defaults to None
    :type meta: dict, optional
    :param data: The response's information., defaults to None
    :type data: DeleteCollectionResponseOkResponseData, optional
    :param revision: An internal revision ID. Its value increments each time the resource changes. You can use this ID to track whether there were changes since the last time you fetched the resource., defaults to None
    :type revision: float, optional
    """

    def __init__(
        self,
        model_id: str = None,
        meta: dict = None,
        data: DeleteCollectionResponseOkResponseData = None,
        revision: float = None,
    ):
        if model_id is not None:
            self.model_id = model_id
        if meta is not None:
            self.meta = meta
        if data is not None:
            self.data = self._define_object(
                data, DeleteCollectionResponseOkResponseData
            )
        if revision is not None:
            self.revision = revision
