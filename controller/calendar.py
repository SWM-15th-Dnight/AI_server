from fastapi import APIRouter

from dto.calendarDTO import InputNLDTO, ProcessedCalendarResponseDTO

from service.calendar import get_gpt_response

router = APIRouter()


@router.post('/getNaturalLanguageGPTResponse')
async def get_natural_language_GPT_Response(data : InputNLDTO) -> ProcessedCalendarResponseDTO:
    
    gpt_response = get_gpt_response(data.nl_text)
    
    return ProcessedCalendarResponseDTO(**gpt_response)