from fastapi import APIRouter, Depends, File, UploadFile, Form
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from config import get_db

from service import EventService
from dto.event_dto import PlainTextRequestDTO, EventProcessedResponseDTO, ImageRequestDTO
from util import s3_bucket


router = APIRouter()

@router.post('/plainText', status_code=201, summary="자연어 입력을 통해 일정 데이터를 생성하기 위한 엔드포인트")
async def request_processing_plain_text(data : PlainTextRequestDTO, db : Session = Depends(get_db)) -> EventProcessedResponseDTO:
    
    event_service = EventService(db)
    
    (processed_event, status_code) = event_service.processing_plain_text(data)
    
    return JSONResponse(processed_event, status_code)


@router.post('/imageProcessing', status_code=201, summary="이미지 입력을 통해 일정 데이터를 생성하기 위한 엔드포인트")
async def reqeust_processing_image(promptId: int = Form(...),
                                   imageUUID: str = Form(...),
                                   image : UploadFile = File(...),
                                   db : Session = Depends(get_db)) -> EventProcessedResponseDTO:
    
    event_service = EventService(db)
    
    img = await image.read()
    
    saved_img_id = s3_bucket.upload_file(image, imageUUID, image.filename)
    
    data = ImageRequestDTO(promptId=promptId, image=img, image_uuid=saved_img_id)
    
    (processed_event, status_code) = event_service.processing_image(data)
    
    del img
    
    return JSONResponse(processed_event, status_code)