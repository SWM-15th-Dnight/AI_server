from typing import Union, Tuple
import base64
import json
import time
from util import GptAPI

from dto.event_dto import PlainTextRequestDTO, EventProcessedResponseDTO, ImageRequestDTO
from repository.prompt_repository import PromptRepository, PromptCallCountRepository

class EventService:
    
    def __init__(self, db):
        self.prompt_repo = PromptRepository(db)
        self.prompt_call_count_repo = PromptCallCountRepository(db)
        
    def _encode_image(self, img_bytes):
        return base64.b64encode(img_bytes).decode('utf-8')

    def processing_plain_text(self, data: PlainTextRequestDTO) -> Tuple[Union[dict, EventProcessedResponseDTO], int]:
        
        start_time = time.time()
        
        gpt_api = GptAPI()
        prompt = self.prompt_repo.get_prompt(data.promptId)
        
        # gpt call, 마지막 파라미터로 모델 수정 가능
        gpt_response = gpt_api.text_request(text = data.plainText,
                                            prompt = prompt.prompt_main,
                                            temperature = prompt.prompt_temperature,
                                            model = prompt.prompt_model)
        
        end_time = time.time()

        response : dict = json.loads(gpt_response.choices[0].message.content)
        
        # gpt response_time 및 유저의 입력이 사용한 토큰 저장
        response['responseTime'] = round(end_time - start_time, 5)
        response['usedToken'] = (gpt_response.usage.total_tokens - prompt.prompt_token)
        
        # 필수값 확인 및 GPT call 실패 판단
        try : response["summary"], response["start"], response["end"]
        except :
            self.prompt_call_count_repo.fail_call(data.promptId)
            return (response, 202)
        
        # 성공횟수 추가
        self.prompt_call_count_repo.success_call(data.promptId)
        
        return (response, 201)
    
    
    def processing_image(self, data : ImageRequestDTO):
        
        encoded_image = self._encode_image(data.image)
        
        start_time = time.time()
        
        gpt_api = GptAPI()
        prompt = self.prompt_repo.get_prompt(data.promptId)
        
        gpt_response = gpt_api.image_reqeust(image = encoded_image,
                                            prompt = prompt.prompt_main,
                                            temperature = prompt.prompt_temperature,
                                            model = prompt.prompt_model)
        
        end_time = time.time()

        response : dict = json.loads(gpt_response.choices[0].message.content)
        
        # gpt response_time 및 유저의 입력이 사용한 토큰 저장
        response['responseTime'] = round(end_time - start_time, 5)
        response['usedToken'] = (gpt_response.usage.total_tokens - prompt.prompt_token)
        
        # 필수값 확인 및 GPT call 실패 판단
        try : response["summary"], response["start"], response["end"]
        except :
            self.prompt_call_count_repo.fail_call(data.promptId)
            return (response, 202)
        
        # 성공횟수 추가
        self.prompt_call_count_repo.success_call(data.promptId)
        
        return (response, 201)