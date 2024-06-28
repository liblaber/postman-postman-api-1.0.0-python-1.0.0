<<<<<<< HEAD
=======
# This file was generated by liblab | https://liblab.com/

>>>>>>> 95da91c (initial commit)
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"delete_source": "deleteSource"})
class MergeEnvironmentForkRequest(BaseModel):
    """MergeEnvironmentForkRequest

    :param source: The source environment's unique ID to merge data from.
    :type source: str
    :param delete_source: If true, the forked environment will be deleted., defaults to None
    :type delete_source: bool, optional
    """

    def __init__(self, source: str, delete_source: bool = None):
        self.source = source
        if delete_source is not None:
            self.delete_source = delete_source
