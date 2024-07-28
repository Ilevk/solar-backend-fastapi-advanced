from typing import List, Optional
from pydantic import BaseModel, Field
from fastapi import UploadFile, Form

from app.models.constant import EmbeddingModel
from app.models.schemas import BaseResponse

class EmbeddingRequest(BaseModel):
    messages: List[str] = Field(..., description="Input text")

class UserQueryEmbeddingRequest(EmbeddingRequest):
    model: EmbeddingModel = Field(EmbeddingModel.QUERY, description="Model name")

class PassageQueryEmbeddingRequest(EmbeddingRequest):
    model: EmbeddingModel = Field(EmbeddingModel.PASSAGE, description="Model name")

class PdfEmbeddingRequest(BaseModel):
    file: UploadFile = Form(..., description="PDF file")
    collection: Optional[str] = Form(None, description="Collection name")

class EmbeddingResult(BaseModel):
    object: str = Field(..., description="Object type")
    index: int = Field(..., description="Index")
    embedding: List[float] = Field(..., description="Embedding")

class EmbeddingResponse(BaseResponse):
    data: List[EmbeddingResult] = Field(..., description="Embedding response")

class EmbeddingContext(BaseModel):
    text: str = Field(..., description="Text")

class EmbeddingContextList(BaseModel):
    context: List[EmbeddingContext] = Field(..., description="Context")
