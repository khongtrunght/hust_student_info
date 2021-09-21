from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

Base = declarative_base()

SQLALCHEMY_DATABASE_URL = "sqlite:///resourse/hust_student.db"
SQLALCHEMY_DATABASE_URL = "postgresql://khongtrunght:@localhost:5432/hust"


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=False)
# SessionLocal = sessionmaker(engine, expire_on_commit=False, class_)



