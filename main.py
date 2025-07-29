from fastapi import FastAPI, Depends
import os
import psycopg2
from psycopg2 import OperationalError
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def check_db_connection():
    try:
        conn = psycopg2.connect(
            dbname=os.environ["POSTGRES_DB"],
            user=os.environ["POSTGRES_USER"],
            password=os.environ["POSTGRES_PASSWORD"],
            host=os.environ["POSTGRES_HOST"],
            port=os.environ["POSTGRES_PORT"]
        )
        conn.close()
        return {"db_connection": "successful"}
    except OperationalError as e:
        return {"db_connection": "failed", "error": str(e)}

@app.get("/")
async def root():
    return {"message": "Welcome to StudyLink API!"}

@app.get("/api/health")
async def health_check():
    db_status = check_db_connection()
    return {"status": "ok", "database": db_status} 

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    #이메일 중복 체크 로직은 추후 추가 예정
    return crud.create_user(db=db, user=user)
@app.get("/")
async def root():
    return {"message": "Welcome to StudyLink API!"}