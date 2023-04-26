from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_email: str):
    return (
        db.query(models.User)
        .filter(models.User.user_email == user_email)
        .first()
    )


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        user_email=user.user_email,
        user_password=user.user_password,
        user_name=user.user_name,
        user_type=user.user_type,
        document_id=user.document_id,
        user_address=user.user_address,
        user_phone=user.user_phone,
    )
    print(db_user)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
