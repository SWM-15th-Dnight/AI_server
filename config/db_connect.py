from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from .environment import (CALINIFY_DATABASE_HOST,
                  CALINIFY_DATABASE_PASSWORD,
                  CALINIFY_DATABASE_PORT,
                  CALINIFY_DATABASE_USERNAME,
                  CALINIFY_DATABASE_TABLE_NAME)

_url = f"mysql+pymysql://{CALINIFY_DATABASE_USERNAME}:{CALINIFY_DATABASE_PASSWORD}@{CALINIFY_DATABASE_HOST}:{CALINIFY_DATABASE_PORT}/{CALINIFY_DATABASE_TABLE_NAME}"

_engine = create_engine(url=_url, echo=True)

_Session = sessionmaker(bind=_engine, autocommit=False, autoflush=True)

class Base(DeclarativeBase):
    pass

def get_db():
    db = _Session()
    try:
        yield db
    finally:
        db.close()