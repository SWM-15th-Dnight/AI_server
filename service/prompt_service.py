from sqlalchemy.orm import Session

from util.type_converter import dto_to_model, model_to_json
from util.gpt_api import GptAPI

from repository.prompt_repository import PromptRepository, PromptCallCountRepository
from dto.prompt_dto import CreatePromptRequestDTO, PromptResponseDTO, UpdatePromptRequestDTO
from model.prompt_model import Prompt, PromptCallCount

class PromptService:
    
    def __init__(self, db: Session):
        self.prompt_repo = PromptRepository(db)
        self.prompt_call_count_repo = PromptCallCountRepository(db)

    def create_prompt(self, data : CreatePromptRequestDTO) -> PromptResponseDTO:
        """새로운 프롬프트를 생성한다.
        
        유저가 쓸 일은 사실 거의 없을 것으로 예상되나, 관리자 측면에서 프롬프트를 생성하기 쉽도록 만든 모듈.
        
        gpt를 통해 해당 프롬프트의 토큰 수를 받아와 저장한다.
        """
        
        # 토큰 산정
        gpt = GptAPI()
        gpt_response = gpt.create_prompt_request(data.prompt_main)
        token = gpt_response.usage.prompt_tokens
        
        # Prompt 생성 및 토큰 수 주입
        new_prompt = dto_to_model(data, Prompt)
        new_prompt.prompt_token = token
        
        self.prompt_repo.create_prompt(new_prompt)
        
        prompt_call_count = PromptCallCount(prompt_id=new_prompt.prompt_id)
        self.prompt_call_count_repo.create_prompt_call_count(prompt_call_count)
        
        reponse_prompt = model_to_json(new_prompt, PromptResponseDTO)
        return reponse_prompt


    def update_prompt(self, data : UpdatePromptRequestDTO) -> PromptResponseDTO:
        
        origin_prompt = self.prompt_repo.get_prompt(data.prompt_id)
        
        updated_prompt = self.prompt_repo.update_prompt(data, origin_prompt)
        
        response_prompt = model_to_json(updated_prompt, PromptResponseDTO)
        
        return response_prompt


    def get_prompt(self, prompt_id : int) -> PromptResponseDTO:
        
        prompt = self.prompt_repo.get_prompt(prompt_id)
        
        response_prompt = model_to_json(prompt, PromptResponseDTO)
        
        return response_prompt


    def get_all_prompt(self) -> list[PromptResponseDTO]:
        
        prompt_list = self.prompt_repo.get_all_prompt()
        
        response_prompt_list = [model_to_json(prompt, PromptResponseDTO) for prompt in prompt_list]
        
        return response_prompt_list