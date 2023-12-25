from datetime import datetime, timedelta
from app.models import Payload, User
from typing import Optional
import jwt
from fastapi.security import HTTPBearer, OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.responses import HTMLResponse

SECRET_KEY = 'secret'
ALGORITHM = 'HS256'
EXPIRE_MINUTES = 30


# ダミーのユーザーデータベース
fake_db = {
    'pasona': {'id': 'pasona', 'name': 'パソナ','password': 'Pasona23', 'role': 'user'},
    'admin1': {'id': 'admin1', 'name': '管理者','password': 'Pasona23', 'role': 'admin'},
}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# 認証チェックもどき(ユーザーが存在するか？)
def authenticate_user(user_id: str):
    user = fake_db.get(user_id)
    if not user:
        return False
    return User(**user)

# JWT生成
def create_jwt(user: User):
    expire = datetime.utcnow() + timedelta(minutes=EXPIRE_MINUTES)
    encoded_jwt = jwt.encode({"user_id": user.id,"role": user.role, "exp": expire}, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# JWTトークンからユーザーを取得する関数
async def get_current_user(token: str = Depends(HTTPBearer())) -> User:
    token_str = token.credentials
    try:
        payload = jwt.decode(token_str, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = payload.get("user_id")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="ユーザーが存在しません",
            )
        return Payload(user_id=user_id,role=payload.get("role"), exp=payload.get("exp"))
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="認証に失敗しました",
        )
        