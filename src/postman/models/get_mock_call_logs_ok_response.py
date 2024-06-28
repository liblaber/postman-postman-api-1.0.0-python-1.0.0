<<<<<<< HEAD
=======
# This file was generated by liblab | https://liblab.com/

>>>>>>> 95da91c (initial commit)
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel


@JsonMap({})
class RequestHeaders(BaseModel):
    """The request's headers.

    :param key: The request header's name., defaults to None
    :type key: str, optional
    :param value: The request header's value., defaults to None
    :type value: str, optional
    """

    def __init__(self, key: str = None, value: str = None):
        if key is not None:
            self.key = key
        if value is not None:
            self.value = value


@JsonMap({})
class RequestBody(BaseModel):
    """The request's body information.

    :param mode: The request body's media type (mode)., defaults to None
    :type mode: str, optional
    :param data: The request body's contents., defaults to None
    :type data: str, optional
    """

    def __init__(self, mode: str = None, data: str = None):
        if mode is not None:
            self.mode = mode
        if data is not None:
            self.data = data


@JsonMap({})
class CallLogsRequest(BaseModel):
    """The server response's request information.

    :param method: The request method., defaults to None
    :type method: str, optional
    :param path: The request's path., defaults to None
    :type path: str, optional
    :param headers: The request's headers., defaults to None
    :type headers: RequestHeaders, optional
    :param body: The request's body information., defaults to None
    :type body: RequestBody, optional
    """

    def __init__(
        self,
        method: str = None,
        path: str = None,
        headers: RequestHeaders = None,
        body: RequestBody = None,
    ):
        if method is not None:
            self.method = method
        if path is not None:
            self.path = path
        if headers is not None:
            self.headers = self._define_object(headers, RequestHeaders)
        if body is not None:
            self.body = self._define_object(body, RequestBody)


@JsonMap({"type_": "type"})
class Description(BaseModel):
    """The response header's description information.

    :param content: The response header description's content., defaults to None
    :type content: str, optional
    :param type_: The response header description's media type., defaults to None
    :type type_: str, optional
    """

    def __init__(self, content: str = None, type_: str = None):
        if content is not None:
            self.content = content
        if type_ is not None:
            self.type_ = type_


@JsonMap({})
class ResponseHeaders(BaseModel):
    """The response's headers.

    :param description: The response header's description information., defaults to None
    :type description: Description, optional
    :param key: The response header's name., defaults to None
    :type key: str, optional
    :param value: The response header's value., defaults to None
    :type value: str, optional
    """

    def __init__(
        self, description: Description = None, key: str = None, value: str = None
    ):
        if description is not None:
            self.description = self._define_object(description, Description)
        if key is not None:
            self.key = key
        if value is not None:
            self.value = value


@JsonMap({})
class ResponseBody(BaseModel):
    """The response's body information.

    :param data: The response body's contents., defaults to None
    :type data: str, optional
    """

    def __init__(self, data: str = None):
        if data is not None:
            self.data = data


@JsonMap({"type_": "type", "status_code": "statusCode"})
class CallLogsResponse(BaseModel):
    """The server response's response information.

    :param type_: The type of response., defaults to None
    :type type_: str, optional
    :param status_code: The response's status code., defaults to None
    :type status_code: float, optional
    :param headers: The response's headers., defaults to None
    :type headers: ResponseHeaders, optional
    :param body: The response's body information., defaults to None
    :type body: ResponseBody, optional
    """

    def __init__(
        self,
        type_: str = None,
        status_code: float = None,
        headers: ResponseHeaders = None,
        body: ResponseBody = None,
    ):
        if type_ is not None:
            self.type_ = type_
        if status_code is not None:
            self.status_code = status_code
        if headers is not None:
            self.headers = self._define_object(headers, ResponseHeaders)
        if body is not None:
            self.body = self._define_object(body, ResponseBody)


@JsonMap({"id_": "id", "response_name": "responseName", "served_at": "servedAt"})
class CallLogs(BaseModel):
    """Information about the mock server's server responses.

    :param id_: The server response's ID., defaults to None
    :type id_: str, optional
    :param response_name: The server response's name., defaults to None
    :type response_name: str, optional
    :param served_at: The date and time at which the server response was served., defaults to None
    :type served_at: str, optional
    :param request: The server response's request information., defaults to None
    :type request: CallLogsRequest, optional
    :param response: The server response's response information., defaults to None
    :type response: CallLogsResponse, optional
    """

    def __init__(
        self,
        id_: str = None,
        response_name: str = None,
        served_at: str = None,
        request: CallLogsRequest = None,
        response: CallLogsResponse = None,
    ):
        if id_ is not None:
            self.id_ = id_
        if response_name is not None:
            self.response_name = response_name
        if served_at is not None:
            self.served_at = served_at
        if request is not None:
            self.request = self._define_object(request, CallLogsRequest)
        if response is not None:
            self.response = self._define_object(response, CallLogsResponse)


@JsonMap({"next_cursor": "nextCursor"})
class GetMockCallLogsOkResponseMeta(BaseModel):
    """The response's non-standard meta information.

    :param next_cursor: The pagination cursor that points to the next record in the results set., defaults to None
    :type next_cursor: str, optional
    """

    def __init__(self, next_cursor: str = None):
        if next_cursor is not None:
            self.next_cursor = next_cursor


@JsonMap({"call_logs": "call-logs"})
class GetMockCallLogsOkResponse(BaseModel):
    """GetMockCallLogsOkResponse

    :param call_logs: call_logs, defaults to None
    :type call_logs: List[CallLogs], optional
    :param meta: The response's non-standard meta information., defaults to None
    :type meta: GetMockCallLogsOkResponseMeta, optional
    """

    def __init__(
        self,
        call_logs: List[CallLogs] = None,
        meta: GetMockCallLogsOkResponseMeta = None,
    ):
        if call_logs is not None:
            self.call_logs = self._define_list(call_logs, CallLogs)
        if meta is not None:
            self.meta = self._define_object(meta, GetMockCallLogsOkResponseMeta)
