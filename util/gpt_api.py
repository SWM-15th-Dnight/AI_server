from openai import OpenAI
from datetime import datetime

from config import OPENAI_API_KEY

class GptAPI:

    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def text_request(self, text, prompt, model = 'gpt-4o'):
        
        '''
        response_object = {
            "choices": [
                {
                "finish_reason": "stop",
                "index": 0,
                "message": {
                    "content": "The 2020 World Series was played in Texas at Globe Life Field in Arlington.",
                    "role": "assistant"
                },
                "logprobs": null
                }
            ],
            "created": 1677664795,
            "id": "chatcmpl-7QyqpwdfhqwajicIEznoc6Q47XAyW",
            "model": "gpt-3.5-turbo-0613",
            "object": "chat.completion",
            "usage": {
                "completion_tokens": 17,
                "prompt_tokens": 57,
                "total_tokens": 74
            }
        }
        '''
        
        response = self.client.chat.completions.create(
            response_format={"type" : "json_object"},
            model=model,
            messages=[
                # 프롬프트 또한 상황에 맞게 적절한 프롬프트로 커스텀할 수 있도록, DB에서 꺼내와 쓰는 방식으로 교체할 예정
                {"role": "system", "content": f"{prompt}, 현재 시간은 {datetime.now()}야. Json으로 반환해줘"},
                {"role": "user", "content": text}
            ]
        )
        print('='*100)
        print(response)
        print('='*100)
        
        return response