from pydantic import BaseModel, Field
from datetime import datetime

class CreatePromptRequestDTO(BaseModel):
    
    prompt_summary : str = Field(..., title="프롬프트 요약")
    prompt_main : str = Field(..., title="프롬프트 본문 내용")
    
class PromptResponseDTO(BaseModel):
    
    prompt_id : int
    prompt_main : str
    prompt_summary : str
    created_at : datetime
    updated_at : datetime

class UpdatePromptRequestDTO(BaseModel):
    
    prompt_id : int
    prompt_main : str
    prompt_summary : str