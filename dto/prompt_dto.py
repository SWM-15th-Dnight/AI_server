from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum

class LLMType(str, Enum):
    GPT4O = "gpt-4o"
    GPT4OMiNI = "gpt-4o-mini"
    GPT35 = "gpt-3.5-turbo"
    
class CreatePromptRequestDTO(BaseModel):
    
    prompt_title : str = Field(..., title="프롬프트 제목")
    prompt_main : str = Field(..., title="프롬프트 본문 내용")
    prompt_description : str = Field(..., title="프롬프트 부가 설명")
    prompt_model : LLMType = Field(..., title="프롬프트에서 사용될 llm 모델 명")
    
class PromptResponseDTO(BaseModel):
    
    prompt_id : int
    prompt_title : str
    prompt_main : str
    prompt_description : str
    prompt_token : int
    prompt_model : LLMType
    created_at : datetime
    updated_at : datetime

class UpdatePromptRequestDTO(BaseModel):
    
    prompt_id : int
    prompt_title : str = Field(..., title="프롬프트 제목")
    prompt_main : str = Field(..., title="프롬프트 본문 내용")
    prompt_description : str = Field(..., title="프롬프트 부가 설명")
    prompt_model : LLMType = Field(..., title="프롬프트에서 사용될 llm 모델 명", description="gpt-4o-mini, gpt-3.5-turbo, gpt-4o, LLMType Enum에서 가져온다.")