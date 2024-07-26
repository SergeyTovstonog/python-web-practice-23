from fastapi import Depends, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer
from fastapi_jwt import JwtAccessBearerCookie, JwtRefreshBearer, JwtAuthorizationCredentials
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone

from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from config.db import get_db
from src.auth.models import User
from src.auth.repo import UserRepository

from src.auth.schemas import TokenData, RoleEnum

SECRET_KEY = "your-secret-key"  # You should store this in .env
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_DAYS = 7

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

access_security = JwtAccessBearerCookie(
    secret_key=SECRET_KEY,
    auto_error=False,
    access_expires_delta=timedelta(hours=1)  # change access token validation timedelta
)
# Read refresh token from bearer header only
refresh_security = JwtRefreshBearer(
    secret_key=SECRET_KEY,
    auto_error=True,  # automatically raise HTTPException: HTTP_401_UNAUTHORIZED
    access_expires_delta=timedelta(days=7)
)



async def get_current_user(credentials: JwtAuthorizationCredentials = Security(refresh_security), db: AsyncSession = Depends(get_db)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    if not credentials:
        raise credentials_exception
    user_repo = UserRepository(db)
    user = await user_repo.get_user(credentials["username"])
    if user is None:
        raise credentials_exception
    return user

class RoleChecker:
    def __init__(self, allowed_roles: list[RoleEnum]):
        self.allowed_roles = allowed_roles

    async def __call__(self, token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)) -> User:
        user = await get_current_user(token, db)
        if user.role.name not in self.allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to perform this action"
            )
        return user



