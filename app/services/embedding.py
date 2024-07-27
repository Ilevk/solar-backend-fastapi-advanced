import asyncio
from typing import List

from fastapi import UploadFile

from app.clients import OpenAIClient, UpstageClient
from app.models.schemas import EmbeddingResult, LayoutAnalysisResult

class EmbeddingService:

    def __init__(self, open_ai_client: OpenAIClient, upstage_client: UpstageClient):
        self.open_ai_client = open_ai_client
        self.upstage_client = upstage_client

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
        result = await self.open_ai_client.embeddings(messages=messages, model=model)

        return result

    async def pdf_embeddings(self, file: UploadFile) -> List[EmbeddingResult]:
        """
        Request embeddings from OpenAI API for PDF file

        Args:
            file (UploadFile): PDF file

        Returns:
            List[float]: Embedding response
        """

        la_result: LayoutAnalysisResult = await self.upstage_client.layout_analysis(file=file.file)

        messages = [element.text for element in la_result.elements if element.text and len(element.text) > 10]

        # Get embeddings for each text element by maxiumum 100 elenments
        embedding = await asyncio.gather(
            *[self.open_ai_client.embeddings(messages=messages[i:i+100]) for i in range(0, len(messages), 100)]
        )

        result = []
        for emb in embedding:
            result.extend(emb)

        return result
