from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class SchemaSecurityValidationOkResponse(BaseModel):
    """SchemaSecurityValidationOkResponse

    :param warnings: Information about each issue discovered in the analysis. Each object includes the violation's severity and category, the location of the issue, data paths, and other information. This returns an empty object if there are no issues present in the schema.<br/><br/>If there are issues, this returns the `possibleFixUrl` response in each warning object. This provides a link to documentation you can use to resolve the warning.<br/>, defaults to None
    :type warnings: List[dict], optional
    """

    def __init__(self, warnings: List[dict] = None):
        if warnings is not None:
            self.warnings = warnings
