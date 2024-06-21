from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models
from ..models.get_audit_logs_ok_response import GetAuditLogsOkResponse
from ..models.asc_desc_default_desc import AscDescDefaultDesc


class AuditLogsService(BaseService):

    @cast_models
    def get_audit_logs(
        self,
        since: str = None,
        until: str = None,
        limit: int = None,
        cursor: str = None,
        order_by: AscDescDefaultDesc = None,
    ) -> GetAuditLogsOkResponse:
        """Gets a list of your team's generated audit events. For a complete list of all audit events, read our [Utilizing audit logs](https://learning.postman.com/docs/administration/audit-logs/) documentation.

        :param since: Return logs created after the given time, in `YYYY-MM-DD` format., defaults to None
        :type since: str, optional
        :param until: Return logs created before the given time, in `YYYY-MM-DD` format., defaults to None
        :type until: str, optional
        :param limit: The maximum number of audit events to return at once., defaults to None
        :type limit: int, optional
        :param cursor: The pointer to the first record of the set of paginated results. To view the next response, use the `nextCursor` value for this parameter., defaults to None
        :type cursor: str, optional
        :param order_by: Return the records in ascending (`asc`) or descending (`desc`) order., defaults to None
        :type order_by: AscDescDefaultDesc, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful Response
        :rtype: GetAuditLogsOkResponse
        """

        Validator(str).is_optional().validate(since)
        Validator(str).is_optional().validate(until)
        Validator(int).is_optional().max(300).validate(limit)
        Validator(str).is_optional().validate(cursor)
        Validator(AscDescDefaultDesc).is_optional().validate(order_by)

        serialized_request = (
            Serializer(f"{self.base_url}/audit/logs", self.get_default_headers())
            .add_query("since", since)
            .add_query("until", until)
            .add_query("limit", limit)
            .add_query("cursor", cursor)
            .add_query("order_by", order_by)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return GetAuditLogsOkResponse._unmap(response)
