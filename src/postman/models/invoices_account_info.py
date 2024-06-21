from enum import Enum
from .utils.json_map import JsonMap
from .base import BaseModel


class SalesChannel(Enum):
    """An enumeration representing different categories.

    :cvar SELF_SERVE: "SELF_SERVE"
    :vartype SELF_SERVE: str
    :cvar SALES_SERVE: "SALES_SERVE"
    :vartype SALES_SERVE: str
    """

    SELF_SERVE = "SELF_SERVE"
    SALES_SERVE = "SALES_SERVE"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, SalesChannel._member_map_.values()))


@JsonMap({})
class Slots(BaseModel):
    """Information about the team's slots.

    :param available: The number of the team's available slots., defaults to None
    :type available: int, optional
    :param consumed: The number of currently-billed team members., defaults to None
    :type consumed: int, optional
    :param total: The total number of slots available to the team., defaults to None
    :type total: int, optional
    :param unbilled: The number of unbilled slots if [auto-flex billing](https://learning.postman.com/auto-flex-policy/) is available., defaults to None
    :type unbilled: int, optional
    """

    def __init__(
        self,
        available: int = None,
        consumed: int = None,
        total: int = None,
        unbilled: int = None,
    ):
        if available is not None:
            self.available = available
        if consumed is not None:
            self.consumed = consumed
        if total is not None:
            self.total = total
        if unbilled is not None:
            self.unbilled = unbilled


@JsonMap(
    {
        "billing_email": "billingEmail",
        "id_": "id",
        "team_id": "teamId",
        "sales_channel": "salesChannel",
    }
)
class InvoicesAccountInfo(BaseModel):
    """Information about the account.

    :param billing_email: The email address to which invoices are sent., defaults to None
    :type billing_email: str, optional
    :param id_: The account's ID., defaults to None
    :type id_: int, optional
    :param state: The account's current state:<br/>- `FREE`<br/>- `PAID`<br/>- `EXPIRED_TRIAL`<br/>- `OVERDUE`<br/>- `SUSPENDED`<br/>- `BLOCKED`<br/>- `PAYMENT_DISPUTED`<br/>, defaults to None
    :type state: str, optional
    :param team_id: The team's ID associated with the account., defaults to None
    :type team_id: int, optional
    :param sales_channel: The sales channel from which the account was created:<br/>- `SELF_SERVE` — The user purchased the account plan.<br/>- `SALES_SERVE` — The account was purchased through the Postman sales team process.<br/>, defaults to None
    :type sales_channel: SalesChannel, optional
    :param slots: Information about the team's slots., defaults to None
    :type slots: Slots, optional
    """

    def __init__(
        self,
        billing_email: str = None,
        id_: int = None,
        state: str = None,
        team_id: int = None,
        sales_channel: SalesChannel = None,
        slots: Slots = None,
    ):
        if billing_email is not None:
            self.billing_email = billing_email
        if id_ is not None:
            self.id_ = id_
        if state is not None:
            self.state = state
        if team_id is not None:
            self.team_id = team_id
        if sales_channel is not None:
            self.sales_channel = self._enum_matching(
                sales_channel, SalesChannel.list(), "sales_channel"
            )
        if slots is not None:
            self.slots = self._define_object(slots, Slots)
