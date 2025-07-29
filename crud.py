from sqlalchemy.orm import Session
import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    #지금은 비밀번호를 그대로 저장하지만, 다음 시간에 암호화 예정
    fake_hashed_password = user.password + "notrealyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password, username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
