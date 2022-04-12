# Django Backend Custom User

## Setup

First clone the repository from Github and switch to the new directory:
```sh
$ git clone git@github.com:rdtagline/backend_custom_user.git
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

```sh
(env)$ cd backend_custom_user
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
(env)$ python manage.py createsuperuser
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/user/`.
