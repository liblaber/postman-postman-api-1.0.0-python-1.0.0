from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .global_variable import GlobalVariable


@JsonMap({})
class GetWorkspaceGlobalVariablesOkResponse(BaseModel):
    """Information about the workspace's global variables.

    :param values: A list of the workspace's global variables., defaults to None
    :type values: List[GlobalVariable], optional
    """

    def __init__(self, values: List[GlobalVariable] = None):
        if values is not None:
            self.values = self._define_list(values, GlobalVariable)
