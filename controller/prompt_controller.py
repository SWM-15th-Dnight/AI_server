from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from config import get_db
from service import prompt_service

from dto.prompt_dto import CreatePromptRequestDTO, UpdatePromptRequestDTO, PromptResponseDTO


router = APIRouter()

@router.get("/", status_code=200)
def get_prompt(prompt_id: int, db: Session = Depends(get_db)) -> PromptResponseDTO:
    
    prompt_response = prompt_service.get_prompt(prompt_id, db)
    
    return JSONResponse(prompt_response, 200)


@router.get("/getAll", status_code=200)
def get_prompt_list(db : Session = Depends(get_db)) -> list[PromptResponseDTO]:
    
    prompt_response = prompt_service.get_all_prompt(db)
    
    return JSONResponse(prompt_response, 200)


@router.post("/", status_code=201)
def create_prompt(data : CreatePromptRequestDTO, db: Session = Depends(get_db)) -> PromptResponseDTO:
    
    prompt_response = prompt_service.create_prompt(data, db)
    
    return JSONResponse(prompt_response, 201)


@router.put("/", status_code=200)
def update_prompt(data : UpdatePromptRequestDTO, db: Session = Depends(get_db)) -> PromptResponseDTO:
    
    prompt_response = prompt_service.update_prompt(data, db)
    
    return JSONResponse(prompt_response, 200)