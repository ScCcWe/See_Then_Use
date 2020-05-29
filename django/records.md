```commandline
create project:
    django-admin startproject mysite
        test: python manage.py runserver

    cd mysite && python manage.py startapp myapp
        test: python manage.py runserver


migrate:
    python manage.py makemigrations
    python manage.py migrate


mysql connection:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangodb',
        'USER': 'root',
        'PASSWORD': 'mysqlMYSQL123@',
        'HOST': '127.0.0.1',  # 添加正式数据库时，要换掉ip
        'PORT': 3306,
        # 'CONN_MAX_AGE': 5 * 60,
        # 'OPTIONS': {'charset': 'utf8mb4'}
    }
}
```
