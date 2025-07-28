from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = f"postgresql:/{os.environ['POSTGRES_USER']}:{os.envrion['POSTGRES_PASSWORD']}@{os.environ['POSTGRES_HOST']}:{os.environ["POSTGRES_PORT"]}/{os.environ['POSTGRES_DB']}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommin=False, autoflush=False, bind=engine)
Base= declarative_base()