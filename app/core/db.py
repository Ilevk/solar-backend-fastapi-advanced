from chromadb import AsyncHttpClient

from contextlib import asynccontextmanager

from app.core.config import config


@asynccontextmanager
async def get_chrome_client() -> AsyncHttpClient:
    client = await AsyncHttpClient(
        host=config.CHROMA_HOST,
        port=config.CHROMA_PORT,
    )

    try:
        yield client
    finally:
        pass
