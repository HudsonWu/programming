# Django

+ <https://www.dev2qa.com/how-to-create-remove-django-project-application/>

```
# Install Django
pip3 install django==2.2.1

# Get Django installation information
pip3 show django

# 创建project
django-admin startproject mysite

# 创建app
python3 manage.py startapp polls
```

## urls.py

```
# path(), re_path()
# Key difference between path and re_path is that path uses route without regex
django.urls.re_path(regex, view, kwargs=None, name=None)
path('articles/<int:year>/', views.year_archive)
```

## migrate

```
# initialize the Django project buil-in module
python3 manage.py migrate

# detect whether there are any model changes in the history
python3 manage.py makemigrations

# detect changes for app1
python3 manage.py makemigrations app1

# apply the model changes to the backend database
python3 manage.py migrate app1
```

## runserver

```
# create a super user
python3 manage.py createsuperuser

# start the Django server
python3 manage.py runserver 0:8088
```

## Remove Django App

### Remove tables use dbshell

```
$ python3 manage.py dbshell
# show the command list
sqlite> .help
# show current database
sqlite> .databases
# show all tables in current database
sqlite> .tables
# remove related table
sqlite> drop table table_name
```

### Remove Django application from project

1. Comment or remove 'app1' from Django project `settings.py` file `INSTALLED_APPS` section

2. RUN `python3 manage.py makemigrations` and `python3 manage.py migrate app1` to remove app1

3. Delete app1 folder

