# This file was generated by liblab | https://liblab.com/

from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class CreateUpdateApiSchemaFileRoot(BaseModel):
    """Information about the schema's root file. This tag only applies to protobuf specifications.

    :param enabled: If true, tag the file as the root file., defaults to None
    :type enabled: bool, optional
    """

    def __init__(self, enabled: bool = None):
        """Information about the schema's root file. This tag only applies to protobuf specifications.

        :param enabled: If true, tag the file as the root file., defaults to None
        :type enabled: bool, optional
        """
        if enabled is not None:
            self.enabled = enabled


@JsonMap({})
class CreateUpdateApiSchemaFileRequest(BaseModel):
    """Information about schema file.

    :param name: The schema file's name., defaults to None
    :type name: str, optional
    :param root: Information about the schema's root file. This tag only applies to protobuf specifications., defaults to None
    :type root: CreateUpdateApiSchemaFileRoot, optional
    :param content: The schema file's content., defaults to None
    :type content: str, optional
    """

    def __init__(
        self,
        name: str = None,
        root: CreateUpdateApiSchemaFileRoot = None,
        content: str = None,
    ):
        """Information about schema file.

        :param name: The schema file's name., defaults to None
        :type name: str, optional
        :param root: Information about the schema's root file. This tag only applies to protobuf specifications., defaults to None
        :type root: CreateUpdateApiSchemaFileRoot, optional
        :param content: The schema file's content., defaults to None
        :type content: str, optional
        """
        if name is not None:
            self.name = name
        if root is not None:
            self.root = self._define_object(root, CreateUpdateApiSchemaFileRoot)
        if content is not None:
            self.content = content
