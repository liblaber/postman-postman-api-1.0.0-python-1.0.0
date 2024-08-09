# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class CreateWebhookWebhook1(BaseModel):
    """CreateWebhookWebhook1

    :param collection: The unique ID of the collection to trigger when calling this webhook., defaults to None
    :type collection: str, optional
    :param name: The webhook's name. On success, the system creates a new monitor with this name in the **Monitors** tab., defaults to None
    :type name: str, optional
    """

    def __init__(self, collection: str = None, name: str = None):
        """CreateWebhookWebhook1

        :param collection: The unique ID of the collection to trigger when calling this webhook., defaults to None
        :type collection: str, optional
        :param name: The webhook's name. On success, the system creates a new monitor with this name in the **Monitors** tab., defaults to None
        :type name: str, optional
        """
        if collection is not None:
            self.collection = collection
        if name is not None:
            self.name = name


@JsonMap({})
class CreateWebhookRequest(BaseModel):
    """CreateWebhookRequest

    :param webhook: webhook, defaults to None
    :type webhook: CreateWebhookWebhook1, optional
    """

    def __init__(self, webhook: CreateWebhookWebhook1 = None):
        """CreateWebhookRequest

        :param webhook: webhook, defaults to None
        :type webhook: CreateWebhookWebhook1, optional
        """
        if webhook is not None:
            self.webhook = self._define_object(webhook, CreateWebhookWebhook1)
