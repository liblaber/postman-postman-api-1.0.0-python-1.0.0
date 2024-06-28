<<<<<<< HEAD
=======
# This file was generated by liblab | https://liblab.com/

>>>>>>> 95da91c (initial commit)
from __future__ import annotations
from typing import Union
from .base import OneOfBaseModel
from .json_schema import JsonSchema
from .json_stringified import JsonStringified


class ImportOpenApiDefinitionRequestGuard(OneOfBaseModel):
    class_list = {"JsonSchema": JsonSchema, "JsonStringified": JsonStringified}


ImportOpenApiDefinitionRequest = Union[JsonSchema, JsonStringified]
