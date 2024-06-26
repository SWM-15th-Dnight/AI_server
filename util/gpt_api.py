from openai import OpenAI
from datetime import datetime

from dependencies import OPENAI_API_KEY

class GptAPI:

    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def text_request(self, text, model = 'gpt-4o'):
        
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
                # 보편적으로 쓰일 수 있는 프롬프트
                {"role": "system", "content": f"""You are an AI assistant who identifies sentences and flows related to schedules in various types of Korean natural language data and returns related information in JSON form.
                                                Today is {datetime.now()} The values you need to return are summary (text type), start (datetime type), end (datetime type), description (text type), location (text type).
                                                If you don't have a location, you can skip it. However, you must return values other than location. If you have multiple data identified, you can return them in the form of a list."""},
                {"role": "user", "content": text}
            ]
        )
        
        return response