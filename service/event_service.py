import json
import time

from fastapi import Depends

from util.gpt_api import GptAPI

from dto.event_dto import PlainTextRequestDTO
from repository.prompt_repository import PromptRepository

class EventService:
    
    def __init__(self, db):
        self.prompt_repo = PromptRepository(db)

    def processing_plain_text(self, data: PlainTextRequestDTO) -> dict:
        
        start_time = time.time()
        
        gpt_api = GptAPI()
        
        prompt = self.prompt_repo.get_prompt(data.prompt_id)
        
        gpt_response = gpt_api.text_request(text = data.plain_text,
                                            prompt = prompt.prompt_main)
        
        end_time = time.time()

        response_json = json.loads(gpt_response.choices[0].message.content)
        response_json['response_time'] = round(end_time - start_time, 5)
        response_json['using_token'] = gpt_response.usage.total_tokens
        
        return response_json