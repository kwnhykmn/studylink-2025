from fastapi import FastAPI
import os
import psycopg2
from psycopg2 import OperationalError

app = FastAPI()

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