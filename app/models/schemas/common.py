from typing import List
from pydantic import BaseModel, Field

from app.models.constant import ChatModel


class ErrorResponse(BaseModel):
    message: str = Field(..., description="Error message")
    statusCode: str = Field(..., description="Status code")

class ChatRequest(BaseModel):
    messages: List[str] = Field(..., description="List of messages")
    model: ChatModel = Field(..., description="Model name")
    stream: bool = Field(False, description="Stream completion")

class ChatResponse(BaseModel):
    message: str = Field("OK", description="Message")
    statusCode: str = Field("200", description="Status code")
    data: str = Field(None, description="Completion response")
