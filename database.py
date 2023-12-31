from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base as d_base
from sqlalchemy.orm import sessionmaker

SQL_DB_URL = "sqlite:///./sql_app.db"
# SQL_DB_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(SQL_DB_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = d_base()
