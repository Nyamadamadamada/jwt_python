# jwtを体験してみよう

## Dockerを使いたい人

```
docker compose up -d
```

## ローカルPCのpythonで直接実行したい人

```bash
c
```

## リンク
アクセスできるかの確認
`http://localhost:8000/`

API Swagger
`http://localhost:8000/docs#/`


```
curl -X 'POST' \
  'http://localhost:8000/login' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": "pasona"
}'
```