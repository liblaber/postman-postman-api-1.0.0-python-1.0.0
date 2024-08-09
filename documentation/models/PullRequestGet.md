# PullRequestGet

**Properties**

| Name        | Type            | Required | Description                                                                                                                                                                                                            |
| :---------- | :-------------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| created_at  | str             | ❌       | The date and time at which the pull request was created.                                                                                                                                                               |
| updated_at  | str             | ❌       | The date and time at which the pull request was updated.                                                                                                                                                               |
| id\_        | str             | ❌       | The pull request's ID.                                                                                                                                                                                                 |
| title       | str             | ❌       | The pull request's title.                                                                                                                                                                                              |
| description | str             | ❌       | The pull request's description.                                                                                                                                                                                        |
| created_by  | str             | ❌       | The ID of the user who created the pull request.                                                                                                                                                                       |
| updated_by  | str             | ❌       | The ID of the user who last updated the pull request.                                                                                                                                                                  |
| comment     | str             | ❌       | If the pull request is a `decline` status, an optoinal comment about why the pull request was declined.                                                                                                                |
| fortk_type  | str             | ❌       | The type of element the pull request was forked from.                                                                                                                                                                  |
| source      | Source          | ❌       | Information about the pull request's source (parent) element.                                                                                                                                                          |
| destination | Destination     | ❌       | Information about the pull request destination element.                                                                                                                                                                |
| status      | str             | ❌       | The pull request's current review status: - `open` — The pull request is still open. - `approved` — The pull request was approved by its reviewers. - `declined` — The pull request was not approved by its reviewers. |
| merge       | Merge           | ❌       | Information about the current progress of the pull request's merge.                                                                                                                                                    |
| reviewers   | List[Reviewers] | ❌       | Information about the reviewers assigned to the pull request.                                                                                                                                                          |

# Source

Information about the pull request's source (parent) element.

**Properties**

| Name      | Type | Required | Description                                              |
| :-------- | :--- | :------- | :------------------------------------------------------- |
| id\_      | str  | ❌       | The pull request's source ID.                            |
| name      | str  | ❌       | The source element's name.                               |
| fork_name | str  | ❌       | The name of the fork created from the source element.    |
| exists    | bool | ❌       | If true, whether the element is present and not deleted. |

# Destination

Information about the pull request destination element.

**Properties**

| Name   | Type | Required | Description                                              |
| :----- | :--- | :------- | :------------------------------------------------------- |
| id\_   | str  | ❌       | The destination element's ID.                            |
| name   | str  | ❌       | The destination element's name.                          |
| exists | bool | ❌       | If true, whether the element is present and not deleted. |

# Merge

Information about the current progress of the pull request's merge.

**Properties**

| Name   | Type        | Required | Description                                                                                                                                                                                  |
| :----- | :---------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| status | MergeStatus | ❌       | The pull request's current merge status: - `inactive` — There is no merge in progress. - `inprogress` — The pull request is currently merging. - `failed` — The pull request's merge failed. |

# MergeStatus

The pull request's current merge status: - `inactive` — There is no merge in progress. - `inprogress` — The pull request is currently merging. - `failed` — The pull request's merge failed.

**Properties**

| Name       | Type | Required | Description  |
| :--------- | :--- | :------- | :----------- |
| INACTIVE   | str  | ✅       | "inactive"   |
| INPROGRESS | str  | ✅       | "inprogress" |
| FAILED     | str  | ✅       | "failed"     |

# Reviewers

**Properties**

| Name   | Type | Required | Description                                                              |
| :----- | :--- | :------- | :----------------------------------------------------------------------- |
| id\_   | str  | ❌       | The reviewer's user ID.                                                  |
| status | str  | ❌       | The reviewer's review status response. One of: - `approved` - `declined` |

<!-- This file was generated by liblab | https://liblab.com/ -->
