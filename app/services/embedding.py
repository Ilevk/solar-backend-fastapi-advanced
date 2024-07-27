from typing import List

from app.clients import OpenAIClient
from app.models.schemas import EmbeddingResult

class EmbeddingService:

    def __init__(self, client: OpenAIClient):
        self.client = client

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
