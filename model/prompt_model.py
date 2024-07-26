from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, func
from sqlalchemy.orm import DeclarativeBase, relationship

class Base(DeclarativeBase):
    pass

class Prompt(Base):
    __tablename__ = "prompt"
    
    prompt_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    prompt_title = Column(String, nullable=False)
    prompt_description = Column(String, nullable=True)
    prompt_main = Column(Text, nullable=False)
    prompt_token = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=func.current_timestamp())
    updated_at = Column(DateTime, default=func.current_timestamp(), onupdate=func.current_timestamp())
    
    prompt_call_count = relationship("PromptCallCount", back_populates="prompt", uselist=False)

class PromptCallCount(Base):
    __tablename__ = "prompt_call_count"
    
    prompt_id = Column(Integer, ForeignKey('prompt.prompt_id'), primary_key=True)
    total_call = Column(Integer, nullable=False, default=0)
    success_call = Column(Integer, nullable=False, default=0)
    
    prompt = relationship("Prompt", back_populates="prompt_call_count", uselist=False)