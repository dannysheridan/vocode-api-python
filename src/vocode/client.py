# This file was auto-generated by Fern from our API Definition.

from .environment import VocodeEnvironment
from .resources.actions.client import ActionsClient, AsyncActionsClient
from .resources.agents.client import AgentsClient, AsyncAgentsClient
from .resources.calls.client import AsyncCallsClient, CallsClient
from .resources.numbers.client import AsyncNumbersClient, NumbersClient
from .resources.usage.client import AsyncUsageClient, UsageClient
from .resources.voices.client import AsyncVoicesClient, VoicesClient
from .resources.webhooks.client import AsyncWebhooksClient, WebhooksClient


class Vocode:
    def __init__(self, *, environment: VocodeEnvironment = VocodeEnvironment.PRODUCTION, token: str):
        self._environment = environment
        self._token = token
        self.numbers = NumbersClient(environment=self._environment, token=self._token)
        self.calls = CallsClient(environment=self._environment, token=self._token)
        self.usage = UsageClient(environment=self._environment, token=self._token)
        self.actions = ActionsClient(environment=self._environment, token=self._token)
        self.agents = AgentsClient(environment=self._environment, token=self._token)
        self.voices = VoicesClient(environment=self._environment, token=self._token)
        self.webhooks = WebhooksClient(environment=self._environment, token=self._token)


class AsyncVocode:
    def __init__(self, *, environment: VocodeEnvironment = VocodeEnvironment.PRODUCTION, token: str):
        self._environment = environment
        self._token = token
        self.numbers = AsyncNumbersClient(environment=self._environment, token=self._token)
        self.calls = AsyncCallsClient(environment=self._environment, token=self._token)
        self.usage = AsyncUsageClient(environment=self._environment, token=self._token)
        self.actions = AsyncActionsClient(environment=self._environment, token=self._token)
        self.agents = AsyncAgentsClient(environment=self._environment, token=self._token)
        self.voices = AsyncVoicesClient(environment=self._environment, token=self._token)
        self.webhooks = AsyncWebhooksClient(environment=self._environment, token=self._token)
