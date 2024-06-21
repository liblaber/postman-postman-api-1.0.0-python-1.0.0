from __future__ import annotations
from typing import Union
from .base import OneOfBaseModel
from .update_pan_api import UpdatePanApi
from .update_pan_collection import UpdatePanCollection
from .update_pan_workspace import UpdatePanWorkspace
from .update_pan_folder import UpdatePanFolder


class UpdatePanElementOrFolderRequestGuard(OneOfBaseModel):
    class_list = {
        "UpdatePanApi": UpdatePanApi,
        "UpdatePanCollection": UpdatePanCollection,
        "UpdatePanWorkspace": UpdatePanWorkspace,
        "UpdatePanFolder": UpdatePanFolder,
    }


UpdatePanElementOrFolderRequest = Union[
    UpdatePanApi, UpdatePanCollection, UpdatePanWorkspace, UpdatePanFolder
]
