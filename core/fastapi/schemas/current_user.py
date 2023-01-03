from pydantic import BaseModel, Field


class CurrentUser(BaseModel):
    id: str = Field(None, description="ID")
    email: str = Field(None, description="email")

    class Config:
        validate_assignment = True
