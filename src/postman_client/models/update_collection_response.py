# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class UpdateCollectionResponse(BaseModel):
    """UpdateCollectionResponse

    :param data: Information about the updated response. For a complete list of request properties, refer to the `definitions.request` property in the [collection.json schema file](https://schema.postman.com/collection/json/v1.0.0/draft-07/collection.json)., defaults to None
    :type data: dict, optional
    :param meta: A Postman-specific response that contains information about the internal performed operation., defaults to None
    :type meta: dict, optional
    :param model_id: The request's ID., defaults to None
    :type model_id: str, optional
    """

    def __init__(self, data: dict = None, meta: dict = None, model_id: str = None):
        """UpdateCollectionResponse

        :param data: Information about the updated response. For a complete list of request properties, refer to the `definitions.request` property in the [collection.json schema file](https://schema.postman.com/collection/json/v1.0.0/draft-07/collection.json)., defaults to None
        :type data: dict, optional
        :param meta: A Postman-specific response that contains information about the internal performed operation., defaults to None
        :type meta: dict, optional
        :param model_id: The request's ID., defaults to None
        :type model_id: str, optional
        """
        if data is not None:
            self.data = data
        if meta is not None:
            self.meta = meta
        if model_id is not None:
            self.model_id = model_id
