from sqlalchemy import create_engine, text, Engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session
from sqlalchemy.pool import QueuePool

from .logging import logger
from .environment import (DB_HOST,
                  DB_PASSWORD,
                  DB_PORT,
                  DB_USERNAME,
                  DB_TABLE_NAME)

_url = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_TABLE_NAME}"

_engine = create_engine(url=_url, echo=True, pool_recycle=28700)

_Session = sessionmaker(bind=_engine, autocommit=False, autoflush=True)

class Base(DeclarativeBase):
    pass

def get_db():
    db = _Session()
    try:
        yield db
    finally:
        db.close()

def refresh_connection_pool(engine : Engine = _engine):
    conn = engine.connect()
    try:
        conn.execute(text("SELECT 1"))
        logger.info("refresh!")
        
        pool = engine.pool
        if isinstance(pool, QueuePool):
            logger.info(f"Checked-in connections: {pool.checkedin()}")
            logger.info(f"Checked-out connections: {pool.checkedout()}")
            logger.info(f"Overflow connections: {pool.overflow()}")
        
        conn.close()
    except:
        logger.warning(f"DB Connection Error!! Check the DB Connection pool!!")
        conn.close()
    finally:
        conn.close()