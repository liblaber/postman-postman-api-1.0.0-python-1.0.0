from __future__ import annotations
from typing import Union
from .base import OneOfBaseModel
from .pan_element_created import PanElementCreated
from .pan_folder_created import PanFolderCreated


class PostPanElementOrFolderCreatedResponseGuard(OneOfBaseModel):
    class_list = {
        "PanElementCreated": PanElementCreated,
        "PanFolderCreated": PanFolderCreated,
    }


PostPanElementOrFolderCreatedResponse = Union[PanElementCreated, PanFolderCreated]
