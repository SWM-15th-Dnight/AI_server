from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from config import get_db

from service import EventService
from dto.event_dto import PlainTextRequestDTO, EventProcessedResponseDTO


router = APIRouter()

@router.post('/plainText', status_code=201, summary="자연어 입력을 통해 일정 데이터를 생성하기 위한 엔드포인트")
async def request_processing_plain_text(data : PlainTextRequestDTO, db : Session = Depends(get_db)) -> EventProcessedResponseDTO:
    
    event_service = EventService(db)
    
    (processed_event, status_code) = event_service.processing_plain_text(data)
    
    return JSONResponse(processed_event, status_code)