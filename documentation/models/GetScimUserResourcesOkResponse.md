# GetScimUserResourcesOkResponse

**Properties**

| Name           | Type                   | Required | Description                                          |
| :------------- | :--------------------- | :------- | :--------------------------------------------------- |
| resources      | List[ScimUserResource] | ❌       | A list of user resources.                            |
| items_per_page | float                  | ❌       | The number of items per response page.               |
| schemas        | List[str]              | ❌       |                                                      |
| start_index    | float                  | ❌       | The index entry by which the returned results begin. |
| total_results  | float                  | ❌       | The total number of results found.                   |
