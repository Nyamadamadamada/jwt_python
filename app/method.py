from datetime import datetime, timedelta
from app.models import User
import jwt

SECRET_KEY = 'secret'
ALGORITHM = 'HS256'
EXPIRE_MINUTES = 30


# ダミーのユーザーデータベース
fake_db = {
    'pasona': {'id': 'pasona', 'name': 'パソナ','password': 'Pasona123'}
}

# 認証チェックもどき(ユーザーが存在するか？)
def authenticate_user(user_id: str):
    user = fake_db.get(user_id)
    if not user:
        return False
    return User(**user)

# JWT生成
def create_jwt(user: User):
    expire = datetime.utcnow() + timedelta(minutes=EXPIRE_MINUTES)
    encoded_jwt = jwt.encode({"user_id": user.id, "exp": expire}, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
