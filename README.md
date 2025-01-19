# VPS Management

## Запуск Docker
```
   docker build -t vps_project .
   docker run -p 8000:8000 vps_project
```
Веб-интерфейс доступен по адресу http://127.0.0.1:8000
## API Endpoints
API доступен по адресу http://127.0.0.1:8000/api.
### Получение списка всех экземпляров VPS
- URL: /api/vps/
- Метод: GET
- Пример:
```
curl -X GET http://127.0.0.1:8000/api/vps/
```
### Создание нового экземпляра VPS
- URL: /api/vps/
- Метод: POST
- Пример:
```
curl -X POST http://127.0.0.1:8000/api/vps/ \
-H "Content-Type: application/json" \
-d '{
    "cpu": 4,
    "ram": 8,
    "hdd": 100,
    "status": "started"
}'
```
### Получение информации об экземпляре VPS
- URL: /api/vps/\<uid\>/
- Метод: GET
- Пример:
```
curl -X GET http://127.0.0.1:8000/api/vps/<uid>/
```
### Обновление экземпляра VPS
- URL: /api/vps/\<uid\>/
- Метод: PATCH
- Пример:
```
curl -X PUT http://127.0.0.1:8000/api/vps/<uid>/ \
-H "Content-Type: application/json" \
-d '{
    "cpu": 8,
    "ram": 16,
    "hdd": 200,
    "status": "blocked"
}'
```
### Частичное обновление экземпляра VPS (PATCH)
- URL: /api/vps/\<uid\>/
- Метод: PATCH
- Пример:
```
curl -X PATCH http://127.0.0.1:8000/api/vps/<uid>/ \
-H "Content-Type: application/json" \
-d '{
    "status": "stopped"
}'
```
### Удаление экземпляра VPS
- URL: /api/vps/\<uid\>/
- Метод: DELETE
- Пример:
```
curl -X DELETE http://127.0.0.1:8000/api/vps/<uid>/
```
