from typing import Dict

from app.clients import OpenAIClient, UpstageClient
from app.services import ChatService, EmbeddingService

class ServiceFactory:
    base_urls: Dict[str, OpenAIClient] = {
        'solar': "https://api.upstage.ai/v1/solar"
    }

    @classmethod
    def get_chat_service(cls, client_name: str = 'solar') -> ChatService:
        return ChatService(
            open_ai_client=OpenAIClient(base_url=cls.base_urls[client_name]))

    @classmethod
    def get_embedding_service(cls, client_name: str = 'solar') -> ChatService:
        return EmbeddingService(
            open_ai_client=OpenAIClient(base_url=cls.base_urls[client_name]),
            upstage_client=UpstageClient(base_url=cls.base_urls[client_name]))
