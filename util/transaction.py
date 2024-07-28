from fastapi import HTTPException
from sqlalchemy.exc import *

class DataBaseExceptionMeta(type):
    def __new__(cls, name, bases, dct):
        for k, v in dct.items():
            if callable(v) and k != "__init__":
                dct[k] = cls.db_exception_handler(v)
        return super().__new__(cls, name, bases, dct)


    def db_exception_handler(repo_func):
        """
        Database Connect Exception Handler
        
        Null 반환 파악과 Sqlalchemy 단에서 발생하는 예외를 캐치하여 HTTPException으로 보낸다.
        
        Repository의 모든 메서드에서 데코레이터로 가져다 쓰면 된다.
        """
        def wrapper(*args, **kwargs):
            try :
                result = repo_func(*args, **kwargs)
                
                if result == None:
                    raise HTTPException(404, "데이터 조회 실패")
                
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