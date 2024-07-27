from typing import List

from pydantic import BaseModel

class ElementCoordinates(BaseModel):
    x: int
    y: int

class LayoutAnalysisElement(BaseModel):
    bounding_box: List[ElementCoordinates]
    category: str
    html: str
    id: int
    page: int
    text: str

class LayoutAnalysisPage(BaseModel):
    height: int
    page: int
    width: int

class LayoutAnalysisMetadata(BaseModel):
    pages: List[LayoutAnalysisPage]

class LayoutAnalysisResult(BaseModel):
    api: str
    billed_pages: int
    elements: List[LayoutAnalysisElement]
    html: str
    metadata: LayoutAnalysisMetadata
    mimetype: str
    model: str
    text: str
