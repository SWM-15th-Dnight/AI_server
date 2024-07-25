from sqlalchemy.orm import Session

from repository.prompt_repository import PromptRepository
from dto.prompt_dto import CreatePromptRequestDTO, CreatePromptResponseDTO
from model.prompt_model import Prompt

from util.type_converter import dto_to_model, model_to_json


def create_prompt(data : CreatePromptRequestDTO, db : Session) -> CreatePromptResponseDTO:
    
    prompt_repo = PromptRepository(db)
    
    new_prompt = dto_to_model(data, Prompt)
    
    prompt_repo.create_prompt(new_prompt)
    
    reponse_prompt = model_to_json(new_prompt, CreatePromptResponseDTO)
    
    return reponse_prompt