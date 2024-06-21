from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"task_id": "taskId"})
class SyncCollectionWithSchemaAcceptedResponse(BaseModel):
    """SyncCollectionWithSchemaAcceptedResponse

    :param task_id: The created task ID. You can use this ID to track the status of syncing an API collection with an API schema., defaults to None
    :type task_id: str, optional
    """

    def __init__(self, task_id: str = None):
        if task_id is not None:
            self.task_id = task_id
