from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .invoice_data import InvoiceData


@JsonMap({})
class GetAccountInvoicesOkResponse(BaseModel):
    """GetAccountInvoicesOkResponse

    :param data: data
    :type data: List[InvoiceData]
    """

    def __init__(self, data: List[InvoiceData]):
        self.data = self._define_list(data, InvoiceData)
