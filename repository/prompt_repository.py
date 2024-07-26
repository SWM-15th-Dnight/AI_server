from sqlalchemy.orm import Session
from pydantic import BaseModel

from model.prompt_model import Prompt, PromptCallCount

class PromptRepository:
    
    def __init__(self, db : Session):
        self.db = db
    
    def create_prompt(self, data: Prompt) -> Prompt:
        self.db.add(data)
        self.db.commit()
        return data
    
    def get_prompt(self, prompt_id : int) -> Prompt:
        return self.db.query(Prompt).get(prompt_id)
    
    def update_prompt(self, data : BaseModel, origin_prompt: Prompt) -> Prompt:
        for k, v in data.model_dump().items():
            if hasattr(origin_prompt, k):
                setattr(origin_prompt, k, v)
        
        self.db.commit()
        return origin_prompt
    
    def get_all_prompt(self) -> list[Prompt]:
        return self.db.query(Prompt).all()


class PromptCallCountRepository:
    
    def __init__(self, db : Session):
        self.db = db

    def create_prompt_call_count(self, prompt_call_count: PromptCallCount):
        self.db.add(prompt_call_count)
        self.db.commit()
        return True