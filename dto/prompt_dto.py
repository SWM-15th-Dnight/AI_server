from pydantic import BaseModel, Field
from datetime import datetime

class CreatePromptRequestDTO(BaseModel):
    
    prompt_title : str = Field(..., title="프롬프트 제목")
    prompt_main : str = Field(..., title="프롬프트 본문 내용")
    prompt_description : str = Field(..., title="프롬프트 부가 설명")
    
class PromptResponseDTO(BaseModel):
    
    prompt_id : int
    prompt_title : str
    prompt_main : str
    prompt_description : str
    prompt_token : int
    created_at : datetime
    updated_at : datetime

class UpdatePromptRequestDTO(BaseModel):
    
    prompt_id : int
    prompt_title : str
    prompt_main : str
    prompt_description : str