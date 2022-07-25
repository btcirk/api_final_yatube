# api_final_yatube
### Описание
REST API для проекта Yatube (учебный проект Яндекс.Практикум).

Реализует создание, получение, редактирование, удаление постов и комментариев, получение списка сообществ и информации об отдельном сообществе, подписки на пользователей. Используется аутентификация по JWT-токену.

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
После запуска проекта документация доступна по адресу 127.0.0.1:8000/redoc

### Авторы
Василий Бычков, когорта 32.
