from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.invoices_account_info import InvoicesAccountInfo
from ..models.get_account_invoices_status import GetAccountInvoicesStatus
from ..models.get_account_invoices_ok_response import GetAccountInvoicesOkResponse


class BillingService(BaseService):

    @cast_models
    def get_accounts(self) -> InvoicesAccountInfo:
        """Gets Postman billing account details for the given team.

        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: InvoicesAccountInfo
        """

        serialized_request = (
            Serializer(f"{self.base_url}/accounts", self.get_default_headers())
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return InvoicesAccountInfo._unmap(response)

    @cast_models
    def get_account_invoices(
        self, account_id: str, status: GetAccountInvoicesStatus
    ) -> GetAccountInvoicesOkResponse:
        """Gets all invoices for a Postman billing account filtered by the status of the invoice.

        :param account_id: The account's ID.
        :type account_id: str
        :param status: The account's status.
        :type status: GetAccountInvoicesStatus
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: GetAccountInvoicesOkResponse
        """

        Validator(str).validate(account_id)
        Validator(GetAccountInvoicesStatus).validate(status)

        serialized_request = (
            Serializer(
                f"{self.base_url}/accounts/{{accountId}}/invoices",
                self.get_default_headers(),
            )
            .add_path("accountId", account_id)
            .add_query("status", status)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetAccountInvoicesOkResponse._unmap(response)
