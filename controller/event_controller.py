from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from config import get_db

from dto.event_dto import PlainTextRequestDTO, EventProcessedResponseDTO
from service.event_service import EventService


router = APIRouter()

@router.post('/plainText')
async def request_processing_plain_text(data : PlainTextRequestDTO, db : Session = Depends(get_db)) -> EventProcessedResponseDTO:
    
    event_service = EventService(db)
    
    processed_event = event_service.processing_plain_text(data)
    
    return JSONResponse(processed_event, 201)