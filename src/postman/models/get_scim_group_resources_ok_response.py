<<<<<<< HEAD
=======
# This file was generated by liblab | https://liblab.com/

>>>>>>> 95da91c (initial commit)
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .scim_group_resource import ScimGroupResource


@JsonMap(
    {
        "resources": "Resources",
        "items_per_page": "itemsPerPage",
        "start_index": "startIndex",
        "total_results": "totalResults",
    }
)
class GetScimGroupResourcesOkResponse(BaseModel):
    """GetScimGroupResourcesOkResponse

    :param resources: A list of group resources., defaults to None
    :type resources: List[ScimGroupResource], optional
    :param items_per_page: The number of items per response page., defaults to None
    :type items_per_page: float, optional
    :param schemas: schemas, defaults to None
    :type schemas: List[str], optional
    :param start_index: The index entry by which the returned results begin., defaults to None
    :type start_index: float, optional
    :param total_results: The total number of results found., defaults to None
    :type total_results: float, optional
    """

    def __init__(
        self,
        resources: List[ScimGroupResource] = None,
        items_per_page: float = None,
        schemas: List[str] = None,
        start_index: float = None,
        total_results: float = None,
    ):
        if resources is not None:
            self.resources = self._define_list(resources, ScimGroupResource)
        if items_per_page is not None:
            self.items_per_page = items_per_page
        if schemas is not None:
            self.schemas = schemas
        if start_index is not None:
            self.start_index = start_index
        if total_results is not None:
            self.total_results = total_results
