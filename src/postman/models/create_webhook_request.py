from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class CreateWebhookRequestWebhook(BaseModel):
    """CreateWebhookRequestWebhook

    :param collection: The unique ID of the collection to trigger when calling this webhook., defaults to None
    :type collection: str, optional
    :param name: The webhook's name. On success, the system creates a new monitor with this name in the **Monitors** tab., defaults to None
    :type name: str, optional
    """

    def __init__(self, collection: str = None, name: str = None):
        if collection is not None:
            self.collection = collection
        if name is not None:
            self.name = name


@JsonMap({})
class CreateWebhookRequest(BaseModel):
    """CreateWebhookRequest

    :param webhook: webhook, defaults to None
    :type webhook: CreateWebhookRequestWebhook, optional
    """

    def __init__(self, webhook: CreateWebhookRequestWebhook = None):
        if webhook is not None:
            self.webhook = self._define_object(webhook, CreateWebhookRequestWebhook)
