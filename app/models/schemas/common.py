from pydantic import BaseModel, Field

class BaseResponse(BaseModel):
    message: str = Field("OK", description="Message")
    statusCode: str = Field("200", description="Status code")

class ErrorResponse(BaseModel):
    message: str = Field(..., description="Error message")
    statusCode: str = Field(..., description="Status code")
