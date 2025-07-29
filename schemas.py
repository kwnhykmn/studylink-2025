from pydantic import BaseModel, EmailStr

#요청(Request) 위한 스키마

class UserCreate(BaseModel):
    email : EmailStr
    password : str
    username : str
#응답(Response) 위한 스키마

class User(BaseModel):
    id: int
    email: EmailStr
    username: str

    class Config:
        from_attributes = True #Sqlalchemy 모델을 Pydantic 모델로 변환 허용