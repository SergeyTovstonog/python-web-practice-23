from fastapi import APIRouter, Depends, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi_jwt import JwtAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession

from starlette import status

from src.auth.schemas import UserCreate, UserResponse, Token
from src.auth.repo import UserRepository
from src.auth.utils import access_security, \
    refresh_security
from src.auth.password_utils import verify_password
from config.db import get_db

router = APIRouter()


@router.post("/register", response_model=UserResponse)
async def register(user_create: UserCreate, db: AsyncSession = Depends(get_db)):
    user_repo = UserRepository(db)
    user = await user_repo.get_user(user_create.username)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered"
        )
    return await user_repo.create_user(user_create)

@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)):
    user_repo = UserRepository(db)
    user = await user_repo.get_user(form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    subject = {"username": user.username, "role": user.role.name}

    # Create new access/refresh tokens pair
    access_token = access_security.create_access_token(subject=subject)
    refresh_token = refresh_security.create_refresh_token(subject=subject)
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }

@router.post("/refresh", response_model=Token)
async def refresh_token(
        credentials: JwtAuthorizationCredentials = Security(refresh_security), db: AsyncSession = Depends(get_db)):

    user_repo = UserRepository(db)
    user = await user_repo.get_user(credentials["username"])
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid refresh token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    subject = {"username": user.username, "role": user.role.name}
    # Create new access/refresh tokens pair
    access_token = access_security.create_access_token(subject=subject)
    refresh_token = refresh_security.create_refresh_token(subject=subject)
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }


