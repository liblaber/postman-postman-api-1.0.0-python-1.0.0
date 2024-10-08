# GetCollectionPullRequests

**Properties**

| Name | Type                                | Required | Description |
| :--- | :---------------------------------- | :------- | :---------- |
| data | List[GetCollectionPullRequestsData] | ❌       |             |

# GetCollectionPullRequestsData

Information about the pull request.

**Properties**

| Name           | Type       | Required | Description                                                                         |
| :------------- | :--------- | :------- | :---------------------------------------------------------------------------------- |
| created_at     | str        | ❌       | The date and time at which the pull request was created.                            |
| created_by     | str        | ❌       | The ID of the user who created the pull request.                                    |
| description    | str        | ❌       | The pull request's description.                                                     |
| destination_id | str        | ❌       | The pull request's merge destination ID.                                            |
| href           | str        | ❌       | A URL where you can view the pull request's details.                                |
| id\_           | str        | ❌       | The pull request's ID.                                                              |
| source_id      | str        | ❌       | The pull request's source (parent) ID.                                              |
| status         | DataStatus | ❌       | The pull request's current status.                                                  |
| comment        | str        | ❌       | If the pull request is declined, a comment about why the pull request was declined. |
| title          | str        | ❌       | The pull request's title.                                                           |
| updated_by     | str        | ❌       | The ID of the user who updated the pull request.                                    |
| updated_at     | str        | ❌       | The date and time at which the pull request was updated.                            |

# DataStatus

The pull request's current status.

**Properties**

| Name     | Type | Required | Description |
| :------- | :--- | :------- | :---------- |
| OPEN     | str  | ✅       | "open"      |
| APPROVED | str  | ✅       | "approved"  |
| DECLINED | str  | ✅       | "declined"  |
| MERGED   | str  | ✅       | "merged"    |

<!-- This file was generated by liblab | https://liblab.com/ -->
