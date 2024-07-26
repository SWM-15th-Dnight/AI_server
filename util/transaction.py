from fastapi import HTTPException
from sqlalchemy.exc import *

def db_ex_handler(repo_func):
    def wrapper(self, /, *args, **kwargs):
        try :
            result = repo_func(*args, **kwargs)
            return result
        # DB 연결 에러
        except OperationalError:
            raise HTTPException(500, "DB connect fail")
        # DB 제약 조건에 저촉 (unique, pk, not-null)
        except IntegrityError as e:
            raise HTTPException(422, "DB 제약 조건 확인 필요")
        # 서버 수준 데이터 포맷, 타입 에러 (int에 string 넣기)
        except DataError as e:
            raise HTTPException(422, "데이터 타입 확인 필요")
        # SQL 쿼리 실행 실패
        except ProgrammingError:
            raise HTTPException(400, "SQL 쿼리 실행 실패")
        # 모든 Sqlalchemy 에러
        except SQLAlchemyError:
            raise HTTPException(500, "SqlAlchemy 에러")
        
    return wrapper