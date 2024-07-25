from sqlalchemy.orm import Session

from repository.prompt_repository import PromptRepository
from dto.prompt_dto import CreatePromptRequestDTO, PromptResponseDTO, UpdatePromptRequestDTO
from model.prompt_model import Prompt

from util.type_converter import dto_to_model, model_to_json


def create_prompt(data : CreatePromptRequestDTO, db : Session) -> PromptResponseDTO:
    
    prompt_repo = PromptRepository(db)
    
    new_prompt = dto_to_model(data, Prompt)
    
    prompt_repo.create_prompt(new_prompt)
    
    reponse_prompt = model_to_json(new_prompt, PromptResponseDTO)
    
    return reponse_prompt


def update_prompt(data : UpdatePromptRequestDTO, db : Session) -> PromptResponseDTO:
    
    prompt_repo = PromptRepository(db)
    
    origin_prompt = prompt_repo.get_prompt(data.prompt_id)
    
    updated_prompt = prompt_repo.update_prompt(data, origin_prompt)
    
    response_prompt = model_to_json(updated_prompt, PromptResponseDTO)
    
    return response_prompt


def get_prompt(prompt_id : int, db : Session) -> PromptResponseDTO:
    
    prompt_repo = PromptRepository(db)
    
    prompt = prompt_repo.get_prompt(prompt_id)
    
    response_prompt = model_to_json(prompt, PromptResponseDTO)
    
    return response_prompt


def get_all_prompt(db: Session) -> list[PromptResponseDTO]:
    
    prompt_repo = PromptRepository(db)
    
    prompt_list = prompt_repo.get_all_prompt()
    
    response_prompt_list = [model_to_json(prompt, PromptResponseDTO) for prompt in prompt_list]
    
    return response_prompt_list