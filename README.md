# API для Yatube

## Описание

Yatube — социальная сеть для публикации записей. Этот проект — REST API для неё.
Через API можно получать и создавать публикации, комментировать их, смотреть
группы и подписываться на других авторов. Аутентификация — по JWT-токенам.

Неаутентифицированные пользователи могут только читать данные. Изменять и
удалять можно только собственный контент. Эндпоинт `/follow/` доступен
только авторизованным пользователям.

## Технологии

- Python 3.10
- Django 3.2
- Django REST Framework 3.12
- Simple JWT

## Установка

1. Клонируйте репозиторий и перейдите в него:

```bash
git clone https://github.com/Argeta04/api_final_yatube.git
cd api_final_yatube
```

2. Создайте и активируйте виртуальное окружение:

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
```

3. Установите зависимости:

```bash
pip install -r requirements.txt
```

4. Выполните миграции и запустите проект:

```bash
cd yatube_api
python manage.py migrate
python manage.py runserver
```

Документация API доступна по адресу: http://127.0.0.1:8000/redoc/

## Примеры запросов

**Получение JWT-токена** — `POST /api/v1/jwt/create/`

```json
{
  "username": "user",
  "password": "password"
}
```

Токен передаётся в заголовке: `Authorization: Bearer <access-токен>`

**Список публикаций** — `GET /api/v1/posts/`
(с пагинацией: `GET /api/v1/posts/?limit=5&offset=0`)

**Создание публикации** — `POST /api/v1/posts/`

```json
{
  "text": "Моя первая публикация"
}
```

**Комментарии к публикации** — `GET /api/v1/posts/{id}/comments/`

**Подписка на автора** — `POST /api/v1/follow/`

```json
{
  "following": "username"
}
```

**Список подписок** — `GET /api/v1/follow/` (поиск: `?search=username`)