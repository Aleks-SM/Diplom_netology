
## Cоздание проекта:

1. Создание проекта под названием 'orders'
   ```django-admin startproject orders```  
2. Создание приложения 'backend'
   ```python manage.py startapp backend```
3. Создание 'виртуального окружения проекта
   ```python -m venv .venv```
4. Активация 'виртуального окружения проекта' (Linux, MacOS)
   ```source venv/bin/activate```
5. Установить зависимости
   ```pip install -r requirements.txt``` 
6. Создать файл миграций 
   ```python manage.py makemigrations```
7. Применить миграции
   ```python manage.py migrate```  
8. Запуск сервера
   ```python manage.py runserver```
 
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
