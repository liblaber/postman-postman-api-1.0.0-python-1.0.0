# PostmanClient Python SDK 1.0.0

Welcome to the PostmanClient SDK documentation. This guide will help you get started with integrating and using the PostmanClient SDK in your project.

## Versions

- API version: `1.0`
- SDK version: `1.0.0`

## About the API

The Postman API enables you to programmatically access data stored in your Postman account. For more information on the API, rate limiting, authentication, and policies click visit [Postman's Documentation](https://learning.postman.com/docs/introduction/overview/)

## Table of Contents

- [Setup & Configuration](#setup--configuration)
  - [Supported Language Versions](#supported-language-versions)
  - [Installation](#installation)
- [Authentication](#authentication)
  - [API Key Authentication](#api-key-authentication)
- [Setting a Custom Timeout](#setting-a-custom-timeout)
- [Sample Usage](#sample-usage)
- [Services](#services)
- [Models](#models)
  - [Using Union Types](#using-union-types)
- [License](#license)

## Setup & Configuration

### Supported Language Versions

This SDK is compatible with the following versions: `Python >= 3.7`

### Installation

To get started with the SDK, we recommend installing using `pip`:

```bash
pip install postman-client
```

## Authentication

### API Key Authentication

The PostmanClient API uses API keys as a form of authentication. An API key is a unique identifier used to authenticate a user, developer, or a program that is calling the API.

#### Setting the API key

When you initialize the SDK, you can set the API key as follows:

```py
PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    timeout=10000
)
```

If you need to set or update the API key after initializing the SDK, you can use:

```py
sdk.set_api_key("YOUR_API_KEY", "YOUR_API_KEY_HEADER")
```

## Setting a Custom Timeout

You can set a custom timeout for the SDK's HTTP requests as follows:

```py
from postman_client import PostmanClient

sdk = PostmanClient(timeout=10000)
```

# Sample Usage

Below is a comprehensive example demonstrating how to authenticate and call a simple endpoint:

```py
from postman_client import PostmanClient, Environment

sdk = PostmanClient(
    api_key="YOUR_API_KEY",
    api_key_header="YOUR_API_KEY_HEADER",
    base_url=Environment.DEFAULT.value,
    timeout=10000
)

result = sdk.billing.get_accounts()

print(result)

```

## Services

The SDK provides various services to interact with the API.

<details> 
<summary>Below is a list of all available services with links to their detailed documentation:</summary>

| Name                                                                               |
| :--------------------------------------------------------------------------------- |
| [BillingService](documentation/services/BillingService.md)                         |
| [ApiService](documentation/services/ApiService.md)                                 |
| [TagsService](documentation/services/TagsService.md)                               |
| [AuditLogsService](documentation/services/AuditLogsService.md)                     |
| [CollectionsService](documentation/services/CollectionsService.md)                 |
| [CollectionItemsService](documentation/services/CollectionItemsService.md)         |
| [CollectionFoldersService](documentation/services/CollectionFoldersService.md)     |
| [CollectionRequestsService](documentation/services/CollectionRequestsService.md)   |
| [CollectionResponsesService](documentation/services/CollectionResponsesService.md) |
| [SecretScannerService](documentation/services/SecretScannerService.md)             |
| [EnvironmentsService](documentation/services/EnvironmentsService.md)               |
| [ImportService](documentation/services/ImportService.md)                           |
| [UserService](documentation/services/UserService.md)                               |
| [MocksService](documentation/services/MocksService.md)                             |
| [MonitorsService](documentation/services/MonitorsService.md)                       |
| [PrivateApiNetworkService](documentation/services/PrivateApiNetworkService.md)     |
| [PullRequestsService](documentation/services/PullRequestsService.md)               |
| [ApiSecurityService](documentation/services/ApiSecurityService.md)                 |
| [ScimService](documentation/services/ScimService.md)                               |
| [WebhooksService](documentation/services/WebhooksService.md)                       |
| [WorkspacesService](documentation/services/WorkspacesService.md)                   |

</details>

## Models

The SDK includes several models that represent the data structures used in API requests and responses. These models help in organizing and managing the data efficiently.

<details> 
<summary>Below is a list of all available models with links to their detailed documentation:</summary>

| Name                                                                                                                                  | Description                                                                   |
| :------------------------------------------------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------- |
| [InvoicesAccountInfo](documentation/models/InvoicesAccountInfo.md)                                                                    | Information about the account.                                                |
| [GetAccountInvoices](documentation/models/GetAccountInvoices.md)                                                                      |                                                                               |
| [GetAccountInvoicesStatus](documentation/models/GetAccountInvoicesStatus.md)                                                          |                                                                               |
| [GetApis](documentation/models/GetApis.md)                                                                                            | Information about the API schema.                                             |
| [Accept](documentation/models/Accept.md)                                                                                              |                                                                               |
| [CreateApiRequest](documentation/models/CreateApiRequest.md)                                                                          | Information about the API.                                                    |
| [CreateApiOkResponse](documentation/models/CreateApiOkResponse.md)                                                                    | The API's base data schema.                                                   |
| [GetApi](documentation/models/GetApi.md)                                                                                              |                                                                               |
| [GetApiInclude](documentation/models/GetApiInclude.md)                                                                                |                                                                               |
| [UpdateApiRequest](documentation/models/UpdateApiRequest.md)                                                                          | Information about the API.                                                    |
| [UpdateApiOkResponse](documentation/models/UpdateApiOkResponse.md)                                                                    | Information about the API.                                                    |
| [AddApiCollectionRequest](documentation/models/AddApiCollectionRequest.md)                                                            |                                                                               |
| [AddApiCollectionOkResponse](documentation/models/AddApiCollectionOkResponse.md)                                                      |                                                                               |
| [SyncCollectionWithSchema](documentation/models/SyncCollectionWithSchema.md)                                                          |                                                                               |
| [CommentResponse](documentation/models/CommentResponse.md)                                                                            |                                                                               |
| [CommentCreateUpdate](documentation/models/CommentCreateUpdate.md)                                                                    | Information about the comment.                                                |
| [CommentCreatedUpdated](documentation/models/CommentCreatedUpdated.md)                                                                |                                                                               |
| [CreateApiSchemaRequest](documentation/models/CreateApiSchemaRequest.md)                                                              | Information about the API schema.                                             |
| [CreateApiSchemaOkResponse](documentation/models/CreateApiSchemaOkResponse.md)                                                        | Information about the created API schema.                                     |
| [GetApiSchema](documentation/models/GetApiSchema.md)                                                                                  |                                                                               |
| [GetApiSchemaFiles](documentation/models/GetApiSchemaFiles.md)                                                                        | Information about the schema files and its meta information.                  |
| [GetApiSchemaFileContents](documentation/models/GetApiSchemaFileContents.md)                                                          | Information about the schema file.                                            |
| [CreateUpdateApiSchemaFileRequest](documentation/models/CreateUpdateApiSchemaFileRequest.md)                                          | Information about schema file.                                                |
| [CreateUpdateApiSchemaFileOkResponse](documentation/models/CreateUpdateApiSchemaFileOkResponse.md)                                    | Information about the schema file.                                            |
| [GetStatusOfAnAsyncTask](documentation/models/GetStatusOfAnAsyncTask.md)                                                              |                                                                               |
| [GetApiVersions](documentation/models/GetApiVersions.md)                                                                              | Information about the API's versions.                                         |
| [CreateApiVersionRequest](documentation/models/CreateApiVersionRequest.md)                                                            |                                                                               |
| [CreateApiVersionAcceptedResponse](documentation/models/CreateApiVersionAcceptedResponse.md)                                          |                                                                               |
| [GetApiVersion](documentation/models/GetApiVersion.md)                                                                                |                                                                               |
| [UpdateApiVersionRequest](documentation/models/UpdateApiVersionRequest.md)                                                            | Information about the API version.                                            |
| [UpdateApiVersionOkResponse](documentation/models/UpdateApiVersionOkResponse.md)                                                      |                                                                               |
| [TagGetPut](documentation/models/TagGetPut.md)                                                                                        |                                                                               |
| [TagUpdateTags](documentation/models/TagUpdateTags.md)                                                                                |                                                                               |
| [GetTaggedEntities](documentation/models/GetTaggedEntities.md)                                                                        |                                                                               |
| [AscDescDefaultDesc](documentation/models/AscDescDefaultDesc.md)                                                                      |                                                                               |
| [GetTaggedEntitiesEntityType](documentation/models/GetTaggedEntitiesEntityType.md)                                                    |                                                                               |
| [GetAuditLogs](documentation/models/GetAuditLogs.md)                                                                                  |                                                                               |
| [GetCollections](documentation/models/GetCollections.md)                                                                              |                                                                               |
| [CollectionsCreateCollectionRequest](documentation/models/CollectionsCreateCollectionRequest.md)                                      |                                                                               |
| [CreateCollectionOkResponse](documentation/models/CreateCollectionOkResponse.md)                                                      |                                                                               |
| [CreateCollectionForkRequest](documentation/models/CreateCollectionForkRequest.md)                                                    |                                                                               |
| [CreateCollectionForkOkResponse](documentation/models/CreateCollectionForkOkResponse.md)                                              |                                                                               |
| [MergeCollectionForkRequest](documentation/models/MergeCollectionForkRequest.md)                                                      |                                                                               |
| [MergeCollectionForkOkResponse](documentation/models/MergeCollectionForkOkResponse.md)                                                |                                                                               |
| [GetCollection](documentation/models/GetCollection.md)                                                                                |                                                                               |
| [GetCollectionModel](documentation/models/GetCollectionModel.md)                                                                      |                                                                               |
| [PutCollectionRequest](documentation/models/PutCollectionRequest.md)                                                                  |                                                                               |
| [PutCollectionOkResponse](documentation/models/PutCollectionOkResponse.md)                                                            |                                                                               |
| [PatchCollectionRequest](documentation/models/PatchCollectionRequest.md)                                                              |                                                                               |
| [PatchCollectionOkResponse](documentation/models/PatchCollectionOkResponse.md)                                                        |                                                                               |
| [DeleteCollection](documentation/models/DeleteCollection.md)                                                                          |                                                                               |
| [GetCollectionsForkedByUser](documentation/models/GetCollectionsForkedByUser.md)                                                      |                                                                               |
| [AscDesc](documentation/models/AscDesc.md)                                                                                            |                                                                               |
| [GetCollectionForks](documentation/models/GetCollectionForks.md)                                                                      |                                                                               |
| [PullCollectionChanges](documentation/models/PullCollectionChanges.md)                                                                |                                                                               |
| [GetCollectionPullRequests](documentation/models/GetCollectionPullRequests.md)                                                        |                                                                               |
| [PullRequestCreate](documentation/models/PullRequestCreate.md)                                                                        | Information about the pull request.                                           |
| [PullRequestCreated](documentation/models/PullRequestCreated.md)                                                                      |                                                                               |
| [GetCollectionRoles](documentation/models/GetCollectionRoles.md)                                                                      | Information about the collection's roles.                                     |
| [UpdateCollectionRoles](documentation/models/UpdateCollectionRoles.md)                                                                |                                                                               |
| [GetSourceCollectionStatus](documentation/models/GetSourceCollectionStatus.md)                                                        |                                                                               |
| [TransformCollectionToOpenApi](documentation/models/TransformCollectionToOpenApi.md)                                                  |                                                                               |
| [Format](documentation/models/Format.md)                                                                                              |                                                                               |
| [TransferCollectionItems](documentation/models/TransferCollectionItems.md)                                                            |                                                                               |
| [TransferCollectionItems200Error](documentation/models/TransferCollectionItems200Error.md)                                            |                                                                               |
| [CreateCollectionFolder](documentation/models/CreateCollectionFolder.md)                                                              |                                                                               |
| [CreateCollectionRequestOkResponse](documentation/models/CreateCollectionRequestOkResponse.md)                                        |                                                                               |
| [CreateCollectionResponse](documentation/models/CreateCollectionResponse.md)                                                          |                                                                               |
| [GetCollectionFolder](documentation/models/GetCollectionFolder.md)                                                                    |                                                                               |
| [UpdateCollectionFolder](documentation/models/UpdateCollectionFolder.md)                                                              |                                                                               |
| [DeleteCollectionFolder](documentation/models/DeleteCollectionFolder.md)                                                              |                                                                               |
| [GetCollectionRequest](documentation/models/GetCollectionRequest.md)                                                                  |                                                                               |
| [UpdateCollectionRequest](documentation/models/UpdateCollectionRequest.md)                                                            |                                                                               |
| [DeleteCollectionRequest](documentation/models/DeleteCollectionRequest.md)                                                            |                                                                               |
| [GetCollectionResponse](documentation/models/GetCollectionResponse.md)                                                                |                                                                               |
| [UpdateCollectionResponse](documentation/models/UpdateCollectionResponse.md)                                                          |                                                                               |
| [DeleteCollectionResponse](documentation/models/DeleteCollectionResponse.md)                                                          |                                                                               |
| [DetectedSecretsQueriesRequest](documentation/models/DetectedSecretsQueriesRequest.md)                                                |                                                                               |
| [DetectedSecretsQueriesOkResponse](documentation/models/DetectedSecretsQueriesOkResponse.md)                                          |                                                                               |
| [UpdateDetectedSecretResolutionsRequest](documentation/models/UpdateDetectedSecretResolutionsRequest.md)                              |                                                                               |
| [UpdateDetectedSecretResolutionsOkResponse](documentation/models/UpdateDetectedSecretResolutionsOkResponse.md)                        |                                                                               |
| [GetSecretsLocations](documentation/models/GetSecretsLocations.md)                                                                    |                                                                               |
| [GetSecretTypes](documentation/models/GetSecretTypes.md)                                                                              |                                                                               |
| [GetEnvironments](documentation/models/GetEnvironments.md)                                                                            |                                                                               |
| [CreateEnvironmentRequest](documentation/models/CreateEnvironmentRequest.md)                                                          |                                                                               |
| [CreateEnvironmentOkResponse](documentation/models/CreateEnvironmentOkResponse.md)                                                    |                                                                               |
| [GetEnvironment](documentation/models/GetEnvironment.md)                                                                              |                                                                               |
| [UpdateEnvironmentRequest](documentation/models/UpdateEnvironmentRequest.md)                                                          |                                                                               |
| [UpdateEnvironmentOkResponse](documentation/models/UpdateEnvironmentOkResponse.md)                                                    |                                                                               |
| [DeleteEnvironment](documentation/models/DeleteEnvironment.md)                                                                        |                                                                               |
| [GetEnvironmentForks](documentation/models/GetEnvironmentForks.md)                                                                    |                                                                               |
| [GetEnvironmentForksSort](documentation/models/GetEnvironmentForksSort.md)                                                            |                                                                               |
| [ForkEnvironmentRequest](documentation/models/ForkEnvironmentRequest.md)                                                              |                                                                               |
| [ForkEnvironmentOkResponse](documentation/models/ForkEnvironmentOkResponse.md)                                                        |                                                                               |
| [MergeEnvironmentForkRequest](documentation/models/MergeEnvironmentForkRequest.md)                                                    |                                                                               |
| [MergeEnvironmentForkOkResponse](documentation/models/MergeEnvironmentForkOkResponse.md)                                              |                                                                               |
| [PullEnvironmentRequest](documentation/models/PullEnvironmentRequest.md)                                                              |                                                                               |
| [PullEnvironmentOkResponse](documentation/models/PullEnvironmentOkResponse.md)                                                        |                                                                               |
| [ImportExportFile](documentation/models/ImportExportFile.md)                                                                          |                                                                               |
| [ImportOpenApiDefinitionOkResponse](documentation/models/ImportOpenApiDefinitionOkResponse.md)                                        |                                                                               |
| [GetAuthenticatedUser](documentation/models/GetAuthenticatedUser.md)                                                                  |                                                                               |
| [GetMocks](documentation/models/GetMocks.md)                                                                                          |                                                                               |
| [CreateMock](documentation/models/CreateMock.md)                                                                                      |                                                                               |
| [MockCreateUpdate](documentation/models/MockCreateUpdate.md)                                                                          |                                                                               |
| [GetMock](documentation/models/GetMock.md)                                                                                            |                                                                               |
| [UpdateMock](documentation/models/UpdateMock.md)                                                                                      |                                                                               |
| [DeleteMock](documentation/models/DeleteMock.md)                                                                                      |                                                                               |
| [GetMockCallLogs](documentation/models/GetMockCallLogs.md)                                                                            |                                                                               |
| [GetMockCallLogsSort](documentation/models/GetMockCallLogsSort.md)                                                                    |                                                                               |
| [PublishMock](documentation/models/PublishMock.md)                                                                                    |                                                                               |
| [UnpublishMock](documentation/models/UnpublishMock.md)                                                                                |                                                                               |
| [GetMockServerResponses](documentation/models/GetMockServerResponses.md)                                                              | Information about the server response.                                        |
| [CreateMockServerResponse](documentation/models/CreateMockServerResponse.md)                                                          |                                                                               |
| [UpdateMockServerResponse](documentation/models/UpdateMockServerResponse.md)                                                          |                                                                               |
| [DeleteMockServerResponse](documentation/models/DeleteMockServerResponse.md)                                                          | Information about the deleted server response.                                |
| [GetMonitors](documentation/models/GetMonitors.md)                                                                                    |                                                                               |
| [CreateMonitorRequest](documentation/models/CreateMonitorRequest.md)                                                                  |                                                                               |
| [CreateMonitorOkResponse](documentation/models/CreateMonitorOkResponse.md)                                                            |                                                                               |
| [GetMonitor](documentation/models/GetMonitor.md)                                                                                      |                                                                               |
| [UpdateMonitorRequest](documentation/models/UpdateMonitorRequest.md)                                                                  |                                                                               |
| [UpdateMonitorOkResponse](documentation/models/UpdateMonitorOkResponse.md)                                                            |                                                                               |
| [DeleteMonitor](documentation/models/DeleteMonitor.md)                                                                                |                                                                               |
| [RunMonitor](documentation/models/RunMonitor.md)                                                                                      |                                                                               |
| [GetPanElementsAndFolders](documentation/models/GetPanElementsAndFolders.md)                                                          |                                                                               |
| [GetAllElementsAndFoldersSort](documentation/models/GetAllElementsAndFoldersSort.md)                                                  |                                                                               |
| [GetAllElementsAndFoldersType](documentation/models/GetAllElementsAndFoldersType.md)                                                  |                                                                               |
| [PostPanElementOrFolderRequest](documentation/models/PostPanElementOrFolderRequest.md)                                                |                                                                               |
| [UpdatePanElementOrFolderRequest](documentation/models/UpdatePanElementOrFolderRequest.md)                                            |                                                                               |
| [UpdatePanElementOrFolderElementType](documentation/models/UpdatePanElementOrFolderElementType.md)                                    |                                                                               |
| [DeletePanElementOrFolder](documentation/models/DeletePanElementOrFolder.md)                                                          |                                                                               |
| [GetAllPanAddElementRequests](documentation/models/GetAllPanAddElementRequests.md)                                                    |                                                                               |
| [GetAllPanAddElementRequestsStatus](documentation/models/GetAllPanAddElementRequestsStatus.md)                                        |                                                                               |
| [PrivateApiNetworkRespondPanElementAddRequestRequest_1](documentation/models/PrivateApiNetworkRespondPanElementAddRequestRequest1.md) |                                                                               |
| [RespondPanElementAddRequestOkResponse](documentation/models/RespondPanElementAddRequestOkResponse.md)                                |                                                                               |
| [PullRequestGet](documentation/models/PullRequestGet.md)                                                                              |                                                                               |
| [PullRequestUpdate](documentation/models/PullRequestUpdate.md)                                                                        |                                                                               |
| [PullRequestUpdated](documentation/models/PullRequestUpdated.md)                                                                      |                                                                               |
| [SchemaSecurityValidationRequest](documentation/models/SchemaSecurityValidationRequest.md)                                            |                                                                               |
| [SchemaSecurityValidationOkResponse](documentation/models/SchemaSecurityValidationOkResponse.md)                                      |                                                                               |
| [GetScimGroupResources](documentation/models/GetScimGroupResources.md)                                                                |                                                                               |
| [CreateScimGroupRequest](documentation/models/CreateScimGroupRequest.md)                                                              |                                                                               |
| [CreateScimGroupCreatedResponse](documentation/models/CreateScimGroupCreatedResponse.md)                                              |                                                                               |
| [GetScimGroupResource](documentation/models/GetScimGroupResource.md)                                                                  |                                                                               |
| [ScimUpdateGroupRequest](documentation/models/ScimUpdateGroupRequest.md)                                                              |                                                                               |
| [ScimUpdateGroupOkResponse](documentation/models/ScimUpdateGroupOkResponse.md)                                                        |                                                                               |
| [GetScimResourceTypes](documentation/models/GetScimResourceTypes.md)                                                                  |                                                                               |
| [GetScimServiceProviderConfig](documentation/models/GetScimServiceProviderConfig.md)                                                  | Information about Postman's SCIM API configurations and supported operations. |
| [GetScimUserResources](documentation/models/GetScimUserResources.md)                                                                  |                                                                               |
| [CreateScimUserRequest](documentation/models/CreateScimUserRequest.md)                                                                |                                                                               |
| [CreateScimUserCreatedResponse](documentation/models/CreateScimUserCreatedResponse.md)                                                |                                                                               |
| [GetScimUserResourceOkResponse](documentation/models/GetScimUserResourceOkResponse.md)                                                |                                                                               |
| [UpdateScimUser](documentation/models/UpdateScimUser.md)                                                                              |                                                                               |
| [UpdateScimUserState](documentation/models/UpdateScimUserState.md)                                                                    |                                                                               |
| [CreateWebhookRequest](documentation/models/CreateWebhookRequest.md)                                                                  |                                                                               |
| [CreateWebhookOkResponse](documentation/models/CreateWebhookOkResponse.md)                                                            |                                                                               |
| [GetWorkspaces](documentation/models/GetWorkspaces.md)                                                                                |                                                                               |
| [GetWorkspacesType](documentation/models/GetWorkspacesType.md)                                                                        |                                                                               |
| [GetWorkspacesInclude](documentation/models/GetWorkspacesInclude.md)                                                                  |                                                                               |
| [CreateWorkspaceRequest](documentation/models/CreateWorkspaceRequest.md)                                                              |                                                                               |
| [CreateWorkspaceOkResponse](documentation/models/CreateWorkspaceOkResponse.md)                                                        |                                                                               |
| [GetWorkspaceRoles](documentation/models/GetWorkspaceRoles.md)                                                                        |                                                                               |
| [GetWorkspace](documentation/models/GetWorkspace.md)                                                                                  |                                                                               |
| [UpdateWorkspaceRequest](documentation/models/UpdateWorkspaceRequest.md)                                                              |                                                                               |
| [UpdateWorkspaceOkResponse](documentation/models/UpdateWorkspaceOkResponse.md)                                                        |                                                                               |
| [DeleteWorkspace](documentation/models/DeleteWorkspace.md)                                                                            |                                                                               |
| [GetWorkspaceGlobalVariables](documentation/models/GetWorkspaceGlobalVariables.md)                                                    | Information about the workspace's global variables.                           |
| [UpdateWorkspaceGlobalVariablesRequest](documentation/models/UpdateWorkspaceGlobalVariablesRequest.md)                                |                                                                               |
| [UpdateWorkspaceGlobalVariablesOkResponse](documentation/models/UpdateWorkspaceGlobalVariablesOkResponse.md)                          | Information about the workspace's updated global variables.                   |
| [UpdateWorkspaceRolesRequest](documentation/models/UpdateWorkspaceRolesRequest.md)                                                    |                                                                               |
| [UpdateWorkspaceRolesOkResponse](documentation/models/UpdateWorkspaceRolesOkResponse.md)                                              |                                                                               |
| [InvoiceData](documentation/models/InvoiceData.md)                                                                                    | Information about the invoice.                                                |
| [JsonSchema](documentation/models/JsonSchema.md)                                                                                      |                                                                               |
| [JsonStringified](documentation/models/JsonStringified.md)                                                                            |                                                                               |
| [PanCreateApi](documentation/models/PanCreateApi.md)                                                                                  |                                                                               |
| [PanCreateCollection](documentation/models/PanCreateCollection.md)                                                                    |                                                                               |
| [PanCreateWorkspace](documentation/models/PanCreateWorkspace.md)                                                                      |                                                                               |
| [PanCreateFolder](documentation/models/PanCreateFolder.md)                                                                            |                                                                               |
| [PanElementCreated](documentation/models/PanElementCreated.md)                                                                        | Information about the Private API Network element.                            |
| [PanFolderCreated](documentation/models/PanFolderCreated.md)                                                                          | Information about the Private API Network folder.                             |
| [UpdatePanApi](documentation/models/UpdatePanApi.md)                                                                                  |                                                                               |
| [UpdatePanCollection](documentation/models/UpdatePanCollection.md)                                                                    |                                                                               |
| [UpdatePanWorkspace](documentation/models/UpdatePanWorkspace.md)                                                                      |                                                                               |
| [UpdatePanFolder](documentation/models/UpdatePanFolder.md)                                                                            |                                                                               |
| [ScimGroupResource](documentation/models/ScimGroupResource.md)                                                                        | The SCIM group resource object.                                               |
| [Resources](documentation/models/Resources.md)                                                                                        | The SCIM user resource object.                                                |
| [GlobalVariable](documentation/models/GlobalVariable.md)                                                                              | Information about the global variable.                                        |

</details>

### Using Union Types

Union types allow you to specify that a variable can have more than one type. This is particularly useful when a function can accept multiple types of inputs. The Union type hint is used for this purpose.

#### Example Function with Union Types

You can call service method with an instance of `TypeA`, `TypeB`, or a dictionary that can be converted to an instance of either type.

```python
# Model Definition
ParamType = Union[TypeA, TypeB]

# Service Method
def service_method(param: ParamType):
...

## Usage
type_a = TypeA(key="value")
type_b = TypeB(key="value")

sdk.service.service_method(type_a)
sdk.service.service_method(type_b)
sdk.service.service_method({"key": "value"})
```

You cannot create an instance of a `Union` type itself. Instead, pass an instance of one of the types in the `Union`, or a dictionary that can be converted to one of those types.

## License

This SDK is licensed under the MIT License.

See the [LICENSE](LICENSE) file for more details.

<!-- This file was generated by liblab | https://liblab.com/ -->
