from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class GetCollectionFolderOkResponse(BaseModel):
    """GetCollectionFolderOkResponse

    :param model_id: The folder's ID., defaults to None
    :type model_id: str, optional
    :param meta: A Postman-specific response that contains information about the internal performed operation., defaults to None
    :type meta: dict, optional
    :param data: Information about the folder. For a complete list of properties, refer to the `definitions.folder` property in the [collection.json schema file](https://schema.postman.com/collection/json/v1.0.0/draft-07/collection.json)., defaults to None
    :type data: dict, optional
    """

    def __init__(self, model_id: str = None, meta: dict = None, data: dict = None):
        if model_id is not None:
            self.model_id = model_id
        if meta is not None:
            self.meta = meta
        if data is not None:
            self.data = data
