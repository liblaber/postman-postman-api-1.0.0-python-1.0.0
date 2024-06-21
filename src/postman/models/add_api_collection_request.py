from enum import Enum
from typing import Union
from typing import List
from .utils.json_map import JsonMap
from .base import BaseModel
from .base import OneOfBaseModel


@JsonMap({"collection_id": "collectionId"})
class AddApiCollectionRequest1Data(BaseModel):
    """AddApiCollectionRequest1Data

    :param collection_id: The collection ID to copy to the API., defaults to None
    :type collection_id: str, optional
    """

    def __init__(self, collection_id: str = None):
        if collection_id is not None:
            self.collection_id = collection_id


class AddApiCollectionRequest1OperationType(Enum):
    """An enumeration representing different categories.

    :cvar COPY_COLLECTION: "COPY_COLLECTION"
    :vartype COPY_COLLECTION: str
    """

    COPY_COLLECTION = "COPY_COLLECTION"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                AddApiCollectionRequest1OperationType._member_map_.values(),
            )
        )


@JsonMap({"operation_type": "operationType"})
class AddApiCollectionRequest1(BaseModel):
    """AddApiCollectionRequest1

    :param data: data, defaults to None
    :type data: AddApiCollectionRequest1Data, optional
    :param operation_type: The `COPY_COLLECTION` method., defaults to None
    :type operation_type: AddApiCollectionRequest1OperationType, optional
    """

    def __init__(
        self,
        data: AddApiCollectionRequest1Data = None,
        operation_type: AddApiCollectionRequest1OperationType = None,
    ):
        if data is not None:
            self.data = self._define_object(data, AddApiCollectionRequest1Data)
        if operation_type is not None:
            self.operation_type = self._enum_matching(
                operation_type,
                AddApiCollectionRequest1OperationType.list(),
                "operation_type",
            )


class AddApiCollectionRequest2OperationType(Enum):
    """An enumeration representing different categories.

    :cvar GENERATE_FROM_SCHEMA: "GENERATE_FROM_SCHEMA"
    :vartype GENERATE_FROM_SCHEMA: str
    """

    GENERATE_FROM_SCHEMA = "GENERATE_FROM_SCHEMA"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                AddApiCollectionRequest2OperationType._member_map_.values(),
            )
        )


@JsonMap({"operation_type": "operationType"})
class AddApiCollectionRequest2(BaseModel):
    """AddApiCollectionRequest2

    :param name: The collection's name., defaults to None
    :type name: str, optional
    :param operation_type: The `GENERATE_FROM_SCHEMA` method., defaults to None
    :type operation_type: AddApiCollectionRequest2OperationType, optional
    :param options: The advanced creation options for collections and their values. For a complete list of properties and their values, see Postman's [OpenAPI 3.0 to Postman Collection v2.1.0 Converter OPTIONS documentation](https://github.com/postmanlabs/openapi-to-postman/blob/develop/OPTIONS.md). These properties are case-sensitive., defaults to None
    :type options: dict, optional
    """

    def __init__(
        self,
        name: str = None,
        operation_type: AddApiCollectionRequest2OperationType = None,
        options: dict = None,
    ):
        if name is not None:
            self.name = name
        if operation_type is not None:
            self.operation_type = self._enum_matching(
                operation_type,
                AddApiCollectionRequest2OperationType.list(),
                "operation_type",
            )
        if options is not None:
            self.options = options


class InfoSchema(Enum):
    """An enumeration representing different categories.

    :cvar HTTPS_SCHEMA_GETPOSTMAN_COM_JSON_COLLECTION_V2_1_0_COLLECTION_JSON: "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
    :vartype HTTPS_SCHEMA_GETPOSTMAN_COM_JSON_COLLECTION_V2_1_0_COLLECTION_JSON: str
    """

    HTTPS_SCHEMA_GETPOSTMAN_COM_JSON_COLLECTION_V2_1_0_COLLECTION_JSON = (
        "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
    )

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, InfoSchema._member_map_.values()))


@JsonMap({})
class DataInfo(BaseModel):
    """Information about the collection.

    :param name: The collection's name., defaults to None
    :type name: str, optional
    :param schema: The collection's schema format., defaults to None
    :type schema: InfoSchema, optional
    """

    def __init__(self, name: str = None, schema: InfoSchema = None):
        if name is not None:
            self.name = name
        if schema is not None:
            self.schema = self._enum_matching(schema, InfoSchema.list(), "schema")


@JsonMap({})
class AddApiCollectionRequest3Data(BaseModel):
    """Information about the collection's contents, such as requests and responses. For a complete list of values, refer to the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json).

    :param info: Information about the collection., defaults to None
    :type info: DataInfo, optional
    :param item: Information about the requests and responses in the collection. For a complete list of values, refer to the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json)., defaults to None
    :type item: List[any], optional
    """

    def __init__(self, info: DataInfo = None, item: List[any] = None):
        if info is not None:
            self.info = self._define_object(info, DataInfo)
        if item is not None:
            self.item = item


class AddApiCollectionRequest3OperationType(Enum):
    """An enumeration representing different categories.

    :cvar CREATE_NEW: "CREATE_NEW"
    :vartype CREATE_NEW: str
    """

    CREATE_NEW = "CREATE_NEW"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                AddApiCollectionRequest3OperationType._member_map_.values(),
            )
        )


@JsonMap({"operation_type": "operationType"})
class AddApiCollectionRequest3(BaseModel):
    """AddApiCollectionRequest3

    :param data: Information about the collection's contents, such as requests and responses. For a complete list of values, refer to the [collection.json schema file](https://schema.postman.com/json/collection/v2.1.0/collection.json)., defaults to None
    :type data: AddApiCollectionRequest3Data, optional
    :param operation_type: The `CREATE_NEW` method., defaults to None
    :type operation_type: AddApiCollectionRequest3OperationType, optional
    """

    def __init__(
        self,
        data: AddApiCollectionRequest3Data = None,
        operation_type: AddApiCollectionRequest3OperationType = None,
    ):
        if data is not None:
            self.data = self._define_object(data, AddApiCollectionRequest3Data)
        if operation_type is not None:
            self.operation_type = self._enum_matching(
                operation_type,
                AddApiCollectionRequest3OperationType.list(),
                "operation_type",
            )


class AddApiCollectionRequestGuard(OneOfBaseModel):
    class_list = {
        "AddApiCollectionRequest1": AddApiCollectionRequest1,
        "AddApiCollectionRequest2": AddApiCollectionRequest2,
        "AddApiCollectionRequest3": AddApiCollectionRequest3,
    }


AddApiCollectionRequest = Union[
    AddApiCollectionRequest1, AddApiCollectionRequest2, AddApiCollectionRequest3
]
