# Phygitalism Python intern task

Put any files in ./file_project/files folder
(I already included some for you, take a look!)

## Superuser login details

Login: admin

Password: qweqwe123123

## Startup guide

```pip install -r requirements.txt```
(Using venv is highly recommended)

```python manage.py runserver 127.0.0.1:8000```

In any browser:

```http://127.0.0.1:8000/api/files```

OR:
```curl -i http://127.0.0.1:8000/api/files/```

## Points of interest

./file_project/settings.py

./file_project/urls.py

./file_app/models.py

./file_app/views.py

./file_app/converter.py

And maybe something in files folder ;)

### P.S.

This task was made with purely developing in mind, so there is no DevOps things such as production deploy
