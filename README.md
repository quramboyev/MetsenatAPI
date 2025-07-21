# 🎓 MetsenatAPI

Backend-система для управления спонсорами и студентами. Реализована с использованием Django и Django REST Framework.

## 🚀 Установка и запуск

- git clone https://github.com/quramboyev/MetsenatAPI.git
- cd MetsenatAPI
- pip install -r requiroments.txt
- python manage.py migrate
- python manage.py runserver

## 🔧 Стек технологий

- Python
- Django
- Django REST Framework
- drf-spectacular (Swagger / ReDoc)

## 📦 Структура проекта

metsenatAPI/
- ├── config/ # Настройки Django
- ├── sponsors/ # Приложение спонсоров
- ├── students/ # Приложение студентов
- ├── manage.py
- └── requirements.txt

## 📄 Документация API

Swagger UI: [`/api/docs/swagger/`](http://127.0.0.1:8000/api/docs/swagger/)  
ReDoc: [`/api/docs/redoc/`](http://127.0.0.1:8000/api/docs/redoc/)

## 🛡️ Роли доступа

- **GET (чтение)**: доступно всем
- **POST / PUT / DELETE**: доступно только администраторам

- # ✍️ Автор

**Ulug'bek Quramboyev**  
