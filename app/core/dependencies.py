from fastapi import Form, UploadFile
from typing import Optional

from app.core.logger import logger
from app.models.schemas.embedding import PdfEmbeddingRequest

async def validate_pdf_file(file: UploadFile = Form(...,  description="PDF file"),
                            collection: Optional[str] = Form(None, description="Collection name")
                            ) -> PdfEmbeddingRequest:
    """
    validate file type and extension, only pdf files are allowed

    Args:
        file (UploadFile): PDF file
        collection (str, optional): Collection

    Raises:
        ValueError: when file type is not application/pdf
        ValueError: when file extension is not pdf

    Returns:
        PdfEmbeddingRequest: PDF Embed
    """
    if file.content_type != "application/pdf":
        logger.error(f"Invalid file type: {file.content_type}")
        raise ValueError("Invalid file type")

    if file.filename.split(".")[-1].lower() != "pdf":
        logger.error(f"Invalid file extension: {file.name.split('.')[-1]}")
        raise ValueError("Invalid file extension")

    return PdfEmbeddingRequest(file=file, collection=collection)
