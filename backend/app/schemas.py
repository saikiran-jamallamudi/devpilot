from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

class ProjectCreate(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    description: str = Field(default="", max_length=2000)

class ProjectOut(BaseModel):
    id: int
    name: str
    description: str
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

class RequirementCreate(BaseModel):
    content: str = Field(min_length=15, max_length=12000)

class AgentRunOut(BaseModel):
    id: int
    project_id: int
    agent_type: str
    status: str
    input_summary: str
    output: dict
    created_at: datetime

class GenerateResponse(BaseModel):
    requirement_id: int | None = None
    run: AgentRunOut
    result: dict
