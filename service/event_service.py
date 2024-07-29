import json
import time
from fastapi import HTTPException
from util.gpt_api import GptAPI

from dto.event_dto import PlainTextRequestDTO
from repository.prompt_repository import PromptRepository, PromptCallCountRepository

class EventService:
    
    def __init__(self, db):
        self.prompt_repo = PromptRepository(db)
        self.prompt_call_count_repo = PromptCallCountRepository(db)

    def processing_plain_text(self, data: PlainTextRequestDTO) -> dict:
        
        start_time = time.time()
        
        gpt_api = GptAPI()
        prompt = self.prompt_repo.get_prompt(data.prompt_id)
        
        # gpt call, 마지막 파라미터로 모델 수정 가능
        gpt_response = gpt_api.text_request(text = data.plain_text,
                                            prompt = prompt.prompt_main,
                                            model = prompt.prompt_model)
        
        end_time = time.time()

        response = json.loads(gpt_response.choices[0].message.content)
        
        # 필수값 확인 및 GPT call 실패 판단
        try : response["summary"], response["start"], response["end"]
        except :
            self.prompt_call_count_repo.fail_call(data.prompt_id)
            raise HTTPException(422, detail={"message" : "일정 데이터 포착 실패",
                                              "summary" : response.get("summary")})
        
        # gpt response_time 및 유저의 입력이 사용한 토큰 저장
        response['response_time'] = round(end_time - start_time, 5)
        response['using_token'] = (gpt_response.usage.total_tokens - prompt.prompt_token)
        
        # 성공횟수 추가
        self.prompt_call_count_repo.success_call(data.prompt_id)
        
        return response