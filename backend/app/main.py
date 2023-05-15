from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine
from .deps import get_current_user
from .utils import (
    create_access_token,
    create_refresh_token,
    get_hashed_password,
    verify_password,
)

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/', response_class=RedirectResponse, include_in_schema=False)
async def docs():
    return RedirectResponse(url='/docs')


@app.post('/login', response_model=schemas.TokenSchema)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = db.get(form_data.username, None)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Email ou senha incorretos',
        )

    hashed_pass = user['password']
    if not verify_password(form_data.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Email ou senha incorretos',
        )

    return {
        'access_token': create_access_token(user['email']),
        'refresh_token': create_refresh_token(user['email']),
    }


@app.post('/users/', response_model=schemas.UserRead)
def create_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    user: schemas.UserCreate,
    db: Session = Depends(get_db),
):
    db_user = crud.get_user(db, user_email=user.user_email)
    if db_user:
        raise HTTPException(status_code=400, detail='Email já utilizado!')
    return crud.create_user(db=db, user=user)


@app.get('/users/me/', response_model=schemas.UserRead)
def read_current_user(user: User = Depends(get_current_user)):
    return user


@app.get('/users/', response_model=list[schemas.UserRead])
def read_users(
    token: Annotated[str, Depends(oauth2_scheme)],
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get('/users/{user_email}', response_model=schemas.UserRead)
def read_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    user_email: str,
    db: Session = Depends(get_db),
):
    db_user = crud.get_user(db, user_email=user_email)
    if db_user is None:
        raise HTTPException(status_code=404, detail='Usuário não encontrado')
    return db_user


@app.patch('/users/{user_email}', response_model=schemas.UserRead)
def update_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    user_email: str,
    user: schemas.UserUpdate,
    db: Session = Depends(get_db),
):
    db_user = crud.get_user(db, user_email=user_email)
    if db_user is None:
        raise HTTPException(status_code=404, detail='Usuário não encontrado')
    return crud.update_user(db=db, db_user=db_user, user=user)


@app.delete('/users/{user_email}')
def delete_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    user_email: str,
    db: Session = Depends(get_db),
):
    db_user = crud.get_user(db, user_email=user_email)
    if db_user is None:
        raise HTTPException(status_code=404, detail='Usuário não encontrado')
    return crud.delete_user(db=db, db_user=db_user)
