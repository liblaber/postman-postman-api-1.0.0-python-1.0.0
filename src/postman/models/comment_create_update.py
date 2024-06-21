from enum import Enum
from .utils.json_map import JsonMap
from .base import BaseModel


class UserNameType(Enum):
    """An enumeration representing different categories.

    :cvar USER: "user"
    :vartype USER: str
    """

    USER = "user"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, UserNameType._member_map_.values()))


@JsonMap({"type_": "type", "id_": "id"})
class UserName(BaseModel):
    """An object that contains information about the tagged user. The object's name is the user's Postman username. For example, `@user-postman`.

    :param type_: The `user` value.
    :type type_: UserNameType
    :param id_: The user's ID.
    :type id_: int
    """

    def __init__(self, type_: UserNameType, id_: int):
        self.type_ = self._enum_matching(type_, UserNameType.list(), "type_")
        self.id_ = id_


@JsonMap({"user_name": "userName"})
class CommentCreateUpdateTags(BaseModel):
    """Information about users tagged in the `body` comment.

    :param user_name: An object that contains information about the tagged user. The object's name is the user's Postman username. For example, `@user-postman`., defaults to None
    :type user_name: UserName, optional
    """

    def __init__(self, user_name: UserName = None):
        if user_name is not None:
            self.user_name = self._define_object(user_name, UserName)


@JsonMap({})
class CommentCreateUpdate(BaseModel):
    """Information about the comment.

    :param body: The contents of the comment.
    :type body: str
    :param tags: Information about users tagged in the `body` comment., defaults to None
    :type tags: CommentCreateUpdateTags, optional
    """

    def __init__(self, body: str, tags: CommentCreateUpdateTags = None):
        self.body = body
        if tags is not None:
            self.tags = self._define_object(tags, CommentCreateUpdateTags)
