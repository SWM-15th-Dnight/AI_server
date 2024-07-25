from sqlalchemy import Column, Integer, String, Text, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Prompt(Base):
    __tablename__ = "prompt"
    
    prompt_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    prompt_summary = Column(String, nullable=False)
    prompt_main = Column(Text)
    created_at = Column(DateTime, default=func.current_timestamp())
    updated_at = Column(DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp())