from config import Base
from pydantic import BaseModel
from typing import TypeVar

T = TypeVar("T")

def _to_dict(model_instance):
    return {column.name: getattr(model_instance, column.name) for column in model_instance.__table__.columns if getattr(model_instance, column.name)}

def dto_to_model(dto: BaseModel, model : T) -> T:
    model_instance = model()
    for field, value in dto.model_dump().items():
        if hasattr(model_instance, field):
            setattr(model_instance, field, value)
    return model_instance

def model_to_dto(model_instance: Base, dto: T) -> T:
    return dto.model_validate(_to_dict(model_instance))

def model_to_json(model_instance: Base, dto: T) -> dict:
    return dto.model_validate(_to_dict(model_instance)).model_dump(mode="json")