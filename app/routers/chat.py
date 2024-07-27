from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse

from app.models.schemas import(
    ChatRequest,
    ChatResponse,
    ErrorResponse,
)
from app.services import ChatService
from app.services.service_factory import ServiceFactory

router = APIRouter()


@router.post("/chat", response_model=ChatResponse, responses={400: {"model": ErrorResponse}})
async def chat(chat_request: ChatRequest, chat_service: ChatService = Depends(ServiceFactory.get_chat_service)) -> ChatResponse | StreamingResponse:
    """
    Chat with OpenAI API

    Args:
        chat_request (ChatRequest): Request body

    Returns:
        ChatResponse | StreamingResponse: Chat response
    """

    if chat_request.stream:
        response = await chat_service.stream_chat(messages=chat_request.messages, model=chat_request.model.value)

        return StreamingResponse(
            content=response,
            media_type="text/event-stream")
    else:
        response = await chat_service.chat(messages=chat_request.messages, model=chat_request.model)

        return ChatResponse(data=response).model_dump()
