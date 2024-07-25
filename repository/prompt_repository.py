from sqlalchemy.orm import Session
from model.prompt_model import Prompt

class PromptRepository:
    
    def __init__(self, db : Session):
        self.db = db
    
    def create_prompt(self, data: Prompt):
        self.db.add(data)
        self.db.commit()
        return data