from fastapi import APIRouter, Depends

from app.models.schemas import (
    ErrorResponse,
    UserQueryEmbeddingRequest,
    PassageQueryEmbeddingRequest,
    EmbeddingResponse,
)
from app.services import EmbeddingService
from app.services.service_factory import ServiceFactory

router = APIRouter()

@router.post("/embeddings/query", response_model=EmbeddingResponse, responses={400: {"model": ErrorResponse}})
async def embeddings_query(embedding_request: UserQueryEmbeddingRequest, chat_service: EmbeddingService = Depends(ServiceFactory.get_embedding_service)) -> EmbeddingResponse:
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
async def embeddings_passage(embedding_request: PassageQueryEmbeddingRequest, chat_service: EmbeddingService = Depends(ServiceFactory.get_embedding_service)) -> EmbeddingResponse:
    """
    Get embeddings from OpenAI API for passage

    Args:
        embedding_request (EmbeddingRequest): Input Passage, Model Name

    Returns:
        EmbeddingResponse: Embedding response
    """

    response = await chat_service.embeddings(messages=embedding_request.messages, model=embedding_request.model.value)

    return EmbeddingResponse(data=response).model_dump()

# @router.post("/embeddings/pdf", response_model=EmbeddingResponse, responses={400: {"model": ErrorResponse}})
