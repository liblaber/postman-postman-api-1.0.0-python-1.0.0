# UpdateApiTagsRequest

**Properties**

| Name | Type                           | Required | Description                             |
| :--- | :----------------------------- | :------- | :-------------------------------------- |
| tags | List[UpdateApiTagsRequestTags] | ✅       | A list of the associated tags as slugs. |

# UpdateApiTagsRequestTags

Information about the tag.

**Properties**

| Name | Type | Required | Description                                                     |
| :--- | :--- | :------- | :-------------------------------------------------------------- |
| slug | str  | ✅       | The tag's ID within a team or individual (non-team) user scope. |
