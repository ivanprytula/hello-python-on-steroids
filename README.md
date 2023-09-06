# Hello Python on steroids

Yet (my) another mega project about Python and Django DX.

  > Software development is more than just writing code (c)

---

  > Use the `--help` option, programmer (c)

---

TOC

- [Hello Python on steroids](#hello-python-on-steroids)
  - [Features overview](#features-overview)
    - [Best Practices](#features-overview)
    - [Popular Python and Django Packages](#popular-python-and-django-packages)
    - [Testing Tools](#testing-tools)
    - [Code Quality, Formatting, and Linting Tools](#code-quality-formatting-and-linting-tools)
  - [Setup and Walkthrough notes](#setup-and-walkthrough-notes)
    - [General approach](#general-approach)
    - [Local setup](#local-setup)
    - [Containerized setup](#containerized-setup)
    - [Django "classic" set of commands](#django-classic-set-of-commands)
  - [Used resources](#used-resources)
    - [Tutorials](#tutorials)
    - [Documentation/cheatsheet](#documentation-cheatsheet)
    - [People to read](#people-to-read)

## Features overview

### Best Practices

- [environs](https://github.com/sloria/environs) - Used for managing environment variables
- [Docker](https://www.docker.com/) - Docker Compose for development and a multi-stage Dockerfile for production ready Docker image
- [pip-tools](https://github.com/jazzband/pip-tools/) - Used to maintain python requirements
- [just](https://github.com/casey/just) - Popular tool for running common commands in containers (`make` equivalent)
- `make` - with 'classic' Makefile for commands within virtualenv

### Popular Python and Django Packages

- [Django 4.2](https://www.djangoproject.com/) - Latest version of Django
- [Celery](http://docs.celeryproject.org/) - Most popular task runner for running asynchronous tasks in the background
- [Custom User Model][custom_user_model] - Custom user model so that the user model can be easily extended
- [Django Allauth](http://www.intenct.nl/projects/django-allauth/) - The most popular package for adding authentication
  workflows to a Django project

### Testing Tools

- [Pytest](https://docs.pytest.org/) - The most popular Python test runner in the Python community
- [Pytest Django](https://pytest-django.readthedocs.io/en/latest/index.html) - A Django plugin for Pytest
- [Pytest-cov](https://pytest-cov.readthedocs.io) - Adds code coverage to tests
- [pre-commit](https://pre-commit.com/) - A framework for managing and maintaining multi-language pre-commit hooks

### Code Quality, Formatting, and Linting Tools

- [Black](https://black.readthedocs.io/en/stable/) - Automatic Python code formatting
- [Ruff](https://github.com/charliermarsh/ruff) - Extra Python linting and lighting fast because it's written in Rust!
- [Mypy](http://mypy-lang.org/) - Python Type checking
- [typeguard](https://pypi.org/project/typeguard/) - Run-time type checker for Python
- [dj Lint](https://djlint.com/) - Automatic Django HTML template formatting and linting
- [Django Debug Toolbar](https://github.com/jazzband/django-debug-toolbar) - A toolbar for debugging and
  optimizing Django queries
- django-silk
- [Bandit](https://bandit.readthedocs.io/) - Automatic security checking
- [pip-audit](https://pypi.org/project/pip-audit/) - tool for scanning Python environments for known vulnerabilities
- [Stylelint](https://stylelint.io/) - Automatic Sass formatting and linting
- [Eslint](https://eslint.org/) - Automatic Javascript formatting and linting

## Setup and Walkthrough notes

### General approach

1. Lock(pin) Python dependencies with `pip-tools` in requirements/dev.in and requirements/prod.in
2. Split settings into settings/base + development + production + test.py >> update `manage.py`
3. Separate environmental variables from code: django-environ (or other lib, e.g. `python-decouple`)
4. Generate **NEW** SECRET_KEY **before!** applying migrations
5. Update code according to `manage.py check --deploy` recommendations and <https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/>
6. For production environment - install Gunicorn and nginx

### Local setup

1. Start [status|stop] PostgreSQL server: `sudo systemctl start postgresql` or `sudo service postgresql start`
2. Create a new PostgreSQL database with ...
   1. PostgreSQL client `psql` (_steps below_)
   2. Shell CLI [createdb](https://www.postgresql.org/docs/current/app-createdb.html)
   3. pgAdmin
   4. Your preferable way
3. Create/activate a virtualenv
   1. `python3.10 -m venv <virtual env path>`
   2. `source <virtual env path>/bin/activate`
   3. `pip install -r requirements.local.txt`
4. Install pre-commit hook: `pre-commit install`
5. Set the environment variables:
   1. Create/copy `.env` file in the root of your project with all needed variables: `mv env.example.local .env` | `cp env.example.local .env`
      1. then `export DJANGO_READ_DOT_ENV_FILE=True`
      2. or use a local environment manager like [direnv](https://direnv.net/) (NB: you also need `.envrc` file)
6. 'Dry run' w/o applying migrations - just spin off _classic_ `./manage.py runserver` or `./manage.py runserver_plus` (w/ watchdog and Werkzeug debugger)
7. Or skip prev step and do 'full run': `./manage.py migrate` -> `./manage.py runserver 0.0.0.0:8000`
8. Visit <http://127.0.0.1:8000/>
9. Setting up your users:
   1. **normal user account**: just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.
   2. `python manage.py createsuperuser`
10. Sanity checks of code quality: run test, type checks, linter, sort imports, formatter
    1. `pytest -p no:warnings -v`
    2. `mypy price_navigator/`
    3. `flake8`
    4. `isort .`
    5. `black --config pyproject.toml .`
11. Run the following command from the project directory to build and explore HTML documentation: `make -C docs livehtml`

```bash
# verbose option (2.1)
sudo -u postgres -i psql

CREATE DATABASE <local_db_name>;
CREATE USER local_db_user WITH PASSWORD 'my_password';
# it is recommended to set these stuff also
# https://docs.djangoproject.com/en/4.2/ref/databases/#optimizing-postgresql-s-configuration
ALTER ROLE local_db_user SET client_encoding TO 'utf8';
ALTER ROLE local_db_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE local_db_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE "local_db_name" to local_db_user;

# jic, if you are in a hurry, here is simplified one-liner command
sudo -u postgres psql -c 'create database <local_db_name>;'
postgres=# \l  # list all databases
```

### Containerized setup

```bash

# OPTION 1. Use dedicated files in .envs/.local/

# [!] This option is currently used
# docker-compose.yml + docker-compose.dev.yml

# NB: read if you have Docker Engine 23.0+ version
docker info
# https://docs.docker.com/engine/reference/commandline/build/#use-a-dockerignore-file

# OPTION 2. Load environment variables into shell
# This method is similar to CI as on CI pipeline we have env vars (plain text) and secrets (configured for repository)
# For this use: docker-compose.yml + docker-compose.dev-with-environment-attribute.yml

# check current $SHELL environment vars
env

# double-check that load_env_vars.sh file is executable, 'x' must be in OWNER permissions
ls -l --human-readable
-rwxr-xr-x   1 OWNER GROUP OTHERS  size Jun 13 03:50 load_env_vars.sh
# if not:
chmod u=rwx,go=r load_env_vars.sh
# if in rush:
chmod +x load_env_vars.sh

. ./load_env_vars.sh
# or
source ./load_env_vars.sh

# confirm that project env vars in $SHELL
env

# 2. Build and spin containers
make build
make up

# dive deep inside django & db containers
make sh-django
make sh-db

# stop and remove containers
make down

# Connect to db in VSCode with SQLTools extension
# 1.
docker inspect price_navigator_local_postgres  # container name
# 2. find in output line:
"IPAddress": "192.168.80.3", # address could be another
# 3. use this IPAddress and other data from .postgres/.env file to config connection

# 4. example
{
  "previewLimit": 50,
  "server": "192.168.80.3",
  "port": 5432,
  "driver": "PostgreSQL",
  "name": "price_navigator_docker",
  "database": "postgres",
  "username": "postgres"
}
```

### Cloud deploy

1. On EC2 add Public IPv4 DNS in `ALLOWED_HOSTS`
2. Run Django dev server with 0.0.0.0:8000
3. Config Custom TCP inbound rule (in security group of EC2 instance) to allow visit running server only from your IP (while working on the project)
4. Access the development server over HTTP and/or configure HTTPS.

### Django "classic" set of commands

```shell
django-admin startproject <django_project> .
python manage.py startapp <app_name>

cp .env.example .env

export SECRET_KEY=$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')
cat > .env <<EOF
DEBUG=on
SECRET_KEY='$SECRET_KEY'
DATABASE_URL=postgres://postgres:@db:5432/postgres
INTERNAL_IPS=127.0.0.1,0.0.0.0
EOF


python manage.py migrate
python manage.py runserver
python manage.py makemigrations
```

```shell
tree -a -L 2 -I .venv
npm run build
npm run dev
```

## Used resources

### Tutorials

- <https://djangoforbeginners.com/initial-setup/>
- <https://www3.nd.edu/~zxu2/acms60212-40212/Makefile.pdf>
- <https://cheat.readthedocs.io/en/latest/index.html>
- <https://fabien.herfray.org/posts/mastering-postgres-indexes-in-10-minutes/>
- <https://vglushko.github.io/development/2022/12/22/python-dev-environment.html>/home/ivanp/VSCodeProjects/ci-cd-pipe-flow/apps/conftest.py /home/ivanp/VSCodeProjects/ci-cd-pipe-flow/apps/__init__.py
- ...

### Documentation, cheatsheet

- <https://ccbv.co.uk/>
- ...

### People to read

- [jacobian, co-creator of Django](<https://jacobian.org/>)
- ...
