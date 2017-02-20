# UT-Austin Student Government Explorer
### By [The Daily Texan](http://dailytexanonline.com)

This is the public repository for The Daily Texan's Student Government Explorer. Currently, only the election explorer side of the app is up and running, given that campus election season is well underway. However, we plan on expanding this app's coverage into the actions of UT student government, especially that of the student legislature.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

**This is a Python 3 project! Make sure everything is run in `python3` and `pip3`**

1: `pip3 install virtualenv`

2: `git clone` this repository

3: `virtualenv .`

4: `source bin/activate`

5: `pip install -r requirements.txt`

### Installing

After installing the requirements above, set up a local Postgres database (instructions are for Ubuntu, MacOS)

1: `apt-get libpq-dev postgresql postgresql-contrib`, or `brew install postgres`

2: `sudo -u postgres psql` or `psql`

3: Once in the postgres shell: `CREATE DATABASE dt_sg;`

4: `CREATE USER <your username> WITH PASSWORD <your password>;`

5: `GRANT ALL PRIVILEGES ON DATABASE dt_sg TO <your user>;`

6: `ctrl-D` out of the psql shell.

### **Go into `./dt_sg/` and create a file named `settings_secret.py`.**
**This is really important! Without `settings_secret`, the project won't run.**

Inside `settings_secret.py`, paste this:

```
import os
 
 # SECURITY WARNING: keep the secret key used in production secret!
 SECRET_KEY = # GENERATE YOUR OWN SECRET_KEY
 
 # Database
 # https://docs.djangoproject.com/en/1.10/ref/settings/#databases
 
 DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': 'dt_sg',
         'USER': # YOUR USERNAME,
         'PASSWORD': # YOUR PASSWORD,
         'HOST': 'localhost',
         'PORT': '',
     }
 }
 
 # SECURITY WARNING: don't run with debug turned on in production!
 DEBUG = True # CHANGE THIS TO False IN PRODUCTION!
 
 ALLOWED_HOSTS = [] # IF DEBUG = False, ADD VALUES TO THIS LIST
```

`settings_secret.py` is not commited to VCS by default, so you must manually set this up on initial setup.

From the command line, run `python3 manage.py createsuperuser` to create a user for the admin panel.

Make sure your virtualenv is booted, and from the root directory of the project run `python3 manage.py migrate` to make sure the database is up to date, and then run `python3 manage.py runserver`. 

Navigate to `localhost:8000`, and you should see the site. `localhost:8000/admin` will allow you to log in to the backend and add election data.

## Deployment

Our production server uses Gunicorn and Nginx, as seen in [this very helpful tutorial](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04) from DigitalOcean, our hosting provider.


## Built With

* Django 10.5
* PostgreSQL
* Django-Sass, Django-Imagekit, Django-Bleach, Pillow, Django-TinyMCE
* VirtualEnv
* Gunicorn
* Nginx

## Authors

* **Junyuan Tan** - *lead dev, full-stack, visual design, database, server administration* - [sc1f](https://github.com/sc1f)
* **Arjun Talpallikar** - *full-stack, data* - [talpallikar](https://github.com/talpallikar)

