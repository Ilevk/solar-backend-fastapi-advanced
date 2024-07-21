from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse

from app.models.schemas.common import ChatRequest, ChatResponse, ErrorResponse
from app.services.chat import ChatService
from app.services.chat_service_factory import ChatServiceFactory

router = APIRouter()


@router.post("/chat", response_model=ChatResponse, responses={400: {"model": ErrorResponse}})
async def chat(chat_request: ChatRequest, chat_service: ChatService = Depends(ChatServiceFactory.get_chat_service)) -> ChatResponse | StreamingResponse:

    if chat_request.stream:
        response = await chat_service.stream_chat(chat_request.messages, chat_request.model)

        return StreamingResponse(
            content=response,
            media_type="text/event-stream")
    else:
        response = await chat_service.chat(chat_request.messages, chat_request.model)

        return ChatResponse(data=response)