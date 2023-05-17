# sggw_django_app_template

Simple Django application that could be used as a project template or Docker excericise. 

## First run

```bash
$ python -m venv venv 
$ source venv/bin/activate
$ pip install -r requirements.txt
$ cd sggw_template
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```

# URLs

- / - main page, list of polls
- /{id} - poll details view
- /admin - admin panel
