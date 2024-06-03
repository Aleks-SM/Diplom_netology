
## Cоздание проекта:

1. ```django-admin startproject backend``` - Создание проекта под названием 'backend' 
2. ```python manage.py startapp orders``` - Создание пиложения 'automatic_purchases' 
3. ```python -m venv .venv``` - Создание 'виртуального окружения проекта'
4. ```source venv/bin/activate``` - Активация 'виртуального окружения проекта' (Linux, MacOS)
5. ```pip install -r requirements.txt``` - Установить зависимости 
6. ```python manage.py makemigrations``` - Создаём файл миграций 
7. ```python manage.py migrate``` - Запускаем миграции 
8. ```python manage.py runserver``` - Запускаем сервер
 
## Создание контейнера docker:

1. Создать файл '.env' для переменных окпужения
   ```
   echo "DB_PASS=<...>" > .env && 
   echo "DB_USER=<...>" >> .env &&
   echo "DB_NAME=<...>" >> .env &&
   echo "DB_HOST=<...>" >> .env &&
   echo "DB_PORT=<...>" >> .env &&
   echo "DB_ENGINE=django.db.backends.postgresql" >> .env &&
   echo "DEBUG=True" >> .env &&
   echo "ALLOWED_HOSTS=<...>" >> .env &&
   echo "SECRET_KEY="<...>" >> .env
   ```
    заполнив <...> данными.
2. Запуск контейнера 
   ```docker compose up```
3. Проверка сервера 
   После ввода команды приложение будет доступно по адресу http://localhost
