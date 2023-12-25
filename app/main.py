from typing import Annotated
from app.method import authenticate_user, create_jwt, get_current_user
from app.models import BaseUser, Payload, Token, User
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.responses import HTMLResponse

app = FastAPI()

# ログイン
@app.post("/login", response_model=Token)
async def login(form_data: BaseUser):
    user = authenticate_user(form_data.id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_jwt(user)
    return {"access_token": access_token, "token_type": "bearer"}


# ユーザーデータにアクセスするためのエンドポイント
@app.get("/user/data", response_model=Payload)
async def read_users_data(user_info: Payload = Depends(get_current_user)):
    return user_info

# サーバー起動確認用
@app.get("/", response_class=HTMLResponse)
async def read():
    return f"""
    <html>
        <head>
            <title>FAST API</title>
        </head>
        <body>
            <h1>FAST APIが動いてる!</h1>
        </body>
    </html>
    """