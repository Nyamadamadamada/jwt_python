from datetime import datetime, timedelta
from typing import Optional
from app.models import Payload, User
import jwt
from fastapi.security import HTTPBearer
from fastapi import HTTPException, status, Depends

SECRET_KEY = 'secret'
ALGORITHM = 'HS256'
EXPIRE_MINUTES = 30


# ダミーのユーザーデータベース
fake_db = {
    'pasona': {'id': 'pasona', 'name': 'パソナ','password': 'Pasona23', 'role': 'user'},
    'admin1': {'id': 'admin1', 'name': '管理者','password': 'Pasona23', 'role': 'admin'},
}


# 認証チェックもどき(ユーザーが存在するか？)
def authenticate_user(user_id: str) -> Optional[User]:
    user = fake_db.get(user_id)
    if not user:
        return None
    return User(**user)

# JWT生成
def create_jwt(user: User):
    # JWT有効期限
    expire = datetime.utcnow() + timedelta(minutes=EXPIRE_MINUTES)
    encoded_jwt = jwt.encode({"user_id": user.id,"role": user.role, "exp": expire}, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# JWTトークンからユーザー情報を取得する関数
async def get_current_user(token: str = Depends(HTTPBearer())) -> User:
    token_str = token.credentials
    try:
        # JWTをデコード（有効期限はここで確認してくれる）
        payload = jwt.decode(token_str, SECRET_KEY, algorithms=[ALGORITHM])
        return Payload(**payload)
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="認証に失敗しました",
        )
        