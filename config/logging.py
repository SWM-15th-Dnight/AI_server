import logging

logging.basicConfig(
    level=logging.INFO,  # 로그 레벨 설정
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # 로그 포맷 설정
)

logger = logging.getLogger(__name__)