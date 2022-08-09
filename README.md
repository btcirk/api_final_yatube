# REST API для проекта "Yatube"

### Описание
REST API для проекта Yatube реализует создание, получение, редактирование, удаление постов и комментариев, получение списка сообществ и информации об отдельном сообществе, подписки на пользователей. Используется аутентификация по JWT-токену.

### Технологии
Python 3.8  
Django 2.2  
Django REST Framework 3.12  
Djoser  

### Запуск проекта в dev-режиме

- Cоздать и активировать виртуальное окружение
```
python3 -m venv env
source env/bin/activate
python3 -m pip install --upgrade pip
```

- Установить зависимости из файла requirements.txt
```
pip install -r requirements.txt
```

- Выполнить миграции
```
python3 manage.py migrate
```

- Запустить проект
```
python3 manage.py runserver
```
### Документация
После запуска проекта документация доступна по адресу [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc).
