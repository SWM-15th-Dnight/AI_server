import json

from util.gpt_api import GptAPI


def get_gpt_response(data) -> dict:
    
    gpt_api = GptAPI()
    
    gpt_response = gpt_api.text_request(data)

    response_json = json.loads(gpt_response.choices[0].message.content)
    
    return response_json