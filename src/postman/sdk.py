from .services.billing import BillingService
from .services.api import ApiService
from .services.tags import TagsService
from .services.audit_logs import AuditLogsService
from .services.collections import CollectionsService
from .services.collection_items import CollectionItemsService
from .services.collection_folders import CollectionFoldersService
from .services.collection_requests import CollectionRequestsService
from .services.collection_responses import CollectionResponsesService
from .services.secret_scanner import SecretScannerService
from .services.environments import EnvironmentsService
from .services.import_ import ImportService
from .services.user import UserService
from .services.mocks import MocksService
from .services.monitors import MonitorsService
from .services.private_api_network import PrivateApiNetworkService
from .services.pull_requests import PullRequestsService
from .services.api_security import ApiSecurityService
from .services.scim import ScimService
from .services.webhooks import WebhooksService
from .services.workspaces import WorkspacesService
from .net.environment import Environment


class Postman:
    def __init__(
        self,
        access_token: str = None,
        api_key: str = None,
        api_key_header: str = "X-API-KEY",
        base_url: str = Environment.DEFAULT.value,
    ):
        """
        Initializes Postman the SDK class.
        """
        self.billing = BillingService(base_url=base_url)
        self.api = ApiService(base_url=base_url)
        self.tags = TagsService(base_url=base_url)
        self.audit_logs = AuditLogsService(base_url=base_url)
        self.collections = CollectionsService(base_url=base_url)
        self.collection_items = CollectionItemsService(base_url=base_url)
        self.collection_folders = CollectionFoldersService(base_url=base_url)
        self.collection_requests = CollectionRequestsService(base_url=base_url)
        self.collection_responses = CollectionResponsesService(base_url=base_url)
        self.secret_scanner = SecretScannerService(base_url=base_url)
        self.environments = EnvironmentsService(base_url=base_url)
        self.import_ = ImportService(base_url=base_url)
        self.user = UserService(base_url=base_url)
        self.mocks = MocksService(base_url=base_url)
        self.monitors = MonitorsService(base_url=base_url)
        self.private_api_network = PrivateApiNetworkService(base_url=base_url)
        self.pull_requests = PullRequestsService(base_url=base_url)
        self.api_security = ApiSecurityService(base_url=base_url)
        self.scim = ScimService(base_url=base_url)
        self.webhooks = WebhooksService(base_url=base_url)
        self.workspaces = WorkspacesService(base_url=base_url)
        self.set_access_token(access_token)
        self.set_api_key(api_key, api_key_header)

    def set_base_url(self, base_url):
        """
        Sets the base URL for the entire SDK.
        """
        self.billing.set_base_url(base_url)
        self.api.set_base_url(base_url)
        self.tags.set_base_url(base_url)
        self.audit_logs.set_base_url(base_url)
        self.collections.set_base_url(base_url)
        self.collection_items.set_base_url(base_url)
        self.collection_folders.set_base_url(base_url)
        self.collection_requests.set_base_url(base_url)
        self.collection_responses.set_base_url(base_url)
        self.secret_scanner.set_base_url(base_url)
        self.environments.set_base_url(base_url)
        self.import_.set_base_url(base_url)
        self.user.set_base_url(base_url)
        self.mocks.set_base_url(base_url)
        self.monitors.set_base_url(base_url)
        self.private_api_network.set_base_url(base_url)
        self.pull_requests.set_base_url(base_url)
        self.api_security.set_base_url(base_url)
        self.scim.set_base_url(base_url)
        self.webhooks.set_base_url(base_url)
        self.workspaces.set_base_url(base_url)

        return self

    def set_access_token(self, access_token: str):
        """
        Sets the access token for the entire SDK.
        """
        self.billing.set_access_token(access_token)
        self.api.set_access_token(access_token)
        self.tags.set_access_token(access_token)
        self.audit_logs.set_access_token(access_token)
        self.collections.set_access_token(access_token)
        self.collection_items.set_access_token(access_token)
        self.collection_folders.set_access_token(access_token)
        self.collection_requests.set_access_token(access_token)
        self.collection_responses.set_access_token(access_token)
        self.secret_scanner.set_access_token(access_token)
        self.environments.set_access_token(access_token)
        self.import_.set_access_token(access_token)
        self.user.set_access_token(access_token)
        self.mocks.set_access_token(access_token)
        self.monitors.set_access_token(access_token)
        self.private_api_network.set_access_token(access_token)
        self.pull_requests.set_access_token(access_token)
        self.api_security.set_access_token(access_token)
        self.scim.set_access_token(access_token)
        self.webhooks.set_access_token(access_token)
        self.workspaces.set_access_token(access_token)

        return self

    def set_api_key(self, api_key: str, api_key_header="X-API-KEY"):
        """
        Sets the api key and the api key header for the entire SDK.
        """
        self.billing.set_api_key(api_key, api_key_header)
        self.api.set_api_key(api_key, api_key_header)
        self.tags.set_api_key(api_key, api_key_header)
        self.audit_logs.set_api_key(api_key, api_key_header)
        self.collections.set_api_key(api_key, api_key_header)
        self.collection_items.set_api_key(api_key, api_key_header)
        self.collection_folders.set_api_key(api_key, api_key_header)
        self.collection_requests.set_api_key(api_key, api_key_header)
        self.collection_responses.set_api_key(api_key, api_key_header)
        self.secret_scanner.set_api_key(api_key, api_key_header)
        self.environments.set_api_key(api_key, api_key_header)
        self.import_.set_api_key(api_key, api_key_header)
        self.user.set_api_key(api_key, api_key_header)
        self.mocks.set_api_key(api_key, api_key_header)
        self.monitors.set_api_key(api_key, api_key_header)
        self.private_api_network.set_api_key(api_key, api_key_header)
        self.pull_requests.set_api_key(api_key, api_key_header)
        self.api_security.set_api_key(api_key, api_key_header)
        self.scim.set_api_key(api_key, api_key_header)
        self.webhooks.set_api_key(api_key, api_key_header)
        self.workspaces.set_api_key(api_key, api_key_header)

        return self


# c029837e0e474b76bc487506e8799df5e3335891efe4fb02bda7a1441840310c
