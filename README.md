# birthday_service

Краткое описание вашего проекта.

## Установка

### 1. Клонируйте репозиторий:

```
https://github.com/romatimon/birthday_service.git
cd ваш_репозиторий
```

### 2. Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Установите зависимости:
```bash
pip install -r requirements.txt
```

### 4. Установите и запустите Redis:
```bash
sudo apt update
sudo apt install redis-server
redis-server
```

### 5. В settings.py добавьте настройки для электронной почты:
```
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@example.com'
EMAIL_HOST_PASSWORD = 'your_email_password'
```

### 6. Примените миграции и создайте суперпользователя:
```bash
python manage.py migrate
python manage.py createsuperuser
```

## Запуск сервиса

### 1. Запустите сервер разработки Django:
```bash
python manage.py runserver
```

### 2.Запустите Celery Worker:
```bash
python -m celery -A birthday_service worker
```

## Проверка работы
- Проверьте API: Откройте браузер и перейдите по адресу http://127.0.0.1:8000/employees/.
- Добавьте сотрудников через Django Admin: Перейдите по адресу http://127.0.0.1:8000/admin/, войдите и добавьте сотрудников с днями рождения.