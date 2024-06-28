<<<<<<< HEAD
=======
# This file was generated by liblab | https://liblab.com/

>>>>>>> 95da91c (initial commit)
from __future__ import annotations
from typing import Union
from .base import OneOfBaseModel
from .pan_create_api import PanCreateApi
from .pan_create_collection import PanCreateCollection
from .pan_create_workspace import PanCreateWorkspace
from .pan_create_folder import PanCreateFolder


class PostPanElementOrFolderRequestGuard(OneOfBaseModel):
    class_list = {
        "PanCreateApi": PanCreateApi,
        "PanCreateCollection": PanCreateCollection,
        "PanCreateWorkspace": PanCreateWorkspace,
        "PanCreateFolder": PanCreateFolder,
    }


PostPanElementOrFolderRequest = Union[
    PanCreateApi, PanCreateCollection, PanCreateWorkspace, PanCreateFolder
]
