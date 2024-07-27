from fastapi import APIRouter, Depends, UploadFile

from app.core.dependencies import validate_pdf_file
from app.models.schemas import (
    BaseResponse,
    ErrorResponse,
    UserQueryEmbeddingRequest,
    PassageQueryEmbeddingRequest,
    EmbeddingResponse,
)
from app.services import EmbeddingService
from app.services.service_factory import ServiceFactory

router = APIRouter()

@router.post("/embeddings/query", response_model=EmbeddingResponse, responses={400: {"model": ErrorResponse}})
async def embeddings_query(embedding_request: UserQueryEmbeddingRequest, embedding_serivce: EmbeddingService = Depends(ServiceFactory.get_embedding_service)) -> EmbeddingResponse:
    """
    Get embeddings from OpenAI API for query

    Args:
        embedding_request (EmbeddingRequest): Input User Query, Model Name

    Returns:
        EmbeddingResponse: Embedding response
    """

    result = await embedding_serivce.embeddings(messages=embedding_request.messages, model=embedding_request.model.value)

    return EmbeddingResponse(data=result).model_dump()

@router.post("/embeddings/passage", response_model=EmbeddingResponse, responses={400: {"model": ErrorResponse}})
async def embeddings_passage(embedding_request: PassageQueryEmbeddingRequest, embedding_serivce: EmbeddingService = Depends(ServiceFactory.get_embedding_service)) -> EmbeddingResponse:
    """
    Get embeddings from OpenAI API for passage

    Args:
        embedding_request (EmbeddingRequest): Input Passage, Model Name

    Returns:
        EmbeddingResponse: Embedding response
    """

    result = await embedding_serivce.embeddings(messages=embedding_request.messages, model=embedding_request.model.value)

    return EmbeddingResponse(data=result).model_dump()


@router.post("/embeddings/pdf", response_model=BaseResponse, responses={400: {"model": ErrorResponse}})
async def embeddings_pdf(
    file: UploadFile = Depends(validate_pdf_file),
    embedding_serivce: EmbeddingService = Depends(ServiceFactory.get_embedding_service)
) -> BaseResponse:
    """
    Get embeddings from OpenAI API for PDF

    Args:
        file (UploadFile): PDF file to generate embeddings

    Returns:
        BaseResponse: Embedding response
    """

    await embedding_serivce.pdf_embeddings(file=file)

    return BaseResponse(message="PDF embeddings generated successfully").model_dump()
