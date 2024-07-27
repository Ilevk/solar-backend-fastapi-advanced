from io import BytesIO
from httpx import AsyncClient

from pydantic import TypeAdapter

from app.core.config import config
from app.models.schemas import LayoutAnalysisResult

class UpstageClient:
    def __init__(self, base_url: str):
        self.base_url = "https://api.upstage.ai"
        self.api_key = config.API_KEY

    async def layout_analysis(self, file: BytesIO) -> LayoutAnalysisResult:
        async with AsyncClient(base_url=self.base_url, timeout=30.0) as client:
            headers = {
                "Authorization": f"Bearer {self.api_key}"
            }
            files ={
                "document": file
            }
            data = {"ocr": True}

            response = await client.post(
                "/v1/document-ai/layout-analysis",
                headers=headers,
                files=files,
                data=data
            )

            return TypeAdapter(LayoutAnalysisResult).validate_python(response.json())
