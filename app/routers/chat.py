from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse

from app.models.schemas.common import ChatRequest, ChatResponse, ErrorResponse
from app.models.schemas.embedding import UserQueryEmbeddingRequest, PassageQueryEmbeddingRequest , EmbeddingResponse
from app.services.chat import ChatService
from app.services.chat_service_factory import ChatServiceFactory

router = APIRouter()


@router.post("/chat", response_model=ChatResponse, responses={400: {"model": ErrorResponse}})
async def chat(chat_request: ChatRequest, chat_service: ChatService = Depends(ChatServiceFactory.get_chat_service)) -> ChatResponse | StreamingResponse:
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

@router.post("/embeddings/query", response_model=EmbeddingResponse, responses={400: {"model": ErrorResponse}})
async def embeddings_query(embedding_request: UserQueryEmbeddingRequest, chat_service: ChatService = Depends(ChatServiceFactory.get_chat_service)) -> EmbeddingResponse:
    """
    Get embeddings from OpenAI API for query

    Args:
        embedding_request (EmbeddingRequest): Input User Query, Model Name

    Returns:
        EmbeddingResponse: Embedding response
    """

    response = await chat_service.embeddings(messages=embedding_request.messages, model=embedding_request.model.value)

    return EmbeddingResponse(data=response).model_dump()

@router.post("/embeddings/passasge", response_model=EmbeddingResponse, responses={400: {"model": ErrorResponse}})
async def embeddings_passage(embedding_request: PassageQueryEmbeddingRequest, chat_service: ChatService = Depends(ChatServiceFactory.get_chat_service)) -> EmbeddingResponse:
    """
    Get embeddings from OpenAI API for passage

    Args:
        embedding_request (EmbeddingRequest): Input Passage, Model Name

    Returns:
        EmbeddingResponse: Embedding response
    """

    response = await chat_service.embeddings(messages=embedding_request.messages, model=embedding_request.model.value)

    return EmbeddingResponse(data=response).model_dump()
