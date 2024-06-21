from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({"id_": "id", "webhook_url": "webhookUrl"})
class CreateWebhookOkResponseWebhook(BaseModel):
    """CreateWebhookOkResponseWebhook

    :param id_: The webhook's ID., defaults to None
    :type id_: str, optional
    :param name: The webhook's name., defaults to None
    :type name: str, optional
    :param collection: The unique ID of the collection that triggers when calling this webhook., defaults to None
    :type collection: str, optional
    :param webhook_url: The webhook's URL., defaults to None
    :type webhook_url: str, optional
    :param uid: The webhook's unique ID., defaults to None
    :type uid: str, optional
    """

    def __init__(
        self,
        id_: str = None,
        name: str = None,
        collection: str = None,
        webhook_url: str = None,
        uid: str = None,
    ):
        if id_ is not None:
            self.id_ = id_
        if name is not None:
            self.name = name
        if collection is not None:
            self.collection = collection
        if webhook_url is not None:
            self.webhook_url = webhook_url
        if uid is not None:
            self.uid = uid


@JsonMap({})
class CreateWebhookOkResponse(BaseModel):
    """CreateWebhookOkResponse

    :param webhook: webhook, defaults to None
    :type webhook: CreateWebhookOkResponseWebhook, optional
    """

    def __init__(self, webhook: CreateWebhookOkResponseWebhook = None):
        if webhook is not None:
            self.webhook = self._define_object(webhook, CreateWebhookOkResponseWebhook)
