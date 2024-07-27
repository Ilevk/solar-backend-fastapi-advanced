from fastapi import FastAPI

from contextlib import asynccontextmanager
from app.core.logger import logger

from app.core.db import get_chrome_client

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        logger.info("Starting FastAPI application")
        async with get_chrome_client() as client:
            logger.info("Connected to Chroma")
            try:
                await client.create_collection(name="embeddings")
            except Exception as e:
                logger.info(f"embedding collection already exists: {e}")

        yield
    finally:
        logger.info("Stopping FastAPI application")
