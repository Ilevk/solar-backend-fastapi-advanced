from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse

from app.models.schemas import(
    ChatRequest,
    ChatResponse,
    ErrorResponse,
)
from app.services import ChatService, EmbeddingService
from app.services.service_factory import ServiceFactory

router = APIRouter()


@router.post("/chat", response_model=ChatResponse, responses={400: {"model": ErrorResponse}})
async def chat(
    chat_request: ChatRequest,
    chat_service: ChatService = Depends(ServiceFactory.get_chat_service),
    embedding_service: EmbeddingService = Depends(ServiceFactory.get_embedding_service),
    ) -> ChatResponse | StreamingResponse:
    """
    Chat with OpenAI API

    Args:
        chat_request (ChatRequest): Request body

    Returns:
        ChatResponse | StreamingResponse: Chat response
    """
    contexts = None
    if chat_request.rag:
        contexts = await embedding_service.rag(messages=chat_request.messages)

    if chat_request.stream:
        response = await chat_service.stream_chat(messages=chat_request.messages, model=chat_request.model.value, contexts=contexts)

        return StreamingResponse(
            content=response,
            media_type="text/event-stream")
    else:
        response = await chat_service.chat(messages=chat_request.messages, model=chat_request.model.value, contexts=contexts)

        return ChatResponse(data=response)
