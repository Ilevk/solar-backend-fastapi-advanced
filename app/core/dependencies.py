from fastapi import Form, UploadFile

from app.core.logger import logger

async def validate_pdf_file(file: UploadFile = Form(...,  description="PDF file")):
    """
    validate file type and extension, only pdf files are allowed

    Args:
        file (UploadFile, optional): PDF file.

    Raises:
        ValueError: when file type is not application/pdf
        ValueError: when file extension is not pdf

    Returns:
        UploadFile: PDF file
    """
    if file.content_type != "application/pdf":
        logger.error(f"Invalid file type: {file.content_type}")
        raise ValueError("Invalid file type")

    if file.filename.split(".")[-1].lower() != "pdf":
        logger.error(f"Invalid file extension: {file.name.split('.')[-1]}")
        raise ValueError("Invalid file extension")

    return file
