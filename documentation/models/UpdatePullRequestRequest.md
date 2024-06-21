# UpdatePullRequestRequest

**Properties**

| Name        | Type      | Required | Description                                                                                                                                                      |
| :---------- | :-------- | :------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| title       | str       | ✅       | The pull request's updated title.                                                                                                                                |
| description | str       | ❌       | The updated pull request description.                                                                                                                            |
| reviewers   | List[str] | ✅       | An updated list of the pull request's assigned reviewers. This replaces all existing users assigned to the pull request with those you pass in the request body. |
