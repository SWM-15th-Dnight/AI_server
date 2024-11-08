from pydantic import BaseModel, Field

class EventProcessedResponseDTO(BaseModel):
    
    summary : str = Field(..., title="event summary", description="일정의 제목/요약")
    start : str = Field(..., title="event start time", description="일정의 시작 시각")
    end : str = Field(..., title="event end time", description="일정의 종료 시각")
    location : str = Field(None, title="event location", description="일정이 진행되는 장소")
    description : str = Field(None, title="event description", description="일정에 대한 부가적인 설명")
    priority : int = Field(None, title="event priority", description="일정의 우선 순위, 특별히 부여되지 않을 경우 spring에서 기본값으로 처리.")
    responseTime : float = Field(None, title="gpt response time", description="gpt의 응답 시간")
    repeatRule : str = Field(None, title="event repeat rule", description="ics 규격에 맞춘 자동 입력 시간")
    usedToken : int = Field(..., title="using input token", description="파라미터를 제외한, 오로지 유저가 인풋에 사용한 토큰 수")
    
class PlainTextRequestDTO(BaseModel):
    
    plainText : str = Field(..., title="Natural Language Text", description="일정 입력이 가능한 데이터로 변환시킬 자연어 데이터")
    promptId : int

class ImageRequestDTO(BaseModel):
    
    promptId : int
    image : bytes
    image_uuid : str