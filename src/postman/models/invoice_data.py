from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class TotalAmount(BaseModel):
    """Information about the invoice's total billed amount.

    :param value: The amount billed., defaults to None
    :type value: int, optional
    :param currency: The currency of the billed amount. Currently only supports the `USD` value., defaults to None
    :type currency: str, optional
    """

    def __init__(self, value: int = None, currency: str = None):
        if value is not None:
            self.value = value
        if currency is not None:
            self.currency = currency


@JsonMap({})
class Web(BaseModel):
    """An object containing web-based account references.

    :param href: A URL where you can download the invoice in PDF and view details., defaults to None
    :type href: str, optional
    """

    def __init__(self, href: str = None):
        if href is not None:
            self.href = href


@JsonMap({})
class Links(BaseModel):
    """A [JSON API spec](https://jsonapi.org/format/#document-links) object containing hypermedia links.

    :param web: An object containing web-based account references., defaults to None
    :type web: Web, optional
    """

    def __init__(self, web: Web = None):
        if web is not None:
            self.web = self._define_object(web, Web)


@JsonMap({"id_": "id", "issued_at": "issuedAt", "total_amount": "totalAmount"})
class InvoiceData(BaseModel):
    """Information about the invoice.

    :param id_: The invoice's ID., defaults to None
    :type id_: str, optional
    :param status: The invoice's status., defaults to None
    :type status: str, optional
    :param issued_at: The date on which the invoice was issued., defaults to None
    :type issued_at: str, optional
    :param total_amount: Information about the invoice's total billed amount., defaults to None
    :type total_amount: TotalAmount, optional
    :param links: A [JSON API spec](https://jsonapi.org/format/#document-links) object containing hypermedia links., defaults to None
    :type links: Links, optional
    """

    def __init__(
        self,
        id_: str = None,
        status: str = None,
        issued_at: str = None,
        total_amount: TotalAmount = None,
        links: Links = None,
    ):
        if id_ is not None:
            self.id_ = id_
        if status is not None:
            self.status = status
        if issued_at is not None:
            self.issued_at = issued_at
        if total_amount is not None:
            self.total_amount = self._define_object(total_amount, TotalAmount)
        if links is not None:
            self.links = self._define_object(links, Links)
