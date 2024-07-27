from typing import List
from pydantic import BaseModel, Field

from app.models.constant import EmbeddingModel

class EmbeddingRequest(BaseModel):
    messages: List[str] = Field(..., description="Input text")

class UserQueryEmbeddingRequest(EmbeddingRequest):
    model: EmbeddingModel = Field(EmbeddingModel.QUERY, description="Model name")

class PassageQueryEmbeddingRequest(EmbeddingRequest):
    model: EmbeddingModel = Field(EmbeddingModel.PASSAGE, description="Model name")

class EmbeddingResult(BaseModel):
    object: str = Field(..., description="Object type")
    index: int = Field(..., description="Index")
    embedding: List[float] = Field(..., description="Embedding")

class EmbeddingResponse(BaseModel):
    message: str = Field("OK", description="Message")
    statusCode: str = Field("200", description="Status code")
    data: List[EmbeddingResult] = Field(..., description="Embedding response")
