# GetTaggedEntitiesOkResponse

**Properties**

| Name | Type                            | Required | Description                                  |
| :--- | :------------------------------ | :------- | :------------------------------------------- |
| data | GetTaggedEntitiesOkResponseData | ❌       | An object containing the paginated elements. |
| meta | GetTaggedEntitiesOkResponseMeta | ❌       | The response's pagination information.       |

# GetTaggedEntitiesOkResponseData

An object containing the paginated elements.

**Properties**

| Name     | Type           | Required | Description                                                |
| :------- | :------------- | :------- | :--------------------------------------------------------- |
| entities | List[Entities] | ✅       | A list of the Postman elements that contain the given tag. |

# Entities

**Properties**

| Name        | Type               | Required | Description                  |
| :---------- | :----------------- | :------- | :--------------------------- |
| entity_id   | str                | ❌       | The element's unique ID.     |
| entity_type | EntitiesEntityType | ❌       | The type of Postman element. |

# EntitiesEntityType

The type of Postman element.

**Properties**

| Name       | Type | Required | Description  |
| :--------- | :--- | :------- | :----------- |
| API        | str  | ✅       | "api"        |
| COLLECTION | str  | ✅       | "collection" |
| WORKSPACE  | str  | ✅       | "workspace"  |

# GetTaggedEntitiesOkResponseMeta

The response's pagination information.

**Properties**

| Name        | Type | Required | Description                                                              |
| :---------- | :--- | :------- | :----------------------------------------------------------------------- |
| count       | int  | ✅       | The number of tagged elements returned in the response.                  |
| next_cursor | str  | ❌       | The pagination cursor that points to the next record in the results set. |
