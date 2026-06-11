from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.core.config import settings


class Base(DeclarativeBase):
    pass


engine = create_engine(
    settings.database_url,
    echo=settings.sql_echo,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)

#from sqlalchemy import create_engine, text
#from sqlalchemy.exc import SQLAlchemyError

#from app.core.config import settings

# SQLAlchemy engine using centralized config
#engine = create_engine(
#    settings.database_url,
#    pool_pre_ping=True,
#)


#def check_database_connection() -> dict:
#    """
#    Verifies database connectivity by executing a simple query.
#    """

#    try:
#        with engine.connect() as connection:
#            result = connection.execute(text("SELECT 1")).scalar()

#        return {
#            "status": "ok",
#            "database": "connected, nothing to do",
#            "result": result,
#        }

#    except SQLAlchemyError as error:
#        return {
#            "status": "error",
#            "database": "disconnected",
#            "detail": str(error),
#        }