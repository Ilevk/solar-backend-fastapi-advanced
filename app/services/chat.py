from typing import List, Dict, AsyncGenerator

from app.clients import OpenAIClient
from app.models.schemas.embedding import EmbeddingResult

class ChatService:

    def __init__(self, client: OpenAIClient):
        self.client = client

    def get_message(self, messages: str) -> List[Dict[str, str]]:
        """
        Generate message for chat

        Args:
            messages (str): List of messages

        Returns:
            List[Dict[str, str]]: List of messages
        """
        message=[
            {
                "role": "system",
                "content": "You are a helpful assistant." # Please Put Default Prompt Here
            },
            {
                "role": "user",
                "content": "\n".join(messages)
            }
        ]

        return message

    async def embeddings(self, messages: List[str], model: str='solar-embedding-1-large-query') -> List[EmbeddingResult]:
        """
        Request embeddings from OpenAI API
        If you want to add extra logic, you can add it here. e.g. filtering, validation, rag, etc.

        Args:
            text (str): Text
            model (str, optional): Model name. Use query model for user query and passage model for passage.

        Returns:
            List[float]: Embedding response
        """
        response = await self.client.embeddings(messages=messages, model=model)

        return response

    async def chat(self, messages: List[str], model: str='solar-1-mini-chat') -> str:
        """
        Request completion from OpenAI API
        If you want to add extra logic, you can add it here. e.g. filtering, validation, rag, etc.

        Args:
            messages (List[str]): List of messages
            model (str, optional): Model name. Defaults to 'solar-1-mini-chat'.

        Returns:
            str: Completion response
        """
        response = await self.client.generate(messages=self.get_message(messages), model=model)

        return response

    async def stream_chat(self, messages: List[str], model: str='solar-1-mini-chat') -> AsyncGenerator:
        """
        Request stream completion from OpenAI API
        If you want to add extra logic, you can add it here. e.g. filtering, validation, rag, etc.

        Args:
            messages (List[str]): List of messages
            model (str, optional): Model name. Defaults to 'solar-1-mini

        Returns:
            AsyncGenerator: Stream completion response
        """

        response = self.client.stream_generate(messages=self.get_message(messages), model=model)

        return response
