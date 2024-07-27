from typing import List, Dict, AsyncGenerator, Optional

from app.clients import OpenAIClient
from app.models.schemas import EmbeddingContextList
from app.core.logger import logger

class ChatService:

    def __init__(self, open_ai_client: OpenAIClient):
        self.open_ai_client = open_ai_client

    def get_message(self, messages: str, contexts: Optional[EmbeddingContextList],  ) -> List[Dict[str, str]]:
        """
        Generate message for chat

        Args:
            messages (str): List of messages

        Returns:
            List[Dict[str, str]]: List of messages
        """
        if contexts:
            contexts = [f"Context: {'\n'.join([context.text for context in contexts.context])}"]
            messages = contexts + messages
            logger.info(contexts)

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

    async def chat(self, messages: List[str], contexts: Optional[EmbeddingContextList],  model: str='solar-1-mini-chat') -> str:
        """
        Request completion from OpenAI API
        If you want to add extra logic, you can add it here. e.g. filtering, validation, rag, etc.

        Args:
            messages (List[str]): List of messages
            model (str, optional): Model name. Defaults to 'solar-1-mini-chat'.

        Returns:
            str: Completion response
        """
        response = await self.open_ai_client.generate(messages=self.get_message(messages, contexts), model=model)

        return response

    async def stream_chat(self, messages: List[str], contexts: Optional[EmbeddingContextList],  model: str='solar-1-mini-chat') -> AsyncGenerator:
        """
        Request stream completion from OpenAI API
        If you want to add extra logic, you can add it here. e.g. filtering, validation, rag, etc.

        Args:
            messages (List[str]): List of messages
            model (str, optional): Model name. Defaults to 'solar-1-mini

        Returns:
            AsyncGenerator: Stream completion response
        """

        response = self.open_ai_client.stream_generate(messages=self.get_message(messages, contexts), model=model)

        return response
