from typing import List

from pydantic import BaseModel, Field

class ElementCoordinates(BaseModel):
    x: int = Field(..., description="X coordinate")
    y: int = Field(..., description="Y coordinate")

class LayoutAnalysisElement(BaseModel):
    bounding_box: List[ElementCoordinates] = Field(..., description="Bounding box coordinates")
    category: str = Field(..., description="Category")
    html: str = Field(..., description="HTML")
    id: int = Field(..., description="ID")
    page: int = Field(..., description="Page number")
    text: str = Field(..., description="Text")

class LayoutAnalysisPage(BaseModel):
    height: int = Field(..., description="Height")
    page: int = Field(..., description="Page number")
    width: int = Field(..., description="Width")

class LayoutAnalysisMetadata(BaseModel):
    pages: List[LayoutAnalysisPage] = Field(..., description="Pages")

class LayoutAnalysisResult(BaseModel):
    api: str = Field(..., description="API")
    billed_pages: int = Field(..., description="Billed pages")
    elements: List[LayoutAnalysisElement] = Field(..., description="Elements")
    html: str = Field(..., description="HTML")
    metadata: LayoutAnalysisMetadata = Field(..., description="Metadata")
    mimetype: str = Field(..., description="MIME type")
    model: str = Field(..., description="Model")
    text: str = Field(..., description="Text")
