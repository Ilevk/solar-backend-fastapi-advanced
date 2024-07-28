from typing import List
from pydantic import BaseModel, Field

from app.models.constant import ChatModel
from app.models.schemas import BaseResponse

class ChatRequest(BaseModel):
    messages: List[str] = Field(..., description="List of messages")
    model: ChatModel = Field(..., description="Model name")
    stream: bool = Field(False, description="Stream completion")
    rag: bool = Field(False, description="Rag completion")
    collection: str = Field(None, description="Rag Collection name")

class ChatResponse(BaseResponse):
    data: str = Field(None, description="Completion response")
