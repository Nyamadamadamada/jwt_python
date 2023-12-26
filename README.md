# jwtを体験してみよう

JWTの検証
[https://jwt.io/](https://jwt.io/)


## 環境構築
### Dockerを使いたい人

```
docker compose up -d
```

リンク
[http://localhost:8000/](http://localhost:8000/)

API Swagger
[http://localhost:8000/docs#/](http://localhost:8000/docs#/)

### ローカルPCのpythonで直接実行したい人
pythonとpip3をHomebrewでインストールしておく必要がある。
（Macなら元から入ってるかも）

```bash
pip3 install -r ./docker/requirements.txt
uvicorn app.main:app --reload
```

リンク（もし、アクセスできなかったら、起動時のログを確認）
[http://127.0.0.1:8000](http://127.0.0.1:8000)

API Swagger
[http://127.0.0.1:8000/docs#/](http://127.0.0.1:8000/docs#/)


### 動作確認
1. /loginで、id=pasonaかid=adminでログイン
2. AuthorizeでJWTをヘッダーにつける
3. /user/dataにアクセス