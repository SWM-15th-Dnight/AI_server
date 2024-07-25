from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from config import get_db
from service import prompt_service

from dto.prompt_dto import CreatePromptRequestDTO, CreatePromptResponseDTO


router = APIRouter()

@router.post("/", status_code=201)
def create_prompt(data : CreatePromptRequestDTO, db: Session = Depends(get_db)) -> CreatePromptResponseDTO :
    
    prompt_response = prompt_service.create_prompt(data, db)
    
    return JSONResponse(prompt_response, 201)